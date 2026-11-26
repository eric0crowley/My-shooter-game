#!/usr/bin/env python3
"""Validate the extracted Unity reconstruction data without requiring Unity.

This checks manifest consistency and exported-file integrity. It does not compile
or run the Unity Editor Builder; that still must be verified in Unity itself.
"""

from __future__ import annotations

import gzip
import json
import math
import sys
import wave
import zipfile
from collections import Counter
from pathlib import Path, PurePosixPath
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RECOVERED_ROOT = PROJECT_ROOT / "Assets" / "Recovered"
MANIFEST_ROOT = RECOVERED_ROOT / "Manifests"


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as stream:
        return json.load(stream)


def all_values(value: Any):
    if isinstance(value, dict):
        for child in value.values():
            yield from all_values(child)
    elif isinstance(value, list):
        for child in value:
            yield from all_values(child)
    else:
        yield value


def nested_dict(value: Any, *keys: str) -> dict[str, Any]:
    current = value
    for key in keys:
        if not isinstance(current, dict):
            return {}
        current = current.get(key)
    return current if isinstance(current, dict) else {}


def list_field(value: Any, key: str) -> list[Any]:
    if not isinstance(value, dict):
        return []
    result = value.get(key)
    return result if isinstance(result, list) else []


def count_named_list_items(value: Any, field_name: str) -> int:
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
    if isinstance(value, dict):
        return int(field_name in value) + sum(count_named_fields(child, field_name) for child in value.values())
    if isinstance(value, list):
        return sum(count_named_fields(child, field_name) for child in value)
    return 0


def asset_path_exists(asset_path: Any) -> bool:
    if not isinstance(asset_path, str) or not asset_path.startswith("Assets/"):
        return False
    relative_path = Path(*PurePosixPath(asset_path).parts)
    return (PROJECT_ROOT / relative_path).is_file()


def read_mp3_metadata(path: Path) -> tuple[int, int, float]:
    """Read MPEG Layer III frame metadata without depending on an audio library."""
    data = path.read_bytes()
    offset = 0
    if data.startswith(b"ID3") and len(data) >= 10:
        tag_size = sum((data[6 + i] & 0x7F) << (21 - i * 7) for i in range(4))
        offset = 10 + tag_size + (10 if data[5] & 0x10 else 0)
    bitrate_tables = {
        3: (0, 32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320, 0),
        2: (0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160, 0),
        0: (0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160, 0),
    }
    base_frequencies = (44100, 48000, 32000)
    sample_rate = 0
    channels = 0
    sample_count = 0
    frames = 0
    while offset + 4 <= len(data):
        if data[offset:offset + 3] == b"TAG" and len(data) - offset == 128:
            offset += 128
            break
        header = int.from_bytes(data[offset:offset + 4], "big")
        if header >> 21 != 0x7FF:
            raise ValueError(f"invalid MPEG frame sync at byte {offset}")
        version = (header >> 19) & 0x3
        layer = (header >> 17) & 0x3
        bitrate_index = (header >> 12) & 0xF
        frequency_index = (header >> 10) & 0x3
        padding = (header >> 9) & 0x1
        if version == 1 or layer != 1 or bitrate_index in (0, 15) or frequency_index == 3:
            raise ValueError(f"unsupported MPEG header at byte {offset}")
        frequency = base_frequencies[frequency_index] // {3: 1, 2: 2, 0: 4}[version]
        bitrate = bitrate_tables[version][bitrate_index] * 1000
        frame_length = (144 if version == 3 else 72) * bitrate // frequency + padding
        if frame_length < 4 or offset + frame_length > len(data):
            raise ValueError(f"truncated MPEG frame at byte {offset}")
        frame_channels = 1 if ((header >> 6) & 0x3) == 3 else 2
        if sample_rate and (frequency != sample_rate or frame_channels != channels):
            raise ValueError("MPEG stream changes sample rate or channel count")
        sample_rate = frequency
        channels = frame_channels
        sample_count += 1152 if version == 3 else 576
        frames += 1
        offset += frame_length
    if offset != len(data) or not frames or not sample_rate:
        raise ValueError(f"MPEG stream ended with {len(data) - offset} unparsed byte(s)")
    return channels, sample_rate, sample_count / sample_rate


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    def error(message: str) -> None:
        errors.append(message)

    def warn(message: str) -> None:
        warnings.append(message)

    required_manifests = (
        "meshes.json",
        "materials.json",
        "textures.json",
        "sprites.json",
        "fonts.json",
        "ui-prefabs.json",
        "audio-index.json",
        "animation-index.json",
        "animator-controller-index.json",
        "avatar-index.json",
        "extraction-report.json",
    )
    manifests: dict[str, Any] = {}
    for name in required_manifests:
        path = MANIFEST_ROOT / name
        if not path.is_file():
            error(f"Missing manifest: {path.relative_to(PROJECT_ROOT)}")
            continue
        try:
            manifests[name] = load_json(path)
        except Exception as exc:
            error(f"Cannot parse {name}: {type(exc).__name__}: {exc}")

    scene_path = MANIFEST_ROOT / "scene-data.json.gz"
    scene_manifest: dict[str, Any] = {}
    if not scene_path.is_file():
        error(f"Missing scene manifest: {scene_path.relative_to(PROJECT_ROOT)}")
    else:
        try:
            with gzip.open(scene_path, "rt", encoding="utf-8") as stream:
                scene_manifest = json.load(stream)
        except Exception as exc:
            error(f"Cannot read compressed scene manifest: {type(exc).__name__}: {exc}")

    compressed_manifests: dict[str, dict[str, Any]] = {}
    for name in (
        "mesh-skin-data.json.gz",
        "animation-curve-data.json.gz",
        "animator-controller-data.json.gz",
        "avatar-data.json.gz",
    ):
        path = MANIFEST_ROOT / name
        if not path.is_file():
            error(f"Missing compressed animation/rig data manifest: {path.relative_to(PROJECT_ROOT)}")
            continue
        try:
            with gzip.open(path, "rt", encoding="utf-8") as stream:
                value = json.load(stream)
            if isinstance(value, dict):
                compressed_manifests[name] = value
            else:
                error(f"{name} must contain an object")
        except Exception as exc:
            error(f"Cannot read compressed {name}: {type(exc).__name__}: {exc}")

    il2cpp_metadata_path = MANIFEST_ROOT / "il2cpp-script-metadata.json"
    il2cpp_script_metadata: dict[str, Any] | None = None
    if il2cpp_metadata_path.is_file():
        try:
            parsed_metadata = load_json(il2cpp_metadata_path)
            if isinstance(parsed_metadata, dict):
                il2cpp_script_metadata = parsed_metadata
            else:
                error("il2cpp-script-metadata.json must contain an object")
        except Exception as exc:
            error(f"Cannot parse il2cpp-script-metadata.json: {type(exc).__name__}: {exc}")

    def entries(manifest_name: str, key: str) -> list[dict[str, Any]]:
        manifest = manifests.get(manifest_name, {})
        result = manifest.get(key, []) if isinstance(manifest, dict) else []
        if not isinstance(result, list):
            error(f"{manifest_name}: '{key}' must be a list")
            return []
        return [item for item in result if isinstance(item, dict)]

    mesh_entries = entries("meshes.json", "meshes")
    material_entries = entries("materials.json", "materials")
    texture_entries = entries("textures.json", "textures")
    sprite_entries = entries("sprites.json", "sprites")
    font_entries = entries("fonts.json", "fonts")
    ui_prefab_entries = entries("ui-prefabs.json", "prefabs")
    audio_entries = entries("audio-index.json", "audioClips")
    animation_entries = entries("animation-index.json", "animationClips")
    controller_entries = entries("animator-controller-index.json", "controllers")
    avatar_entries = entries("avatar-index.json", "avatars")
    meshes = {item.get("id"): item for item in mesh_entries if item.get("id")}
    materials = {item.get("id"): item for item in material_entries if item.get("id")}
    textures = {item.get("id"): item for item in texture_entries if item.get("id")}
    sprites = {item.get("id"): item for item in sprite_entries if item.get("id")}
    fonts = {item.get("id"): item for item in font_entries if item.get("id")}
    audio_ids = {item.get("id") for item in audio_entries if item.get("id")}
    exported_audio_ids = {item.get("id") for item in audio_entries if item.get("id") and item.get("exported")}

    # Check all image/audio files Unity will import and every material-to-texture link.
    for label, items in (("texture", texture_entries), ("sprite", sprite_entries)):
        for item in items:
            if not asset_path_exists(item.get("assetPath")):
                error(f"Missing {label} file: {item.get('assetPath')}")
    seen_font_ids: set[str] = set()
    for font in font_entries:
        font_id = font.get("id")
        if not isinstance(font_id, str) or not font_id:
            error("Font manifest contains an entry without a valid id")
        elif font_id in seen_font_ids:
            error(f"Duplicate Font id: {font_id}")
        else:
            seen_font_ids.add(font_id)
        if font.get("exported"):
            asset_path = font.get("assetPath")
            if not asset_path_exists(asset_path):
                error(f"Missing font file: {asset_path}")
                continue
            font_file = PROJECT_ROOT / Path(*PurePosixPath(asset_path).parts)
            data = font_file.read_bytes()
            expected_size = font.get("sizeBytes")
            if not isinstance(expected_size, int) or len(data) != expected_size:
                error(f"Font file size mismatch for {font_id}")
            is_ttf = data.startswith(bytes.fromhex("00010000"))
            is_otf = data.startswith(b"OTTO")
            if not (is_ttf or is_otf):
                error(f"Unrecognized embedded font signature: {asset_path}")
            elif (is_ttf and not str(asset_path).lower().endswith(".ttf")) or (is_otf and not str(asset_path).lower().endswith(".otf")):
                error(f"Font extension does not match its data: {asset_path}")
        elif font.get("assetPath") or font.get("sizeBytes", 0):
            error(f"Non-exported font {font_id} unexpectedly advertises a font file")
    seen_audio_ids: set[str] = set()
    for clip in audio_entries:
        audio_id = clip.get("id")
        if not isinstance(audio_id, str) or not audio_id:
            error("Audio manifest contains a clip without a valid id")
        elif audio_id in seen_audio_ids:
            error(f"Duplicate AudioClip id: {audio_id}")
        else:
            seen_audio_ids.add(audio_id)
        if clip.get("exported"):
            asset_path = clip.get("assetPath")
            if not asset_path_exists(asset_path):
                error(f"Missing audio file: {asset_path}")
                continue
            suffix = PurePosixPath(str(asset_path)).suffix.lower()
            if suffix not in {".wav", ".mp3"}:
                error(f"Unsupported audio file extension: {asset_path}")
                continue
            audio_file = PROJECT_ROOT / Path(*PurePosixPath(asset_path).parts)
            expected_size = clip.get("sizeBytes")
            if not isinstance(expected_size, int) or audio_file.stat().st_size != expected_size:
                error(f"Audio file size mismatch for {audio_id}: manifest={expected_size!r}, file={audio_file.stat().st_size}")
            manifest_format = clip.get("format")
            if manifest_format and manifest_format != suffix.removeprefix("."):
                error(f"Audio format/extension mismatch for {audio_id}")
            if suffix == ".wav":
                try:
                    with wave.open(str(audio_file), "rb") as wav:
                        actual_channels = wav.getnchannels()
                        actual_frequency = wav.getframerate()
                        actual_frames = wav.getnframes()
                        actual_duration = actual_frames / actual_frequency if actual_frequency else 0.0
                    if actual_frames <= 0 or actual_channels != clip.get("channels") or actual_frequency != clip.get("frequency"):
                        error(f"Audio WAV metadata mismatch for {audio_id}")
                    if abs(actual_duration - float(clip.get("lengthSeconds", 0.0))) > max(0.02, actual_duration * 0.001):
                        error(f"Audio WAV duration mismatch for {audio_id}")
                except (OSError, EOFError, wave.Error, ValueError, TypeError, ZeroDivisionError) as exc:
                    error(f"Cannot read audio WAV {asset_path}: {type(exc).__name__}: {exc}")
            else:
                try:
                    actual_channels, actual_frequency, actual_duration = read_mp3_metadata(audio_file)
                    if actual_channels != clip.get("channels") or actual_frequency != clip.get("frequency"):
                        error(f"MP3 metadata mismatch for {audio_id}")
                    if abs(actual_duration - float(clip.get("lengthSeconds", 0.0))) > max(0.02, actual_duration * 0.001):
                        error(f"MP3 duration mismatch for {audio_id}")
                except (OSError, ValueError, TypeError, ZeroDivisionError) as exc:
                    error(f"Cannot read audio MP3 {asset_path}: {type(exc).__name__}: {exc}")
        elif clip.get("assetPath") or clip.get("sizeBytes", 0):
            error(f"Non-exported audio clip {audio_id} unexpectedly advertises an audio asset")

    def records_by_id(records: list[dict[str, Any]], context: str) -> dict[str, dict[str, Any]]:
        result: dict[str, dict[str, Any]] = {}
        for record in records:
            record_id = record.get("id")
            if not isinstance(record_id, str) or not record_id:
                error(f"{context} contains an entry without a valid id")
            elif record_id in result:
                error(f"{context} contains duplicate id {record_id}")
            else:
                result[record_id] = record
        return result

    def archive_records(filename: str, key: str, context: str) -> dict[str, dict[str, Any]]:
        archive = compressed_manifests.get(filename, {})
        values = archive.get(key, []) if isinstance(archive, dict) else []
        if not isinstance(values, list):
            error(f"{filename}: '{key}' must be a list")
            return {}
        return records_by_id([record for record in values if isinstance(record, dict)], context)

    expected_data_files = {
        "meshes.json": ("skinningDataFile", "Assets/Recovered/Manifests/mesh-skin-data.json.gz"),
        "animation-index.json": ("curveDataFile", "Assets/Recovered/Manifests/animation-curve-data.json.gz"),
        "animator-controller-index.json": ("dataFile", "Assets/Recovered/Manifests/animator-controller-data.json.gz"),
        "avatar-index.json": ("dataFile", "Assets/Recovered/Manifests/avatar-data.json.gz"),
    }
    for index_name, (field_name, expected_path) in expected_data_files.items():
        index_manifest = manifests.get(index_name, {})
        if not isinstance(index_manifest, dict) or index_manifest.get(field_name) != expected_path:
            error(f"{index_name}: '{field_name}' does not point to {expected_path}")
        if not asset_path_exists(expected_path):
            error(f"Missing serialized animation/rig data file: {expected_path}")

    skin_archive_name = "mesh-skin-data.json.gz"
    skin_archive = compressed_manifests.get(skin_archive_name, {})
    if skin_archive.get("formatVersion") != 2:
        error(f"{skin_archive_name}: unsupported or missing formatVersion")
    mesh_by_id = records_by_id(mesh_entries, "Mesh index")
    skin_data_by_id = archive_records(skin_archive_name, "meshes", "Mesh skin data")
    skin_active_bone_indices: dict[str, set[int]] = {}
    skin_geometry_triangle_count = 0
    expected_skin_ids = {
        mesh_id for mesh_id, record in mesh_by_id.items()
        if record.get("skinDataStatus") == "exported" and record.get("skinDataId")
    }
    if set(skin_data_by_id) != expected_skin_ids:
        error("Mesh index and decoded skin archive contain different mesh IDs")
    for mesh_id, mesh_record in mesh_by_id.items():
        bind_pose_count = mesh_record.get("bindPoseCount")
        vertex_count = mesh_record.get("boneWeightVertexCount")
        skin_status = mesh_record.get("skinDataStatus")
        skin_data_id = mesh_record.get("skinDataId", "")
        if not isinstance(bind_pose_count, int) or bind_pose_count < 0:
            error(f"Mesh {mesh_id} has an invalid bindPoseCount")
            bind_pose_count = 0
        if not isinstance(vertex_count, int) or vertex_count < 0:
            error(f"Mesh {mesh_id} has an invalid boneWeightVertexCount")
            vertex_count = 0
        if skin_status not in {"noBindPoses", "bindPosesWithoutWeights", "exported", "invalidWeights", "decodeError", "notDecoded"}:
            error(f"Mesh {mesh_id} has an invalid skinDataStatus")
        if skin_status == "exported":
            if not skin_data_id or skin_data_id not in skin_data_by_id:
                error(f"Mesh {mesh_id} advertises missing skin data {skin_data_id!r}")
                continue
            skin_record = skin_data_by_id[skin_data_id]
            if skin_record.get("meshId") != mesh_id:
                error(f"Mesh skin data {skin_data_id} points to a different mesh")
            bind_poses = skin_record.get("bindPoses")
            indices = skin_record.get("boneIndices")
            weights = skin_record.get("boneWeights")
            data_vertex_count = skin_record.get("vertexCount")
            if not isinstance(bind_poses, list) or len(bind_poses) != bind_pose_count:
                error(f"Mesh skin data {skin_data_id} bind-pose array does not match the index")
                bind_poses = bind_poses if isinstance(bind_poses, list) else []
            matrix_fields = [f"e{row}{column}" for row in range(4) for column in range(4)]
            for pose_index, pose in enumerate(bind_poses):
                if not isinstance(pose, dict) or any(
                    not isinstance(pose.get(field), (int, float)) or not math.isfinite(float(pose[field]))
                    for field in matrix_fields
                ):
                    error(f"Mesh skin data {skin_data_id} bind pose {pose_index} is not a finite 4x4 matrix")
                    break
            if not isinstance(data_vertex_count, int) or data_vertex_count < 0:
                error(f"Mesh skin data {skin_data_id} has an invalid vertexCount")
                data_vertex_count = 0
            if data_vertex_count != vertex_count:
                error(f"Mesh skin data {skin_data_id} vertex count does not match the mesh index")

            expected_influence_count = data_vertex_count * 4
            bone_arrays_valid = (
                isinstance(indices, list) and isinstance(weights, list)
                and len(indices) == expected_influence_count and len(weights) == expected_influence_count
            )
            if not bone_arrays_valid:
                error(f"Mesh skin data {skin_data_id} bone arrays must contain four flat influences per vertex")
                indices = []
                weights = []
            corrections = skin_record.get("correctedFourthWeightCount")
            if not isinstance(corrections, int) or corrections < 0 or mesh_record.get("skinWeightCorrections") != corrections:
                error(f"Mesh {mesh_id} fourth-weight correction count does not match its skin data")
            active_bones: set[int] = set()
            for vertex_index in range(data_vertex_count if bone_arrays_valid else 0):
                offset = vertex_index * 4
                indices_row = indices[offset:offset + 4]
                weights_row = weights[offset:offset + 4]
                if any(not isinstance(index, int) for index in indices_row):
                    error(f"Mesh skin data {skin_data_id} vertex {vertex_index} has invalid bone indices")
                    continue
                if any(
                    not isinstance(weight, (int, float)) or not math.isfinite(float(weight))
                    or not -1e-7 <= float(weight) <= 1.000001
                    for weight in weights_row
                ):
                    error(f"Mesh skin data {skin_data_id} vertex {vertex_index} has invalid bone weights")
                    continue
                if abs(sum(float(weight) for weight in weights_row) - 1.0) > 1e-4:
                    error(f"Mesh skin data {skin_data_id} vertex {vertex_index} weights do not sum to one")
                for index, weight in zip(indices_row, weights_row):
                    if weight > 1e-8:
                        if index < 0 or index >= bind_pose_count:
                            error(f"Mesh skin data {skin_data_id} vertex {vertex_index} references a missing bind pose")
                        else:
                            active_bones.add(index)
            skin_active_bone_indices[mesh_id] = active_bones

            geometry = skin_record.get("geometry")
            if not isinstance(geometry, dict):
                error(f"Mesh skin data {skin_data_id} has no source-ordered geometry")
                continue
            geometry_vertex_count = geometry.get("vertexCount")
            if geometry_vertex_count != data_vertex_count:
                error(f"Mesh skin data {skin_data_id} geometry vertex count does not match its weights")
            for field, dimension, required in (
                ("vertices", 3, True), ("normals", 3, False), ("tangents", 4, False), ("colors", 4, False)
            ):
                values = geometry.get(field)
                if not isinstance(values, list):
                    error(f"Mesh skin data {skin_data_id} geometry.{field} must be a flat numeric array")
                    continue
                if (required and len(values) != data_vertex_count * dimension) or (
                    not required and len(values) not in (0, data_vertex_count * dimension)
                ):
                    error(f"Mesh skin data {skin_data_id} geometry.{field} has the wrong vertex-channel length")
                if any(not isinstance(value, (int, float)) or not math.isfinite(float(value)) for value in values):
                    error(f"Mesh skin data {skin_data_id} geometry.{field} contains an invalid number")
                    break

            uv_channels = geometry.get("uvChannels")
            seen_uv_channels: set[int] = set()
            if not isinstance(uv_channels, list):
                error(f"Mesh skin data {skin_data_id} geometry.uvChannels must be an array")
            else:
                for channel_data in uv_channels:
                    if not isinstance(channel_data, dict):
                        error(f"Mesh skin data {skin_data_id} has a malformed UV channel")
                        continue
                    channel = channel_data.get("channel")
                    dimension = channel_data.get("dimension")
                    values = channel_data.get("values")
                    if not isinstance(channel, int) or channel not in range(8) or channel in seen_uv_channels:
                        error(f"Mesh skin data {skin_data_id} has an invalid or duplicate UV channel index")
                        continue
                    seen_uv_channels.add(channel)
                    if not isinstance(dimension, int) or dimension not in range(1, 5) or not isinstance(values, list):
                        error(f"Mesh skin data {skin_data_id} UV{channel} has invalid dimension/data")
                        continue
                    if len(values) != data_vertex_count * dimension or any(
                        not isinstance(value, (int, float)) or not math.isfinite(float(value)) for value in values
                    ):
                        error(f"Mesh skin data {skin_data_id} UV{channel} has invalid vertex-channel data")

            submeshes = geometry.get("submeshes")
            expected_submesh_count = mesh_record.get("submeshes")
            if not isinstance(submeshes, list) or len(submeshes) != expected_submesh_count:
                error(f"Mesh skin data {skin_data_id} submesh array does not match the mesh index")
            elif not submeshes:
                error(f"Mesh skin data {skin_data_id} contains no renderable submeshes")
            else:
                for submesh_index, submesh in enumerate(submeshes):
                    if not isinstance(submesh, dict) or submesh.get("topology") != "Triangles":
                        error(f"Mesh skin data {skin_data_id} submesh {submesh_index} is not serialized as triangles")
                        continue
                    submesh_indices = submesh.get("indices")
                    if not isinstance(submesh_indices, list) or len(submesh_indices) % 3:
                        error(f"Mesh skin data {skin_data_id} submesh {submesh_index} has an invalid triangle index array")
                        continue
                    if any(not isinstance(index, int) or index < 0 or index >= data_vertex_count for index in submesh_indices):
                        error(f"Mesh skin data {skin_data_id} submesh {submesh_index} references an invalid vertex")
                    skin_geometry_triangle_count += len(submesh_indices) // 3
        else:
            if skin_data_id or vertex_count:
                error(f"Mesh {mesh_id} has skin data counts without a decoded archive record")
            if skin_status == "noBindPoses" and bind_pose_count != 0:
                error(f"Mesh {mesh_id} says noBindPoses but has {bind_pose_count} bind poses")
            if skin_status == "bindPosesWithoutWeights" and bind_pose_count == 0:
                error(f"Mesh {mesh_id} reports missing weights without bind poses")
            if skin_status in {"invalidWeights", "decodeError"}:
                error(f"Mesh {mesh_id} skin decoder reported {skin_status}")

    animation_archive_name = "animation-curve-data.json.gz"
    animation_archive = compressed_manifests.get(animation_archive_name, {})
    if animation_archive.get("formatVersion") != 1:
        error(f"{animation_archive_name}: unsupported or missing formatVersion")
    animation_data_by_id = archive_records(animation_archive_name, "animationClips", "Animation curve data")
    animation_by_id = records_by_id(animation_entries, "Animation index")
    if set(animation_by_id) != set(animation_data_by_id):
        error("Animation index and decoded muscle-clip archive contain different clip IDs")
    for clip_id, index_record in animation_by_id.items():
        data_record = animation_data_by_id.get(clip_id)
        if data_record is None:
            continue
        muscle = data_record.get("m_MuscleClip")
        if not isinstance(muscle, dict):
            error(f"Animation curve data {clip_id} has no decoded m_MuscleClip")
            continue
        clip_data = nested_dict(muscle, "m_Clip", "data")
        streamed = nested_dict(clip_data, "m_StreamedClip")
        dense = nested_dict(clip_data, "m_DenseClip")
        constant = nested_dict(clip_data, "m_ConstantClip")
        binding = data_record.get("m_ClipBindingConstant", {})
        if not isinstance(binding, dict):
            binding = {}
        event_data = data_record.get("m_Events", [])
        if not isinstance(event_data, list):
            error(f"Animation curve data {clip_id} has invalid m_Events")
            event_data = []
        start_time = muscle.get("m_StartTime")
        stop_time = muscle.get("m_StopTime")
        if not isinstance(start_time, (int, float)) or not math.isfinite(float(start_time)):
            error(f"Animation index {clip_id} has invalid startTime")
            start_time = 0.0
        if not isinstance(stop_time, (int, float)) or not math.isfinite(float(stop_time)):
            error(f"Animation index {clip_id} has invalid stopTime")
            stop_time = 0.0
        if index_record.get("startTime") != start_time or index_record.get("stopTime") != stop_time:
            error(f"Animation index {clip_id} timing does not match m_MuscleClip")
        expected_duration = max(0.0, float(stop_time) - float(start_time))
        duration = index_record.get("durationSeconds")
        if not isinstance(duration, (int, float)) or not math.isfinite(float(duration)) or abs(float(duration) - expected_duration) > 1e-5:
            error(f"Animation index {clip_id} has an invalid durationSeconds")
        muscle_size = data_record.get("m_MuscleClipSize")
        if not isinstance(muscle_size, int) or muscle_size <= 0 or index_record.get("muscleClipSizeBytes") != muscle_size:
            error(f"Animation index {clip_id} has an invalid m_MuscleClip size")
        actual_curve_counts = {
            "streamed": max(0, int(streamed.get("curveCount", 0) or 0)),
            "dense": max(0, int(dense.get("m_CurveCount", 0) or 0)),
        }
        actual_sample_counts = {
            "streamedWords": len(list_field(streamed, "data")),
            "denseFrames": max(0, int(dense.get("m_FrameCount", 0) or 0)),
            "denseValues": len(list_field(dense, "m_SampleArray")),
            "constantValues": len(list_field(constant, "data")),
        }
        actual_binding_counts = {
            "generic": len(list_field(binding, "genericBindings")),
            "objectReference": len(list_field(binding, "pptrCurveMapping")),
        }
        for section, expected_values in (
            ("curveCounts", actual_curve_counts),
            ("sampleCounts", actual_sample_counts),
            ("bindingCounts", actual_binding_counts),
        ):
            index_values = index_record.get(section, {})
            if not isinstance(index_values, dict):
                error(f"Animation index {clip_id} has invalid {section}")
                continue
            for key, actual in expected_values.items():
                if index_values.get(key) != actual:
                    error(f"Animation index {clip_id} {section}.{key} does not match decoded data")
        if index_record.get("eventCount") != len(event_data):
            error(f"Animation index {clip_id} eventCount does not match decoded events")

    controller_archive_name = "animator-controller-data.json.gz"
    controller_archive = compressed_manifests.get(controller_archive_name, {})
    if controller_archive.get("formatVersion") != 1:
        error(f"{controller_archive_name}: unsupported or missing formatVersion")
    controller_data_by_id = archive_records(controller_archive_name, "controllers", "AnimatorController data")
    controller_by_id = records_by_id(controller_entries, "AnimatorController index")
    if set(controller_by_id) != set(controller_data_by_id):
        error("AnimatorController index and decoded data archive contain different IDs")
    for controller_id, index_record in controller_by_id.items():
        data_record = controller_data_by_id.get(controller_id)
        if data_record is None:
            continue
        tree = data_record.get("data")
        if not isinstance(tree, dict):
            error(f"AnimatorController data {controller_id} has no typetree")
            continue
        expected = {
            "clipCount": len(list_field(tree, "m_AnimationClips")),
            "bindingCount": len(list_field(tree, "m_TOS")),
            "layerCount": count_named_list_items(tree, "m_LayerArray"),
            "stateMachineCount": count_named_list_items(tree, "m_StateMachineArray"),
            "stateCount": count_named_list_items(tree, "m_StateConstantArray"),
            "transitionCount": count_named_fields(tree, "m_DestinationState"),
            "blendTreeCount": count_named_list_items(tree, "m_BlendTreeConstantArray"),
            "stateMachineBehaviourCount": len(list_field(tree, "m_StateMachineBehaviours")),
        }
        for field_name, actual in expected.items():
            if index_record.get(field_name) != actual:
                error(f"AnimatorController index {controller_id} {field_name} does not match decoded data")

    avatar_archive_name = "avatar-data.json.gz"
    avatar_archive = compressed_manifests.get(avatar_archive_name, {})
    if avatar_archive.get("formatVersion") != 1:
        error(f"{avatar_archive_name}: unsupported or missing formatVersion")
    avatar_data_by_id = archive_records(avatar_archive_name, "avatars", "Avatar data")
    avatar_by_id = records_by_id(avatar_entries, "Avatar index")
    if set(avatar_by_id) != set(avatar_data_by_id):
        error("Avatar index and decoded data archive contain different IDs")
    for avatar_id, index_record in avatar_by_id.items():
        data_record = avatar_data_by_id.get(avatar_id)
        if data_record is None:
            continue
        tree = data_record.get("data")
        if not isinstance(tree, dict):
            error(f"Avatar data {avatar_id} has no typetree")
            continue
        avatar_body = nested_dict(tree, "m_Avatar")
        skeleton = nested_dict(avatar_body, "m_AvatarSkeleton", "data")
        skeleton_pose = nested_dict(avatar_body, "m_AvatarSkeletonPose", "data")
        human_description = nested_dict(tree, "m_HumanDescription")
        expected = {
            "sizeBytes": tree.get("m_AvatarSize"),
            "skeletonNodeCount": len(list_field(skeleton, "m_Node")),
            "skeletonPoseCount": len(list_field(skeleton_pose, "m_X")),
            "humanMappingCount": len(list_field(human_description, "m_Human")),
            "humanSkeletonCount": len(list_field(human_description, "m_Skeleton")),
            "transformNameCount": len(list_field(tree, "m_TOS")),
        }
        for field_name, actual in expected.items():
            if index_record.get(field_name) != actual:
                error(f"Avatar index {avatar_id} {field_name} does not match decoded data")

    for material in material_entries:
        for texture in material.get("textures", []) or []:
            texture_id = texture.get("textureId") if isinstance(texture, dict) else None
            if texture_id and texture_id not in textures:
                error(f"Material {material.get('id')} references missing texture {texture_id}")

    scenes = scene_manifest.get("scenes", []) if isinstance(scene_manifest, dict) else []
    if not isinstance(scenes, list) or not scenes:
        error("Scene manifest has no scenes")
        scenes = []

    totals = Counter()
    skin_fallback_mesh_ids: set[str] = set()
    text_font_ids: set[str] = set()

    def validate_button_data(button_data: Any, context: str, objects_by_id: dict[int, dict[str, Any]]) -> None:
        if not isinstance(button_data, dict):
            error(f"{context}: Button has no serialized transition/state data")
            return
        totals["uiButtons"] += 1
        if button_data.get("transition") not in range(4):
            error(f"{context}: Button has an invalid transition mode")
        navigation = button_data.get("navigation")
        if not isinstance(navigation, dict) or navigation.get("mode") not in range(5):
            error(f"{context}: Button has invalid navigation data")
        else:
            for field in ("selectOnUpObject", "selectOnDownObject", "selectOnLeftObject", "selectOnRightObject"):
                target_id = navigation.get(field, 0)
                if not isinstance(target_id, int) or target_id and target_id not in objects_by_id:
                    error(f"{context}: Button navigation {field} references an invalid GameObject")
        colors = button_data.get("colors")
        color_fields = ("normal", "highlighted", "pressed", "selected", "disabled")
        if not isinstance(colors, dict):
            error(f"{context}: Button has no serialized ColorBlock")
        else:
            for field in color_fields:
                value = colors.get(field)
                if not isinstance(value, list) or len(value) != 4 or any(not isinstance(v, (int, float)) or not math.isfinite(v) or not 0 <= v <= 1 for v in value):
                    error(f"{context}: Button ColorBlock.{field} is invalid")
            for field in ("colorMultiplier", "fadeDuration"):
                value = colors.get(field)
                if not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
                    error(f"{context}: Button ColorBlock.{field} is invalid")
        for field in ("highlighted", "pressed", "selected", "disabled"):
            sprite_id = (button_data.get("sprites") or {}).get(field, "")
            if sprite_id and sprite_id not in sprites:
                error(f"{context}: Button sprite state {field} references missing sprite {sprite_id}")
        target_id = button_data.get("targetGraphicObject", 0)
        if not isinstance(target_id, int) or target_id and target_id not in objects_by_id:
            error(f"{context}: Button targetGraphic references a missing GameObject")
        call_count = button_data.get("persistentCallCount", 0)
        if not isinstance(call_count, int) or not 0 <= call_count <= 10000:
            error(f"{context}: Button has an invalid persistent event count")
            call_count = 0
        else:
            totals["buttonPersistentCalls"] += call_count
        calls = button_data.get("persistentCalls")
        if not isinstance(calls, list):
            error(f"{context}: Button has no decoded persistent event list")
            calls = []
        if button_data.get("persistentCallsDecoded") is not True or len(calls) != call_count:
            error(f"{context}: Button persistent event list is incomplete")
        for index, call in enumerate(calls):
            call_context = f"{context}: persistent call {index}"
            if not isinstance(call, dict):
                error(f"{call_context} is not an object")
                continue
            mode = call.get("mode")
            state = call.get("callState")
            target_type = call.get("targetType")
            target_id = call.get("targetObjectId")
            method_name = call.get("methodName")
            if mode not in range(7) or state not in range(3):
                error(f"{call_context} has invalid mode/call state")
            if not isinstance(method_name, str) or not method_name:
                error(f"{call_context} has no method name")
            target_entry = objects_by_id.get(target_id) if isinstance(target_id, int) else None
            if target_entry is None:
                error(f"{call_context} references a missing target GameObject")
                continue
            if not isinstance(call.get("targetPathId"), int) or call.get("targetPathId") == 0:
                error(f"{call_context} has an invalid serialized target path ID")
            if not isinstance(target_type, str) or not target_type:
                error(f"{call_context} has an unresolved serialized target type")
            if target_type == "MonoBehaviour":
                script_status = call.get("targetScriptStatus")
                if script_status not in {"resolved", "nullScriptPointer", "unresolvedScriptPointer", "unreadableMonoBehaviour"}:
                    error(f"{call_context} has no valid target script resolution status")
                elif script_status == "resolved" and not call.get("targetScript"):
                    error(f"{call_context} claims a resolved MonoBehaviour script without a type name")
                elif script_status == "nullScriptPointer" and call.get("targetScript"):
                    error(f"{call_context} has a type name despite a null MonoScript pointer")
            if not isinstance(call.get("intArgument"), int):
                error(f"{call_context} has an invalid integer argument")
            float_argument = call.get("floatArgument")
            if not isinstance(float_argument, (int, float)) or not math.isfinite(float_argument):
                error(f"{call_context} has an invalid float argument")
            if not isinstance(call.get("stringArgument"), str) or not isinstance(call.get("boolArgument"), bool):
                error(f"{call_context} has invalid string/boolean arguments")
            if target_type == "AudioSource" and method_name == "Play" and mode == 1:
                if "AudioSource" not in (target_entry.get("components") or []) or target_entry.get("audioSource") is None:
                    error(f"{call_context} cannot be rebound because its AudioSource component is missing")
                else:
                    totals["nativeButtonCallbacks"] += 1
            elif target_type == "GameObject" and method_name == "SetActive" and mode == 6:
                totals["nativeButtonCallbacks"] += 1

    unexported_referenced_mesh_ids: set[str] = set()
    scene_names: set[str] = set()
    for scene in scenes:
        if not isinstance(scene, dict):
            error("Scene manifest contains a non-object scene entry")
            continue
        scene_name = str(scene.get("name", "<unnamed>"))
        if scene_name in scene_names:
            error(f"Duplicate scene name: {scene_name}")
        scene_names.add(scene_name)
        objects = scene.get("objects", [])
        if not isinstance(objects, list):
            error(f"{scene_name}: objects must be a list")
            continue
        if scene.get("objectCount") != len(objects):
            error(f"{scene_name}: objectCount does not match objects array")

        object_by_id: dict[int, dict[str, Any]] = {}
        for obj in objects:
            if not isinstance(obj, dict):
                error(f"{scene_name}: contains a non-object GameObject record")
                continue
            object_id = obj.get("id")
            if not isinstance(object_id, int):
                error(f"{scene_name}: GameObject has an invalid id: {object_id!r}")
                continue
            if object_id in object_by_id:
                error(f"{scene_name}: duplicate GameObject id {object_id}")
            object_by_id[object_id] = obj

        parents: dict[int, int] = {}
        scene_mesh_ids: set[str] = set()
        for object_id, obj in object_by_id.items():
            totals["objects"] += 1
            parent_id = obj.get("parent", 0)
            if not isinstance(parent_id, int):
                error(f"{scene_name}: object {object_id} has invalid parent id {parent_id!r}")
                parent_id = 0
            parents[object_id] = parent_id
            if parent_id and parent_id not in object_by_id:
                error(f"{scene_name}: object {object_id} references missing parent {parent_id}")
            if parent_id == object_id:
                error(f"{scene_name}: object {object_id} is its own parent")

            transform = obj.get("transform")
            if not isinstance(transform, dict):
                error(f"{scene_name}: object {object_id} has no transform record")
            else:
                arrays = {"position": 3, "rotation": 4, "scale": 3}
                if transform.get("kind") == "RectTransform":
                    arrays.update({"anchorMin": 2, "anchorMax": 2, "anchoredPosition": 3, "sizeDelta": 2, "pivot": 2})
                for key, minimum_length in arrays.items():
                    value = transform.get(key)
                    if not isinstance(value, list) or len(value) < minimum_length:
                        error(f"{scene_name}: object {object_id} has invalid transform.{key}")

            for value in all_values(obj):
                if isinstance(value, float) and not math.isfinite(value):
                    error(f"{scene_name}: object {object_id} contains a non-finite number")
                    break

            for mesh_id in obj.get("meshes", []) or []:
                scene_mesh_ids.add(mesh_id)
                if mesh_id not in meshes:
                    error(f"{scene_name}: object {object_id} references missing mesh {mesh_id}")
            for material_id in obj.get("materials", []) or []:
                if material_id not in materials:
                    error(f"{scene_name}: object {object_id} references missing material {material_id}")
            sprite_id = obj.get("sprite")
            if sprite_id and sprite_id not in sprites:
                error(f"{scene_name}: object {object_id} references missing sprite {sprite_id}")

            image_data = obj.get("uiImageData")
            if obj.get("uiImage"):
                if not isinstance(image_data, dict):
                    error(f"{scene_name}: UI Image on object {object_id} has no serialized style data")
                else:
                    totals["styledImages"] += 1
                    color = image_data.get("color")
                    if not isinstance(color, list) or len(color) != 4 or any(not isinstance(v, (int, float)) or not 0 <= v <= 1 for v in color):
                        error(f"{scene_name}: UI Image on object {object_id} has invalid tint color")
                    if image_data.get("type") not in range(4) or image_data.get("fillMethod") not in range(5):
                        error(f"{scene_name}: UI Image on object {object_id} has invalid type/fill metadata")
            text_data = obj.get("uiTextData")
            if obj.get("uiText"):
                if not isinstance(text_data, dict):
                    error(f"{scene_name}: UI Text on object {object_id} has no serialized style data")
                else:
                    totals["styledTexts"] += 1
                    color = text_data.get("color")
                    if not isinstance(color, list) or len(color) != 4 or any(not isinstance(v, (int, float)) or not 0 <= v <= 1 for v in color):
                        error(f"{scene_name}: UI Text on object {object_id} has invalid tint color")
                    if text_data.get("fontStyle") not in range(4) or text_data.get("alignment") not in range(9):
                        error(f"{scene_name}: UI Text on object {object_id} has invalid font/alignment metadata")
                    font_id = text_data.get("fontId")
                    if not isinstance(font_id, str) or not font_id or font_id not in fonts or not fonts[font_id].get("exported"):
                        error(f"{scene_name}: UI Text on object {object_id} references an unavailable Font asset")
                    else:
                        totals["textFontReferences"] += 1
                        text_font_ids.add(font_id)
                    if text_data.get("maxSize", -1) < text_data.get("minSize", 0):
                        error(f"{scene_name}: UI Text on object {object_id} has inverted best-fit size limits")
            if obj.get("uiButton"):
                validate_button_data(obj.get("uiButtonData"), f"{scene_name}: object {object_id}", object_by_id)
            ui_effects = obj.get("uiEffects", []) or []
            if not isinstance(ui_effects, list):
                error(f"{scene_name}: object {object_id} has invalid UI graphic-effect data")
                ui_effects = []
            for effect_data in ui_effects:
                if not isinstance(effect_data, dict) or effect_data.get("type") not in ("Shadow", "Outline"):
                    error(f"{scene_name}: object {object_id} has unsupported UI graphic effect")
                    continue
                totals["uiGraphicEffects"] += 1
                effect_color = effect_data.get("color")
                effect_distance = effect_data.get("distance")
                if not isinstance(effect_color, list) or len(effect_color) != 4 or any(not isinstance(v, (int, float)) or not 0 <= v <= 1 for v in effect_color):
                    error(f"{scene_name}: {effect_data['type']} on object {object_id} has invalid color")
                if not isinstance(effect_distance, list) or len(effect_distance) != 2 or any(not isinstance(v, (int, float)) for v in effect_distance):
                    error(f"{scene_name}: {effect_data['type']} on object {object_id} has invalid distance")
            scaler_data = obj.get("canvasScaler")
            if scaler_data is not None:
                totals["canvasScalers"] += 1
                if scaler_data.get("uiScaleMode") not in range(3) or scaler_data.get("screenMatchMode") not in range(3):
                    error(f"{scene_name}: CanvasScaler on object {object_id} has invalid scale mode")
                resolution = scaler_data.get("referenceResolution")
                if not isinstance(resolution, list) or len(resolution) != 2 or any(v <= 0 for v in resolution):
                    error(f"{scene_name}: CanvasScaler on object {object_id} has invalid reference resolution")
            canvas_data = obj.get("canvas")
            if canvas_data is not None:
                totals["canvases"] += 1
                camera_id = canvas_data.get("worldCameraObject", 0)
                if camera_id and camera_id not in object_by_id:
                    error(f"{scene_name}: Canvas on object {object_id} references missing camera GameObject {camera_id}")
            canvas_group = obj.get("canvasGroup")
            if canvas_group is not None:
                totals["canvasGroups"] += 1
                if not isinstance(canvas_group.get("alpha"), (int, float)) or not 0 <= canvas_group["alpha"] <= 1:
                    error(f"{scene_name}: CanvasGroup on object {object_id} has invalid alpha")
            renderer_entries = obj.get("renderers", []) or []
            if not isinstance(renderer_entries, list):
                error(f"{scene_name}: object {object_id} has invalid renderer settings")
                renderer_entries = []
            for renderer_data in renderer_entries:
                if not isinstance(renderer_data, dict) or renderer_data.get("type") not in {
                    "MeshRenderer", "SkinnedMeshRenderer", "SpriteRenderer", "ParticleSystemRenderer"
                }:
                    error(f"{scene_name}: object {object_id} has unsupported renderer metadata")
                    continue
                totals["rendererSettings"] += 1
                if renderer_data.get("castShadows") not in range(4):
                    error(f"{scene_name}: object {object_id} has invalid renderer shadow mode")
                if renderer_data.get("type") == "SkinnedMeshRenderer":
                    totals["skinnedRenderers"] += 1
                    skinned_mesh_id = renderer_data.get("meshId")
                    if not isinstance(skinned_mesh_id, str) or skinned_mesh_id not in meshes:
                        error(f"{scene_name}: SkinnedMeshRenderer on object {object_id} references missing mesh {skinned_mesh_id!r}")
                    root_file_id = renderer_data.get("rootBoneFileId")
                    root_path_id = renderer_data.get("rootBonePathId")
                    root_object_id = renderer_data.get("rootBoneObject")
                    if not all(isinstance(value, int) for value in (root_file_id, root_path_id, root_object_id)):
                        error(f"{scene_name}: SkinnedMeshRenderer on object {object_id} has invalid root-bone metadata")
                    elif root_file_id == 0 and root_path_id and (not root_object_id or root_object_id not in object_by_id):
                        error(f"{scene_name}: SkinnedMeshRenderer on object {object_id} has an unresolved local root bone")
                    elif root_object_id and root_object_id not in object_by_id:
                        error(f"{scene_name}: SkinnedMeshRenderer on object {object_id} references missing root-bone GameObject {root_object_id}")
                    bone_files = renderer_data.get("boneFileIds")
                    bone_paths = renderer_data.get("bonePathIds")
                    bone_objects = renderer_data.get("boneObjects")
                    if not all(isinstance(values, list) for values in (bone_files, bone_paths, bone_objects)):
                        error(f"{scene_name}: SkinnedMeshRenderer on object {object_id} has invalid bone arrays")
                    elif not (len(bone_files) == len(bone_paths) == len(bone_objects) == renderer_data.get("boneCount")):
                        error(f"{scene_name}: SkinnedMeshRenderer on object {object_id} bone-array lengths do not match boneCount")
                    else:
                        for bone_file_id, bone_path_id, bone_object_id in zip(bone_files, bone_paths, bone_objects):
                            if not all(isinstance(value, int) for value in (bone_file_id, bone_path_id, bone_object_id)):
                                error(f"{scene_name}: SkinnedMeshRenderer on object {object_id} has invalid bone pointer values")
                                continue
                            if bone_file_id == 0 and bone_path_id and (not bone_object_id or bone_object_id not in object_by_id):
                                error(f"{scene_name}: SkinnedMeshRenderer on object {object_id} has an unresolved local bone")
                            elif bone_object_id and bone_object_id not in object_by_id:
                                error(f"{scene_name}: SkinnedMeshRenderer on object {object_id} references missing bone GameObject {bone_object_id}")
                            if bone_path_id:
                                totals["skinnedBoneReferences"] += 1
                    skin_record = skin_data_by_id.get(skinned_mesh_id) if isinstance(skinned_mesh_id, str) else None
                    if skin_record is None:
                        totals["skinnedStaticFallbacks"] += 1
                        if isinstance(skinned_mesh_id, str) and skinned_mesh_id:
                            skin_fallback_mesh_ids.add(skinned_mesh_id)
                    else:
                        totals["skinnedSkinReadyRenderers"] += 1
                        bind_pose_count = skin_record.get("bindPoseCount")
                        if renderer_data.get("boneCount") != bind_pose_count:
                            error(
                                f"{scene_name}: SkinnedMeshRenderer on object {object_id} has "
                                f"{renderer_data.get('boneCount')} bones for {bind_pose_count} bind poses"
                            )
                        if isinstance(bone_objects, list) and isinstance(bone_files, list) and isinstance(bone_paths, list):
                            for bone_index in skin_active_bone_indices.get(skinned_mesh_id, set()):
                                if bone_index >= len(bone_objects):
                                    error(
                                        f"{scene_name}: SkinnedMeshRenderer on object {object_id} is missing "
                                        f"weighted bone slot {bone_index}"
                                    )
                                elif bone_objects[bone_index] == 0 or bone_files[bone_index] != 0 or bone_paths[bone_index] == 0:
                                    error(
                                        f"{scene_name}: SkinnedMeshRenderer on object {object_id} cannot resolve "
                                        f"weighted bone slot {bone_index} locally"
                                    )

            audio_source_data = obj.get("audioSource")
            if audio_source_data is not None:
                audio_id = audio_source_data.get("clip")
                if audio_id:
                    totals["audioSourceReferences"] += 1
                    if audio_id not in audio_ids:
                        error(f"{scene_name}: AudioSource on object {object_id} references missing AudioClip {audio_id}")
                    elif audio_id in exported_audio_ids:
                        totals["audioAssetsReferenced"] += 1
            animator_data = obj.get("animator")
            if animator_data is not None:
                if not isinstance(animator_data, dict):
                    error(f"{scene_name}: Animator on object {object_id} has invalid serialized data")
                else:
                    controller_id = animator_data.get("controllerId", "")
                    avatar_id = animator_data.get("avatarId", "")
                    if controller_id and controller_id not in controller_by_id:
                        error(f"{scene_name}: Animator on object {object_id} references missing controller {controller_id}")
                    if avatar_id and avatar_id not in avatar_by_id:
                        error(f"{scene_name}: Animator on object {object_id} references missing Avatar {avatar_id}")
            legacy_animation = obj.get("legacyAnimation")
            if legacy_animation is not None:
                if not isinstance(legacy_animation, dict):
                    error(f"{scene_name}: Animation on object {object_id} has invalid serialized data")
                else:
                    for clip_id in legacy_animation.get("clipIds", []) or []:
                        if clip_id not in animation_by_id:
                            error(f"{scene_name}: Animation on object {object_id} references missing AnimationClip {clip_id}")
                    default_clip_id = legacy_animation.get("defaultClipId", "")
                    if default_clip_id and default_clip_id not in animation_by_id:
                        error(f"{scene_name}: Animation on object {object_id} references missing default AnimationClip {default_clip_id}")
            camera_data = obj.get("camera")
            if camera_data is not None:
                totals["cameraSettings"] += 1
                if camera_data.get("clearFlags") not in (1, 2, 3, 4):
                    error(f"{scene_name}: Camera on object {object_id} has invalid clear flags")
                if not isinstance(camera_data.get("cullingMask"), int) or not -(2**31) <= camera_data["cullingMask"] < 2**31:
                    error(f"{scene_name}: Camera on object {object_id} has invalid culling mask")
            light_data = obj.get("light")
            if light_data is not None:
                totals["lightSettings"] += 1
                if light_data.get("type") not in range(4) or light_data.get("shadows") not in range(3):
                    error(f"{scene_name}: Light on object {object_id} has invalid type/shadow metadata")

            colliders = obj.get("colliders", []) or []
            totals["colliders"] += len(colliders)
            for collider in colliders:
                if not isinstance(collider, dict):
                    error(f"{scene_name}: object {object_id} has an invalid collider record")
                    continue
                if collider.get("type") not in {"BoxCollider", "SphereCollider", "CapsuleCollider", "MeshCollider"}:
                    error(f"{scene_name}: unsupported collider type {collider.get('type')!r}")
                collider_mesh = collider.get("mesh")
                if collider_mesh:
                    scene_mesh_ids.add(collider_mesh)
                    if collider_mesh not in meshes:
                        error(f"{scene_name}: collider on object {object_id} references missing mesh {collider_mesh}")
            totals["rigidbodies"] += obj.get("rigidbody") is not None
            totals["characterJoints"] += obj.get("characterJoint") is not None
            totals["navMeshAgents"] += obj.get("navMeshAgent") is not None
            totals["navMeshObstacles"] += obj.get("navMeshObstacle") is not None

        # Parent links should form a forest, not a cyclic transform hierarchy.
        state: dict[int, int] = {}
        for start in parents:
            if state.get(start, 0) == 2:
                continue
            trail: list[int] = []
            node = start
            while node in parents and state.get(node, 0) == 0:
                state[node] = 1
                trail.append(node)
                node = parents[node]
            if node in parents and state.get(node) == 1:
                error(f"{scene_name}: cyclic transform hierarchy includes object {node}")
            for visited in trail:
                state[visited] = 2

        for mesh_id in scene_mesh_ids:
            if mesh_id in meshes and not meshes[mesh_id].get("exported", False):
                unexported_referenced_mesh_ids.add(mesh_id)

    ui_prefab_ids: set[str] = set()
    for prefab in ui_prefab_entries:
        prefab_id = prefab.get("id")
        if not isinstance(prefab_id, str) or not prefab_id:
            error("UI prefab manifest contains an entry without a valid id")
        elif prefab_id in ui_prefab_ids:
            error(f"Duplicate shared-asset UI prefab id: {prefab_id}")
        else:
            ui_prefab_ids.add(prefab_id)
        prefab_name = str(prefab.get("name", "<unnamed>"))
        objects = prefab.get("objects", [])
        if not isinstance(objects, list) or not objects:
            error(f"UI prefab {prefab_name}: objects must be a non-empty list")
            continue
        if prefab.get("objectCount") != len(objects):
            error(f"UI prefab {prefab_name}: objectCount does not match objects array")
        object_by_id: dict[int, dict[str, Any]] = {}
        for obj in objects:
            if not isinstance(obj, dict):
                error(f"UI prefab {prefab_name}: contains a non-object GameObject record")
                continue
            object_id = obj.get("id")
            if not isinstance(object_id, int):
                error(f"UI prefab {prefab_name}: GameObject has an invalid id")
                continue
            if object_id in object_by_id:
                error(f"UI prefab {prefab_name}: duplicate GameObject id {object_id}")
            object_by_id[object_id] = obj
        roots = 0
        parent_by_id: dict[int, int] = {}
        for object_id, obj in object_by_id.items():
            totals["uiPrefabObjects"] += 1
            parent_id = obj.get("parent", 0)
            if not isinstance(parent_id, int):
                error(f"UI prefab {prefab_name}: object {object_id} has invalid parent id")
                parent_id = 0
            parent_by_id[object_id] = parent_id
            if parent_id == 0:
                roots += 1
            elif parent_id not in object_by_id:
                error(f"UI prefab {prefab_name}: object {object_id} references missing parent {parent_id}")
            if not isinstance(obj.get("transform"), dict):
                error(f"UI prefab {prefab_name}: object {object_id} has no transform record")
            sprite_id = obj.get("sprite")
            if sprite_id and sprite_id not in sprites:
                error(f"UI prefab {prefab_name}: object {object_id} references missing sprite {sprite_id}")
            if obj.get("uiImage"):
                image_data = obj.get("uiImageData")
                if not isinstance(image_data, dict):
                    error(f"UI prefab {prefab_name}: Image on object {object_id} has no serialized style data")
                else:
                    totals["prefabStyledImages"] += 1
                    color = image_data.get("color")
                    if not isinstance(color, list) or len(color) != 4 or any(not isinstance(v, (int, float)) or not 0 <= v <= 1 for v in color):
                        error(f"UI prefab {prefab_name}: Image on object {object_id} has invalid tint color")
            if obj.get("uiText"):
                text_data = obj.get("uiTextData")
                if not isinstance(text_data, dict):
                    error(f"UI prefab {prefab_name}: Text on object {object_id} has no serialized style data")
                else:
                    totals["prefabStyledTexts"] += 1
                    color = text_data.get("color")
                    if not isinstance(color, list) or len(color) != 4 or any(not isinstance(v, (int, float)) or not 0 <= v <= 1 for v in color):
                        error(f"UI prefab {prefab_name}: Text on object {object_id} has invalid tint color")
                    font_id = text_data.get("fontId")
                    if not isinstance(font_id, str) or not font_id or font_id not in fonts or not fonts[font_id].get("exported"):
                        error(f"UI prefab {prefab_name}: Text on object {object_id} references an unavailable Font asset")
                    else:
                        totals["textFontReferences"] += 1
                        text_font_ids.add(font_id)
            if obj.get("uiButton"):
                validate_button_data(obj.get("uiButtonData"), f"UI prefab {prefab_name}: object {object_id}", object_by_id)
            effects = obj.get("uiEffects", []) or []
            if not isinstance(effects, list):
                error(f"UI prefab {prefab_name}: object {object_id} has invalid UI graphic-effect data")
                effects = []
            for effect_data in effects:
                if not isinstance(effect_data, dict) or effect_data.get("type") not in ("Shadow", "Outline"):
                    error(f"UI prefab {prefab_name}: object {object_id} has unsupported UI graphic effect")
                    continue
                totals["prefabStyledEffects"] += 1
                effect_color = effect_data.get("color")
                effect_distance = effect_data.get("distance")
                if not isinstance(effect_color, list) or len(effect_color) != 4 or any(not isinstance(v, (int, float)) or not 0 <= v <= 1 for v in effect_color):
                    error(f"UI prefab {prefab_name}: {effect_data['type']} on object {object_id} has invalid color")
                if not isinstance(effect_distance, list) or len(effect_distance) != 2 or any(not isinstance(v, (int, float)) for v in effect_distance):
                    error(f"UI prefab {prefab_name}: {effect_data['type']} on object {object_id} has invalid distance")
        totals["uiPrefabs"] += 1
        if roots != 1:
            error(f"UI prefab {prefab_name}: expected exactly one root GameObject, found {roots}")
        for start in parent_by_id:
            seen: set[int] = set()
            node = start
            while node in parent_by_id and parent_by_id[node] != 0:
                if node in seen:
                    error(f"UI prefab {prefab_name}: cyclic hierarchy includes object {node}")
                    break
                seen.add(node)
                node = parent_by_id[node]

    il2cpp_summary: dict[str, Any] | None = None
    if il2cpp_script_metadata is not None:
        script_types = il2cpp_script_metadata.get("scriptTypes")
        source_script_names = il2cpp_script_metadata.get("sourceScriptNames")
        unmatched_script_names = il2cpp_script_metadata.get("unmatchedScriptNames")
        if not isinstance(script_types, list) or not isinstance(source_script_names, list) or not isinstance(unmatched_script_names, list):
            error("IL2CPP script metadata has invalid script type/name lists")
            script_types = []
            source_script_names = []
            unmatched_script_names = []

        expected_script_names: set[str] = set()
        for scene in scenes:
            for game_object in scene.get("objects", []) or []:
                expected_script_names.update(
                    name for name in game_object.get("scripts", []) or []
                    if isinstance(name, str) and name
                )
        for prefab in ui_prefab_entries:
            for game_object in prefab.get("objects", []) or []:
                expected_script_names.update(
                    name for name in game_object.get("scripts", []) or []
                    if isinstance(name, str) and name
                )
        if set(source_script_names) != expected_script_names:
            error("IL2CPP script metadata is stale: referenced script types differ from the current scene/prefab manifests")

        indexed_script_names: set[str] = set()
        script_type_lookup: dict[tuple[str, str], list[dict[str, Any]]] = {}
        indexed_field_count = 0
        indexed_method_count = 0
        for index, script_type in enumerate(script_types):
            if not isinstance(script_type, dict):
                error(f"IL2CPP script metadata entry {index} is not an object")
                continue
            qualified_name = script_type.get("qualifiedName")
            assembly = script_type.get("assembly")
            fields = script_type.get("fields")
            methods = script_type.get("methods")
            if not isinstance(qualified_name, str) or not qualified_name or not isinstance(assembly, str) or not assembly:
                error(f"IL2CPP script metadata entry {index} has an invalid type identity")
                continue
            if not isinstance(fields, list) or not isinstance(methods, list):
                error(f"IL2CPP type {qualified_name} has invalid field/method lists")
                continue
            indexed_script_names.add(qualified_name)
            script_type_lookup.setdefault((qualified_name, assembly), []).append(script_type)
            indexed_field_count += len(fields)
            indexed_method_count += len(methods)
            for field in fields:
                if not isinstance(field, dict) or not isinstance(field.get("declaration"), str):
                    error(f"IL2CPP type {qualified_name} has an invalid field declaration")
            for method in methods:
                if (
                    not isinstance(method, dict)
                    or not isinstance(method.get("name"), str)
                    or not isinstance(method.get("signature"), str)
                    or method.get("bodyRecovered") is not False
                ):
                    error(f"IL2CPP type {qualified_name} has an invalid method metadata entry")
        if indexed_script_names | set(unmatched_script_names) != expected_script_names:
            error("IL2CPP script metadata does not account for every referenced scene/prefab script type")

        recorded_counts = il2cpp_script_metadata.get("counts", {})
        expected_counts = {
            "referencedScriptTypes": len(source_script_names),
            "indexedScriptTypes": len(script_types),
            "unmatchedScriptTypes": len(unmatched_script_names),
            "indexedFields": indexed_field_count,
            "indexedMethodSignatures": indexed_method_count,
        }
        for key, value in expected_counts.items():
            if not isinstance(recorded_counts, dict) or recorded_counts.get(key) != value:
                error(f"IL2CPP script metadata count mismatch for {key}")

        callback_records: list[dict[str, Any]] = []
        for scene in scenes:
            for game_object in scene.get("objects", []) or []:
                for call in (game_object.get("uiButtonData") or {}).get("persistentCalls", []) or []:
                    if isinstance(call, dict) and call.get("targetType") == "MonoBehaviour":
                        callback_records.append(call)
        for prefab in ui_prefab_entries:
            for game_object in prefab.get("objects", []) or []:
                for call in (game_object.get("uiButtonData") or {}).get("persistentCalls", []) or []:
                    if isinstance(call, dict) and call.get("targetType") == "MonoBehaviour":
                        callback_records.append(call)

        matched_callbacks = 0
        unresolved_callback_reasons: Counter[str] = Counter()
        for call in callback_records:
            target_script = str(call.get("targetScript", "") or "")
            target_assembly = str(call.get("targetScriptAssembly", "") or "")
            if target_assembly and not target_assembly.lower().endswith(".dll"):
                target_assembly += ".dll"
            candidates = [
                item for item in script_type_lookup.get((target_script, target_assembly), [])
            ] if target_assembly else [
                item for (name, _assembly), items in script_type_lookup.items()
                if name == target_script for item in items
            ]
            method_name = call.get("methodName")
            method_matches = [
                method for item in candidates for method in item.get("methods", [])
                if method.get("name") == method_name
            ]
            if method_matches:
                matched_callbacks += 1
            elif not candidates and call.get("targetScriptStatus") == "nullScriptPointer":
                unresolved_callback_reasons["nullScriptPointer"] += 1
            elif not candidates and target_script:
                unresolved_callback_reasons["targetScriptNotInDump"] += 1
            elif not candidates:
                unresolved_callback_reasons["targetScriptMissingOrNotInDump"] += 1
            else:
                unresolved_callback_reasons["methodNameNotFoundInType"] += 1

        callback_counts = il2cpp_script_metadata.get("persistentCallbackResolution", {})
        expected_callback_counts = {
            "monoBehaviourCalls": len(callback_records),
            "methodNameMatchedCalls": matched_callbacks,
            "unresolvedCalls": len(callback_records) - matched_callbacks,
        }
        for key, value in expected_callback_counts.items():
            if not isinstance(callback_counts, dict) or callback_counts.get(key) != value:
                error(f"IL2CPP callback metadata count mismatch for {key}")
        if isinstance(callback_counts, dict) and callback_counts.get("unresolvedByReason") != dict(sorted(unresolved_callback_reasons.items())):
            error("IL2CPP callback unresolved-reason counts do not match serialized scene/prefab data")
        il2cpp_summary = {
            "scriptTypes": len(script_types),
            "fields": indexed_field_count,
            "methods": indexed_method_count,
            "matchedCallbacks": matched_callbacks,
            "totalCallbacks": len(callback_records),
            "unresolvedCallbacks": len(callback_records) - matched_callbacks,
            "unresolvedByReason": dict(sorted(unresolved_callback_reasons.items())),
        }

    for font in font_entries:
        font_id = font.get("id")
        referenced_by_text = font.get("referencedByUiText")
        if not isinstance(referenced_by_text, bool):
            error(f"Font {font_id}: referencedByUiText must be a boolean")
        elif referenced_by_text != (font_id in text_font_ids):
            error(f"Font {font_id}: referencedByUiText does not match serialized Text references")

    # Confirm the ZIP can be read and contains each OBJ advertised as exported.
    archive_path = RECOVERED_ROOT / "Compressed" / "mesh-exports.zip"
    exported_meshes = [item for item in mesh_entries if item.get("exported")]
    if not archive_path.is_file():
        error(f"Missing OBJ archive: {archive_path.relative_to(PROJECT_ROOT)}")
    else:
        try:
            with zipfile.ZipFile(archive_path) as archive:
                damaged_member = archive.testzip()
                if damaged_member:
                    error(f"Corrupt OBJ archive member: {damaged_member}")
                archive_names = {PurePosixPath(name).name for name in archive.namelist()}
                for mesh in exported_meshes:
                    obj_entry = mesh.get("objEntry")
                    if not obj_entry or PurePosixPath(obj_entry).name not in archive_names:
                        error(f"Exported mesh missing from OBJ archive: {mesh.get('id')}")
                if len(archive_names) != len(exported_meshes):
                    error(f"OBJ archive has {len(archive_names)} entries; manifest advertises {len(exported_meshes)} exported meshes")
        except Exception as exc:
            error(f"Cannot validate OBJ archive: {type(exc).__name__}: {exc}")

    project_version_path = PROJECT_ROOT / "ProjectSettings" / "ProjectVersion.txt"
    if project_version_path.is_file() and isinstance(scene_manifest, dict):
        project_version = next(
            (line.split(":", 1)[1].strip() for line in project_version_path.read_text(encoding="utf-8").splitlines() if line.startswith("m_EditorVersion:")),
            None,
        )
        if project_version and scene_manifest.get("unityVersion") != project_version:
            error(f"Unity version mismatch: scene data {scene_manifest.get('unityVersion')}, project {project_version}")

    for name, key in (
        ("fonts.json", "fonts"),
        ("ui-prefabs.json", "prefabs"),
        ("audio-index.json", "audioClips"),
        ("animation-index.json", "animationClips"),
        ("animator-controller-index.json", "controllers"),
        ("avatar-index.json", "avatars"),
    ):
        if name in manifests and not isinstance(manifests[name].get(key), list):
            error(f"{name}: missing or invalid '{key}' list")

    if unexported_referenced_mesh_ids:
        mesh_names = ", ".join(sorted(unexported_referenced_mesh_ids))
        warn(
            f"{len(unexported_referenced_mesh_ids)} referenced mesh asset(s) are not exported "
            f"and will be missing from rebuilt visuals: {mesh_names}"
        )
    if skin_fallback_mesh_ids:
        fallback_names = ", ".join(
            str(mesh_by_id.get(mesh_id, {}).get("name", mesh_id))
            for mesh_id in sorted(skin_fallback_mesh_ids)
        )
        warn(
            f"{totals['skinnedStaticFallbacks']} SkinnedMeshRenderer instance(s) use static MeshRenderer fallback "
            f"because no complete weight archive is available for: {fallback_names}"
        )

    print(f"Unity version: {scene_manifest.get('unityVersion', 'unknown') if isinstance(scene_manifest, dict) else 'unknown'}")
    print(f"Scenes: {len(scenes)} ({', '.join(sorted(scene_names))})")
    print(
        "Scene totals: "
        f"{totals['objects']:,} GameObjects, {totals['colliders']:,} colliders, "
        f"{totals['rigidbodies']:,} rigidbodies, {totals['characterJoints']:,} CharacterJoints, "
        f"{totals['navMeshAgents']:,} NavMeshAgents, {totals['navMeshObstacles']:,} NavMeshObstacles"
    )
    print(
        "Restored visual metadata: "
        f"{totals['styledImages']:,} styled UI Images, {totals['styledTexts']:,} styled UI Texts, "
        f"{totals['uiGraphicEffects']:,} styled Shadow/Outline effects, "
        f"{totals['canvasScalers']:,} CanvasScalers, {totals['canvases']:,} Canvases, "
        f"{totals['canvasGroups']:,} CanvasGroups, {totals['rendererSettings']:,} renderer settings, "
        f"{totals['cameraSettings']:,} Cameras, "
        f"{totals['lightSettings']:,} Lights"
    )
    print(
        f"Shared-asset UI prefabs: {totals['uiPrefabs']:,} roots, {totals['uiPrefabObjects']:,} GameObjects, "
        f"{totals['prefabStyledImages']:,} styled Images, {totals['prefabStyledTexts']:,} styled Texts, "
        f"{totals['prefabStyledEffects']:,} styled Shadow/Outline effects"
    )
    print(
        f"UI Buttons: {totals['uiButtons']:,} with serialized transition/ColorBlock/navigation, "
        f"{totals['buttonPersistentCalls']:,} persistent calls decoded; "
        f"{totals['nativeButtonCallbacks']:,} built-in Unity callbacks can be rebound, "
        f"{max(0, totals['buttonPersistentCalls'] - totals['nativeButtonCallbacks']):,} original script handlers remain metadata-only"
    )
    print(
        "Assets: "
        f"{len(mesh_entries)} meshes ({len(exported_meshes)} exported), "
        f"{len(material_entries)} materials, {len(texture_entries)} textures, {len(sprite_entries)} sprites"
    )
    mesh_bind_pose_count = sum(int(item.get("bindPoseCount", 0) or 0) for item in mesh_entries)
    skin_vertex_count = sum(int(item.get("vertexCount", 0) or 0) for item in skin_data_by_id.values())
    skin_correction_count = sum(int(item.get("correctedFourthWeightCount", 0) or 0) for item in skin_data_by_id.values())
    weighted_bind_pose_count = sum(int(item.get("bindPoseCount", 0) or 0) for item in skin_data_by_id.values())
    print(
        f"Skinned mesh reconstruction data: {sum(int(item.get('bindPoseCount', 0) or 0) > 0 for item in mesh_entries)} bind-pose meshes, "
        f"{len(skin_data_by_id)} with complete weights/geometry ({skin_vertex_count:,} vertices, "
        f"{weighted_bind_pose_count:,} weighted bind poses, {skin_geometry_triangle_count:,} triangles, "
        f"{skin_correction_count:,} corrected fourth weights); {mesh_bind_pose_count:,} bind poses total including unweighted meshes"
    )
    print(
        f"Scene SkinnedMeshRenderer links: {totals['skinnedRenderers']:,} components, "
        f"{totals['skinnedSkinReadyRenderers']:,} have a matched weighted mesh/bone rig, "
        f"{totals['skinnedStaticFallbacks']:,} need static fallback, "
        f"{totals['skinnedBoneReferences']:,} non-null bone references resolve against scene GameObjects"
    )
    exported_font_bytes = sum(int(font.get("sizeBytes", 0) or 0) for font in font_entries if font.get("exported"))
    print(
        f"Fonts: {len(font_entries)} indexed, {sum(bool(font.get('exported')) for font in font_entries)} embedded TTF/OTF files "
        f"({exported_font_bytes / 1024:.1f} KiB; {totals['textFontReferences']:,} Text references across "
        f"{len(text_font_ids)} Font assets)"
    )
    exported_audio_bytes = sum(int(clip.get("sizeBytes", 0) or 0) for clip in audio_entries if clip.get("exported"))
    audio_format_counts = Counter(
        clip.get("format") or PurePosixPath(str(clip.get("assetPath", ""))).suffix.removeprefix(".").lower()
        for clip in audio_entries if clip.get("exported")
    )
    audio_format_summary = ", ".join(f"{audio_format}={count}" for audio_format, count in sorted(audio_format_counts.items())) or "none"
    print(
        f"Audio: {len(audio_entries)} indexed, {len(exported_audio_ids)} files included "
        f"({audio_format_summary}; {exported_audio_bytes / (1024 * 1024):.2f} MiB; "
        f"{totals['audioAssetsReferenced']:,}/{totals['audioSourceReferences']:,} referenced scene AudioSource clips are included)"
    )
    animation_streamed = sum(int((item.get("curveCounts") or {}).get("streamed", 0) or 0) for item in animation_entries)
    animation_dense_curves = sum(int((item.get("curveCounts") or {}).get("dense", 0) or 0) for item in animation_entries)
    animation_dense_frames = sum(int((item.get("sampleCounts") or {}).get("denseFrames", 0) or 0) for item in animation_entries)
    animation_constant_values = sum(int((item.get("sampleCounts") or {}).get("constantValues", 0) or 0) for item in animation_entries)
    controller_states = sum(int(item.get("stateCount", 0) or 0) for item in controller_entries)
    controller_transitions = sum(int(item.get("transitionCount", 0) or 0) for item in controller_entries)
    controller_blend_trees = sum(int(item.get("blendTreeCount", 0) or 0) for item in controller_entries)
    avatar_skeleton_nodes = sum(int(item.get("skeletonNodeCount", 0) or 0) for item in avatar_entries)
    avatar_human_mappings = sum(int(item.get("humanMappingCount", 0) or 0) for item in avatar_entries)
    avatar_transform_names = sum(int(item.get("transformNameCount", 0) or 0) for item in avatar_entries)
    print(
        f"Animations: {len(animation_entries)} clips; {animation_streamed:,} streamed curves, "
        f"{animation_dense_curves:,} dense curves/{animation_dense_frames:,} frames, "
        f"{animation_constant_values:,} constant values; decoded muscle-clip data verified against archive"
    )
    print(
        f"Animator rig metadata: {len(controller_entries)} controllers ({controller_states:,} states, "
        f"{controller_transitions:,} transition records, {controller_blend_trees:,} blend trees); "
        f"{len(avatar_entries)} Avatars ({avatar_skeleton_nodes:,} skeleton nodes, "
        f"{avatar_human_mappings:,} human mappings, {avatar_transform_names:,} transform-name entries)"
    )
    if il2cpp_summary is not None:
        unresolved_summary = ", ".join(
            f"{count} {reason}" for reason, count in sorted(il2cpp_summary["unresolvedByReason"].items())
        ) or "none"
        print(
            f"IL2CPP metadata: {il2cpp_summary['scriptTypes']} referenced script types, "
            f"{il2cpp_summary['fields']:,} fields, {il2cpp_summary['methods']:,} method signatures; "
            f"persistent MonoBehaviour callback names match {il2cpp_summary['matchedCallbacks']:,}/"
            f"{il2cpp_summary['totalCallbacks']:,} ({il2cpp_summary['unresolvedCallbacks']:,} unresolved: {unresolved_summary})"
        )
        print("NOTE: IL2CPP metadata preserves signatures/addresses only; it does not contain recovered C# method bodies.")
    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)
    for message in errors:
        print(f"ERROR: {message}", file=sys.stderr)
    if errors:
        print(f"FAILED: {len(errors)} validation error(s), {len(warnings)} warning(s)")
        return 1
    print(f"PASS: manifest references and exported files are consistent ({len(warnings)} warning(s))")
    print("NOTE: this does not compile or run the Unity Editor Builder.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
