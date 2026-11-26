"""Utilities for recovering UI-prefab roots stored in shared Unity asset files."""

from __future__ import annotations

from collections import defaultdict
from typing import Any

try:
    from .extract_from_apk import (
        find_sprite_pointer,
        object_id,
        ptr_target,
        recover_canvas_scaler_data,
        recover_text,
        recover_ui_button_data,
        recover_ui_effect_data,
        recover_ui_image_data,
        recover_ui_text_font,
        recover_ui_text_data,
        safe_int,
        script_record,
        vec2,
        vec3,
        vec4,
    )
except ImportError:
    from extract_from_apk import (
        find_sprite_pointer,
        object_id,
        ptr_target,
        recover_canvas_scaler_data,
        recover_text,
        recover_ui_button_data,
        recover_ui_effect_data,
        recover_ui_image_data,
        recover_ui_text_font,
        recover_ui_text_data,
        safe_int,
        script_record,
        vec2,
        vec3,
        vec4,
    )


def extract_shared_ui_prefabs(
    shared_file: Any,
    sprite_lookup: dict[tuple[str, int], Any],
    record_asset: Any,
    used_sprites: dict[str, Any],
    used_fonts: dict[str, Any],
) -> list[dict[str, Any]]:
    """Serialize full root hierarchies containing shared-asset UGUI Image/Text.

    Unity stores a handful of UI prefabs directly in sharedassets2.assets rather
    than in any of the four build scenes. This captures only those prefab trees,
    keeping the scene manifests focused on actual scenes.
    """
    if shared_file is None:
        return []

    game_objects = {
        int(obj.path_id): obj
        for obj in shared_file.objects.values()
        if obj.type.name == "GameObject"
    }
    go_trees: dict[int, dict[str, Any]] = {}
    components_by_go: dict[int, list[Any]] = {}
    component_to_game_object: dict[int, int] = {}
    transform_to_go: dict[int, int] = {}
    transform_by_go: dict[int, Any] = {}

    for go_id, game_object in game_objects.items():
        try:
            go_tree = game_object.read_typetree(check_read=False)
        except Exception:
            continue
        go_trees[go_id] = go_tree
        components: list[Any] = []
        for component_ref in go_tree.get("m_Component", []) or []:
            pointer = component_ref.get("component", {}) if isinstance(component_ref, dict) else {}
            component = ptr_target(shared_file, pointer)
            if component is None:
                continue
            components.append(component)
            component_to_game_object[int(component.path_id)] = go_id
            if component.type.name in ("Transform", "RectTransform"):
                transform_id = int(component.path_id)
                transform_to_go[transform_id] = go_id
                transform_by_go[go_id] = component
        components_by_go[go_id] = components

    parent_by_go: dict[int, int] = {}
    for go_id, transform in transform_by_go.items():
        try:
            transform_tree = transform.read_typetree(check_read=False)
        except Exception:
            transform_tree = {}
        parent_transform = (transform_tree.get("m_Father") or {}).get("m_PathID", 0)
        parent_transform_id = int(parent_transform or 0)
        parent_by_go[go_id] = transform_to_go.get(parent_transform_id, 0) if parent_transform_id else 0

    def root_for(go_id: int) -> int:
        current = go_id
        visited: set[int] = set()
        while current in parent_by_go and parent_by_go[current] and current not in visited:
            visited.add(current)
            current = parent_by_go[current]
        return current

    roots: set[int] = set()
    script_cache: dict[int, dict[str, str] | None] = {}
    for go_id, components in components_by_go.items():
        for component in components:
            if component.type.name != "MonoBehaviour":
                continue
            if component.path_id not in script_cache:
                try:
                    tree = component.read_typetree(check_read=False)
                except Exception:
                    tree = {}
                script_cache[int(component.path_id)] = script_record(component, tree)
            script = script_cache[int(component.path_id)]
            if script and script["assembly"] == "UnityEngine.UI" and script["className"] in ("Image", "Text"):
                roots.add(root_for(go_id))

    children: dict[int, list[int]] = defaultdict(list)
    for go_id, parent_id in parent_by_go.items():
        if parent_id:
            children[parent_id].append(go_id)

    prefab_records: list[dict[str, Any]] = []
    for root_id in sorted(roots, key=lambda value: (str(go_trees.get(value, {}).get("m_Name", "")), value)):
        ordered_ids: list[int] = []
        visited: set[int] = set()
        stack = [root_id]
        while stack:
            current = stack.pop()
            if current in visited or current not in go_trees:
                continue
            visited.add(current)
            ordered_ids.append(current)
            stack.extend(sorted(children.get(current, []), reverse=True))

        scene_objects: list[dict[str, Any]] = []
        for go_id in ordered_ids:
            go_tree = go_trees[go_id]
            name = str(go_tree.get("m_Name") or f"GameObject_{go_id}")
            component_types: list[str] = []
            script_types: list[str] = []
            transform_data: dict[str, Any] | None = None
            image_data = None
            text_data = None
            ui_effects: list[dict[str, Any]] = []
            image_sprite = ""
            text_value = ""
            has_image = False
            has_text = False
            has_button = False
            button_data = None
            has_canvas = False
            canvas_scaler = None
            canvas = None
            canvas_group = None

            for component in components_by_go.get(go_id, []):
                component_type = component.type.name
                component_types.append(component_type)
                try:
                    component_tree = component.read_typetree(check_read=False)
                except Exception:
                    component_tree = {}

                if component_type in ("Transform", "RectTransform"):
                    transform_data = {
                        "kind": component_type,
                        "position": vec3(component_tree.get("m_LocalPosition")),
                        "rotation": vec4(component_tree.get("m_LocalRotation"), (0.0, 0.0, 0.0, 1.0)),
                        "scale": vec3(component_tree.get("m_LocalScale"), (1.0, 1.0, 1.0)),
                    }
                    if component_type == "RectTransform":
                        transform_data.update({
                            "anchorMin": vec2(component_tree.get("m_AnchorMin")),
                            "anchorMax": vec2(component_tree.get("m_AnchorMax"), (1.0, 1.0)),
                            "anchoredPosition": vec3(component_tree.get("m_AnchoredPosition")),
                            "sizeDelta": vec2(component_tree.get("m_SizeDelta")),
                            "pivot": vec2(component_tree.get("m_Pivot"), (0.5, 0.5)),
                        })
                elif component_type == "MonoBehaviour":
                    script = script_cache.get(int(component.path_id))
                    if script is None:
                        script = script_record(component, component_tree)
                        script_cache[int(component.path_id)] = script
                    if not script:
                        continue
                    qualified = script["qualifiedName"]
                    script_types.append(qualified)
                    if script["assembly"] == "UnityEngine.UI":
                        if script["className"] == "Image":
                            has_image = True
                            image_data = recover_ui_image_data(component)
                            sprite = find_sprite_pointer(component, sprite_lookup)
                            if sprite is not None:
                                image_sprite = record_asset(sprite)
                                used_sprites[image_sprite] = sprite
                        elif script["className"] == "Text":
                            has_text = True
                            text_data = recover_ui_text_data(component)
                            font = recover_ui_text_font(component)
                            if font is not None:
                                font_id = record_asset(font, "Font")
                                used_fonts[font_id] = font
                                if text_data is not None:
                                    text_data["fontId"] = font_id
                            text_value = recover_text(component)
                        elif script["className"] == "Button":
                            has_button = True
                            button_data = recover_ui_button_data(
                                component, component_to_game_object, record_asset, used_sprites
                            )
                        elif script["className"] == "CanvasScaler":
                            has_canvas = True
                            canvas_scaler = recover_canvas_scaler_data(component)
                        elif script["className"] in ("Shadow", "Outline"):
                            effect = recover_ui_effect_data(component, script["className"])
                            if effect is not None:
                                ui_effects.append(effect)
                    elif qualified.endswith("CanvasScaler"):
                        has_canvas = True
                elif component_type == "CanvasGroup":
                    canvas_group = {
                        "enabled": bool(component_tree.get("m_Enabled", True)),
                        "alpha": float(component_tree.get("m_Alpha", 1.0) or 0.0),
                        "interactable": bool(component_tree.get("m_Interactable", True)),
                        "blocksRaycasts": bool(component_tree.get("m_BlocksRaycasts", True)),
                        "ignoreParentGroups": bool(component_tree.get("m_IgnoreParentGroups", False)),
                    }
                elif component_type == "Canvas":
                    has_canvas = True
                    canvas = {
                        "enabled": bool(component_tree.get("m_Enabled", True)),
                        "renderMode": safe_int(component_tree.get("m_RenderMode", 0)),
                        "worldCameraObject": 0,
                        "planeDistance": float(component_tree.get("m_PlaneDistance", 100.0) or 100.0),
                        "pixelPerfect": bool(component_tree.get("m_PixelPerfect", False)),
                        "receivesEvents": bool(component_tree.get("m_ReceivesEvents", True)),
                        "overrideSorting": bool(component_tree.get("m_OverrideSorting", False)),
                        "sortingLayerId": safe_int(component_tree.get("m_SortingLayerID", 0)),
                        "sortingOrder": safe_int(component_tree.get("m_SortingOrder", 0)),
                        "targetDisplay": safe_int(component_tree.get("m_TargetDisplay", 0)),
                    }

            parent_id = parent_by_go.get(go_id, 0)
            if parent_id not in visited:
                parent_id = 0
            scene_objects.append({
                "id": go_id,
                "name": name,
                "active": bool(go_tree.get("m_IsActive", True)),
                "layer": int(go_tree.get("m_Layer", 0) or 0),
                "tag": str(go_tree.get("m_TagString", "Untagged") or "Untagged"),
                "parent": parent_id,
                "transform": transform_data or {
                    "kind": "Transform",
                    "position": [0.0, 0.0, 0.0],
                    "rotation": [0.0, 0.0, 0.0, 1.0],
                    "scale": [1.0, 1.0, 1.0],
                },
                "components": sorted(set(component_types)),
                "scripts": sorted(set(script_types)),
                "meshes": [],
                "materials": [],
                "sprite": image_sprite,
                "text": text_value,
                "uiImage": has_image,
                "uiText": has_text,
                "uiButton": has_button,
                "uiButtonData": button_data,
                "uiCanvas": has_canvas,
                "uiImageData": image_data,
                "uiTextData": text_data,
                "uiEffects": ui_effects,
                "canvasScaler": canvas_scaler,
                "canvas": canvas,
                "canvasGroup": canvas_group,
                "renderers": [],
                "camera": None,
                "light": None,
                "audioClip": "",
                "audioSource": None,
                "colliders": [],
                "rigidbody": None,
                "characterJoint": None,
                "navMeshAgent": None,
                "navMeshObstacle": None,
            })

        root_tree = go_trees[root_id]
        prefab_records.append({
            "id": object_id(game_objects[root_id], "UIPrefab"),
            "name": str(root_tree.get("m_Name") or f"UI_Prefab_{root_id}"),
            "sourceFile": str(shared_file.name),
            "sourcePathId": root_id,
            "objectCount": len(scene_objects),
            "objects": scene_objects,
        })

    return prefab_records
