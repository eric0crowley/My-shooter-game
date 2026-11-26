#if UNITY_EDITOR
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using UnityEditor;
using UnityEditor.SceneManagement;
using UnityEngine;
using UnityEngine.SceneManagement;

namespace RageOfFight.Reconstruction.EditorTools
{
    /// <summary>
    /// Verifies that generated native skin meshes still match the compressed source
    /// payload and that saved scenes have usable SkinnedMeshRenderer bone links.
    /// Run after Prepare assets and rebuild scenes.
    /// </summary>
    public static partial class RageOfFightProjectBuilder
    {
        private const float SkinValidationTolerance = 0.00001f;

        [MenuItem("Tools/Rage of Fight/Validate rebuilt skinning", false, 13)]
        public static void ValidateRebuiltSkinning()
        {
            var errors = new List<string>();
            var scenesOpenedByValidator = new List<Scene>();
            var previouslyActiveScene = SceneManager.GetActiveScene();
            var sourceSkinnedRendererCount = 0;
            var expectedSkinnedRendererCount = 0;
            var actualSkinnedRendererCount = 0;
            var validatedSkinMeshCount = 0;

            try
            {
                var skinDataById = IndexMeshSkinData(ReadCompressedMeshSkinManifest());
                var sceneManifest = ReadCompressedSceneManifest();
                var skinDataByAssetPath = new Dictionary<string, MeshSkinData>(StringComparer.Ordinal);

                foreach (var skinData in skinDataById.Values)
                {
                    var assetPath = GeneratedMeshPath + "/" + skinData.meshId + ".asset";
                    var mesh = AssetDatabase.LoadAssetAtPath<Mesh>(assetPath);
                    if (mesh == null)
                    {
                        AddSkinValidationError(errors, "Generated skinned Mesh asset is missing: " + assetPath);
                        continue;
                    }

                    skinDataByAssetPath[assetPath] = skinData;
                    ValidateSkinMeshAsset(skinData, mesh, errors);
                    validatedSkinMeshCount++;
                }

                if (sceneManifest.scenes == null || sceneManifest.scenes.Length == 0)
                {
                    AddSkinValidationError(errors, "The scene manifest contains no scenes.");
                }
                else
                {
                    for (var sceneIndex = 0; sceneIndex < sceneManifest.scenes.Length; sceneIndex++)
                    {
                        var sceneData = sceneManifest.scenes[sceneIndex];
                        if (sceneData == null || string.IsNullOrEmpty(sceneData.name))
                        {
                            AddSkinValidationError(errors, "The scene manifest contains an unnamed scene at index " + sceneIndex + ".");
                            continue;
                        }

                        var scenePath = SceneOutputPath + "/" + sceneData.name + ".unity";
                        var sceneObjectIds = GetSceneObjectIds(sceneData);
                        CountExpectedSkinnedRenderers(
                            sceneData,
                            sceneObjectIds,
                            skinDataById,
                            out var sourceCount,
                            out var expectedCount);
                        sourceSkinnedRendererCount += sourceCount;
                        expectedSkinnedRendererCount += expectedCount;

                        if (!File.Exists(ToAbsoluteAssetPath(scenePath)))
                        {
                            AddSkinValidationError(errors, "Rebuilt scene is missing: " + scenePath);
                            continue;
                        }

                        EditorUtility.DisplayProgressBar(
                            "Rage of Fight skinning validation",
                            "Checking " + sceneData.name + "…",
                            (sceneIndex + 1.0f) / sceneManifest.scenes.Length);

                        var scene = SceneManager.GetSceneByPath(scenePath);
                        if (!scene.IsValid() || !scene.isLoaded)
                        {
                            scene = EditorSceneManager.OpenScene(scenePath, OpenSceneMode.Additive);
                            if (scene.IsValid() && scene.isLoaded)
                                scenesOpenedByValidator.Add(scene);
                        }
                        if (!scene.IsValid() || !scene.isLoaded)
                        {
                            AddSkinValidationError(errors, "Unity could not load rebuilt scene: " + scenePath);
                            continue;
                        }

                        var sceneRendererCount = 0;
                        foreach (var root in scene.GetRootGameObjects())
                        {
                            foreach (var renderer in root.GetComponentsInChildren<SkinnedMeshRenderer>(true))
                            {
                                sceneRendererCount++;
                                ValidateSceneSkinnedRenderer(renderer, scene, skinDataByAssetPath, errors);
                            }
                        }
                        actualSkinnedRendererCount += sceneRendererCount;
                        if (sceneRendererCount != expectedCount)
                        {
                            AddSkinValidationError(
                                errors,
                                sceneData.name + ": expected " + expectedCount + " weighted SkinnedMeshRenderer(s), found "
                                + sceneRendererCount + ". Source SkinnedMeshRenderer records: " + sourceCount + ".");
                        }
                    }
                }
            }
            catch (Exception exception)
            {
                AddSkinValidationError(errors, "Skinning validation could not finish: " + exception.Message);
                Debug.LogException(exception);
            }
            finally
            {
                for (var i = scenesOpenedByValidator.Count - 1; i >= 0; i--)
                {
                    var scene = scenesOpenedByValidator[i];
                    if (scene.IsValid() && scene.isLoaded)
                        EditorSceneManager.CloseScene(scene, true);
                }
                if (previouslyActiveScene.IsValid() && previouslyActiveScene.isLoaded)
                    SceneManager.SetActiveScene(previouslyActiveScene);
                EditorUtility.ClearProgressBar();
            }

            var expectedFallbackCount = Math.Max(0, sourceSkinnedRendererCount - expectedSkinnedRendererCount);
            if (errors.Count == 0)
            {
                var report = "Skinning validation PASS: " + validatedSkinMeshCount + " native Mesh asset(s) match the version 2 source payload; "
                    + actualSkinnedRendererCount + " weighted SkinnedMeshRenderer instance(s) have valid mesh/bone links across "
                    + expectedSkinnedRendererCount + " expected instances. " + expectedFallbackCount
                    + " source renderer(s) are expected to use the documented static fallback.";
                Debug.Log("Rage of Fight: " + report);
                if (!Application.isBatchMode)
                    EditorUtility.DisplayDialog("Rage of Fight skinning validation", report, "OK");
            }
            else
            {
                var report = "Skinning validation FAILED with " + errors.Count + " issue(s).\n"
                    + string.Join("\n", errors.Take(12))
                    + (errors.Count > 12 ? "\n… and " + (errors.Count - 12) + " more. See the Console for details." : "");
                Debug.LogError("Rage of Fight: " + report);
                if (!Application.isBatchMode)
                    EditorUtility.DisplayDialog("Rage of Fight skinning validation failed", report, "OK");
            }
        }

        private static HashSet<int> GetSceneObjectIds(SceneData sceneData)
        {
            var result = new HashSet<int>();
            if (sceneData == null || sceneData.objects == null)
                return result;
            foreach (var sceneObject in sceneData.objects)
            {
                if (sceneObject != null)
                    result.Add(sceneObject.id);
            }
            return result;
        }

        private static void CountExpectedSkinnedRenderers(
            SceneData sceneData,
            HashSet<int> sceneObjectIds,
            Dictionary<string, MeshSkinData> skinDataById,
            out int sourceRendererCount,
            out int expectedRendererCount)
        {
            sourceRendererCount = 0;
            expectedRendererCount = 0;
            if (sceneData == null || sceneData.objects == null)
                return;

            foreach (var sceneObject in sceneData.objects)
            {
                if (sceneObject == null)
                    continue;
                var rendererData = FindRendererSettings(sceneObject.renderers, "SkinnedMeshRenderer");
                if (rendererData == null)
                    continue;
                sourceRendererCount++;
                if (CanRestoreSkinnedRendererFromManifest(rendererData, sceneObjectIds, skinDataById))
                    expectedRendererCount++;
            }
        }

        private static bool CanRestoreSkinnedRendererFromManifest(
            RendererData rendererData,
            HashSet<int> sceneObjectIds,
            Dictionary<string, MeshSkinData> skinDataById)
        {
            if (rendererData == null || string.IsNullOrEmpty(rendererData.meshId)
                || sceneObjectIds == null || skinDataById == null
                || !skinDataById.TryGetValue(rendererData.meshId, out var skinData)
                || skinData == null || skinData.geometry == null
                || skinData.vertexCount <= 0 || skinData.geometry.vertexCount != skinData.vertexCount
                || skinData.geometry.vertices == null || skinData.geometry.vertices.Length != skinData.vertexCount * 3
                || skinData.geometry.submeshes == null || skinData.geometry.submeshes.Length == 0
                || skinData.bindPoseCount <= 0 || skinData.bindPoses == null
                || skinData.bindPoses.Length != skinData.bindPoseCount
                || rendererData.boneCount != skinData.bindPoseCount
                || rendererData.boneObjects == null || rendererData.boneFileIds == null || rendererData.bonePathIds == null
                || rendererData.boneObjects.Length != skinData.bindPoseCount
                || rendererData.boneFileIds.Length != skinData.bindPoseCount
                || rendererData.bonePathIds.Length != skinData.bindPoseCount
                || skinData.boneIndices == null || skinData.boneWeights == null
                || skinData.boneIndices.Length != skinData.vertexCount * 4
                || skinData.boneWeights.Length != skinData.vertexCount * 4)
                return false;

            for (var i = 0; i < rendererData.bonePathIds.Length; i++)
            {
                if (rendererData.bonePathIds[i] == 0)
                {
                    if (rendererData.boneFileIds[i] != 0 || rendererData.boneObjects[i] != 0)
                        return false;
                }
                else if (rendererData.boneFileIds[i] != 0 || rendererData.boneObjects[i] == 0
                    || !sceneObjectIds.Contains(rendererData.boneObjects[i]))
                {
                    return false;
                }
            }

            if (rendererData.rootBonePathId != 0
                && (rendererData.rootBoneFileId != 0 || rendererData.rootBoneObject == 0
                    || !sceneObjectIds.Contains(rendererData.rootBoneObject)))
                return false;

            for (var vertex = 0; vertex < skinData.vertexCount; vertex++)
            {
                var offset = vertex * 4;
                var total = 0.0f;
                for (var influence = 0; influence < 4; influence++)
                {
                    var weight = skinData.boneWeights[offset + influence];
                    var boneIndex = skinData.boneIndices[offset + influence];
                    if (!IsFinite(weight) || weight < -0.0000001f || weight > 1.000001f)
                        return false;
                    total += Mathf.Max(0.0f, weight);
                    if (weight > 0.00000001f
                        && (boneIndex < 0 || boneIndex >= rendererData.bonePathIds.Length
                            || rendererData.bonePathIds[boneIndex] == 0))
                        return false;
                }
                if (Mathf.Abs(total - 1.0f) > 0.0001f)
                    return false;
            }
            return true;
        }

        private static void ValidateSkinMeshAsset(MeshSkinData skinData, Mesh mesh, List<string> errors)
        {
            var meshId = skinData == null ? "<missing record>" : skinData.meshId;
            if (skinData == null || mesh == null || skinData.geometry == null)
            {
                AddSkinValidationError(errors, "Skin Mesh " + meshId + " has a null source record, geometry, or generated asset.");
                return;
            }

            var geometry = skinData.geometry;
            if (skinData.vertexCount <= 0 || mesh.vertexCount != skinData.vertexCount
                || geometry.vertexCount != skinData.vertexCount)
                AddSkinValidationError(errors, meshId + ": native Mesh vertex count does not match the source skin record.");
            if (mesh.vertexCount > 65535 && mesh.indexFormat != UnityEngine.Rendering.IndexFormat.UInt32)
                AddSkinValidationError(errors, meshId + ": native Mesh requires 32-bit indices but is not using UInt32 format.");

            CompareVector3Channel(meshId, "vertices", geometry.vertices, mesh.vertices, skinData.vertexCount, true, errors);
            CompareVector3Channel(meshId, "normals", geometry.normals, mesh.normals, skinData.vertexCount, false, errors);
            CompareVector4Channel(meshId, "tangents", geometry.tangents, mesh.tangents, skinData.vertexCount, errors);
            CompareColorChannel(meshId, geometry.colors, mesh.colors, skinData.vertexCount, errors);
            CompareUvChannels(meshId, geometry.uvChannels, mesh, skinData.vertexCount, errors);
            CompareSubmeshes(meshId, geometry.submeshes, mesh, errors);
            CompareBindPoses(meshId, skinData, mesh, errors);
            CompareBoneWeights(meshId, skinData, mesh, errors);

            var bounds = mesh.bounds;
            if (!IsFinite(bounds.center.x) || !IsFinite(bounds.center.y) || !IsFinite(bounds.center.z)
                || !IsFinite(bounds.extents.x) || !IsFinite(bounds.extents.y) || !IsFinite(bounds.extents.z))
                AddSkinValidationError(errors, meshId + ": native Mesh bounds contain a non-finite value.");
        }

        private static void CompareVector3Channel(
            string meshId,
            string channelName,
            float[] expected,
            Vector3[] actual,
            int vertexCount,
            bool required,
            List<string> errors)
        {
            if (expected == null || expected.Length == 0)
            {
                if (required)
                    AddSkinValidationError(errors, meshId + ": source geometry is missing required " + channelName + ".");
                return;
            }
            if (expected.Length != vertexCount * 3 || actual == null || actual.Length != vertexCount)
            {
                AddSkinValidationError(errors, meshId + ": native " + channelName + " channel length does not match the source.");
                return;
            }
            for (var i = 0; i < vertexCount; i++)
            {
                var offset = i * 3;
                if (!NearlyEqual(actual[i].x, expected[offset])
                    || !NearlyEqual(actual[i].y, expected[offset + 1])
                    || !NearlyEqual(actual[i].z, expected[offset + 2]))
                {
                    AddSkinValidationError(errors, meshId + ": native " + channelName + " differs from source vertex " + i + ".");
                    return;
                }
            }
        }

        private static void CompareVector4Channel(
            string meshId,
            string channelName,
            float[] expected,
            Vector4[] actual,
            int vertexCount,
            List<string> errors)
        {
            if (expected == null || expected.Length == 0)
                return;
            if (expected.Length != vertexCount * 4 || actual == null || actual.Length != vertexCount)
            {
                AddSkinValidationError(errors, meshId + ": native " + channelName + " channel length does not match the source.");
                return;
            }
            for (var i = 0; i < vertexCount; i++)
            {
                var offset = i * 4;
                if (!NearlyEqual(actual[i].x, expected[offset])
                    || !NearlyEqual(actual[i].y, expected[offset + 1])
                    || !NearlyEqual(actual[i].z, expected[offset + 2])
                    || !NearlyEqual(actual[i].w, expected[offset + 3]))
                {
                    AddSkinValidationError(errors, meshId + ": native " + channelName + " differs from source vertex " + i + ".");
                    return;
                }
            }
        }

        private static void CompareColorChannel(
            string meshId,
            float[] expected,
            Color[] actual,
            int vertexCount,
            List<string> errors)
        {
            if (expected == null || expected.Length == 0)
                return;
            if (expected.Length != vertexCount * 4 || actual == null || actual.Length != vertexCount)
            {
                AddSkinValidationError(errors, meshId + ": native color channel length does not match the source.");
                return;
            }
            for (var i = 0; i < vertexCount; i++)
            {
                var offset = i * 4;
                if (!NearlyEqual(actual[i].r, expected[offset])
                    || !NearlyEqual(actual[i].g, expected[offset + 1])
                    || !NearlyEqual(actual[i].b, expected[offset + 2])
                    || !NearlyEqual(actual[i].a, expected[offset + 3]))
                {
                    AddSkinValidationError(errors, meshId + ": native colors differ from source vertex " + i + ".");
                    return;
                }
            }
        }

        private static void CompareUvChannels(
            string meshId,
            MeshUvChannelData[] channels,
            Mesh mesh,
            int vertexCount,
            List<string> errors)
        {
            if (channels == null)
                return;
            foreach (var channel in channels)
            {
                if (channel == null || channel.channel < 0 || channel.channel > 7
                    || channel.dimension < 1 || channel.dimension > 4
                    || channel.values == null || channel.values.Length != vertexCount * channel.dimension)
                {
                    AddSkinValidationError(errors, meshId + ": source UV channel has an invalid index, dimension, or length.");
                    continue;
                }

                var matches = true;
                if (channel.dimension <= 2)
                {
                    var actual = new List<Vector2>(vertexCount);
                    mesh.GetUVs(channel.channel, actual);
                    if (actual.Count != vertexCount)
                    {
                        AddSkinValidationError(errors, meshId + ": native UV" + channel.channel + " vertex count differs from source.");
                        continue;
                    }
                    for (var i = 0; i < vertexCount; i++)
                    {
                        var offset = i * channel.dimension;
                        var expectedY = channel.dimension > 1 ? channel.values[offset + 1] : 0.0f;
                        if (!NearlyEqual(actual[i].x, channel.values[offset]) || !NearlyEqual(actual[i].y, expectedY))
                        {
                            matches = false;
                            break;
                        }
                    }
                }
                else if (channel.dimension == 3)
                {
                    var actual = new List<Vector3>(vertexCount);
                    mesh.GetUVs(channel.channel, actual);
                    if (actual.Count != vertexCount)
                    {
                        AddSkinValidationError(errors, meshId + ": native UV" + channel.channel + " vertex count differs from source.");
                        continue;
                    }
                    for (var i = 0; i < vertexCount; i++)
                    {
                        var offset = i * 3;
                        if (!NearlyEqual(actual[i].x, channel.values[offset])
                            || !NearlyEqual(actual[i].y, channel.values[offset + 1])
                            || !NearlyEqual(actual[i].z, channel.values[offset + 2]))
                        {
                            matches = false;
                            break;
                        }
                    }
                }
                else
                {
                    var actual = new List<Vector4>(vertexCount);
                    mesh.GetUVs(channel.channel, actual);
                    if (actual.Count != vertexCount)
                    {
                        AddSkinValidationError(errors, meshId + ": native UV" + channel.channel + " vertex count differs from source.");
                        continue;
                    }
                    for (var i = 0; i < vertexCount; i++)
                    {
                        var offset = i * 4;
                        if (!NearlyEqual(actual[i].x, channel.values[offset])
                            || !NearlyEqual(actual[i].y, channel.values[offset + 1])
                            || !NearlyEqual(actual[i].z, channel.values[offset + 2])
                            || !NearlyEqual(actual[i].w, channel.values[offset + 3]))
                        {
                            matches = false;
                            break;
                        }
                    }
                }
                if (!matches)
                    AddSkinValidationError(errors, meshId + ": native UV" + channel.channel + " differs from source geometry.");
            }
        }

        private static void CompareSubmeshes(
            string meshId,
            MeshSubmeshData[] expected,
            Mesh mesh,
            List<string> errors)
        {
            if (expected == null || mesh.subMeshCount != expected.Length)
            {
                AddSkinValidationError(errors, meshId + ": native submesh count does not match source geometry.");
                return;
            }
            for (var submeshIndex = 0; submeshIndex < expected.Length; submeshIndex++)
            {
                var sourceSubmesh = expected[submeshIndex];
                if (sourceSubmesh == null || sourceSubmesh.topology != "Triangles" || sourceSubmesh.indices == null
                    || mesh.GetTopology(submeshIndex) != MeshTopology.Triangles)
                {
                    AddSkinValidationError(errors, meshId + ": source/native submesh " + submeshIndex + " is not a valid triangle list.");
                    continue;
                }
                var actualIndices = mesh.GetTriangles(submeshIndex);
                if (actualIndices.Length != sourceSubmesh.indices.Length)
                {
                    AddSkinValidationError(errors, meshId + ": triangle index count differs in submesh " + submeshIndex + ".");
                    continue;
                }
                for (var i = 0; i < actualIndices.Length; i++)
                {
                    if (actualIndices[i] != sourceSubmesh.indices[i])
                    {
                        AddSkinValidationError(errors, meshId + ": triangle topology differs in submesh " + submeshIndex + ".");
                        break;
                    }
                }
            }
        }

        private static void CompareBindPoses(string meshId, MeshSkinData skinData, Mesh mesh, List<string> errors)
        {
            if (skinData.bindPoses == null || mesh.bindposes == null
                || skinData.bindPoses.Length != skinData.bindPoseCount
                || mesh.bindposes.Length != skinData.bindPoseCount)
            {
                AddSkinValidationError(errors, meshId + ": native bind-pose count does not match source.");
                return;
            }
            var actualBindPoses = mesh.bindposes;
            for (var poseIndex = 0; poseIndex < skinData.bindPoses.Length; poseIndex++)
            {
                var expected = ToMatrix4x4(skinData.bindPoses[poseIndex]);
                var actual = actualBindPoses[poseIndex];
                var expectedValues = MatrixValues(expected);
                var actualValues = MatrixValues(actual);
                for (var valueIndex = 0; valueIndex < expectedValues.Length; valueIndex++)
                {
                    if (!NearlyEqual(actualValues[valueIndex], expectedValues[valueIndex]))
                    {
                        AddSkinValidationError(errors, meshId + ": bind pose " + poseIndex + " differs from source.");
                        return;
                    }
                }
            }
        }

        private static void CompareBoneWeights(string meshId, MeshSkinData skinData, Mesh mesh, List<string> errors)
        {
            if (skinData.boneIndices == null || skinData.boneWeights == null
                || skinData.boneIndices.Length != skinData.vertexCount * 4
                || skinData.boneWeights.Length != skinData.vertexCount * 4)
            {
                AddSkinValidationError(errors, meshId + ": source bone-weight arrays are malformed.");
                return;
            }
            var actualWeights = mesh.boneWeights;
            if (actualWeights == null || actualWeights.Length != skinData.vertexCount)
            {
                AddSkinValidationError(errors, meshId + ": native BoneWeight count does not match source vertices.");
                return;
            }
            for (var vertex = 0; vertex < skinData.vertexCount; vertex++)
            {
                var offset = vertex * 4;
                var expected0 = ValidBoneIndex(skinData.boneIndices[offset], skinData.bindPoseCount);
                var expected1 = ValidBoneIndex(skinData.boneIndices[offset + 1], skinData.bindPoseCount);
                var expected2 = ValidBoneIndex(skinData.boneIndices[offset + 2], skinData.bindPoseCount);
                var expected3 = ValidBoneIndex(skinData.boneIndices[offset + 3], skinData.bindPoseCount);
                var expectedWeight0 = Mathf.Max(0.0f, skinData.boneWeights[offset]);
                var expectedWeight1 = Mathf.Max(0.0f, skinData.boneWeights[offset + 1]);
                var expectedWeight2 = Mathf.Max(0.0f, skinData.boneWeights[offset + 2]);
                var expectedWeight3 = Mathf.Max(0.0f, skinData.boneWeights[offset + 3]);
                var actual = actualWeights[vertex];
                if (actual.boneIndex0 != expected0 || actual.boneIndex1 != expected1
                    || actual.boneIndex2 != expected2 || actual.boneIndex3 != expected3
                    || !NearlyEqual(actual.weight0, expectedWeight0) || !NearlyEqual(actual.weight1, expectedWeight1)
                    || !NearlyEqual(actual.weight2, expectedWeight2) || !NearlyEqual(actual.weight3, expectedWeight3))
                {
                    AddSkinValidationError(errors, meshId + ": native BoneWeight differs at source vertex " + vertex + ".");
                    return;
                }
            }
        }

        private static void ValidateSceneSkinnedRenderer(
            SkinnedMeshRenderer renderer,
            Scene scene,
            Dictionary<string, MeshSkinData> skinDataByAssetPath,
            List<string> errors)
        {
            if (renderer == null)
                return;
            var mesh = renderer.sharedMesh;
            var label = renderer.name + " in " + scene.name;
            if (mesh == null)
            {
                AddSkinValidationError(errors, label + ": SkinnedMeshRenderer has no shared Mesh.");
                return;
            }

            var assetPath = AssetDatabase.GetAssetPath(mesh);
            if (string.IsNullOrEmpty(assetPath) || !skinDataByAssetPath.TryGetValue(assetPath, out var skinData))
            {
                AddSkinValidationError(errors, label + ": shared Mesh is not one of the generated weighted Mesh assets.");
                return;
            }

            var bones = renderer.bones;
            if (bones == null || bones.Length != skinData.bindPoseCount || mesh.bindposes.Length != skinData.bindPoseCount)
                AddSkinValidationError(errors, label + ": renderer bone count does not match the Mesh bind poses.");
            else
            {
                for (var boneIndex = 0; boneIndex < bones.Length; boneIndex++)
                {
                    if (bones[boneIndex] != null && bones[boneIndex].gameObject.scene.handle != scene.handle)
                    {
                        AddSkinValidationError(errors, label + ": bone " + boneIndex + " belongs to a different scene.");
                        break;
                    }
                }

                if (skinData.boneIndices != null && skinData.boneWeights != null
                    && skinData.boneIndices.Length == skinData.boneWeights.Length)
                {
                    for (var i = 0; i < skinData.boneWeights.Length; i++)
                    {
                        if (skinData.boneWeights[i] <= 0.00000001f)
                            continue;
                        var boneIndex = skinData.boneIndices[i];
                        if (boneIndex < 0 || boneIndex >= bones.Length || bones[boneIndex] == null)
                        {
                            AddSkinValidationError(errors, label + ": active skin influence " + i + " has no scene bone.");
                            break;
                        }
                    }
                }
            }

            if (renderer.rootBone != null && renderer.rootBone.gameObject.scene.handle != scene.handle)
                AddSkinValidationError(errors, label + ": rootBone belongs to a different scene.");

            var bounds = renderer.localBounds;
            if (!IsFinite(bounds.center.x) || !IsFinite(bounds.center.y) || !IsFinite(bounds.center.z)
                || !IsFinite(bounds.extents.x) || !IsFinite(bounds.extents.y) || !IsFinite(bounds.extents.z)
                || bounds.extents.x < 0.0f || bounds.extents.y < 0.0f || bounds.extents.z < 0.0f)
                AddSkinValidationError(errors, label + ": renderer local bounds are invalid.");
        }

        private static int ValidBoneIndex(int index, int bindPoseCount)
        {
            return index >= 0 && index < bindPoseCount ? index : 0;
        }

        private static float[] MatrixValues(Matrix4x4 matrix)
        {
            return new[]
            {
                matrix.m00, matrix.m01, matrix.m02, matrix.m03,
                matrix.m10, matrix.m11, matrix.m12, matrix.m13,
                matrix.m20, matrix.m21, matrix.m22, matrix.m23,
                matrix.m30, matrix.m31, matrix.m32, matrix.m33
            };
        }

        private static bool NearlyEqual(float actual, float expected)
        {
            if (!IsFinite(actual) || !IsFinite(expected))
                return false;
            var scale = Math.Max(1.0f, Math.Max(Math.Abs(actual), Math.Abs(expected)));
            return Math.Abs(actual - expected) <= SkinValidationTolerance * scale;
        }

        private static bool IsFinite(float value)
        {
            return !float.IsNaN(value) && !float.IsInfinity(value);
        }

        private static void AddSkinValidationError(List<string> errors, string message)
        {
            if (errors != null && !string.IsNullOrEmpty(message))
                errors.Add(message);
        }
    }
}
#endif
