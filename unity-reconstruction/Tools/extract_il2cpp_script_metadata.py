#!/usr/bin/env python3
"""Index IL2CPP type, field, and method metadata from an Il2CppDumper dump.cs.

The output contains declarations and native addresses only. It does not recover
or reconstruct the original C# method bodies.
"""
from __future__ import annotations

import argparse
import collections
import gzip
import json
import re
import sys
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
MANIFEST_ROOT = PROJECT_ROOT / "Assets" / "Recovered" / "Manifests"
DEFAULT_OUTPUT = MANIFEST_ROOT / "il2cpp-script-metadata.json"

IMAGE_RE = re.compile(r"^// Image \d+: (.+?) - (\d+)\s*$")
NAMESPACE_RE = re.compile(r"^// Namespace:\s*(.*?)\s*$")
TYPE_INDEX_RE = re.compile(r"// TypeDefIndex:\s*(\d+)\s*$")
TYPE_DECL_RE = re.compile(r"\b(class|struct|enum|interface|delegate)\s+([^\s:<,]+(?:<[^>]+>)?)")
HEX_VALUE_RE = re.compile(r"0x[0-9a-fA-F]+")


def load_json(path: Path) -> Any:
    opener = gzip.open if path.suffix.lower() == ".gz" else open
    with opener(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def format_address(value: str | None) -> str | None:
    if value is None:
        return None
    return f"0x{int(value, 0):X}"


def parameter_count(signature: str) -> int | None:
    """Count top-level C# parameters while ignoring generic/array commas."""
    opening = signature.find("(")
    closing = signature.rfind(")")
    if opening < 0 or closing <= opening:
        return None
    contents = signature[opening + 1:closing].strip()
    if not contents:
        return 0
    depth = 0
    count = 1
    for character in contents:
        if character in "<([":
            depth += 1
        elif character in ">)]":
            depth = max(0, depth - 1)
        elif character == "," and depth == 0:
            count += 1
    return count


def parse_method_signature(line: str, marker: str) -> dict[str, Any] | None:
    signature = line.strip()
    signature = re.sub(r"\s*\{\s*\}\s*$", "", signature).strip()
    if "(" not in signature or ")" not in signature:
        return None
    method_head = signature.split("(", 1)[0].strip()
    if not method_head:
        return None
    method_name = method_head.split()[-1]
    values = {
        name.lower(): value
        for name, value in re.findall(
            r"\b(RVA|Offset|VA|Slot):\s*(0x[0-9a-fA-F]+|\d+)", marker
        )
    }
    return {
        "name": method_name,
        "signature": signature,
        "parameterCount": parameter_count(signature),
        "rva": format_address(values.get("rva")),
        "fileOffset": format_address(values.get("offset")),
        "va": format_address(values.get("va")),
        "slot": int(values["slot"], 0) if "slot" in values else None,
        "bodyRecovered": False,
    }


def parse_dump(path: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    images: list[dict[str, Any]] = []
    for line in lines:
        match = IMAGE_RE.match(line)
        if match:
            images.append({"typeStart": int(match.group(2)), "name": match.group(1)})
    images.sort(key=lambda image: image["typeStart"])
    if not images:
        raise ValueError("dump.cs has no // Image headers; is this an Il2CppDumper output?")

    declarations: list[dict[str, Any]] = []
    namespace = ""
    for line_index, line in enumerate(lines):
        namespace_match = NAMESPACE_RE.match(line)
        if namespace_match:
            namespace = namespace_match.group(1).strip()
        type_index_match = TYPE_INDEX_RE.search(line)
        if not type_index_match:
            continue
        declaration = line[:type_index_match.start()].strip()
        type_match = TYPE_DECL_RE.search(declaration)
        if not type_match:
            continue
        type_index = int(type_index_match.group(1))
        image = next(
            (candidate for candidate in reversed(images) if candidate["typeStart"] <= type_index),
            None,
        )
        if image is None:
            raise ValueError(f"TypeDefIndex {type_index} precedes all image headers")
        raw_type_name = type_match.group(2)
        qualified_name = f"{namespace}.{raw_type_name}" if namespace else raw_type_name
        declarations.append({
            "lineIndex": line_index,
            "typeDefIndex": type_index,
            "name": raw_type_name,
            "namespace": namespace,
            "qualifiedName": qualified_name,
            "assembly": image["name"],
            "kind": type_match.group(1),
            "declaration": declaration,
        })

    if not declarations:
        raise ValueError("dump.cs contains no parseable TypeDef declarations")

    types: list[dict[str, Any]] = []
    for index, declaration in enumerate(declarations):
        end_index = declarations[index + 1]["lineIndex"] if index + 1 < len(declarations) else len(lines)
        body = lines[declaration["lineIndex"] + 1:end_index]
        fields: list[dict[str, Any]] = []
        methods: list[dict[str, Any]] = []
        section = ""
        pending_method_marker = ""
        base_types = ""
        if ":" in declaration["declaration"]:
            base_types = declaration["declaration"].split(":", 1)[1].strip()

        for line in body:
            stripped = line.strip()
            if stripped == "// Fields":
                section = "fields"
                continue
            if stripped == "// Methods":
                section = "methods"
                pending_method_marker = ""
                continue
            if stripped.startswith("//"):
                if section == "methods" and stripped.startswith("// RVA:"):
                    pending_method_marker = stripped
                continue
            if section == "fields":
                field_declaration = stripped.split("//", 1)[0].strip()
                if field_declaration.endswith(";"):
                    offset_match = HEX_VALUE_RE.search(stripped.split("//", 1)[1]) if "//" in stripped else None
                    fields.append({
                        "declaration": field_declaration,
                        "offset": format_address(offset_match.group(0)) if offset_match else None,
                    })
            elif section == "methods" and stripped:
                parsed = parse_method_signature(stripped, pending_method_marker)
                if parsed:
                    methods.append(parsed)
                    pending_method_marker = ""

        qualified_name = declaration["qualifiedName"]
        types.append({
            "name": declaration["name"],
            "namespace": declaration["namespace"],
            "qualifiedName": qualified_name,
            "assembly": declaration["assembly"],
            "typeDefIndex": declaration["typeDefIndex"],
            "kind": declaration["kind"],
            "declaration": declaration["declaration"],
            "baseTypes": base_types,
            "fields": fields,
            "methods": methods,
        })
    return images, types


def serialized_script_names(scene_data: dict[str, Any], prefab_data: dict[str, Any]) -> set[str]:
    names: set[str] = set()
    for scene in scene_data.get("scenes", []) or []:
        for game_object in scene.get("objects", []) or []:
            names.update(
                script for script in game_object.get("scripts", []) or []
                if isinstance(script, str) and script
            )
    for prefab in prefab_data.get("prefabs", []) or []:
        for game_object in prefab.get("objects", []) or []:
            names.update(
                script for script in game_object.get("scripts", []) or []
                if isinstance(script, str) and script
            )
    return names


def persistent_calls(scene_data: dict[str, Any], prefab_data: dict[str, Any]):
    for scene in scene_data.get("scenes", []) or []:
        game_objects = scene.get("objects", []) or []
        names_by_id = {item.get("id"): item.get("name", "") for item in game_objects if isinstance(item, dict)}
        for game_object in game_objects:
            button_data = game_object.get("uiButtonData") or {}
            for call in button_data.get("persistentCalls", []) or []:
                if isinstance(call, dict) and call.get("targetType") == "MonoBehaviour":
                    yield call, {
                        "container": scene.get("name", ""),
                        "button": game_object.get("name", ""),
                        "targetObject": names_by_id.get(call.get("targetObjectId"), ""),
                    }
    for prefab in prefab_data.get("prefabs", []) or []:
        game_objects = prefab.get("objects", []) or []
        names_by_id = {item.get("id"): item.get("name", "") for item in game_objects if isinstance(item, dict)}
        for game_object in game_objects:
            button_data = game_object.get("uiButtonData") or {}
            for call in button_data.get("persistentCalls", []) or []:
                if isinstance(call, dict) and call.get("targetType") == "MonoBehaviour":
                    yield call, {
                        "container": f"UI prefab {prefab.get('name', '')}",
                        "button": game_object.get("name", ""),
                        "targetObject": names_by_id.get(call.get("targetObjectId"), ""),
                    }


def normalize_assembly_name(name: str) -> str:
    return name if not name or name.lower().endswith(".dll") else f"{name}.dll"


def build_metadata(
    dump_path: Path,
    scene_data: dict[str, Any],
    prefab_data: dict[str, Any],
    metadata_version: str,
    dumper: str,
) -> dict[str, Any]:
    images, all_types = parse_dump(dump_path)
    script_names = serialized_script_names(scene_data, prefab_data)
    calls = list(persistent_calls(scene_data, prefab_data))
    script_names.update(
        str(call.get("targetScript", ""))
        for call, _context in calls
        if call.get("targetScript")
    )

    classes_by_name: dict[str, list[dict[str, Any]]] = collections.defaultdict(list)
    for item in all_types:
        classes_by_name[item["qualifiedName"]].append(item)
    script_types = [
        item
        for name in sorted(script_names)
        for item in classes_by_name.get(name, [])
    ]
    indexed_keys = {
        (item["qualifiedName"], item["assembly"])
        for item in script_types
    }
    unmatched_script_names = sorted(
        name for name in script_names if name not in classes_by_name
    )

    matched_handler_counts: collections.Counter[tuple[str, str, str, tuple[str, ...]]] = collections.Counter()
    unresolved_groups: dict[tuple[str, str, str, str, str], dict[str, Any]] = {}
    unresolved_reasons: collections.Counter[str] = collections.Counter()
    for call, context in calls:
        target_script = str(call.get("targetScript", "") or "")
        target_assembly = normalize_assembly_name(str(call.get("targetScriptAssembly", "") or ""))
        method_name = str(call.get("methodName", "") or "")
        target_candidates = [
            item for item in classes_by_name.get(target_script, [])
            if not target_assembly or item["assembly"] == target_assembly
        ]
        method_candidates = [
            method for item in target_candidates for method in item["methods"]
            if method["name"] == method_name
        ]
        if method_candidates:
            signatures = tuple(sorted({method["signature"] for method in method_candidates}))
            matched_handler_counts[(target_script, target_assembly, method_name, signatures)] += 1
            continue
        if not target_candidates and call.get("targetScriptStatus") == "nullScriptPointer":
            reason = "nullScriptPointer"
        elif not target_candidates and target_script:
            reason = "targetScriptNotInDump"
        elif not target_candidates:
            reason = "targetScriptMissingOrNotInDump"
        else:
            reason = "methodNameNotFoundInType"
        unresolved_reasons[reason] += 1
        key = (reason, target_script, target_assembly, str(context["targetObject"]), method_name)
        group = unresolved_groups.setdefault(key, {
            "reason": reason,
            "targetScript": target_script,
            "targetScriptAssembly": target_assembly,
            "targetObject": context["targetObject"],
            "methodName": method_name,
            "callCount": 0,
            "contexts": [],
        })
        group["callCount"] += 1
        group["contexts"].append({"container": context["container"], "button": context["button"]})

    matched_handlers = [
        {
            "targetScript": script,
            "targetScriptAssembly": assembly,
            "methodName": method,
            "callCount": count,
            "signatures": list(signatures),
        }
        for (script, assembly, method, signatures), count in sorted(matched_handler_counts.items())
    ]
    unresolved_handlers = sorted(
        unresolved_groups.values(),
        key=lambda item: (item["reason"], item["targetObject"], item["methodName"]),
    )
    for group in unresolved_handlers:
        group["contexts"].sort(key=lambda context: (context["container"], context["button"]))

    return {
        "formatVersion": 1,
        "unityVersion": scene_data.get("unityVersion", ""),
        "il2cppMetadataVersion": metadata_version,
        "dumper": dumper,
        "dumperRepository": "https://github.com/springmusk026/Il2CppDumper-Python",
        "dumpSource": dump_path.name,
        "imageHeaders": images,
        "limitations": [
            "Only IL2CPP type, field, method-signature, and native-address metadata is indexed; original C# source is not recovered.",
            "Method declarations from dump.cs contain placeholder empty bodies; they do not encode gameplay behavior.",
            "Native RVAs and file offsets are references for further binary analysis, not decompiled or validated method implementations.",
            "Persistent callback matches are by serialized target type and method name; overload/signature binding and runtime behavior are not proven.",
        ],
        "sourceScriptNames": sorted(script_names),
        "unmatchedScriptNames": unmatched_script_names,
        "scriptTypes": script_types,
        "counts": {
            "referencedScriptTypes": len(script_names),
            "indexedScriptTypes": len(script_types),
            "unmatchedScriptTypes": len(unmatched_script_names),
            "indexedFields": sum(len(item["fields"]) for item in script_types),
            "indexedMethodSignatures": sum(len(item["methods"]) for item in script_types),
        },
        "persistentCallbackResolution": {
            "monoBehaviourCalls": len(calls),
            "methodNameMatchedCalls": sum(matched_handler_counts.values()),
            "unresolvedCalls": sum(unresolved_reasons.values()),
            "unresolvedByReason": dict(sorted(unresolved_reasons.items())),
            "matchedHandlerMethods": matched_handlers,
            "unresolvedHandlerGroups": unresolved_handlers,
        },
    }


def render_markdown(metadata: dict[str, Any]) -> str:
    counts = metadata["counts"]
    callbacks = metadata["persistentCallbackResolution"]
    lines = [
        "# IL2CPP script metadata index",
        "",
        f"- Unity: `{metadata.get('unityVersion') or 'unknown'}`; IL2CPP metadata version: `{metadata.get('il2cppMetadataVersion')}`",
        f"- Dumper: `{metadata['dumper']}`",
        f"- Script types referenced by scenes/UI prefabs: {counts['indexedScriptTypes']}/{counts['referencedScriptTypes']} indexed ({counts['indexedFields']} field declarations, {counts['indexedMethodSignatures']} method signatures)",
        f"- Persistent MonoBehaviour callbacks: {callbacks['methodNameMatchedCalls']}/{callbacks['monoBehaviourCalls']} have a matching target type and method name in IL2CPP metadata; {callbacks['unresolvedCalls']} remain unresolved.",
        "",
        "## Unresolved callback references",
        "",
    ]
    if callbacks["unresolvedHandlerGroups"]:
        for group in callbacks["unresolvedHandlerGroups"]:
            type_name = group["targetScript"] or "<target MonoBehaviour script unresolved>"
            target = group["targetObject"] or type_name
            lines.append(
                f"- `{target}` / `{type_name}.{group['methodName']}` — "
                f"{group['callCount']} call(s), reason: `{group['reason']}`."
            )
    else:
        lines.append("- None.")
    lines += [
        "",
        "## Limits",
        "",
        "- This index preserves serialized type/field/method metadata and native addresses, not the original C# source.",
        "- `dump.cs` method bodies are empty placeholders; they do not show the implementation or prove gameplay behavior.",
        "- Callback matches are based on target type and method name only; overload binding, Editor compilation, and runtime behavior remain unverified.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dump_cs", type=Path, help="dump.cs produced by an IL2CPP metadata dumper")
    parser.add_argument("--scene-manifest", type=Path, default=MANIFEST_ROOT / "scene-data.json.gz")
    parser.add_argument("--ui-prefabs-manifest", type=Path, default=MANIFEST_ROOT / "ui-prefabs.json")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--metadata-version", default="unknown", help="IL2CPP metadata version reported by the dumper")
    parser.add_argument(
        "--dumper",
        default="Il2CppDumper-Python 0.1.0 (commit 126b6c9db3c9f67649f5c4645cada55763f0a0e1)",
        help="Dumper name/version/commit for provenance metadata",
    )
    args = parser.parse_args()
    if not args.dump_cs.is_file():
        parser.error(f"dump.cs does not exist: {args.dump_cs}")
    if not args.scene_manifest.is_file() or not args.ui_prefabs_manifest.is_file():
        parser.error("scene-data and ui-prefabs manifests must exist; run extract_from_apk.py first")
    try:
        metadata = build_metadata(
            args.dump_cs,
            load_json(args.scene_manifest),
            load_json(args.ui_prefabs_manifest),
            args.metadata_version,
            args.dumper,
        )
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        report_path = args.output.with_suffix(".md")
        report_path.write_text(render_markdown(metadata), encoding="utf-8")
    except Exception as exc:
        print(f"ERROR: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2

    counts = metadata["counts"]
    callbacks = metadata["persistentCallbackResolution"]
    print(f"Indexed script types: {counts['indexedScriptTypes']}/{counts['referencedScriptTypes']}")
    print(f"Fields/method signatures: {counts['indexedFields']}/{counts['indexedMethodSignatures']}")
    print(
        "MonoBehaviour callback method-name matches: "
        f"{callbacks['methodNameMatchedCalls']}/{callbacks['monoBehaviourCalls']} "
        f"({callbacks['unresolvedCalls']} unresolved)"
    )
    print(f"Wrote: {args.output}")
    print(f"Wrote: {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
