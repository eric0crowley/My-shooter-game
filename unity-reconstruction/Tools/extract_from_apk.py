#!/usr/bin/env python3
"""Export editable Unity assets and scene manifests from a Unity APK with UnityPy.

This does not recover original C# source. It exports scene hierarchy/transform
metadata, OBJ/PNG assets, material properties, UI strings/sprites, shared-asset UI
prefab trees and an index of native/managed component types so the companion Unity
Editor builder can recreate editable scenes and prefab assets.
"""
from __future__ import annotations

import argparse
import collections
import gzip
import json
import math
import os
import re
import shutil
import struct
import sys
import tempfile
import zipfile
from pathlib import Path, PurePosixPath
from typing import Any, Iterable

try:
    import UnityPy
    from UnityPy.classes.PPtr import PPtr
    from UnityPy.helpers.MeshHelper import MeshHandler
except ImportError as exc:
    raise SystemExit(
        "Missing dependencies. Run: python -m pip install -r Tools/requirements.txt"
    ) from exc

try:
    from fsb5 import load as load_fsb5
except ImportError:
    load_fsb5 = None

PROJECT_ROOT = Path(__file__).resolve().parents[1]
ASSET_ROOT = PROJECT_ROOT / "Assets" / "Recovered"
SCENE_BUILD_NAMES = [
    "00 - Splash",
    "01 - MainMenu",
    "02 - GamePlay",
    "03 - Z-GamePlay",
]


def safe_name(value: Any, limit: int = 56) -> str:
    value = str(value or "Unnamed")
    value = re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("._-")
    return (value[:limit] or "Unnamed")


def vec3(value: Any, default=(0.0, 0.0, 0.0)) -> list[float]:
    if not isinstance(value, dict):
        return [float(x) for x in default]
    return [float(value.get("x", default[0])), float(value.get("y", default[1])), float(value.get("z", default[2]))]


def vec2(value: Any, default=(0.0, 0.0)) -> list[float]:
    if not isinstance(value, dict):
        return [float(x) for x in default]
    return [float(value.get("x", default[0])), float(value.get("y", default[1]))]


def vec4(value: Any, default=(0.0, 0.0, 0.0, 0.0)) -> list[float]:
    if not isinstance(value, dict):
        return [float(x) for x in default]
    return [
        float(value.get("x", default[0])),
        float(value.get("y", default[1])),
        float(value.get("z", default[2])),
        float(value.get("w", default[3])),
    ]


def color4(value: Any, default=(1.0, 1.0, 1.0, 1.0)) -> list[float]:
    if not isinstance(value, dict):
        return [float(x) for x in default]
    return [
        float(value.get("r", default[0])),
        float(value.get("g", default[1])),
        float(value.get("b", default[2])),
        float(value.get("a", default[3])),
    ]


def input_data_folder(source: Path, temp_root: Path) -> Path:
    """Resolve an APK, APKTool output folder, or Unity Data folder to a folder."""
    source = source.expanduser().resolve()
    if source.is_file() and source.suffix.lower() == ".apk":
        extracted = temp_root / "apk-data"
        extracted.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(source) as apk:
            names = apk.namelist()
            prefixes = ("assets/bin/Data/", "bin/Data/")
            prefix = next((p for p in prefixes if any(n.startswith(p) for n in names)), None)
            if prefix is None:
                raise RuntimeError("APK has no assets/bin/Data directory")
            for name in names:
                if not name.startswith(prefix) or name.endswith("/"):
                    continue
                relative = PurePosixPath(name[len(prefix):])
                if ".." in relative.parts:
                    continue
                target = extracted.joinpath(*relative.parts)
                target.parent.mkdir(parents=True, exist_ok=True)
                with apk.open(name) as src, target.open("wb") as dst:
                    shutil.copyfileobj(src, dst)
        return extracted

    if not source.is_dir():
        raise RuntimeError(f"Input does not exist: {source}")
    candidates = [source / "assets" / "bin" / "Data", source / "bin" / "Data"]
    for candidate in candidates:
        if candidate.is_dir():
            return candidate
    return source


def merge_split_files(source: Path, destination: Path) -> Path:
    """Copy Unity Data files while joining Unity's .split0/.split1 asset chunks."""
    source = source.resolve()
    destination.mkdir(parents=True, exist_ok=True)
    split_re = re.compile(r"^(.*)\.split(\d+)$")
    groups: dict[Path, list[tuple[int, Path]]] = collections.defaultdict(list)
    regular: list[Path] = []
    for path in source.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(source)
        match = split_re.match(path.name)
        if match:
            base = rel.parent / match.group(1)
            groups[base].append((int(match.group(2)), path))
        else:
            regular.append(path)
    grouped_bases = set(groups)
    for path in regular:
        rel = path.relative_to(source)
        if rel in grouped_bases:
            continue
        target = destination / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
    for relative_base, chunks in groups.items():
        target = destination / relative_base
        target.parent.mkdir(parents=True, exist_ok=True)
        # A non-split base, if present, is the first segment; Unity normally
        # stores split assets only as .splitN files.
        with target.open("wb") as output:
            original = source / relative_base
            if original.is_file():
                with original.open("rb") as base_stream:
                    shutil.copyfileobj(base_stream, output)
            for _, chunk in sorted(chunks):
                with chunk.open("rb") as part:
                    shutil.copyfileobj(part, output)
    return destination


def file_map(environment) -> dict[str, Any]:
    return {
        str(getattr(f, "name", "")).replace("\\", "/").split("/")[-1].lower(): f
        for f in environment.files.values()
        if hasattr(f, "objects")
    }


def object_id(obj: Any, kind: str | None = None) -> str:
    tree = {}
    try:
        tree = obj.read_typetree(check_read=False)
    except Exception:
        pass
    name = tree.get("m_Name", "") if isinstance(tree, dict) else ""
    source = Path(str(obj.assets_file.name)).name
    source = source.rsplit(".", 1)[0] if "." in source else source
    prefix = safe_name(kind or obj.type.name, 14)
    return f"{prefix}_{safe_name(source, 24)}_{int(obj.path_id):08d}_{safe_name(name, 40)}"


def ptr_target(source_file: Any, value: Any):
    if not isinstance(value, dict):
        return None
    path_id = int(value.get("m_PathID", 0) or 0)
    if not path_id:
        return None
    try:
        pointer = PPtr(
            m_FileID=int(value.get("m_FileID", 0) or 0),
            m_PathID=path_id,
            assetsfile=source_file,
        )
        return pointer.deref()
    except Exception:
        return None


def source_name_for_file_id(source_file: Any, file_id: int) -> str | None:
    if file_id == 0:
        return str(source_file.name).replace("\\", "/").split("/")[-1].lower()
    externals = getattr(source_file, "externals", [])
    index = file_id - 1
    if index < 0 or index >= len(externals):
        return None
    path = str(getattr(externals[index], "path", "")).replace("\\", "/")
    path = path.removeprefix("archive:/")
    path = path.removeprefix("assets/")
    return path.rsplit("/", 1)[-1].lower()


def script_record(component: Any, tree: dict[str, Any]) -> dict[str, str] | None:
    script = ptr_target(component.assets_file, tree.get("m_Script"))
    if script is None or script.type.name != "MonoScript":
        return None
    try:
        data = script.read_typetree(check_read=False)
    except Exception:
        return None
    class_name = str(data.get("m_ClassName", ""))
    namespace = str(data.get("m_Namespace", ""))
    assembly = str(data.get("m_AssemblyName", ""))
    qualified = f"{namespace}.{class_name}" if namespace else class_name
    return {
        "className": class_name,
        "namespace": namespace,
        "qualifiedName": qualified,
        "assembly": assembly,
    }


def find_sprite_pointer(component: Any, sprite_lookup: dict[tuple[str, int], Any]) -> Any | None:
    """Find a serialized Sprite PPtr in an IL2CPP MonoBehaviour payload.

    UnityPy can read the MonoBehaviour header, but the original managed TypeTrees
    are not included in this APK. Searching for valid fileID/pathID pairs lets us
    recover the UI Image sprite reference without claiming to recover its C# data.
    """
    try:
        raw = component.get_raw_data()
    except Exception:
        return None
    found = []
    for offset in range(0, max(0, len(raw) - 11)):
        try:
            file_id = struct.unpack_from("<i", raw, offset)[0]
        except struct.error:
            continue
        if file_id < 0 or file_id > len(component.assets_file.externals):
            continue
        file_name = source_name_for_file_id(component.assets_file, file_id)
        if not file_name:
            continue
        for path_offset in (4, 8):
            if offset + path_offset + 8 > len(raw):
                continue
            path_id = struct.unpack_from("<q", raw, offset + path_offset)[0]
            if path_id <= 0:
                continue
            target = sprite_lookup.get((file_name, path_id))
            if target is not None:
                found.append(target)
    if not found:
        return None
    unique = {(str(x.assets_file.name), int(x.path_id)): x for x in found}
    return next(iter(unique.values()))


def mono_payload_offset(raw: bytes) -> int | None:
    """Find the first serialized script-specific field in a MonoBehaviour payload."""
    if len(raw) < 32:
        return None
    name_length = struct.unpack_from("<I", raw, 28)[0]
    if name_length > 65536 or 32 + name_length > len(raw):
        return None
    return 32 + ((name_length + 3) & ~3)


def recover_text(component: Any) -> str:
    """Recover UnityEngine.UI.Text.m_Text from the known legacy Text layout."""
    try:
        raw = component.get_raw_data()
    except Exception:
        return ""
    payload = mono_payload_offset(raw)
    if payload is not None and payload + 116 <= len(raw):
        length = struct.unpack_from("<I", raw, payload + 112)[0]
        if length <= 4096 and payload + 116 + length <= len(raw):
            try:
                return raw[payload + 116:payload + 116 + length].decode("utf-8")
            except UnicodeDecodeError:
                pass

    # Defensive fallback for an unexpected serialized layout.
    candidates: list[tuple[int, int, str]] = []
    for offset in range(0, max(0, len(raw) - 3), 4):
        length = struct.unpack_from("<i", raw, offset)[0]
        if length <= 0 or length > 4096 or offset + 4 + length > len(raw):
            continue
        try:
            value = raw[offset + 4:offset + 4 + length].decode("utf-8")
        except UnicodeDecodeError:
            continue
        if value and any(ch.isalnum() for ch in value):
            printable = sum(ch.isprintable() or ch in "\n\r\t" for ch in value)
            if printable / len(value) >= 0.8 and offset >= 96:
                candidates.append((offset, length, value))
    return max(candidates, key=lambda item: (item[0], item[1]))[2] if candidates else ""


def write_json(path: Path, value: Any, compressed: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(value, ensure_ascii=False, separators=(",", ":"), allow_nan=False).encode("utf-8")
    if compressed:
        with path.open("wb") as raw:
            with gzip.GzipFile(fileobj=raw, mode="wb", compresslevel=9, mtime=0) as stream:
                stream.write(payload)
    else:
        path.write_bytes(payload)


def clean_float(value: Any, default: float = 0.0) -> float:
    try:
        result = float(value)
        if result != result or result in (float("inf"), float("-inf")):
            return default
        return result
    except (TypeError, ValueError):
        return default


def safe_int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except (TypeError, ValueError, OverflowError):
        return default


def json_safe(value: Any) -> Any:
    """Convert UnityPy typetree values to strict, deterministic JSON-compatible data."""
    if isinstance(value, dict):
        return {str(key): json_safe(child) for key, child in value.items()}
    if isinstance(value, (list, tuple)):
        return [json_safe(child) for child in value]
    if isinstance(value, float):
        return clean_float(value)
    if isinstance(value, (str, int, bool)) or value is None:
        return value
    if isinstance(value, bytes):
        return {"bytesHex": value.hex()}
    return str(value)


def flatten_vertex_attribute(
    values: Any,
    dimensions: int,
    vertex_count: int,
    field_name: str,
    required: bool = False,
) -> list[float]:
    """Pack a UnityPy per-vertex vector channel into a Unity JsonUtility-friendly array."""
    if values is None or len(values) == 0:
        if required:
            raise ValueError(f"Mesh skin geometry has no {field_name}")
        return []
    if len(values) != vertex_count:
        raise ValueError(
            f"Mesh skin geometry {field_name} has {len(values)} rows for {vertex_count} vertices"
        )

    flattened: list[float] = []
    for vertex_index, row in enumerate(values):
        try:
            components = list(row)
        except TypeError as exc:
            raise ValueError(f"Mesh skin geometry {field_name} vertex {vertex_index} is not a vector") from exc
        if len(components) < dimensions:
            raise ValueError(
                f"Mesh skin geometry {field_name} vertex {vertex_index} has fewer than {dimensions} components"
            )
        for component in components[:dimensions]:
            number = clean_float(component, float("nan"))
            if not math.isfinite(number):
                raise ValueError(
                    f"Mesh skin geometry {field_name} vertex {vertex_index} has a non-finite component"
                )
            flattened.append(number)
    return flattened


def pack_mesh_skin_geometry(handler: Any, vertex_count: int, submesh_count: int) -> dict[str, Any]:
    """Store source vertex streams and triangle indices in the same order as skin weights."""
    vertices = flatten_vertex_attribute(handler.m_Vertices, 3, vertex_count, "vertices", required=True)
    normals = flatten_vertex_attribute(handler.m_Normals, 3, vertex_count, "normals")
    tangents = flatten_vertex_attribute(handler.m_Tangents, 4, vertex_count, "tangents")
    colors = flatten_vertex_attribute(handler.m_Colors, 4, vertex_count, "colors")

    uv_channels: list[dict[str, Any]] = []
    for channel in range(8):
        values = getattr(handler, f"m_UV{channel}", None)
        if values is None or len(values) == 0:
            continue
        try:
            dimensions = len(values[0])
        except TypeError as exc:
            raise ValueError(f"Mesh skin geometry UV{channel} is not a vector channel") from exc
        if dimensions < 1 or dimensions > 4:
            raise ValueError(f"Mesh skin geometry UV{channel} has unsupported dimension {dimensions}")
        uv_channels.append({
            "channel": channel,
            "dimension": dimensions,
            "values": flatten_vertex_attribute(values, dimensions, vertex_count, f"UV{channel}"),
        })

    triangles_by_submesh = handler.get_triangles()
    if len(triangles_by_submesh) != submesh_count:
        raise ValueError(
            f"Mesh skin geometry has {len(triangles_by_submesh)} triangle groups for {submesh_count} submeshes"
        )
    submeshes: list[dict[str, Any]] = []
    for submesh_index, triangles in enumerate(triangles_by_submesh):
        indices: list[int] = []
        for triangle_index, triangle in enumerate(triangles):
            if len(triangle) != 3:
                raise ValueError(
                    f"Mesh skin geometry submesh {submesh_index} triangle {triangle_index} is not triangular"
                )
            for value in triangle:
                index = safe_int(value, -1)
                if index < 0 or index >= vertex_count:
                    raise ValueError(
                        f"Mesh skin geometry submesh {submesh_index} has out-of-range vertex index {index}"
                    )
                indices.append(index)
        submeshes.append({"topology": "Triangles", "indices": indices})

    return {
        "vertexCount": vertex_count,
        "vertices": vertices,
        "normals": normals,
        "tangents": tangents,
        "colors": colors,
        "uvChannels": uv_channels,
        "submeshes": submeshes,
    }


def count_named_list_items(value: Any, field_name: str) -> int:
    """Count entries in every list stored under a matching serialized field."""
    if isinstance(value, dict):
        return sum(
            (len(child) if key == field_name and isinstance(child, list) else 0)
            + count_named_list_items(child, field_name)
            for key, child in value.items()
        )
    if isinstance(value, list):
        return sum(count_named_list_items(child, field_name) for child in value)
    return 0


def count_named_fields(value: Any, field_name: str) -> int:
    """Count occurrences of a field name in a decoded Unity typetree."""
    if isinstance(value, dict):
        return int(field_name in value) + sum(count_named_fields(child, field_name) for child in value.values())
    if isinstance(value, list):
        return sum(count_named_fields(child, field_name) for child in value)
    return 0


def nested_dict(value: Any, *keys: str) -> dict[str, Any]:
    """Return a nested typetree dictionary, or an empty mapping for absent fields."""
    current = value
    for key in keys:
        if not isinstance(current, dict):
            return {}
        current = current.get(key)
    return current if isinstance(current, dict) else {}


def signed_int32(value: Any, default: int = 0) -> int:
    result = safe_int(value, default) & 0xFFFFFFFF
    return result - 0x100000000 if result >= 0x80000000 else result


def strip_fsb5_mpeg_frame_padding(
    packed_audio: bytes,
    sample_count: int,
    expected_frequency: int,
    expected_channels: int,
) -> bytes | None:
    """Remove zero alignment padding and retain exactly the declared MPEG sample span."""
    if sample_count <= 0:
        return None
    bitrate_tables = {
        3: (0, 32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320, 0),
        2: (0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160, 0),
        0: (0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160, 0),
    }
    base_frequencies = (44100, 48000, 32000)
    output = bytearray()
    decoded_samples = 0
    offset = 0
    while decoded_samples < sample_count:
        if offset + 4 > len(packed_audio):
            return None
        header = int.from_bytes(packed_audio[offset:offset + 4], "big")
        if header >> 21 != 0x7FF:
            return None
        version = (header >> 19) & 0x3
        layer = (header >> 17) & 0x3
        bitrate_index = (header >> 12) & 0xF
        frequency_index = (header >> 10) & 0x3
        padding = (header >> 9) & 0x1
        if version == 1 or layer != 1 or bitrate_index in (0, 15) or frequency_index == 3:
            return None
        bitrate = bitrate_tables[version][bitrate_index] * 1000
        frequency = base_frequencies[frequency_index] // {3: 1, 2: 2, 0: 4}[version]
        channels = 1 if ((header >> 6) & 0x3) == 3 else 2
        samples_per_frame = 1152 if version == 3 else 576
        if frequency != expected_frequency or channels != expected_channels or sample_count % samples_per_frame:
            return None
        frame_length = (144 if version == 3 else 72) * bitrate // frequency + padding
        frame_end = offset + frame_length
        if frame_length < 4 or frame_end > len(packed_audio):
            return None
        output.extend(packed_audio[offset:frame_end])
        decoded_samples += samples_per_frame
        aligned_end = (frame_end + 3) & ~3
        if decoded_samples < sample_count:
            if aligned_end > len(packed_audio) or any(packed_audio[frame_end:aligned_end]):
                return None
            offset = aligned_end
        else:
            # FSB5 may pad the end of a sample block with zero bytes too.
            if any(packed_audio[frame_end:]):
                return None
            offset = len(packed_audio)
    return bytes(output) if decoded_samples == sample_count and offset == len(packed_audio) else None


def extract_fsb5_mpeg_audio(tree: dict[str, Any], resource_root: Path) -> bytes | None:
    """Recover the original MP3 frames for large FSB5-backed AudioClips."""
    if load_fsb5 is None:
        return None
    resource = tree.get("m_Resource")
    if not isinstance(resource, dict):
        return None
    source = str(resource.get("m_Source", "")).replace("\\", "/")
    relative_source = PurePosixPath(source)
    if not source or relative_source.is_absolute() or ".." in relative_source.parts:
        return None
    offset = safe_int(resource.get("m_Offset", 0))
    size = safe_int(resource.get("m_Size", 0))
    if offset < 0 or size <= 0:
        return None
    resource_path = resource_root.joinpath(*relative_source.parts)
    if not resource_path.is_file():
        return None
    try:
        resource_bytes = resource_path.read_bytes()
        bank_bytes = resource_bytes[offset:offset + size]
        if len(bank_bytes) != size or not bank_bytes.startswith(b"FSB5"):
            return None
        bank = load_fsb5(bank_bytes)
        if bank.header.mode.name != "MPEG" or bank.raw_size != len(bank_bytes) or len(bank.samples) != 1:
            return None
        sample = bank.samples[0]
        expected_frequency = safe_int(tree.get("m_Frequency", 0))
        expected_channels = safe_int(tree.get("m_Channels", 0))
        if sample.frequency != expected_frequency or sample.channels != expected_channels:
            return None
        packed_audio = bank.rebuild_sample(sample)
        return strip_fsb5_mpeg_frame_padding(
            packed_audio,
            safe_int(sample.samples),
            expected_frequency,
            expected_channels,
        )
    except Exception:
        return None


def raw_color(raw: bytes, offset: int) -> list[float]:

    if offset + 16 > len(raw):
        return [1.0, 1.0, 1.0, 1.0]
    return [clean_float(value, 1.0) for value in struct.unpack_from("<4f", raw, offset)]


def recover_ui_image_data(component: Any) -> dict[str, Any] | None:
    """Decode the stable Unity 2022 UGUI Image serialization layout."""
    try:
        raw = component.get_raw_data()
    except Exception:
        return None
    payload = mono_payload_offset(raw)
    if payload is None or payload + 104 > len(raw):
        return None
    return {
        "color": raw_color(raw, payload + 12),
        "raycastTarget": bool(raw[payload + 28]),
        "raycastPadding": [clean_float(v) for v in struct.unpack_from("<4f", raw, payload + 32)],
        "maskable": bool(raw[payload + 48]),
        "type": safe_int(struct.unpack_from("<i", raw, payload + 68)[0]),
        "preserveAspect": bool(raw[payload + 72]),
        "fillCenter": bool(raw[payload + 76]),
        "fillMethod": safe_int(struct.unpack_from("<i", raw, payload + 80)[0]),
        "fillAmount": clean_float(struct.unpack_from("<f", raw, payload + 84)[0], 1.0),
        "fillClockwise": bool(raw[payload + 88]),
        "fillOrigin": safe_int(struct.unpack_from("<i", raw, payload + 92)[0]),
        "useSpriteMesh": bool(raw[payload + 96]),
        "pixelsPerUnitMultiplier": clean_float(struct.unpack_from("<f", raw, payload + 100)[0], 1.0),
    }


def recover_ui_text_data(component: Any) -> dict[str, Any] | None:
    """Decode Graphic color and the serialized legacy UI Text font/layout settings."""
    try:
        raw = component.get_raw_data()
    except Exception:
        return None
    payload = mono_payload_offset(raw)
    if payload is None or payload + 112 > len(raw):
        return None
    return {
        "color": raw_color(raw, payload + 12),
        "raycastTarget": bool(raw[payload + 28]),
        "raycastPadding": [clean_float(v) for v in struct.unpack_from("<4f", raw, payload + 32)],
        "maskable": bool(raw[payload + 48]),
        "fontSize": safe_int(struct.unpack_from("<i", raw, payload + 68)[0]),
        "fontStyle": safe_int(struct.unpack_from("<i", raw, payload + 72)[0]),
        "bestFit": bool(raw[payload + 76]),
        "minSize": safe_int(struct.unpack_from("<i", raw, payload + 80)[0]),
        "maxSize": safe_int(struct.unpack_from("<i", raw, payload + 84)[0]),
        "alignment": safe_int(struct.unpack_from("<i", raw, payload + 88)[0]),
        "alignByGeometry": bool(raw[payload + 92]),
        "richText": bool(raw[payload + 96]),
        "horizontalOverflow": safe_int(struct.unpack_from("<i", raw, payload + 100)[0]),
        "verticalOverflow": safe_int(struct.unpack_from("<i", raw, payload + 104)[0]),
        "lineSpacing": clean_float(struct.unpack_from("<f", raw, payload + 108)[0], 1.0),
    }


def recover_ui_text_font(component: Any) -> Any | None:
    """Resolve the embedded Font PPtr in UnityEngine.UI.Text raw data."""
    try:
        raw = component.get_raw_data()
    except Exception:
        return None
    payload = mono_payload_offset(raw)
    if payload is None or payload + 68 > len(raw):
        return None
    pointer = {
        "m_FileID": struct.unpack_from("<i", raw, payload + 56)[0],
        "m_PathID": struct.unpack_from("<q", raw, payload + 60)[0],
    }
    target = ptr_target(component.assets_file, pointer)
    return target if target is not None and target.type.name == "Font" else None


def recover_ui_effect_data(component: Any, effect_type: str) -> dict[str, Any] | None:
    """Decode the shared Unity UI Shadow/Outline effect payload."""
    try:
        raw = component.get_raw_data()
        tree = component.read_typetree(check_read=False)
    except Exception:
        return None
    payload = mono_payload_offset(raw)
    if payload is None or payload + 25 > len(raw):
        return None
    return {
        "type": effect_type,
        "enabled": bool(tree.get("m_Enabled", True)),
        "color": raw_color(raw, payload),
        "distance": [clean_float(v) for v in struct.unpack_from("<2f", raw, payload + 16)],
        "useGraphicAlpha": bool(raw[payload + 24]),
    }


def recover_ui_button_data(
    component: Any,
    component_to_game_object: dict[int, int],
    record_asset: Any,
    used_sprites: dict[str, Any],
) -> dict[str, Any] | None:
    """Decode serialized Selectable/Button presentation fields and local targets."""
    try:
        raw = component.get_raw_data()
        tree = component.read_typetree(check_read=False)
    except Exception:
        return None
    payload = mono_payload_offset(raw)
    if payload is None or payload + 208 > len(raw):
        return None

    def pointer_at(offset: int) -> dict[str, int]:
        return {
            "m_FileID": struct.unpack_from("<i", raw, offset)[0],
            "m_PathID": struct.unpack_from("<q", raw, offset + 4)[0],
        }

    def game_object_at(offset: int) -> int:
        pointer = pointer_at(offset)
        if pointer["m_FileID"] != 0 or pointer["m_PathID"] == 0:
            return 0
        return safe_int(component_to_game_object.get(pointer["m_PathID"], 0))

    navigation = {
        "mode": safe_int(struct.unpack_from("<i", raw, payload)[0]),
        "wrapAround": bool(raw[payload + 4]),
        "selectOnUpObject": game_object_at(payload + 8),
        "selectOnDownObject": game_object_at(payload + 20),
        "selectOnLeftObject": game_object_at(payload + 32),
        "selectOnRightObject": game_object_at(payload + 44),
    }
    transition = safe_int(struct.unpack_from("<i", raw, payload + 56)[0])
    color_names = ("normal", "highlighted", "pressed", "selected", "disabled")
    colors = {
        name: raw_color(raw, payload + 60 + index * 16)
        for index, name in enumerate(color_names)
    }
    color_block = {
        **colors,
        "colorMultiplier": clean_float(struct.unpack_from("<f", raw, payload + 140)[0], 1.0),
        "fadeDuration": clean_float(struct.unpack_from("<f", raw, payload + 144)[0], 0.1),
    }

    sprite_names = ("highlighted", "pressed", "selected", "disabled")
    sprites: dict[str, str] = {}
    for index, name in enumerate(sprite_names):
        pointer = pointer_at(payload + 148 + index * 12)
        target = ptr_target(component.assets_file, pointer)
        if target is not None and target.type.name == "Sprite":
            sprite_id = record_asset(target)
            used_sprites[sprite_id] = target
            sprites[name] = sprite_id
        else:
            sprites[name] = ""

    animation_triggers: dict[str, str] = {}
    cursor = payload + 196
    for name in ("normal", "highlighted", "pressed", "selected", "disabled"):
        if cursor + 4 > len(raw):
            return None
        length = struct.unpack_from("<I", raw, cursor)[0]
        if length > 65536 or cursor + 4 + length > len(raw):
            return None
        try:
            animation_triggers[name] = raw[cursor + 4:cursor + 4 + length].decode("utf-8")
        except UnicodeDecodeError:
            return None
        cursor = (cursor + 4 + length + 3) & ~3

    if cursor + 1 > len(raw):
        return None
    interactable = bool(raw[cursor])
    target_graphic_offset = (cursor + 4) & ~3
    if target_graphic_offset + 12 > len(raw):
        return None
    target_graphic_pointer = pointer_at(target_graphic_offset)
    target_object = game_object_at(target_graphic_offset)
    persistent_count_offset = target_graphic_offset + 12
    persistent_call_count = 0
    persistent_calls: list[dict[str, Any]] = []
    if persistent_count_offset + 4 <= len(raw):
        persistent_call_count = safe_int(struct.unpack_from("<i", raw, persistent_count_offset)[0])
        if not 0 <= persistent_call_count <= 10000:
            persistent_call_count = 0
        else:
            def read_serialized_string(offset: int) -> tuple[str, int]:
                if offset + 4 > len(raw):
                    raise ValueError("Truncated serialized UnityEvent string length")
                length = struct.unpack_from("<i", raw, offset)[0]
                if length < 0 or length > 65536 or offset + 4 + length > len(raw):
                    raise ValueError("Invalid serialized UnityEvent string length")
                value = raw[offset + 4:offset + 4 + length].decode("utf-8")
                return value, (offset + 4 + length + 3) & ~3

            cursor = persistent_count_offset + 4
            for call_index in range(persistent_call_count):
                if cursor + 12 > len(raw):
                    raise ValueError("Truncated serialized UnityEvent target pointer")
                target_pointer = {
                    "m_FileID": struct.unpack_from("<i", raw, cursor)[0],
                    "m_PathID": struct.unpack_from("<q", raw, cursor + 4)[0],
                }
                cursor += 12
                target_assembly_type, cursor = read_serialized_string(cursor)
                method_name, cursor = read_serialized_string(cursor)
                if cursor + 4 > len(raw):
                    raise ValueError("Truncated serialized UnityEvent call mode")
                call_mode = safe_int(struct.unpack_from("<i", raw, cursor)[0])
                cursor += 4
                if cursor + 12 > len(raw):
                    raise ValueError("Truncated serialized UnityEvent object argument pointer")
                object_argument = {
                    "m_FileID": struct.unpack_from("<i", raw, cursor)[0],
                    "m_PathID": struct.unpack_from("<q", raw, cursor + 4)[0],
                }
                cursor += 12
                object_argument_type, cursor = read_serialized_string(cursor)
                if cursor + 9 > len(raw):
                    raise ValueError("Truncated serialized UnityEvent arguments")
                int_argument = safe_int(struct.unpack_from("<i", raw, cursor)[0])
                float_argument = clean_float(struct.unpack_from("<f", raw, cursor + 4)[0])
                cursor += 8
                string_argument, cursor = read_serialized_string(cursor)
                if cursor + 1 > len(raw):
                    raise ValueError("Truncated serialized UnityEvent bool argument")
                bool_argument = bool(raw[cursor])
                cursor = (cursor + 1 + 3) & ~3
                if cursor + 4 > len(raw):
                    raise ValueError("Truncated serialized UnityEvent call state")
                call_state = safe_int(struct.unpack_from("<i", raw, cursor)[0])
                cursor += 4

                target = ptr_target(component.assets_file, target_pointer)
                target_type = target.type.name if target is not None else ""
                target_object_id = 0
                target_script: dict[str, str] | None = None
                target_script_status = "targetObjectUnresolved" if target is None else "notApplicable"
                if target is not None:
                    if target.assets_file is component.assets_file and target_pointer["m_FileID"] == 0:
                        if target_type == "GameObject":
                            target_object_id = int(target.path_id)
                        else:
                            target_object_id = safe_int(component_to_game_object.get(int(target.path_id), 0))
                    if target_type == "MonoBehaviour":
                        try:
                            target_tree = target.read_typetree(check_read=False)
                            script_pointer = target_tree.get("m_Script", {}) or {}
                            if safe_int(script_pointer.get("m_PathID", 0)) == 0:
                                target_script_status = "nullScriptPointer"
                            else:
                                target_script = script_record(target, target_tree)
                                target_script_status = "resolved" if target_script else "unresolvedScriptPointer"
                        except Exception:
                            target_script_status = "unreadableMonoBehaviour"

                persistent_calls.append({
                    "targetFileId": target_pointer["m_FileID"],
                    "targetPathId": target_pointer["m_PathID"],
                    "targetType": target_type,
                    "targetObjectId": target_object_id,
                    "targetScript": target_script["qualifiedName"] if target_script else "",
                    "targetScriptAssembly": target_script["assembly"] if target_script else "",
                    "targetScriptStatus": target_script_status,
                    "targetAssemblyTypeName": target_assembly_type,
                    "methodName": method_name,
                    "mode": call_mode,
                    "objectArgumentFileId": object_argument["m_FileID"],
                    "objectArgumentPathId": object_argument["m_PathID"],
                    "objectArgumentAssemblyTypeName": object_argument_type,
                    "intArgument": int_argument,
                    "floatArgument": float_argument,
                    "stringArgument": string_argument,
                    "boolArgument": bool_argument,
                    "callState": call_state,
                })

    return {
        "enabled": bool(tree.get("m_Enabled", True)),
        "interactable": interactable,
        "transition": transition,
        "navigation": navigation,
        "colors": color_block,
        "sprites": sprites,
        "animationTriggers": animation_triggers,
        "targetGraphicPresent": bool(target_graphic_pointer["m_PathID"]),
        "targetGraphicObject": target_object,
        "persistentCallCount": persistent_call_count,
        "persistentCalls": persistent_calls,
        "persistentCallsDecoded": len(persistent_calls) == persistent_call_count,
    }


def recover_canvas_scaler_data(component: Any) -> dict[str, Any] | None:
    """Decode the UnityEngine.UI.CanvasScaler serialized fields (fixed-layout UGUI data)."""
    try:
        raw = component.get_raw_data()
    except Exception:
        return None
    payload = mono_payload_offset(raw)
    if payload is None or payload + 45 > len(raw):
        return None
    return {
        "uiScaleMode": safe_int(struct.unpack_from("<i", raw, payload)[0]),
        "referencePixelsPerUnit": clean_float(struct.unpack_from("<f", raw, payload + 4)[0], 100.0),
        "scaleFactor": clean_float(struct.unpack_from("<f", raw, payload + 8)[0], 1.0),
        "referenceResolution": [clean_float(v, 1080.0) for v in struct.unpack_from("<2f", raw, payload + 12)],
        "screenMatchMode": safe_int(struct.unpack_from("<i", raw, payload + 20)[0]),
        "matchWidthOrHeight": clean_float(struct.unpack_from("<f", raw, payload + 24)[0], 0.5),
        "physicalUnit": safe_int(struct.unpack_from("<i", raw, payload + 28)[0]),
        "fallbackScreenDPI": clean_float(struct.unpack_from("<f", raw, payload + 32)[0], 96.0),
        "defaultSpriteDPI": clean_float(struct.unpack_from("<f", raw, payload + 36)[0], 96.0),
        "dynamicPixelsPerUnit": clean_float(struct.unpack_from("<f", raw, payload + 40)[0], 1.0),
        "presetInfoIsWorld": bool(raw[payload + 44]),
    }


def extract(
    source: Path,
    include_audio: bool = False,
    include_audio_sfx: bool = False,
    output_root: Path = ASSET_ROOT,
) -> dict[str, Any]:
    output_root = output_root.resolve()
    temp_root = Path(tempfile.mkdtemp(prefix="rage-unity-extract-"))
    try:
        raw_data = input_data_folder(source, temp_root)
        merged = merge_split_files(raw_data, temp_root / "merged-data")
        environment = UnityPy.load(str(merged))
        files = file_map(environment)
        build_scenes: list[str] = []
        build_settings = next((o for o in environment.objects if o.type.name == "BuildSettings"), None)
        if build_settings:
            try:
                build_scenes = list(build_settings.read_typetree(check_read=False).get("scenes", []))
            except Exception:
                pass
        scene_file_names = ["level0", "level1", "level2", "level3"]
        scene_label_map = {
            "level0": "00 - Splash",
            "level1": "01 - MainMenu",
            "level2": "02 - GamePlay",
            "level3": "03 - Z-GamePlay",
        }

        sprite_lookup: dict[tuple[str, int], Any] = {}
        all_sprites = [o for o in environment.objects if o.type.name == "Sprite"]
        for obj in all_sprites:
            sprite_lookup[(str(obj.assets_file.name).replace("\\", "/").split("/")[-1].lower(), int(obj.path_id))] = obj

        asset_objects: dict[tuple[str, str, int], Any] = {}
        used_meshes: dict[str, Any] = {}
        used_materials: dict[str, Any] = {}
        used_textures: dict[str, Any] = {}
        used_sprites: dict[str, Any] = {}
        used_fonts: dict[str, Any] = {}
        audio_sources: dict[str, dict[str, Any]] = {}
        scene_payload: list[dict[str, Any]] = []
        script_counts: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
        component_counts: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
        export_errors: list[str] = []

        def record_asset(obj: Any, kind: str | None = None) -> str:
            use_kind = kind or obj.type.name
            key = (use_kind, str(obj.assets_file.name), int(obj.path_id))
            asset_objects[key] = obj
            return object_id(obj, use_kind)

        def ref_id(source_file: Any, pointer_value: Any, expected: str | None = None) -> str | None:
            target = ptr_target(source_file, pointer_value)
            if target is None:
                return None
            if expected and target.type.name not in expected.split("|"):
                return None
            return record_asset(target)

        for scene_index, file_name in enumerate(scene_file_names):
            scene_file = files.get(file_name.lower())
            if scene_file is None:
                export_errors.append(f"Missing scene serialized file: {file_name}")
                continue
            game_objects = [o for o in scene_file.objects.values() if o.type.name == "GameObject"]
            transform_to_game_object: dict[int, int] = {}
            component_to_game_object: dict[int, int] = {}
            raw_records: list[dict[str, Any]] = []
            for go in game_objects:
                try:
                    go_tree = go.read_typetree(check_read=False)
                except Exception as exc:
                    export_errors.append(f"GameObject {file_name}:{go.path_id}: {exc}")
                    continue
                components: list[Any] = []
                for component_ref in go_tree.get("m_Component", []) or []:
                    ptr = component_ref.get("component", {}) if isinstance(component_ref, dict) else {}
                    comp = ptr_target(scene_file, ptr)
                    if comp is None:
                        continue
                    components.append(comp)
                    component_to_game_object[int(comp.path_id)] = int(go.path_id)
                    if comp.type.name in ("Transform", "RectTransform"):
                        transform_to_game_object[int(comp.path_id)] = int(go.path_id)
                raw_records.append({"object": go, "tree": go_tree, "components": components})

            scene_objects: list[dict[str, Any]] = []
            for rec in raw_records:
                go = rec["object"]
                go_tree = rec["tree"]
                components = rec["components"]
                name = str(go_tree.get("m_Name") or f"GameObject_{go.path_id}")
                script_types: list[str] = []
                component_types: list[str] = []
                mesh_ids: list[str] = []
                material_ids: list[str] = []
                sprite_id: str | None = None
                text_value = ""
                transform_data: dict[str, Any] | None = None
                parent_transform_id = 0
                ui_image = False
                ui_text = False
                ui_button = False
                ui_button_data: dict[str, Any] | None = None
                ui_canvas = False
                ui_image_data: dict[str, Any] | None = None
                ui_text_data: dict[str, Any] | None = None
                ui_effects: list[dict[str, Any]] = []
                canvas_scaler_data: dict[str, Any] | None = None
                canvas_data: dict[str, Any] | None = None
                canvas_group_data: dict[str, Any] | None = None
                renderer_data: list[dict[str, Any]] = []
                camera_data: dict[str, Any] | None = None
                light_data: dict[str, Any] | None = None
                audio_clip_id: str | None = None
                audio_source_data: dict[str, Any] | None = None
                animator_data: dict[str, Any] | None = None
                legacy_animation_data: dict[str, Any] | None = None
                collider_data: list[dict[str, Any]] = []
                rigidbody_data: dict[str, Any] | None = None
                character_joint_data: dict[str, Any] | None = None
                nav_agent_data: dict[str, Any] | None = None
                nav_obstacle_data: dict[str, Any] | None = None
                for comp in components:
                    comp_type = comp.type.name
                    component_types.append(comp_type)
                    component_counts[file_name][comp_type] += 1
                    try:
                        comp_tree = comp.read_typetree(check_read=False)
                    except Exception:
                        comp_tree = {}
                    if comp_type in ("Transform", "RectTransform"):
                        father = comp_tree.get("m_Father", {}) or {}
                        parent_transform_id = int(father.get("m_PathID", 0) or 0)
                        transform_data = {
                            "kind": comp_type,
                            "position": vec3(comp_tree.get("m_LocalPosition")),
                            "rotation": vec4(comp_tree.get("m_LocalRotation"), (0.0, 0.0, 0.0, 1.0)),
                            "scale": vec3(comp_tree.get("m_LocalScale"), (1.0, 1.0, 1.0)),
                        }
                        if comp_type == "RectTransform":
                            transform_data.update({
                                "anchorMin": vec2(comp_tree.get("m_AnchorMin")),
                                "anchorMax": vec2(comp_tree.get("m_AnchorMax"), (1.0, 1.0)),
                                "anchoredPosition": vec3(comp_tree.get("m_AnchoredPosition")),
                                "sizeDelta": vec2(comp_tree.get("m_SizeDelta")),
                                "pivot": vec2(comp_tree.get("m_Pivot"), (0.5, 0.5)),
                            })
                    elif comp_type == "MeshFilter":
                        mesh_id = ref_id(comp.assets_file, comp_tree.get("m_Mesh"), "Mesh")
                        if mesh_id:
                            mesh_ids.append(mesh_id)
                            used_meshes[mesh_id] = ptr_target(comp.assets_file, comp_tree.get("m_Mesh"))
                    elif comp_type in ("MeshRenderer", "SkinnedMeshRenderer", "SpriteRenderer", "ParticleSystemRenderer"):
                        renderer_entry = {
                            "type": comp_type,
                            "enabled": bool(comp_tree.get("m_Enabled", True)),
                            "castShadows": safe_int(comp_tree.get("m_CastShadows", 0)),
                            "receiveShadows": bool(comp_tree.get("m_ReceiveShadows", False)),
                            "motionVectors": safe_int(comp_tree.get("m_MotionVectors", 0)),
                            "lightProbeUsage": safe_int(comp_tree.get("m_LightProbeUsage", 0)),
                            "reflectionProbeUsage": safe_int(comp_tree.get("m_ReflectionProbeUsage", 0)),
                            "renderingLayerMask": safe_int(comp_tree.get("m_RenderingLayerMask", 1), 1),
                            "sortingLayerId": safe_int(comp_tree.get("m_SortingLayerID", 0)),
                            "sortingOrder": safe_int(comp_tree.get("m_SortingOrder", 0)),
                        }
                        if comp_type == "SpriteRenderer":
                            renderer_entry.update({
                                "color": color4(comp_tree.get("m_Color")),
                                "flipX": bool(comp_tree.get("m_FlipX", False)),
                                "flipY": bool(comp_tree.get("m_FlipY", False)),
                                "drawMode": safe_int(comp_tree.get("m_DrawMode", 0)),
                                "size": vec2(comp_tree.get("m_Size")),
                                "spriteTileMode": safe_int(comp_tree.get("m_SpriteTileMode", 0)),
                                "maskInteraction": safe_int(comp_tree.get("m_MaskInteraction", 0)),
                                "spriteSortPoint": safe_int(comp_tree.get("m_SpriteSortPoint", 0)),
                            })
                        renderer_data.append(renderer_entry)
                        if comp_type == "SkinnedMeshRenderer":
                            mesh_pointer = comp_tree.get("m_Mesh", {}) or {}
                            mesh_id = ref_id(comp.assets_file, mesh_pointer, "Mesh")
                            if mesh_id:
                                mesh_ids.append(mesh_id)
                                used_meshes[mesh_id] = ptr_target(comp.assets_file, mesh_pointer)
                            root_bone = comp_tree.get("m_RootBone", {}) or {}
                            root_file_id = safe_int(root_bone.get("m_FileID", 0))
                            root_path_id = safe_int(root_bone.get("m_PathID", 0))
                            root_object_id = safe_int(component_to_game_object.get(root_path_id, 0)) if root_file_id == 0 else 0
                            bone_file_ids: list[int] = []
                            bone_path_ids: list[int] = []
                            bone_object_ids: list[int] = []
                            for bone_pointer in comp_tree.get("m_Bones", []) or []:
                                bone_pointer = bone_pointer if isinstance(bone_pointer, dict) else {}
                                bone_file_id = safe_int(bone_pointer.get("m_FileID", 0))
                                bone_path_id = safe_int(bone_pointer.get("m_PathID", 0))
                                bone_file_ids.append(bone_file_id)
                                bone_path_ids.append(bone_path_id)
                                bone_object_ids.append(
                                    safe_int(component_to_game_object.get(bone_path_id, 0))
                                    if bone_file_id == 0 else 0
                                )
                            local_bounds = comp_tree.get("m_AABB", {}) or {}
                            renderer_entry.update({
                                "meshId": mesh_id or "",
                                "rootBoneFileId": root_file_id,
                                "rootBonePathId": root_path_id,
                                "rootBoneObject": root_object_id,
                                "boneFileIds": bone_file_ids,
                                "bonePathIds": bone_path_ids,
                                "boneObjects": bone_object_ids,
                                "boneCount": len(bone_path_ids),
                                "quality": safe_int(comp_tree.get("m_Quality", 0)),
                                "updateWhenOffscreen": bool(comp_tree.get("m_UpdateWhenOffscreen", False)),
                                "skinnedMotionVectors": bool(comp_tree.get("m_SkinnedMotionVectors", False)),
                                "localBoundsCenter": vec3(local_bounds.get("m_Center")),
                                "localBoundsExtents": vec3(local_bounds.get("m_Extent")),
                            })
                        if comp_type in ("MeshRenderer", "SkinnedMeshRenderer", "ParticleSystemRenderer"):
                            for material_ref in comp_tree.get("m_Materials", []) or []:
                                material_id = ref_id(comp.assets_file, material_ref, "Material")
                                if material_id:
                                    material_ids.append(material_id)
                                    used_materials[material_id] = ptr_target(comp.assets_file, material_ref)
                        if comp_type == "SpriteRenderer":
                            sprite_target = ptr_target(comp.assets_file, comp_tree.get("m_Sprite"))
                            if sprite_target is not None and sprite_target.type.name == "Sprite":
                                sprite_id = record_asset(sprite_target)
                                used_sprites[sprite_id] = sprite_target
                    elif comp_type == "Animator":
                        controller_id = ref_id(
                            comp.assets_file,
                            comp_tree.get("m_Controller"),
                            "AnimatorController|AnimatorOverrideController",
                        )
                        avatar_id = ref_id(comp.assets_file, comp_tree.get("m_Avatar"), "Avatar")
                        animator_data = {
                            "enabled": bool(comp_tree.get("m_Enabled", True)),
                            "controllerId": controller_id or "",
                            "avatarId": avatar_id or "",
                            "cullingMode": safe_int(comp_tree.get("m_CullingMode", 0)),
                            "updateMode": safe_int(comp_tree.get("m_UpdateMode", 0)),
                            "applyRootMotion": bool(comp_tree.get("m_ApplyRootMotion", False)),
                            "linearVelocityBlending": bool(comp_tree.get("m_LinearVelocityBlending", False)),
                            "stabilizeFeet": bool(comp_tree.get("m_StabilizeFeet", False)),
                            "hasTransformHierarchy": bool(comp_tree.get("m_HasTransformHierarchy", False)),
                            "allowConstantClipSamplingOptimization": bool(comp_tree.get("m_AllowConstantClipSamplingOptimization", False)),
                            "keepAnimatorStateOnDisable": bool(comp_tree.get("m_KeepAnimatorStateOnDisable", False)),
                            "writeDefaultValuesOnDisable": bool(comp_tree.get("m_WriteDefaultValuesOnDisable", False)),
                        }
                    elif comp_type == "Animation":
                        default_clip_id = ref_id(comp.assets_file, comp_tree.get("m_Animation"), "AnimationClip")
                        clip_ids = [
                            clip_id
                            for clip_pointer in comp_tree.get("m_Animations", []) or []
                            if (clip_id := ref_id(comp.assets_file, clip_pointer, "AnimationClip"))
                        ]
                        legacy_animation_data = {
                            "enabled": bool(comp_tree.get("m_Enabled", True)),
                            "defaultClipId": default_clip_id or "",
                            "clipIds": list(dict.fromkeys(clip_ids)),
                            "wrapMode": safe_int(comp_tree.get("m_WrapMode", 0)),
                            "playAutomatically": bool(comp_tree.get("m_PlayAutomatically", True)),
                            "animatePhysics": bool(comp_tree.get("m_AnimatePhysics", False)),
                            "cullingType": safe_int(comp_tree.get("m_CullingType", 0)),
                        }
                    elif comp_type in ("BoxCollider", "SphereCollider", "CapsuleCollider", "MeshCollider"):
                        collider = {
                            "type": comp_type,
                            "enabled": bool(comp_tree.get("m_Enabled", True)),
                            "isTrigger": bool(comp_tree.get("m_IsTrigger", False)),
                            "center": vec3(comp_tree.get("m_Center")),
                        }
                        if comp_type == "BoxCollider":
                            collider["size"] = vec3(comp_tree.get("m_Size"), (1.0, 1.0, 1.0))
                        elif comp_type == "SphereCollider":
                            collider["radius"] = clean_float(comp_tree.get("m_Radius", 0.5), 0.5)
                        elif comp_type == "CapsuleCollider":
                            collider["radius"] = clean_float(comp_tree.get("m_Radius", 0.5), 0.5)
                            collider["height"] = clean_float(comp_tree.get("m_Height", 2.0), 2.0)
                            collider["direction"] = int(comp_tree.get("m_Direction", 1) or 0)
                        else:
                            collider["convex"] = bool(comp_tree.get("m_Convex", False))
                            mesh_pointer = comp_tree.get("m_Mesh")
                            mesh_id = ref_id(comp.assets_file, mesh_pointer, "Mesh")
                            if mesh_id:
                                collider["mesh"] = mesh_id
                                mesh_ids.append(mesh_id)
                                used_meshes[mesh_id] = ptr_target(comp.assets_file, mesh_pointer)
                        collider_data.append(collider)
                    elif comp_type == "Rigidbody":
                        rigidbody_data = {
                            "mass": clean_float(comp_tree.get("m_Mass", 1.0), 1.0),
                            "drag": clean_float(comp_tree.get("m_Drag", 0.0)),
                            "angularDrag": clean_float(comp_tree.get("m_AngularDrag", 0.05), 0.05),
                            "useGravity": bool(comp_tree.get("m_UseGravity", True)),
                            "isKinematic": bool(comp_tree.get("m_IsKinematic", False)),
                            "interpolation": int(comp_tree.get("m_Interpolate", 0) or 0),
                            "constraints": int(comp_tree.get("m_Constraints", 0) or 0),
                            "collisionDetection": int(comp_tree.get("m_CollisionDetection", 0) or 0),
                            "enabled": True,
                        }
                    elif comp_type == "CharacterJoint":
                        connected = comp_tree.get("m_ConnectedBody", {}) or {}
                        connected_id = 0
                        if int(connected.get("m_FileID", 0) or 0) == 0:
                            connected_id = component_to_game_object.get(int(connected.get("m_PathID", 0) or 0), 0)
                        character_joint_data = {
                            "connectedBodyObject": int(connected_id),
                            "anchor": vec3(comp_tree.get("m_Anchor")),
                            "axis": vec3(comp_tree.get("m_Axis"), (1.0, 0.0, 0.0)),
                            "swingAxis": vec3(comp_tree.get("m_SwingAxis"), (0.0, 1.0, 0.0)),
                            "connectedAnchor": vec3(comp_tree.get("m_ConnectedAnchor")),
                            "autoConfigureConnectedAnchor": bool(comp_tree.get("m_AutoConfigureConnectedAnchor", True)),
                            "enableCollision": bool(comp_tree.get("m_EnableCollision", False)),
                            "breakForce": clean_float(comp_tree.get("m_BreakForce", 3.0e30), 3.0e30),
                            "breakTorque": clean_float(comp_tree.get("m_BreakTorque", 3.0e30), 3.0e30),
                            "massScale": clean_float(comp_tree.get("m_MassScale", 1.0), 1.0),
                            "connectedMassScale": clean_float(comp_tree.get("m_ConnectedMassScale", 1.0), 1.0),
                        }
                    elif comp_type == "NavMeshAgent":
                        nav_agent_data = {
                            "enabled": bool(comp_tree.get("m_Enabled", True)),
                            "radius": clean_float(comp_tree.get("m_Radius", 0.5), 0.5),
                            "height": clean_float(comp_tree.get("m_Height", 2.0), 2.0),
                            "speed": clean_float(comp_tree.get("m_Speed", 3.5), 3.5),
                            "acceleration": clean_float(comp_tree.get("m_Acceleration", 8.0), 8.0),
                            "angularSpeed": clean_float(comp_tree.get("m_AngularSpeed", 120.0), 120.0),
                            "stoppingDistance": clean_float(comp_tree.get("m_StoppingDistance", 0.0)),
                            "baseOffset": clean_float(comp_tree.get("m_BaseOffset", 0.0)),
                            "avoidancePriority": int(comp_tree.get("avoidancePriority", 50) or 50),
                            "autoBraking": bool(comp_tree.get("m_AutoBraking", True)),
                            "autoRepath": bool(comp_tree.get("m_AutoRepath", True)),
                        }
                    elif comp_type == "NavMeshObstacle":
                        nav_obstacle_data = {
                            "enabled": bool(comp_tree.get("m_Enabled", True)),
                            "radius": clean_float(comp_tree.get("m_Radius", 0.5), 0.5),
                            "height": clean_float(comp_tree.get("m_Height", 2.0), 2.0),
                            "carving": bool(comp_tree.get("m_Carve", False)),
                        }
                    elif comp_type == "MonoBehaviour":
                        script = script_record(comp, comp_tree)
                        if script:
                            qualified = script["qualifiedName"]
                            script_types.append(qualified)
                            script_counts[file_name][qualified] += 1
                            if script["assembly"] == "UnityEngine.UI":
                                if script["className"] == "Image":
                                    ui_image = True
                                    ui_image_data = recover_ui_image_data(comp)
                                    sprite_target = find_sprite_pointer(comp, sprite_lookup)
                                    if sprite_target is not None:
                                        sprite_id = record_asset(sprite_target)
                                        used_sprites[sprite_id] = sprite_target
                                elif script["className"] == "Text":
                                    ui_text = True
                                    ui_text_data = recover_ui_text_data(comp)
                                    font_target = recover_ui_text_font(comp)
                                    if font_target is not None:
                                        font_id = record_asset(font_target, "Font")
                                        used_fonts[font_id] = font_target
                                        if ui_text_data is not None:
                                            ui_text_data["fontId"] = font_id
                                    text_value = recover_text(comp)
                                elif script["className"] == "Button":
                                    ui_button = True
                                    ui_button_data = recover_ui_button_data(
                                        comp, component_to_game_object, record_asset, used_sprites
                                    )
                                elif script["className"] == "CanvasScaler":
                                    ui_canvas = True
                                    canvas_scaler_data = recover_canvas_scaler_data(comp)
                                elif script["className"] in ("Shadow", "Outline"):
                                    effect_data = recover_ui_effect_data(comp, script["className"])
                                    if effect_data is not None:
                                        ui_effects.append(effect_data)
                            if qualified.endswith("CanvasScaler"):
                                ui_canvas = True
                    elif comp_type == "CanvasGroup":
                        canvas_group_data = {
                            "enabled": bool(comp_tree.get("m_Enabled", True)),
                            "alpha": clean_float(comp_tree.get("m_Alpha", 1.0), 1.0),
                            "interactable": bool(comp_tree.get("m_Interactable", True)),
                            "blocksRaycasts": bool(comp_tree.get("m_BlocksRaycasts", True)),
                            "ignoreParentGroups": bool(comp_tree.get("m_IgnoreParentGroups", False)),
                        }
                    elif comp_type == "Canvas":
                        ui_canvas = True
                        camera_pointer = comp_tree.get("m_Camera", {}) or {}
                        camera_object_id = 0
                        if safe_int(camera_pointer.get("m_FileID", 0)) == 0:
                            camera_object_id = component_to_game_object.get(safe_int(camera_pointer.get("m_PathID", 0)), 0)
                        canvas_data = {
                            "enabled": bool(comp_tree.get("m_Enabled", True)),
                            "renderMode": safe_int(comp_tree.get("m_RenderMode", 0)),
                            "worldCameraObject": int(camera_object_id),
                            "planeDistance": clean_float(comp_tree.get("m_PlaneDistance", 100.0), 100.0),
                            "pixelPerfect": bool(comp_tree.get("m_PixelPerfect", False)),
                            "receivesEvents": bool(comp_tree.get("m_ReceivesEvents", True)),
                            "overrideSorting": bool(comp_tree.get("m_OverrideSorting", False)),
                            "sortingLayerId": safe_int(comp_tree.get("m_SortingLayerID", 0)),
                            "sortingOrder": safe_int(comp_tree.get("m_SortingOrder", 0)),
                            "targetDisplay": safe_int(comp_tree.get("m_TargetDisplay", 0)),
                        }
                    elif comp_type == "AudioSource":
                        audio_id = ref_id(comp.assets_file, comp_tree.get("m_audioClip"), "AudioClip")
                        if audio_id:
                            audio_clip_id = audio_id
                            audio_sources[audio_id] = {"id": audio_id}
                        audio_source_data = {
                            "enabled": bool(comp_tree.get("m_Enabled", True)),
                            "clip": audio_id or "",
                            "playOnAwake": bool(comp_tree.get("m_PlayOnAwake", False)),
                            "loop": bool(comp_tree.get("Loop", False)),
                            "volume": clean_float(comp_tree.get("m_Volume", 1.0), 1.0),
                            "pitch": clean_float(comp_tree.get("m_Pitch", 1.0), 1.0),
                            "priority": int(comp_tree.get("Priority", 128) or 128),
                            "minDistance": clean_float(comp_tree.get("MinDistance", 1.0), 1.0),
                            "maxDistance": clean_float(comp_tree.get("MaxDistance", 500.0), 500.0),
                        }
                    elif comp_type == "Camera":
                        viewport = comp_tree.get("m_NormalizedViewPortRect", {}) or {}
                        culling_mask = comp_tree.get("m_CullingMask", {}) or {}
                        camera_data = {
                            "enabled": bool(comp_tree.get("m_Enabled", True)),
                            "orthographic": bool(comp_tree.get("orthographic", False)),
                            "fieldOfView": clean_float(comp_tree.get("field of view", comp_tree.get("fieldOfView", 60.0)), 60.0),
                            "nearClip": clean_float(comp_tree.get("near clip plane", comp_tree.get("nearClipPlane", 0.3)), 0.3),
                            "farClip": clean_float(comp_tree.get("far clip plane", comp_tree.get("farClipPlane", 1000.0)), 1000.0),
                            "orthographicSize": clean_float(comp_tree.get("orthographic size", comp_tree.get("orthographicSize", 5.0)), 5.0),
                            "clearFlags": safe_int(comp_tree.get("m_ClearFlags", 1), 1),
                            "backgroundColor": color4(comp_tree.get("m_BackGroundColor")),
                            "viewportRect": [
                                clean_float(viewport.get("x")), clean_float(viewport.get("y")),
                                clean_float(viewport.get("width", 1.0), 1.0), clean_float(viewport.get("height", 1.0), 1.0),
                            ],
                            "depth": clean_float(comp_tree.get("m_Depth", 0.0)),
                            "cullingMask": signed_int32(culling_mask.get("m_Bits", 0xFFFFFFFF), -1),
                            "allowHDR": bool(comp_tree.get("m_HDR", True)),
                            "allowMSAA": bool(comp_tree.get("m_AllowMSAA", True)),
                            "useOcclusionCulling": bool(comp_tree.get("m_OcclusionCulling", True)),
                            "renderingPath": safe_int(comp_tree.get("m_RenderingPath", -1), -1),
                        }
                    elif comp_type == "Light":
                        shadows = comp_tree.get("m_Shadows", {}) or {}
                        area_size = comp_tree.get("m_AreaSize", {}) or {}
                        light_data = {
                            "enabled": bool(comp_tree.get("m_Enabled", True)),
                            "type": safe_int(comp_tree.get("m_Type", 1), 1),
                            "color": color4(comp_tree.get("m_Color")),
                            "intensity": clean_float(comp_tree.get("m_Intensity", 1.0), 1.0),
                            "range": clean_float(comp_tree.get("m_Range", 10.0), 10.0),
                            "spotAngle": clean_float(comp_tree.get("m_SpotAngle", 30.0), 30.0),
                            "innerSpotAngle": clean_float(comp_tree.get("m_InnerSpotAngle", 21.8), 21.8),
                            "shadows": safe_int(shadows.get("m_Type", 0)),
                            "shadowStrength": clean_float(shadows.get("m_Strength", 1.0), 1.0),
                            "shadowBias": clean_float(shadows.get("m_Bias", 0.05), 0.05),
                            "shadowNormalBias": clean_float(shadows.get("m_NormalBias", 0.4), 0.4),
                            "drawHalo": bool(comp_tree.get("m_DrawHalo", False)),
                            "bounceIntensity": clean_float(comp_tree.get("m_BounceIntensity", 1.0), 1.0),
                            "useColorTemperature": bool(comp_tree.get("m_UseColorTemperature", False)),
                            "colorTemperature": clean_float(comp_tree.get("m_ColorTemperature", 6570.0), 6570.0),
                            "areaSize": vec2(area_size, (1.0, 1.0)),
                        }

                # Material references on SpriteRenderer do not affect its texture;
                # Sprite is stored separately as an editable single-sprite PNG.
                transform = transform_data or {
                    "kind": "Transform",
                    "position": [0.0, 0.0, 0.0],
                    "rotation": [0.0, 0.0, 0.0, 1.0],
                    "scale": [1.0, 1.0, 1.0],
                }
                parent_go = transform_to_game_object.get(parent_transform_id, 0) if parent_transform_id else 0
                scene_objects.append({
                    "id": int(go.path_id),
                    "name": name,
                    "active": bool(go_tree.get("m_IsActive", True)),
                    "layer": int(go_tree.get("m_Layer", 0) or 0),
                    "tag": str(go_tree.get("m_TagString", "Untagged") or "Untagged"),
                    "parent": int(parent_go),
                    "transform": transform,
                    "components": sorted(set(component_types)),
                    "scripts": sorted(set(script_types)),
                    "meshes": list(dict.fromkeys(mesh_ids)),
                    "materials": list(dict.fromkeys(material_ids)),
                    "sprite": sprite_id or "",
                    "text": text_value,
                    "uiImage": ui_image,
                    "uiText": ui_text,
                    "uiButton": ui_button,
                    "uiButtonData": ui_button_data,
                    "uiCanvas": ui_canvas,
                    "uiImageData": ui_image_data,
                    "uiTextData": ui_text_data,
                    "uiEffects": ui_effects,
                    "canvasScaler": canvas_scaler_data,
                    "canvas": canvas_data,
                    "canvasGroup": canvas_group_data,
                    "renderers": renderer_data,
                    "camera": camera_data,
                    "light": light_data,
                    "audioClip": audio_clip_id or "",
                    "audioSource": audio_source_data,
                    "animator": animator_data,
                    "legacyAnimation": legacy_animation_data,
                    "colliders": collider_data,
                    "rigidbody": rigidbody_data,
                    "characterJoint": character_joint_data,
                    "navMeshAgent": nav_agent_data,
                    "navMeshObstacle": nav_obstacle_data,
                })

            scene_payload.append({
                "key": file_name,
                "name": scene_label_map.get(file_name, SCENE_BUILD_NAMES[scene_index]),
                "buildScene": build_scenes[scene_index] if scene_index < len(build_scenes) else "",
                "objectCount": len(scene_objects),
                "objects": scene_objects,
            })

        # Some editable UI prefab roots live in sharedassets files, not scenes.
        try:
            from .ui_prefab_extraction import extract_shared_ui_prefabs
        except ImportError:
            from ui_prefab_extraction import extract_shared_ui_prefabs
        ui_prefab_records = extract_shared_ui_prefabs(
            files.get("sharedassets2.assets"), sprite_lookup, record_asset, used_sprites, used_fonts
        )

        # Resolve textures referenced by exported Materials.
        material_records: list[dict[str, Any]] = []
        for material_id, material in sorted(used_materials.items()):
            try:
                tree = material.read_typetree(check_read=False)
            except Exception as exc:
                export_errors.append(f"Material {material_id}: {exc}")
                continue
            shader_name = ""
            shader = ptr_target(material.assets_file, tree.get("m_Shader"))
            if shader is not None:
                try:
                    shader_name = str(shader.read_typetree(check_read=False).get("m_Name", ""))
                except Exception:
                    pass
            properties = tree.get("m_SavedProperties", {}) or {}
            colors = []
            for entry in properties.get("m_Colors", []) or []:
                try:
                    property_name, value = entry
                    colors.append({"property": str(property_name), "value": color4(value)})
                except Exception:
                    continue
            floats = []
            for entry in properties.get("m_Floats", []) or []:
                try:
                    property_name, value = entry
                    floats.append({"property": str(property_name), "value": clean_float(value)})
                except Exception:
                    continue
            textures = []
            for entry in properties.get("m_TexEnvs", []) or []:
                try:
                    property_name, value = entry
                    texture = ptr_target(material.assets_file, value.get("m_Texture"))
                    if texture is None or texture.type.name not in ("Texture2D", "Cubemap"):
                        continue
                    texture_id = record_asset(texture)
                    used_textures[texture_id] = texture
                    textures.append({
                        "property": str(property_name),
                        "textureId": texture_id,
                        "scale": vec2(value.get("m_Scale"), (1.0, 1.0)),
                        "offset": vec2(value.get("m_Offset")),
                    })
                except Exception:
                    continue
            material_records.append({
                "id": material_id,
                "name": str(tree.get("m_Name", material_id)),
                "shaderName": shader_name,
                "colors": colors,
                "floats": floats,
                "textures": textures,
            })

        output_root.mkdir(parents=True, exist_ok=True)
        for folder in ("Meshes", "Textures", "Sprites", "Fonts", "Compressed", "Manifests", "GeneratedMeshes", "Materials"):
            (output_root / folder).mkdir(parents=True, exist_ok=True)

        font_records: list[dict[str, Any]] = []
        exported_font_bytes = 0
        all_font_objects = [obj for obj in environment.objects if obj.type.name == "Font"]
        for font in all_font_objects:
            try:
                tree = font.read_typetree(check_read=False)
                font_data = bytes(tree.get("m_FontData", []) or [])
                suffix = ".otf" if font_data.startswith(b"OTTO") else ".ttf" if font_data.startswith(bytes.fromhex("00010000")) else ""
                if not suffix:
                    raise ValueError("Font data has no recognized TrueType/OpenType signature")
                font_id = object_id(font, "Font")
                filename = f"{font_id}{suffix}"
                (output_root / "Fonts" / filename).write_bytes(font_data)
                referenced_by_ui = font_id in used_fonts
                font_records.append({
                    "id": font_id,
                    "name": str(tree.get("m_Name", font_id)),
                    "fontNames": [str(name) for name in tree.get("m_FontNames", []) or []],
                    "sourceFile": str(font.assets_file.name),
                    "sourcePathId": int(font.path_id),
                    "defaultStyle": safe_int(tree.get("m_DefaultStyle", 0)),
                    "lineSpacing": clean_float(tree.get("m_LineSpacing", 0.0)),
                    "ascent": clean_float(tree.get("m_Ascent", 0.0)),
                    "descent": clean_float(tree.get("m_Descent", 0.0)),
                    "assetPath": f"Assets/Recovered/Fonts/{filename}",
                    "sizeBytes": len(font_data),
                    "referencedByUiText": referenced_by_ui,
                    "exported": True,
                })
                exported_font_bytes += len(font_data)
            except Exception as exc:
                font_records.append({
                    "id": object_id(font, "Font"),
                    "name": str(getattr(font, "path_id", "Font")),
                    "sourceFile": str(font.assets_file.name),
                    "sourcePathId": int(font.path_id),
                    "assetPath": "",
                    "sizeBytes": 0,
                    "referencedByUiText": object_id(font, "Font") in used_fonts,
                    "exported": False,
                })
                export_errors.append(f"Font {font.assets_file.name}:{font.path_id}: {type(exc).__name__}: {exc}")

        texture_records: list[dict[str, Any]] = []
        exported_texture_count = 0
        for texture_id, texture in sorted(used_textures.items()):
            try:
                data = texture.read()
                image = data.image
                if image is None:
                    raise ValueError("UnityPy returned no decoded image")
                name = str(data.m_Name or texture_id)
                filename = f"{texture_id}.png"
                image.save(output_root / "Textures" / filename, format="PNG")
                texture_records.append({
                    "id": texture_id,
                    "name": name,
                    "type": texture.type.name,
                    "assetPath": f"Assets/Recovered/Textures/{filename}",
                    "width": int(getattr(data, "m_Width", image.width) or image.width),
                    "height": int(getattr(data, "m_Height", image.height) or image.height),
                })
                exported_texture_count += 1
            except Exception as exc:
                export_errors.append(f"Texture {texture_id}: {type(exc).__name__}: {exc}")

        sprite_records: list[dict[str, Any]] = []
        exported_sprite_count = 0
        for sprite_id, sprite in sorted(used_sprites.items()):
            try:
                data = sprite.read()
                image = data.image
                if image is None:
                    raise ValueError("UnityPy returned no decoded sprite image")
                filename = f"{sprite_id}.png"
                image.save(output_root / "Sprites" / filename, format="PNG")
                tree = sprite.read_typetree(check_read=False)
                rect = tree.get("m_Rect", {}) or {}
                pivot = vec2(tree.get("m_Pivot"), (0.5, 0.5))
                sprite_records.append({
                    "id": sprite_id,
                    "name": str(tree.get("m_Name", sprite_id)),
                    "assetPath": f"Assets/Recovered/Sprites/{filename}",
                    "width": int(image.width),
                    "height": int(image.height),
                    "pivot": pivot,
                    "pixelsPerUnit": clean_float(tree.get("m_PixelsToUnits", 100.0), 100.0),
                    "originalRect": [
                        clean_float(rect.get("x")), clean_float(rect.get("y")),
                        clean_float(rect.get("width", image.width), image.width),
                        clean_float(rect.get("height", image.height), image.height),
                    ],
                })
                exported_sprite_count += 1
            except Exception as exc:
                export_errors.append(f"Sprite {sprite_id}: {type(exc).__name__}: {exc}")

        mesh_records: list[dict[str, Any]] = []
        mesh_skin_data_records: list[dict[str, Any]] = []
        mesh_zip = output_root / "Compressed" / "mesh-exports.zip"
        exported_mesh_count = 0
        with zipfile.ZipFile(mesh_zip, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for mesh_id, mesh in sorted(used_meshes.items()):
                try:
                    tree = mesh.read_typetree(check_read=False)
                    data = mesh.read()
                    obj_text = data.export("obj")
                    if not isinstance(obj_text, str) or not obj_text.strip():
                        raise ValueError("UnityPy returned an empty/non-exportable mesh")
                    filename = f"{mesh_id}.obj"
                    archive.writestr(filename, obj_text.encode("utf-8"))
                    submesh_count = len(getattr(data, "m_SubMeshes", []) or [])
                    bind_poses = tree.get("m_BindPose", []) or []
                    skin_data_id = ""
                    skin_vertex_count = 0
                    skin_weight_corrections = 0
                    skin_status = "noBindPoses"
                    if bind_poses:
                        try:
                            # process() mutates MeshHandler; its return value is None.
                            # UnityPy 1.25.4 computes an implicit fourth packed weight
                            # as 1 - integerSum; correct that residual to 1 - weightSum.
                            handler = MeshHandler(data)
                            handler.process()
                            bone_indices = handler.m_BoneIndices or []
                            bone_weights = handler.m_BoneWeights or []
                            vertex_count = len(handler.m_Vertices or [])
                            if not bone_indices or not bone_weights or len(bone_indices) != len(bone_weights) or len(bone_weights) != vertex_count:
                                skin_status = "bindPosesWithoutWeights"
                            else:
                                decoded_indices: list[int] = []
                                decoded_weights: list[float] = []
                                skin_issues: list[str] = []
                                for vertex_index, (indices_row, weights_row) in enumerate(zip(bone_indices, bone_weights)):
                                    indices_values = [safe_int(value, -1) for value in indices_row]
                                    weights_values = [clean_float(value, -1.0) for value in weights_row]
                                    if len(indices_values) != 4 or len(weights_values) != 4:
                                        skin_issues.append(f"vertex {vertex_index} does not have four influences")
                                        continue
                                    if weights_values[3] < 0 and all(value >= 0 for value in weights_values[:3]):
                                        residual = 1.0 - sum(weights_values[:3])
                                        if -1e-6 <= residual <= 1.0 + 1e-6:
                                            weights_values[3] = max(0.0, min(1.0, residual))
                                            skin_weight_corrections += 1
                                    total_weight = sum(weights_values)
                                    if any(value < -1e-7 or value > 1.0 + 1e-6 for value in weights_values):
                                        skin_issues.append(f"vertex {vertex_index} has out-of-range weights")
                                    if abs(total_weight - 1.0) > 1e-4:
                                        skin_issues.append(f"vertex {vertex_index} weights sum to {total_weight}")
                                    if any(
                                        weight > 1e-8 and (index < 0 or index >= len(bind_poses))
                                        for index, weight in zip(indices_values, weights_values)
                                    ):
                                        skin_issues.append(f"vertex {vertex_index} references a missing bind pose")
                                    decoded_indices.extend(indices_values)
                                    decoded_weights.extend(weights_values)
                                if skin_issues:
                                    skin_status = "invalidWeights"
                                    export_errors.append(
                                        f"Mesh skin {mesh_id}: {len(skin_issues)} invalid row(s); "
                                        + "; ".join(skin_issues[:3])
                                    )
                                else:
                                    geometry = pack_mesh_skin_geometry(handler, vertex_count, submesh_count)
                                    skin_data_id = mesh_id
                                    skin_vertex_count = vertex_count
                                    skin_status = "exported"
                                    mesh_skin_data_records.append({
                                        "id": skin_data_id,
                                        "meshId": mesh_id,
                                        "name": str(tree.get("m_Name", mesh_id)),
                                        "sourceFile": str(mesh.assets_file.name),
                                        "sourcePathId": int(mesh.path_id),
                                        "vertexCount": vertex_count,
                                        "bindPoseCount": len(bind_poses),
                                        "correctedFourthWeightCount": skin_weight_corrections,
                                        "bindPoses": json_safe(bind_poses),
                                        "boneIndices": decoded_indices,
                                        "boneWeights": decoded_weights,
                                        "geometry": geometry,
                                    })
                        except Exception as skin_exc:
                            skin_status = "decodeError"
                            export_errors.append(f"Mesh skin {mesh_id}: {type(skin_exc).__name__}: {skin_exc}")
                    mesh_records.append({
                        "id": mesh_id,
                        "name": str(tree.get("m_Name", mesh_id)),
                        "sourceFile": str(mesh.assets_file.name),
                        "sourcePathId": int(mesh.path_id),
                        "objEntry": filename,
                        "assetPath": f"Assets/Recovered/Meshes/{filename}",
                        "submeshes": submesh_count,
                        "bindPoseCount": len(bind_poses),
                        "skinDataId": skin_data_id,
                        "skinDataStatus": skin_status,
                        "boneWeightVertexCount": skin_vertex_count,
                        "skinWeightCorrections": skin_weight_corrections,
                        "exported": True,
                    })
                    exported_mesh_count += 1
                except Exception as exc:
                    mesh_records.append({
                        "id": mesh_id,
                        "name": mesh_id,
                        "sourceFile": str(mesh.assets_file.name),
                        "sourcePathId": int(mesh.path_id),
                        "objEntry": "",
                        "assetPath": "",
                        "submeshes": 0,
                        "bindPoseCount": 0,
                        "skinDataId": "",
                        "skinDataStatus": "notDecoded",
                        "boneWeightVertexCount": 0,
                        "skinWeightCorrections": 0,
                        "exported": False,
                    })
                    export_errors.append(f"Mesh {mesh_id}: {type(exc).__name__}: {exc}")

        audio_records: list[dict[str, Any]] = []
        audio_exported_bytes = 0
        audio_dir = output_root / "Audio"
        if audio_dir.is_dir():
            # Prevent stale audio files from an earlier extraction mode surviving
            # in Unity after a later index-only or sound-effects extraction.
            for stale_audio in audio_dir.glob("AudioClip_*"):
                if stale_audio.suffix.lower() in {".wav", ".mp3"}:
                    stale_audio.unlink()
        audio_objects = [o for o in environment.objects if o.type.name == "AudioClip"]
        for audio in audio_objects:
            try:
                tree = audio.read_typetree(check_read=False)
                audio_id = object_id(audio, "AudioClip")
                audio_asset_path = ""
                audio_exported = False
                audio_format = ""
                audio_exported_size = 0
                decoded_sample_size = 0
                if include_audio or include_audio_sfx:
                    clip = audio.read()
                    samples = clip.samples
                    decoded_sample_size = sum(len(sample_bytes) for sample_bytes in samples.values())
                    include_this_clip = include_audio or decoded_sample_size <= 2 * 1024 * 1024
                    if include_audio and decoded_sample_size > 2 * 1024 * 1024:
                        # FSB5-backed long music/voice tracks store MP3 frames in
                        # the APK. Preserve those original frames instead of writing
                        # tens of MiB of decoded PCM WAV data.
                        compressed_audio = extract_fsb5_mpeg_audio(tree, merged)
                        if compressed_audio:
                            audio_dir.mkdir(parents=True, exist_ok=True)
                            audio_file = audio_dir / f"{audio_id}.mp3"
                            audio_file.write_bytes(compressed_audio)
                            audio_asset_path = f"Assets/Recovered/Audio/{audio_file.name}"
                            audio_exported = True
                            audio_format = "mp3"
                            audio_exported_size = len(compressed_audio)
                            audio_exported_bytes += audio_exported_size
                    if not audio_exported and include_this_clip and samples:
                        audio_dir.mkdir(parents=True, exist_ok=True)
                        for sample_name, sample_bytes in samples.items():
                            suffix = Path(sample_name).suffix or ".wav"
                            audio_file = audio_dir / f"{audio_id}{suffix}"
                            audio_file.write_bytes(sample_bytes)
                            audio_asset_path = f"Assets/Recovered/Audio/{audio_file.name}"
                            audio_format = suffix.removeprefix(".").lower()
                            audio_exported_size += len(sample_bytes)
                            audio_exported_bytes += len(sample_bytes)
                        audio_exported = bool(audio_asset_path)
                audio_records.append({
                    "id": audio_id,
                    "name": str(tree.get("m_Name", audio_id)),
                    "sourceFile": str(audio.assets_file.name),
                    "sourcePathId": int(audio.path_id),
                    "channels": int(tree.get("m_Channels", 0) or 0),
                    "frequency": int(tree.get("m_Frequency", 0) or 0),
                    "lengthSeconds": clean_float(tree.get("m_Length", 0.0)),
                    "compressionFormat": int(tree.get("m_CompressionFormat", 0) or 0),
                    "assetPath": audio_asset_path,
                    "format": audio_format,
                    "exported": audio_exported,
                    "sizeBytes": audio_exported_size if audio_exported else 0,
                    "decodedSizeBytes": decoded_sample_size if audio_exported else 0,
                })
            except Exception as exc:
                export_errors.append(f"AudioClip {audio.assets_file.name}:{audio.path_id}: {exc}")

        animation_records: list[dict[str, Any]] = []
        animation_data_records: list[dict[str, Any]] = []
        for clip in (o for o in environment.objects if o.type.name == "AnimationClip"):
            try:
                tree = clip.read_typetree(check_read=False)
                muscle = tree.get("m_MuscleClip", {}) or {}
                clip_data = nested_dict(muscle, "m_Clip", "data")
                streamed = nested_dict(clip_data, "m_StreamedClip")
                dense = nested_dict(clip_data, "m_DenseClip")
                constant = nested_dict(clip_data, "m_ConstantClip")
                binding = tree.get("m_ClipBindingConstant", {}) or {}
                generic_bindings = binding.get("genericBindings", []) or []
                object_reference_bindings = binding.get("pptrCurveMapping", []) or []
                events = tree.get("m_Events", []) or []
                start_time = clean_float(muscle.get("m_StartTime", 0.0))
                stop_time = clean_float(muscle.get("m_StopTime", 0.0))
                clip_id = object_id(clip, "AnimationClip")
                streamed_curve_count = max(0, safe_int(streamed.get("curveCount", 0)))
                streamed_word_count = len(streamed.get("data", []) or [])
                dense_curve_count = max(0, safe_int(dense.get("m_CurveCount", 0)))
                dense_frame_count = max(0, safe_int(dense.get("m_FrameCount", 0)))
                dense_value_count = len(dense.get("m_SampleArray", []) or [])
                constant_value_count = len(constant.get("data", []) or [])
                animation_records.append({
                    "id": clip_id,
                    "name": str(tree.get("m_Name", "")),
                    "sourceFile": str(clip.assets_file.name),
                    "sourcePathId": int(clip.path_id),
                    "legacy": bool(tree.get("m_Legacy", False)),
                    "compressed": bool(tree.get("m_Compressed", False)),
                    "sampleRate": clean_float(tree.get("m_SampleRate", 0.0)),
                    "startTime": start_time,
                    "stopTime": stop_time,
                    "durationSeconds": max(0.0, stop_time - start_time),
                    "muscleClipSizeBytes": max(0, safe_int(tree.get("m_MuscleClipSize", 0))),
                    "loopTime": muscle.get("m_LoopTime"),
                    "loopBlend": bool(muscle.get("m_LoopBlend", False)),
                    "curveCounts": {
                        "rotation": len(tree.get("m_RotationCurves", []) or []),
                        "position": len(tree.get("m_PositionCurves", []) or []),
                        "scale": len(tree.get("m_ScaleCurves", []) or []),
                        "float": len(tree.get("m_FloatCurves", []) or []),
                        "objectReference": len(tree.get("m_PPtrCurves", []) or []),
                        "streamed": streamed_curve_count,
                        "dense": dense_curve_count,
                    },
                    "sampleCounts": {
                        "streamedWords": streamed_word_count,
                        "denseFrames": dense_frame_count,
                        "denseValues": dense_value_count,
                        "constantValues": constant_value_count,
                    },
                    "bindingCounts": {
                        "generic": len(generic_bindings),
                        "objectReference": len(object_reference_bindings),
                    },
                    "eventCount": len(events),
                    "denseSampleRate": clean_float(dense.get("m_SampleRate", 0.0)),
                    "denseBeginTime": clean_float(dense.get("m_BeginTime", 0.0)),
                })
                animation_data_records.append({
                    "id": clip_id,
                    "name": str(tree.get("m_Name", "")),
                    "sourceFile": str(clip.assets_file.name),
                    "sourcePathId": int(clip.path_id),
                    "m_MuscleClipSize": max(0, safe_int(tree.get("m_MuscleClipSize", 0))),
                    "m_SampleRate": clean_float(tree.get("m_SampleRate", 0.0)),
                    "m_WrapMode": safe_int(tree.get("m_WrapMode", 0)),
                    "m_MuscleClip": json_safe(muscle),
                    "m_ClipBindingConstant": json_safe(binding),
                    "m_Events": json_safe(events),
                })
            except Exception as exc:
                export_errors.append(f"AnimationClip {clip.assets_file.name}:{clip.path_id}: {exc}")

        controller_records: list[dict[str, Any]] = []
        controller_data_records: list[dict[str, Any]] = []
        for controller in (o for o in environment.objects if o.type.name == "AnimatorController"):
            try:
                tree = controller.read_typetree(check_read=False)
                controller_id = object_id(controller, "AnimatorController")
                controller_records.append({
                    "id": controller_id,
                    "name": str(tree.get("m_Name", "")),
                    "sourceFile": str(controller.assets_file.name),
                    "sourcePathId": int(controller.path_id),
                    "clipCount": len(tree.get("m_AnimationClips", []) or []),
                    "bindingCount": len(tree.get("m_TOS", []) or []),
                    "layerCount": count_named_list_items(tree, "m_LayerArray"),
                    "stateMachineCount": count_named_list_items(tree, "m_StateMachineArray"),
                    "stateCount": count_named_list_items(tree, "m_StateConstantArray"),
                    "transitionCount": count_named_fields(tree, "m_DestinationState"),
                    "blendTreeCount": count_named_list_items(tree, "m_BlendTreeConstantArray"),
                    "stateMachineBehaviourCount": len(tree.get("m_StateMachineBehaviours", []) or []),
                })
                controller_data_records.append({
                    "id": controller_id,
                    "name": str(tree.get("m_Name", "")),
                    "sourceFile": str(controller.assets_file.name),
                    "sourcePathId": int(controller.path_id),
                    "data": json_safe(tree),
                })
            except Exception as exc:
                export_errors.append(f"AnimatorController {controller.assets_file.name}:{controller.path_id}: {exc}")

        avatar_records: list[dict[str, Any]] = []
        avatar_data_records: list[dict[str, Any]] = []
        for avatar in (o for o in environment.objects if o.type.name == "Avatar"):
            try:
                tree = avatar.read_typetree(check_read=False)
                avatar_id = object_id(avatar, "Avatar")
                avatar_body = nested_dict(tree, "m_Avatar")
                skeleton = nested_dict(avatar_body, "m_AvatarSkeleton", "data")
                skeleton_pose = nested_dict(avatar_body, "m_AvatarSkeletonPose", "data")
                human_description = nested_dict(tree, "m_HumanDescription")
                avatar_records.append({
                    "id": avatar_id,
                    "name": str(tree.get("m_Name", "")),
                    "sourceFile": str(avatar.assets_file.name),
                    "sourcePathId": int(avatar.path_id),
                    "sizeBytes": max(0, safe_int(tree.get("m_AvatarSize", 0))),
                    "skeletonNodeCount": len(skeleton.get("m_Node", []) or []),
                    "skeletonPoseCount": len(skeleton_pose.get("m_X", []) or []),
                    "humanMappingCount": len(human_description.get("m_Human", []) or []),
                    "humanSkeletonCount": len(human_description.get("m_Skeleton", []) or []),
                    "transformNameCount": len(tree.get("m_TOS", []) or []),
                })
                avatar_data_records.append({
                    "id": avatar_id,
                    "name": str(tree.get("m_Name", "")),
                    "sourceFile": str(avatar.assets_file.name),
                    "sourcePathId": int(avatar.path_id),
                    "data": json_safe(tree),
                })
            except Exception as exc:
                export_errors.append(f"Avatar {avatar.assets_file.name}:{avatar.path_id}: {exc}")

        scene_objects = [obj for scene in scene_payload for obj in scene["objects"]]
        all_button_data = [
            obj.get("uiButtonData") or {}
            for obj in scene_objects if obj.get("uiButton")
        ] + [
            obj.get("uiButtonData") or {}
            for prefab in ui_prefab_records
            for obj in prefab.get("objects", []) if obj.get("uiButton")
        ]
        all_persistent_calls = [
            call
            for button_data in all_button_data
            for call in button_data.get("persistentCalls", [])
        ]
        audio_play_callbacks = sum(
            call.get("targetType") == "AudioSource"
            and call.get("methodName") == "Play"
            and call.get("mode") == 1
            for call in all_persistent_calls
        )
        game_object_set_active_callbacks = sum(
            call.get("targetType") == "GameObject"
            and call.get("methodName") == "SetActive"
            and call.get("mode") == 6
            for call in all_persistent_calls
        )
        renderer_type_counts = collections.Counter(
            renderer.get("type", "Unknown")
            for obj in scene_objects
            for renderer in (obj.get("renderers") or [])
        )
        visual_metadata = {
            "uiImagesStyled": sum(obj.get("uiImageData") is not None for obj in scene_objects),
            "uiTextsStyled": sum(obj.get("uiTextData") is not None for obj in scene_objects),
            "uiButtons": sum(bool(obj.get("uiButton")) for obj in scene_objects),
            "uiButtonPersistentCalls": sum(
                int((obj.get("uiButtonData") or {}).get("persistentCallCount", 0) or 0)
                for obj in scene_objects
            ),
            "uiButtonPersistentCallsDecoded": len(all_persistent_calls),
            "uiButtonAudioPlayCallbacks": audio_play_callbacks,
            "uiButtonGameObjectSetActiveCallbacks": game_object_set_active_callbacks,
            "uiGraphicEffects": sum(len(obj.get("uiEffects") or []) for obj in scene_objects),
            "canvasScalers": sum(obj.get("canvasScaler") is not None for obj in scene_objects),
            "canvases": sum(obj.get("canvas") is not None for obj in scene_objects),
            "canvasGroups": sum(obj.get("canvasGroup") is not None for obj in scene_objects),
            "rendererSettings": sum(renderer_type_counts.values()),
            "rendererTypes": dict(renderer_type_counts),
            "cameras": sum(obj.get("camera") is not None for obj in scene_objects),
            "lights": sum(obj.get("light") is not None for obj in scene_objects),
            "recoveredTextValues": sum(bool(obj.get("text")) for obj in scene_objects),
            "sharedUiPrefabs": len(ui_prefab_records),
            "sharedUiPrefabObjects": sum(prefab.get("objectCount", 0) for prefab in ui_prefab_records),
            "sharedUiPrefabImages": sum(
                obj.get("uiImageData") is not None
                for prefab in ui_prefab_records for obj in prefab.get("objects", [])
            ),
            "sharedUiPrefabTexts": sum(
                obj.get("uiTextData") is not None
                for prefab in ui_prefab_records for obj in prefab.get("objects", [])
            ),
            "sharedUiPrefabButtons": sum(
                bool(obj.get("uiButton"))
                for prefab in ui_prefab_records for obj in prefab.get("objects", [])
            ),
            "sharedUiPrefabButtonPersistentCalls": sum(
                int((obj.get("uiButtonData") or {}).get("persistentCallCount", 0) or 0)
                for prefab in ui_prefab_records for obj in prefab.get("objects", [])
            ),
            "uiTextFontsResolved": sum(
                bool((obj.get("uiTextData") or {}).get("fontId"))
                for obj in scene_objects
            ) + sum(
                bool((obj.get("uiTextData") or {}).get("fontId"))
                for prefab in ui_prefab_records for obj in prefab.get("objects", [])
            ),
            "sharedUiPrefabEffects": sum(
                len(obj.get("uiEffects") or [])
                for prefab in ui_prefab_records for obj in prefab.get("objects", [])
            ),
        }

        # Use the generated mesh model archive as the source of editable OBJ models.
        manifest_dir = output_root / "Manifests"
        write_json(manifest_dir / "scene-data.json.gz", {
            "formatVersion": 2,
            "source": "Rage of Fight IL2CPP APK; reconstructed data, not original Unity source",
            "unityVersion": "2022.3.62f1",
            "scenes": scene_payload,
        }, compressed=True)
        write_json(manifest_dir / "ui-prefabs.json", {"prefabs": ui_prefab_records})
        write_json(manifest_dir / "fonts.json", {"fonts": font_records})
        write_json(manifest_dir / "materials.json", {"materials": material_records})
        write_json(manifest_dir / "textures.json", {"textures": texture_records})
        write_json(manifest_dir / "sprites.json", {"sprites": sprite_records})
        write_json(manifest_dir / "mesh-skin-data.json.gz", {
            "formatVersion": 2,
            "source": "UnityPy MeshHandler-decoded bind poses, flat per-vertex bone influences, and vertex-aligned Unity-local geometry; implicit fourth weights normalized to the residual",
            "meshes": mesh_skin_data_records,
        }, compressed=True)
        write_json(manifest_dir / "meshes.json", {
            "archive": "Assets/Recovered/Compressed/mesh-exports.zip",
            "skinningDataFile": "Assets/Recovered/Manifests/mesh-skin-data.json.gz",
            "meshes": mesh_records,
        })
        write_json(manifest_dir / "audio-index.json", {"audioClips": audio_records})
        write_json(manifest_dir / "animation-curve-data.json.gz", {
            "formatVersion": 1,
            "source": "UnityPy-decoded AnimationClip typetrees; packed muscle-clip samples, bindings, and events",
            "animationClips": animation_data_records,
        }, compressed=True)
        write_json(manifest_dir / "animation-index.json", {
            "formatVersion": 2,
            "curveDataFile": "Assets/Recovered/Manifests/animation-curve-data.json.gz",
            "animationClips": animation_records,
        })
        write_json(manifest_dir / "animator-controller-data.json.gz", {
            "formatVersion": 1,
            "source": "UnityPy-decoded AnimatorController typetrees; inspection data, not Unity controller assets",
            "controllers": controller_data_records,
        }, compressed=True)
        write_json(manifest_dir / "animator-controller-index.json", {
            "formatVersion": 2,
            "dataFile": "Assets/Recovered/Manifests/animator-controller-data.json.gz",
            "controllers": controller_records,
        })
        write_json(manifest_dir / "avatar-data.json.gz", {
            "formatVersion": 1,
            "source": "UnityPy-decoded Avatar typetrees; skeleton and human-description inspection data, not Unity Avatar assets",
            "avatars": avatar_data_records,
        }, compressed=True)
        write_json(manifest_dir / "avatar-index.json", {
            "formatVersion": 2,
            "dataFile": "Assets/Recovered/Manifests/avatar-data.json.gz",
            "avatars": avatar_records,
        })

        summary = {
            "source": str(source),
            "unityVersion": "2022.3.62f1",
            "buildScenes": build_scenes,
            "scenes": [
                {
                    "key": scene["key"],
                    "name": scene["name"],
                    "objectCount": scene["objectCount"],
                    "componentCounts": dict(component_counts[scene["key"]]),
                    "scripts": dict(script_counts[scene["key"]]),
                }
                for scene in scene_payload
            ],
            "visualMetadata": visual_metadata,
            "assets": {
                "meshesReferenced": len(used_meshes),
                "meshesExported": exported_mesh_count,
                "meshesWithBindPoses": sum(record.get("bindPoseCount", 0) > 0 for record in mesh_records),
                "meshesWithBoneWeights": len(mesh_skin_data_records),
                "meshesWithSkinGeometry": sum(bool(record.get("geometry")) for record in mesh_skin_data_records),
                "skinnedBindPoseCount": sum(record.get("bindPoseCount", 0) for record in mesh_skin_data_records),
                "skinnedVertexCount": sum(record.get("vertexCount", 0) for record in mesh_skin_data_records),
                "skinnedTriangleCount": sum(
                    len(submesh.get("indices", [])) // 3
                    for record in mesh_skin_data_records
                    for submesh in (record.get("geometry", {}).get("submeshes", []) or [])
                ),
                "skinWeightCorrections": sum(record.get("correctedFourthWeightCount", 0) for record in mesh_skin_data_records),
                "materialsReferenced": len(used_materials),
                "texturesReferenced": len(used_textures),
                "texturesExported": exported_texture_count,
                "spritesReferenced": len(used_sprites),
                "spritesExported": exported_sprite_count,
                "fontsIndexed": len(font_records),
                "fontsExported": sum(record.get("exported", False) for record in font_records),
                "fontExportedBytes": exported_font_bytes,
                "uiPrefabsIndexed": len(ui_prefab_records),
                "uiPrefabObjectsIndexed": visual_metadata["sharedUiPrefabObjects"],
                "uiButtonsIndexed": visual_metadata["uiButtons"] + visual_metadata["sharedUiPrefabButtons"],
                "uiButtonPersistentCallsIndexed": visual_metadata["uiButtonPersistentCalls"] + visual_metadata["sharedUiPrefabButtonPersistentCalls"],
                "uiButtonPersistentCallsDecoded": visual_metadata["uiButtonPersistentCallsDecoded"],
                "uiButtonAudioPlayCallbacks": visual_metadata["uiButtonAudioPlayCallbacks"],
                "uiButtonGameObjectSetActiveCallbacks": visual_metadata["uiButtonGameObjectSetActiveCallbacks"],
                "audioClipsIndexed": len(audio_records),
                "animationClipsIndexed": len(animation_records),
                "animationCurveDataRecords": len(animation_data_records),
                "animationStreamedCurves": sum(record["curveCounts"]["streamed"] for record in animation_records),
                "animationStreamedWords": sum(record["sampleCounts"]["streamedWords"] for record in animation_records),
                "animationDenseCurves": sum(record["curveCounts"]["dense"] for record in animation_records),
                "animationDenseFrames": sum(record["sampleCounts"]["denseFrames"] for record in animation_records),
                "animationDenseValues": sum(record["sampleCounts"]["denseValues"] for record in animation_records),
                "animationConstantValues": sum(record["sampleCounts"]["constantValues"] for record in animation_records),
                "animationGenericBindings": sum(record["bindingCounts"]["generic"] for record in animation_records),
                "animatorControllersIndexed": len(controller_records),
                "animatorControllerDataRecords": len(controller_data_records),
                "animatorControllerStates": sum(record["stateCount"] for record in controller_records),
                "animatorControllerTransitions": sum(record["transitionCount"] for record in controller_records),
                "animatorControllerBlendTrees": sum(record["blendTreeCount"] for record in controller_records),
                "avatarsIndexed": len(avatar_records),
                "avatarDataRecords": len(avatar_data_records),
                "avatarSkeletonNodes": sum(record["skeletonNodeCount"] for record in avatar_records),
                "avatarHumanMappings": sum(record["humanMappingCount"] for record in avatar_records),
                "avatarTransformNames": sum(record["transformNameCount"] for record in avatar_records),
                "audioIncluded": bool(include_audio or include_audio_sfx),
                "audioClipsExported": sum(record.get("exported", False) for record in audio_records),
                "audioFormats": dict(collections.Counter(
                    record.get("format", "")
                    for record in audio_records if record.get("exported") and record.get("format")
                )),
                "audioExportedBytes": audio_exported_bytes,
                "audioExportMode": "all" if include_audio else "sound-effects" if include_audio_sfx else "index-only",
            },
            "errors": export_errors,
        }
        write_json(manifest_dir / "extraction-report.json", summary)
        audio_format_summary = ", ".join(
            f"{audio_format}={count}"
            for audio_format, count in sorted(summary["assets"]["audioFormats"].items())
        ) or "none"
        report_lines = [
            "# APK extraction report",
            "",
            "> This is a data/asset reconstruction from the IL2CPP APK, not recovered original C# source.",
            "",
            f"- Unity version: `{summary['unityVersion']}`",
            f"- Referenced meshes: {len(used_meshes)} ({exported_mesh_count} OBJ exports)",
            f"- Skin data: {summary['assets']['meshesWithBindPoses']} bind-pose meshes; {summary['assets']['meshesWithBoneWeights']} weighted meshes include {summary['assets']['skinnedVertexCount']:,} vertex records, {summary['assets']['skinnedBindPoseCount']:,} bind poses, source-ordered vertex geometry and {summary['assets']['skinnedTriangleCount']:,} triangles in `mesh-skin-data.json.gz`; {summary['assets']['skinWeightCorrections']:,} implicit fourth influences were corrected to the normalized residual for the Editor Builder",
            f"- Referenced materials: {len(used_materials)}",
            f"- Referenced textures: {len(used_textures)} ({exported_texture_count} PNG exports)",
            f"- Referenced UI/native sprites: {len(used_sprites)} ({exported_sprite_count} PNG exports)",
            f"- Embedded fonts exported: {summary['assets']['fontsExported']}/{len(font_records)} ({sum(record.get('referencedByUiText', False) for record in font_records)} referenced by UI Text, {exported_font_bytes / 1024:.1f} KiB)",
            f"- Shared-asset UI prefabs indexed: {visual_metadata['sharedUiPrefabs']} roots, {visual_metadata['sharedUiPrefabObjects']} objects, {visual_metadata['sharedUiPrefabImages']} styled Images, {visual_metadata['sharedUiPrefabTexts']} styled Texts, {visual_metadata['sharedUiPrefabButtons']} Buttons, {visual_metadata['sharedUiPrefabEffects']} styled Shadow/Outline effects",
            f"- Audio clips indexed: {len(audio_records)}; audio files exported: {summary['assets']['audioClipsExported']} ({audio_format_summary}; {summary['assets']['audioExportMode']}, {audio_exported_bytes / (1024 * 1024):.2f} MiB)",
            *(["- FSB5/MPEG MP3 export strips zero alignment padding; the offline validator checks MPEG frame structure, channels, sample rate, and frame-derived duration against the manifest."] if any(record.get("exported") and record.get("format") == "mp3" for record in audio_records) else []),
            f"- Animation data: {len(animation_records)} clips; {summary['assets']['animationStreamedCurves']:,} streamed curves, {summary['assets']['animationDenseCurves']:,} dense curves/{summary['assets']['animationDenseFrames']:,} frames, {summary['assets']['animationConstantValues']:,} constant values; decoded muscle clips, bindings and events are preserved in `animation-curve-data.json.gz` (inspection data, not playable Unity clips)",
            f"- Animator rig metadata: {len(controller_records)} AnimatorControllers ({summary['assets']['animatorControllerStates']:,} states, {summary['assets']['animatorControllerTransitions']:,} transition records, {summary['assets']['animatorControllerBlendTrees']:,} blend trees); {len(avatar_records)} Avatars ({summary['assets']['avatarSkeletonNodes']:,} skeleton nodes, {summary['assets']['avatarHumanMappings']:,} human mappings, {summary['assets']['avatarTransformNames']:,} transform-name entries). Full decoded trees are preserved in compressed data manifests (not rebuilt as executable Unity assets)",
            f"- UGUI presentation data: {visual_metadata['uiImagesStyled']} Images, {visual_metadata['uiTextsStyled']} Texts and {visual_metadata['uiGraphicEffects']} Shadow/Outline effects (serialized style settings)",
            f"- UI Buttons: {visual_metadata['uiButtons'] + visual_metadata['sharedUiPrefabButtons']} (transition/color/navigation fields restored); {visual_metadata['uiButtonPersistentCallsDecoded']} persistent onClick calls decoded; Builder can rebind {visual_metadata['uiButtonAudioPlayCallbacks']} AudioSource.Play and {visual_metadata['uiButtonGameObjectSetActiveCallbacks']} GameObject.SetActive calls, while {visual_metadata['uiButtonPersistentCallsDecoded'] - visual_metadata['uiButtonAudioPlayCallbacks'] - visual_metadata['uiButtonGameObjectSetActiveCallbacks']} custom IL2CPP handlers remain metadata-only",
            f"- Canvas metadata: {visual_metadata['canvases']} Canvases, {visual_metadata['canvasScalers']} CanvasScalers, {visual_metadata['canvasGroups']} CanvasGroups",
            f"- Renderer settings: {visual_metadata['rendererSettings']} ({', '.join(f'{name}={count}' for name, count in sorted(renderer_type_counts.items()))})",
            f"- Camera and light settings: {visual_metadata['cameras']} Cameras, {visual_metadata['lights']} Lights",
            f"- UI text values recovered: {visual_metadata['recoveredTextValues']}",
            f"- UI Text Font references resolved from serialized PPtrs: {visual_metadata['uiTextFontsResolved']}",
            "",
            "## Scenes",
            "",
        ]
        for scene in summary["scenes"]:
            report_lines.append(f"- `{scene['key']}` → {scene['name']}: {scene['objectCount']} GameObjects")
        report_lines += ["", "## Extraction warnings", ""]
        if export_errors:
            report_lines.extend(f"- {error}" for error in export_errors[:200])
            if len(export_errors) > 200:
                report_lines.append(f"- … {len(export_errors) - 200} additional warning(s) in `extraction-report.json`.")
        else:
            report_lines.append("- None.")
        (manifest_dir / "extraction-report.md").write_text("\n".join(report_lines) + "\n", encoding="utf-8")
        return summary
    finally:
        shutil.rmtree(temp_root, ignore_errors=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Unity APK, APKTool output directory, or Unity Data directory")
    parser.add_argument("--output", type=Path, default=ASSET_ROOT, help="Assets/Recovered output directory")
    audio_group = parser.add_mutually_exclusive_group()
    audio_group.add_argument("--include-audio", action="store_true", help="Export every AudioClip; preserve long FSB5/MPEG sources as original MP3 frames where possible")
    audio_group.add_argument("--include-audio-sfx", action="store_true", help="Write only clips up to 2 MiB each; omit long music/voice tracks to keep the project compact")
    args = parser.parse_args()
    try:
        result = extract(
            args.input,
            include_audio=args.include_audio,
            include_audio_sfx=args.include_audio_sfx,
            output_root=args.output,
        )
    except Exception as exc:
        print(f"ERROR: {type(exc).__name__}: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
