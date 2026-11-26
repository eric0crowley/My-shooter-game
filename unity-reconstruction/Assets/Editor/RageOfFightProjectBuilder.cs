#if UNITY_EDITOR
using System;
using System.Collections.Generic;
using System.IO;
using System.IO.Compression;
using System.Linq;
using System.Text;
using UnityEditor;
using UnityEditor.Events;
using UnityEditor.SceneManagement;
using UnityEngine;
using UnityEngine.AI;
using UnityEngine.Events;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

namespace RageOfFight.Reconstruction.EditorTools
{
    /// <summary>
    /// Builds editable Unity scenes from the extracted APK data. This restores
    /// hierarchy, transforms, native vertex-aligned skinned meshes, static mesh
    /// visuals and recoverable UI data. It deliberately does not pretend IL2CPP
    /// game scripts or playable animation controllers were restored.
    /// </summary>
    public static partial class RageOfFightProjectBuilder
    {
        private const string RecoveredRoot = "Assets/Recovered";
        private const string ManifestRoot = RecoveredRoot + "/Manifests";
        private const string MeshArchivePath = RecoveredRoot + "/Compressed/mesh-exports.zip";
        private const string MeshOutputPath = RecoveredRoot + "/Meshes";
        private const string GeneratedMeshPath = RecoveredRoot + "/GeneratedMeshes";
        private const string MaterialOutputPath = RecoveredRoot + "/Materials";
        private const string PrefabOutputPath = RecoveredRoot + "/Prefabs";
        private const string SceneOutputPath = "Assets/Scenes";
        private const string SceneManifestFile = ManifestRoot + "/scene-data.json.gz";
        private const string MeshSkinManifestFile = ManifestRoot + "/mesh-skin-data.json.gz";

        [MenuItem("Tools/Rage of Fight/Prepare assets and rebuild scenes", false, 10)]
        public static void PrepareAndBuild()
        {
            try
            {
                if (!File.Exists(MeshArchivePath))
                {
                    throw new FileNotFoundException("The compressed OBJ archive is missing.", MeshArchivePath);
                }
                if (!File.Exists(SceneManifestFile))
                {
                    throw new FileNotFoundException("The scene manifest is missing.", SceneManifestFile);
                }

                EditorUtility.DisplayProgressBar("Rage of Fight reconstruction", "Expanding compressed OBJ meshes…", 0.02f);
                ExpandMeshArchive();
                AssetDatabase.Refresh(ImportAssetOptions.ForceSynchronousImport);

                EditorUtility.DisplayProgressBar("Rage of Fight reconstruction", "Preparing sprite import settings…", 0.25f);
                ConfigureSpriteImporters();
                AssetDatabase.Refresh(ImportAssetOptions.ForceSynchronousImport);

                EditorUtility.DisplayProgressBar("Rage of Fight reconstruction", "Creating editable materials…", 0.42f);
                var spriteManifest = ReadJson<SpriteManifest>(ManifestRoot + "/sprites.json");
                var textureManifest = ReadJson<TextureManifest>(ManifestRoot + "/textures.json");
                var materialManifest = ReadJson<MaterialManifest>(ManifestRoot + "/materials.json");
                var meshManifest = ReadJson<MeshManifest>(ManifestRoot + "/meshes.json");
                var meshSkinManifest = ReadCompressedMeshSkinManifest();
                var meshSkinData = IndexMeshSkinData(meshSkinManifest);
                var uiPrefabManifest = ReadJson<UiPrefabManifest>(ManifestRoot + "/ui-prefabs.json");
                var fontManifest = ReadJson<FontManifest>(ManifestRoot + "/fonts.json");
                var audioManifest = ReadJson<AudioClipManifest>(ManifestRoot + "/audio-index.json");
                var sprites = LoadSprites(spriteManifest);
                var textures = LoadTextures(textureManifest);
                var materials = CreateMaterials(materialManifest, textures);
                var meshes = LoadMeshes(meshManifest, meshSkinData);
                var fonts = LoadFonts(fontManifest);
                var audioClips = LoadAudioClips(audioManifest);

                EditorUtility.DisplayProgressBar("Rage of Fight reconstruction", "Reading the compressed scene manifest…", 0.55f);
                var scenes = ReadCompressedSceneManifest();
                RebuildScenes(scenes, meshes, meshSkinData, materials, sprites, audioClips, fonts);
                RebuildUiPrefabs(uiPrefabManifest, meshes, meshSkinData, materials, sprites, audioClips, fonts);
                AssetDatabase.SaveAssets();
                AssetDatabase.Refresh();
                Debug.Log("Rage of Fight: reconstructed scenes and asset manifests are ready. Original IL2CPP behaviours and animation controllers are not restored.");
                EditorUtility.DisplayDialog(
                    "Rage of Fight reconstruction",
                    "Scene hierarchy, native weighted skinned meshes and bone links, static mesh visuals, recoverable UI sprites/text and basic materials have been rebuilt.\n\nThe original IL2CPP gameplay scripts, playable animation clips/controllers and custom button event logic are not restored.",
                    "OK");
            }
            catch (Exception exception)
            {
                Debug.LogException(exception);
                EditorUtility.DisplayDialog("Rage of Fight reconstruction failed", exception.Message + "\n\nSee the Console for details.", "OK");
            }
            finally
            {
                EditorUtility.ClearProgressBar();
            }
        }

        [MenuItem("Tools/Rage of Fight/Rebuild scenes only", false, 11)]
        public static void RebuildScenesOnly()
        {
            try
            {
                var spriteManifest = ReadJson<SpriteManifest>(ManifestRoot + "/sprites.json");
                var textureManifest = ReadJson<TextureManifest>(ManifestRoot + "/textures.json");
                var materialManifest = ReadJson<MaterialManifest>(ManifestRoot + "/materials.json");
                var meshManifest = ReadJson<MeshManifest>(ManifestRoot + "/meshes.json");
                var meshSkinData = IndexMeshSkinData(ReadCompressedMeshSkinManifest());
                var uiPrefabManifest = ReadJson<UiPrefabManifest>(ManifestRoot + "/ui-prefabs.json");
                var fontManifest = ReadJson<FontManifest>(ManifestRoot + "/fonts.json");
                var audioManifest = ReadJson<AudioClipManifest>(ManifestRoot + "/audio-index.json");
                var sprites = LoadSprites(spriteManifest);
                var textures = LoadTextures(textureManifest);
                var materials = LoadExistingMaterials(materialManifest);
                if (materials.Count == 0)
                    materials = CreateMaterials(materialManifest, textures);
                var meshes = LoadMeshes(meshManifest, meshSkinData);
                var fonts = LoadFonts(fontManifest);
                var audioClips = LoadAudioClips(audioManifest);
                RebuildScenes(ReadCompressedSceneManifest(), meshes, meshSkinData, materials, sprites, audioClips, fonts);
                RebuildUiPrefabs(uiPrefabManifest, meshes, meshSkinData, materials, sprites, audioClips, fonts);
                AssetDatabase.SaveAssets();
                AssetDatabase.Refresh();
            }
            catch (Exception exception)
            {
                Debug.LogException(exception);
                EditorUtility.DisplayDialog("Rage of Fight reconstruction failed", exception.Message + "\n\nSee the Console for details.", "OK");
            }
            finally
            {
                EditorUtility.ClearProgressBar();
            }
        }

        [MenuItem("Tools/Rage of Fight/Rebuild shared UI prefabs only", false, 12)]
        public static void RebuildUiPrefabsOnly()
        {
            try
            {
                AssetDatabase.Refresh(ImportAssetOptions.ForceSynchronousImport);
                var spriteManifest = ReadJson<SpriteManifest>(ManifestRoot + "/sprites.json");
                var materialManifest = ReadJson<MaterialManifest>(ManifestRoot + "/materials.json");
                var meshManifest = ReadJson<MeshManifest>(ManifestRoot + "/meshes.json");
                var meshSkinData = IndexMeshSkinData(ReadCompressedMeshSkinManifest());
                var prefabManifest = ReadJson<UiPrefabManifest>(ManifestRoot + "/ui-prefabs.json");
                var fontManifest = ReadJson<FontManifest>(ManifestRoot + "/fonts.json");
                var audioManifest = ReadJson<AudioClipManifest>(ManifestRoot + "/audio-index.json");
                var sprites = LoadSprites(spriteManifest);
                var materials = LoadExistingMaterials(materialManifest);
                var meshes = LoadMeshes(meshManifest, meshSkinData);
                var fonts = LoadFonts(fontManifest);
                var audioClips = LoadAudioClips(audioManifest);
                RebuildUiPrefabs(prefabManifest, meshes, meshSkinData, materials, sprites, audioClips, fonts);
                AssetDatabase.SaveAssets();
                AssetDatabase.Refresh();
            }
            catch (Exception exception)
            {
                Debug.LogException(exception);
                EditorUtility.DisplayDialog("Rage of Fight UI prefab rebuild failed", exception.Message + "\n\nSee the Console for details.", "OK");
            }
            finally
            {
                EditorUtility.ClearProgressBar();
            }
        }

        private static void ExpandMeshArchive()
        {
            Directory.CreateDirectory(ToAbsoluteAssetPath(MeshOutputPath));
            Directory.CreateDirectory(ToAbsoluteAssetPath(GeneratedMeshPath));
            using (var archive = ZipFile.OpenRead(ToAbsoluteAssetPath(MeshArchivePath)))
            {
                var entries = archive.Entries;
                for (var i = 0; i < entries.Count; i++)
                {
                    var entry = entries[i];
                    var fileName = Path.GetFileName(entry.FullName);
                    if (string.IsNullOrEmpty(fileName) || !fileName.EndsWith(".obj", StringComparison.OrdinalIgnoreCase))
                        continue;
                    var target = Path.Combine(ToAbsoluteAssetPath(MeshOutputPath), fileName);
                    Directory.CreateDirectory(Path.GetDirectoryName(target));
                    using (var input = entry.Open())
                    using (var output = new FileStream(target, FileMode.Create, FileAccess.Write, FileShare.None))
                        input.CopyTo(output);
                }
            }
        }

        private static void ConfigureSpriteImporters()
        {
            var manifest = ReadJson<SpriteManifest>(ManifestRoot + "/sprites.json");
            if (manifest == null || manifest.sprites == null)
                return;

            for (var i = 0; i < manifest.sprites.Length; i++)
            {
                var entry = manifest.sprites[i];
                if (entry == null || string.IsNullOrEmpty(entry.assetPath))
                    continue;
                var importer = AssetImporter.GetAtPath(entry.assetPath) as TextureImporter;
                if (importer == null)
                    continue;
                var pivot = entry.pivot != null && entry.pivot.Length >= 2
                    ? new Vector2(entry.pivot[0], entry.pivot[1])
                    : new Vector2(0.5f, 0.5f);
                var ppu = entry.pixelsPerUnit > 0 ? entry.pixelsPerUnit : 100.0f;
                var changed = importer.textureType != TextureImporterType.Sprite
                              || importer.spriteImportMode != SpriteImportMode.Single
                              || (importer.spritePivot - pivot).sqrMagnitude > 0.0001f
                              || Mathf.Abs(importer.spritePixelsPerUnit - ppu) > 0.01f;
                if (!changed)
                    continue;
                importer.textureType = TextureImporterType.Sprite;
                importer.spriteImportMode = SpriteImportMode.Single;
                importer.spritePivot = pivot;
                importer.spritePixelsPerUnit = ppu;
                importer.alphaIsTransparency = true;
                importer.SaveAndReimport();
            }
        }

        private static Dictionary<string, Sprite> LoadSprites(SpriteManifest manifest)
        {
            var result = new Dictionary<string, Sprite>(StringComparer.Ordinal);
            if (manifest == null || manifest.sprites == null)
                return result;
            foreach (var entry in manifest.sprites)
            {
                if (entry == null || string.IsNullOrEmpty(entry.id))
                    continue;
                var sprite = AssetDatabase.LoadAssetAtPath<Sprite>(entry.assetPath);
                if (sprite != null)
                    result[entry.id] = sprite;
                else
                    Debug.LogWarning("Sprite import did not produce a Sprite subasset: " + entry.assetPath);
            }
            return result;
        }

        private static Dictionary<string, Font> LoadFonts(FontManifest manifest)
        {
            var result = new Dictionary<string, Font>(StringComparer.Ordinal);
            if (manifest == null || manifest.fonts == null)
                return result;
            foreach (var entry in manifest.fonts)
            {
                if (entry == null || !entry.exported || string.IsNullOrEmpty(entry.id) || string.IsNullOrEmpty(entry.assetPath))
                    continue;
                var font = AssetDatabase.LoadAssetAtPath<Font>(entry.assetPath);
                if (font != null)
                    result[entry.id] = font;
                else
                    Debug.LogWarning("Font import did not produce a Font asset: " + entry.assetPath);
            }
            return result;
        }

        private static Dictionary<string, Texture2D> LoadTextures(TextureManifest manifest)
        {
            var result = new Dictionary<string, Texture2D>(StringComparer.Ordinal);
            if (manifest == null || manifest.textures == null)
                return result;
            foreach (var entry in manifest.textures)
            {
                if (entry == null || string.IsNullOrEmpty(entry.id))
                    continue;
                var texture = AssetDatabase.LoadAssetAtPath<Texture2D>(entry.assetPath);
                if (texture != null)
                    result[entry.id] = texture;
            }
            return result;
        }

        private static Dictionary<string, AudioClip> LoadAudioClips(AudioClipManifest manifest)
        {
            var result = new Dictionary<string, AudioClip>(StringComparer.Ordinal);
            if (manifest == null || manifest.audioClips == null)
                return result;
            foreach (var entry in manifest.audioClips)
            {
                if (entry == null || !entry.exported || string.IsNullOrEmpty(entry.id) || string.IsNullOrEmpty(entry.assetPath))
                    continue;
                var clip = AssetDatabase.LoadAssetAtPath<AudioClip>(entry.assetPath);
                if (clip != null)
                    result[entry.id] = clip;
                else
                    Debug.LogWarning("Audio import did not produce an AudioClip: " + entry.assetPath);
            }
            return result;
        }

        private static Dictionary<string, Mesh> LoadMeshes(
            MeshManifest manifest,
            Dictionary<string, MeshSkinData> skinDataByMeshId)
        {
            var result = new Dictionary<string, Mesh>(StringComparer.Ordinal);
            if (manifest == null || manifest.meshes == null)
                return result;
            Directory.CreateDirectory(ToAbsoluteAssetPath(GeneratedMeshPath));
            var sourceAlignedSkinnedMeshes = 0;
            foreach (var entry in manifest.meshes)
            {
                if (entry == null || !entry.exported || string.IsNullOrEmpty(entry.id) || string.IsNullOrEmpty(entry.assetPath))
                    continue;

                if (skinDataByMeshId != null && skinDataByMeshId.TryGetValue(entry.id, out var skinData))
                {
                    try
                    {
                        result[entry.id] = CreateOrUpdateSkinnedMeshAsset(entry.id, skinData);
                        sourceAlignedSkinnedMeshes++;
                        continue;
                    }
                    catch (Exception exception)
                    {
                        Debug.LogWarning(
                            "Could not build vertex-aligned skinned mesh " + entry.id + "; using its OBJ visual as a static fallback. "
                            + exception.Message);
                    }
                }

                var existingGenerated = AssetDatabase.LoadAssetAtPath<Mesh>(GeneratedMeshPath + "/" + entry.id + ".asset");
                if (existingGenerated != null)
                {
                    result[entry.id] = existingGenerated;
                    continue;
                }
                var imported = AssetDatabase.LoadAllAssetsAtPath(entry.assetPath).OfType<Mesh>()
                    .Where(mesh => mesh != null && mesh.vertexCount > 0)
                    .ToArray();
                if (imported.Length == 0)
                {
                    Debug.LogWarning("No Mesh subassets imported from " + entry.assetPath);
                    continue;
                }
                if (imported.Length == 1)
                {
                    result[entry.id] = imported[0];
                    continue;
                }

                var combined = CombineImportedMeshes(imported, entry.id);
                var generatedPath = GeneratedMeshPath + "/" + entry.id + ".asset";
                var generatedAsset = AssetDatabase.LoadAssetAtPath<Mesh>(generatedPath);
                if (generatedAsset == null)
                {
                    AssetDatabase.CreateAsset(combined, generatedPath);
                    generatedAsset = combined;
                }
                result[entry.id] = generatedAsset;
            }
            AssetDatabase.SaveAssets();
            Debug.Log("Rage of Fight: built " + sourceAlignedSkinnedMeshes + " vertex-aligned skinned Mesh assets from decoded geometry and skin records.");
            return result;
        }

        private static Mesh CreateOrUpdateSkinnedMeshAsset(string meshId, MeshSkinData data)
        {
            var generatedPath = GeneratedMeshPath + "/" + meshId + ".asset";
            var temporary = new Mesh { name = "Recovered_Skinned_" + meshId };
            try
            {
                PopulateSkinnedMesh(temporary, data);
                var existing = AssetDatabase.LoadAssetAtPath<Mesh>(generatedPath);
                if (existing == null)
                {
                    AssetDatabase.CreateAsset(temporary, generatedPath);
                    return temporary;
                }

                EditorUtility.CopySerialized(temporary, existing);
                existing.name = temporary.name;
                EditorUtility.SetDirty(existing);
                UnityEngine.Object.DestroyImmediate(temporary);
                return existing;
            }
            catch
            {
                if (temporary != null)
                    UnityEngine.Object.DestroyImmediate(temporary);
                throw;
            }
        }

        private static void PopulateSkinnedMesh(Mesh mesh, MeshSkinData data)
        {
            if (mesh == null || data == null || data.geometry == null)
                throw new InvalidDataException("Skin record has no mesh geometry.");
            var geometry = data.geometry;
            var vertexCount = data.vertexCount;
            if (vertexCount <= 0 || geometry.vertexCount != vertexCount)
                throw new InvalidDataException("Skin geometry and weight vertex counts do not match.");

            var vertices = ReadVector3Channel(geometry.vertices, vertexCount, "vertices", true);
            var normals = ReadVector3Channel(geometry.normals, vertexCount, "normals", false);
            var tangents = ReadVector4Channel(geometry.tangents, vertexCount, "tangents", false);
            var colors = ReadColorChannel(geometry.colors, vertexCount);
            if (data.bindPoses == null || data.bindPoses.Length != data.bindPoseCount || data.bindPoseCount <= 0)
                throw new InvalidDataException("Skin record has an invalid bind-pose array.");
            if (data.boneIndices == null || data.boneWeights == null
                || data.boneIndices.Length != vertexCount * 4 || data.boneWeights.Length != vertexCount * 4)
                throw new InvalidDataException("Skin record must contain four flat bone influences per vertex.");
            if (geometry.submeshes == null || geometry.submeshes.Length == 0)
                throw new InvalidDataException("Skin geometry has no submeshes.");

            mesh.Clear();
            mesh.name = "Recovered_Skinned_" + data.meshId;
            mesh.indexFormat = vertexCount > 65535
                ? UnityEngine.Rendering.IndexFormat.UInt32
                : UnityEngine.Rendering.IndexFormat.UInt16;
            mesh.vertices = vertices;
            if (normals != null)
                mesh.normals = normals;
            if (tangents != null)
                mesh.tangents = tangents;
            if (colors != null)
                mesh.colors = colors;

            if (geometry.uvChannels != null)
            {
                var seenChannels = new HashSet<int>();
                foreach (var channel in geometry.uvChannels)
                {
                    if (channel == null || channel.channel < 0 || channel.channel > 7 || !seenChannels.Add(channel.channel))
                        throw new InvalidDataException("Skin geometry contains an invalid or duplicate UV channel.");
                    ApplyUvChannel(mesh, channel, vertexCount);
                }
            }

            mesh.subMeshCount = geometry.submeshes.Length;
            for (var submeshIndex = 0; submeshIndex < geometry.submeshes.Length; submeshIndex++)
            {
                var submesh = geometry.submeshes[submeshIndex];
                if (submesh == null || submesh.topology != "Triangles" || submesh.indices == null || submesh.indices.Length % 3 != 0)
                    throw new InvalidDataException("Skin geometry has a malformed triangle submesh " + submeshIndex + ".");
                for (var i = 0; i < submesh.indices.Length; i++)
                {
                    if (submesh.indices[i] < 0 || submesh.indices[i] >= vertexCount)
                        throw new InvalidDataException("Skin geometry contains an out-of-range triangle vertex.");
                }
                mesh.SetTriangles(submesh.indices, submeshIndex, false);
            }
            if (normals == null)
                mesh.RecalculateNormals();

            var bindPoses = new Matrix4x4[data.bindPoses.Length];
            for (var i = 0; i < bindPoses.Length; i++)
                bindPoses[i] = ToMatrix4x4(data.bindPoses[i]);
            mesh.bindposes = bindPoses;

            var boneWeights = new BoneWeight[vertexCount];
            var weightValues = new float[4];
            var boneIndices = new int[4];
            for (var vertexIndex = 0; vertexIndex < vertexCount; vertexIndex++)
            {
                var offset = vertexIndex * 4;
                var total = 0.0f;
                for (var influence = 0; influence < 4; influence++)
                {
                    var index = data.boneIndices[offset + influence];
                    var weight = data.boneWeights[offset + influence];
                    if (float.IsNaN(weight) || float.IsInfinity(weight) || weight < -0.0000001f || weight > 1.000001f)
                        throw new InvalidDataException("Skin record contains an invalid bone weight.");
                    if (weight > 0.00000001f && (index < 0 || index >= bindPoses.Length))
                        throw new InvalidDataException("Skin weight references a missing bind pose.");
                    boneIndices[influence] = index >= 0 && index < bindPoses.Length ? index : 0;
                    weightValues[influence] = Mathf.Max(0.0f, weight);
                    total += weightValues[influence];
                }
                if (Mathf.Abs(total - 1.0f) > 0.0001f)
                    throw new InvalidDataException("Skin weights do not sum to one at vertex " + vertexIndex + ".");
                boneWeights[vertexIndex] = new BoneWeight
                {
                    boneIndex0 = boneIndices[0],
                    boneIndex1 = boneIndices[1],
                    boneIndex2 = boneIndices[2],
                    boneIndex3 = boneIndices[3],
                    weight0 = weightValues[0],
                    weight1 = weightValues[1],
                    weight2 = weightValues[2],
                    weight3 = weightValues[3]
                };
            }
            mesh.boneWeights = boneWeights;
            mesh.RecalculateBounds();
        }

        private static Vector3[] ReadVector3Channel(float[] values, int vertexCount, string fieldName, bool required)
        {
            if (values == null || values.Length == 0)
            {
                if (required)
                    throw new InvalidDataException("Skin geometry is missing " + fieldName + ".");
                return null;
            }
            if (values.Length != vertexCount * 3)
                throw new InvalidDataException("Skin geometry " + fieldName + " has the wrong channel length.");
            var result = new Vector3[vertexCount];
            for (var i = 0; i < vertexCount; i++)
            {
                var x = values[i * 3];
                var y = values[i * 3 + 1];
                var z = values[i * 3 + 2];
                if (float.IsNaN(x) || float.IsInfinity(x) || float.IsNaN(y) || float.IsInfinity(y) || float.IsNaN(z) || float.IsInfinity(z))
                    throw new InvalidDataException("Skin geometry " + fieldName + " contains a non-finite value.");
                result[i] = new Vector3(x, y, z);
            }
            return result;
        }

        private static Vector4[] ReadVector4Channel(float[] values, int vertexCount, string fieldName, bool required)
        {
            if (values == null || values.Length == 0)
            {
                if (required)
                    throw new InvalidDataException("Skin geometry is missing " + fieldName + ".");
                return null;
            }
            if (values.Length != vertexCount * 4)
                throw new InvalidDataException("Skin geometry " + fieldName + " has the wrong channel length.");
            var result = new Vector4[vertexCount];
            for (var i = 0; i < vertexCount; i++)
            {
                var x = values[i * 4];
                var y = values[i * 4 + 1];
                var z = values[i * 4 + 2];
                var w = values[i * 4 + 3];
                if (float.IsNaN(x) || float.IsInfinity(x) || float.IsNaN(y) || float.IsInfinity(y)
                    || float.IsNaN(z) || float.IsInfinity(z) || float.IsNaN(w) || float.IsInfinity(w))
                    throw new InvalidDataException("Skin geometry " + fieldName + " contains a non-finite value.");
                result[i] = new Vector4(x, y, z, w);
            }
            return result;
        }

        private static Color[] ReadColorChannel(float[] values, int vertexCount)
        {
            var colors = ReadVector4Channel(values, vertexCount, "colors", false);
            if (colors == null)
                return null;
            var result = new Color[colors.Length];
            for (var i = 0; i < colors.Length; i++)
                result[i] = new Color(colors[i].x, colors[i].y, colors[i].z, colors[i].w);
            return result;
        }

        private static void ApplyUvChannel(Mesh mesh, MeshUvChannelData channel, int vertexCount)
        {
            if (channel.dimension < 1 || channel.dimension > 4 || channel.values == null
                || channel.values.Length != vertexCount * channel.dimension)
                throw new InvalidDataException("Skin geometry UV channel has the wrong dimension or length.");

            if (channel.dimension <= 2)
            {
                var values = new List<Vector2>(vertexCount);
                for (var i = 0; i < vertexCount; i++)
                {
                    var x = channel.values[i * channel.dimension];
                    var y = channel.dimension > 1 ? channel.values[i * channel.dimension + 1] : 0.0f;
                    if (float.IsNaN(x) || float.IsInfinity(x) || float.IsNaN(y) || float.IsInfinity(y))
                        throw new InvalidDataException("Skin geometry UV channel contains a non-finite value.");
                    values.Add(new Vector2(x, y));
                }
                mesh.SetUVs(channel.channel, values);
            }
            else if (channel.dimension == 3)
            {
                var values = new List<Vector3>(vertexCount);
                for (var i = 0; i < vertexCount; i++)
                {
                    var offset = i * 3;
                    var value = new Vector3(channel.values[offset], channel.values[offset + 1], channel.values[offset + 2]);
                    if (float.IsNaN(value.x) || float.IsInfinity(value.x) || float.IsNaN(value.y) || float.IsInfinity(value.y)
                        || float.IsNaN(value.z) || float.IsInfinity(value.z))
                        throw new InvalidDataException("Skin geometry UV channel contains a non-finite value.");
                    values.Add(value);
                }
                mesh.SetUVs(channel.channel, values);
            }
            else
            {
                var values = ReadVector4Channel(channel.values, vertexCount, "UV channel", true);
                mesh.SetUVs(channel.channel, new List<Vector4>(values));
            }
        }

        private static Matrix4x4 ToMatrix4x4(BindPoseData data)
        {
            if (data == null)
                throw new InvalidDataException("Skin record contains a null bind pose.");
            var matrix = new Matrix4x4();
            matrix.m00 = data.e00; matrix.m01 = data.e01; matrix.m02 = data.e02; matrix.m03 = data.e03;
            matrix.m10 = data.e10; matrix.m11 = data.e11; matrix.m12 = data.e12; matrix.m13 = data.e13;
            matrix.m20 = data.e20; matrix.m21 = data.e21; matrix.m22 = data.e22; matrix.m23 = data.e23;
            matrix.m30 = data.e30; matrix.m31 = data.e31; matrix.m32 = data.e32; matrix.m33 = data.e33;
            return matrix;
        }

        private static Mesh CombineImportedMeshes(Mesh[] sourceMeshes, string meshId)
        {
            var combine = new List<CombineInstance>();
            var totalVertices = 0L;
            foreach (var source in sourceMeshes)
            {
                totalVertices += source.vertexCount;
                for (var submesh = 0; submesh < source.subMeshCount; submesh++)
                {
                    combine.Add(new CombineInstance
                    {
                        mesh = source,
                        subMeshIndex = submesh,
                        transform = Matrix4x4.identity
                    });
                }
            }
            var result = new Mesh
            {
                name = "Recovered_" + meshId,
                indexFormat = totalVertices > 65535 ? UnityEngine.Rendering.IndexFormat.UInt32 : UnityEngine.Rendering.IndexFormat.UInt16
            };
            result.CombineMeshes(combine.ToArray(), false, true, false);
            result.RecalculateBounds();
            return result;
        }

        private static Dictionary<string, Material> LoadExistingMaterials(MaterialManifest manifest)
        {
            var result = new Dictionary<string, Material>(StringComparer.Ordinal);
            if (manifest == null || manifest.materials == null)
                return result;
            foreach (var entry in manifest.materials)
            {
                if (entry == null || string.IsNullOrEmpty(entry.id))
                    continue;
                var material = AssetDatabase.LoadAssetAtPath<Material>(MaterialOutputPath + "/" + entry.id + ".mat");
                if (material != null)
                    result[entry.id] = material;
            }
            return result;
        }

        private static Dictionary<string, Material> CreateMaterials(MaterialManifest manifest, Dictionary<string, Texture2D> textures)
        {
            var result = new Dictionary<string, Material>(StringComparer.Ordinal);
            Directory.CreateDirectory(ToAbsoluteAssetPath(MaterialOutputPath));
            if (manifest == null || manifest.materials == null)
                return result;

            var standardShader = Shader.Find("Standard") ?? Shader.Find("Universal Render Pipeline/Lit") ?? Shader.Find("Unlit/Texture");
            if (standardShader == null)
                throw new InvalidOperationException("Could not find a built-in material shader.");

            foreach (var entry in manifest.materials)
            {
                if (entry == null || string.IsNullOrEmpty(entry.id))
                    continue;
                var assetPath = MaterialOutputPath + "/" + entry.id + ".mat";
                var material = AssetDatabase.LoadAssetAtPath<Material>(assetPath);
                if (material == null)
                {
                    material = new Material(standardShader);
                    material.name = string.IsNullOrEmpty(entry.name) ? entry.id : entry.name;
                    AssetDatabase.CreateAsset(material, assetPath);
                }
                else if (material.shader != standardShader)
                {
                    material.shader = standardShader;
                }

                if (entry.colors != null)
                {
                    foreach (var color in entry.colors)
                    {
                        if (color == null || color.value == null || color.value.Length < 4)
                            continue;
                        var property = NormalizeMaterialProperty(color.property);
                        if (material.HasProperty(property))
                            material.SetColor(property, new Color(color.value[0], color.value[1], color.value[2], color.value[3]));
                    }
                }
                if (entry.floats != null)
                {
                    foreach (var value in entry.floats)
                    {
                        if (value == null)
                            continue;
                        var property = NormalizeMaterialProperty(value.property);
                        if (material.HasProperty(property))
                            material.SetFloat(property, value.value);
                    }
                }
                if (entry.textures != null)
                {
                    foreach (var texture in entry.textures)
                    {
                        if (texture == null || string.IsNullOrEmpty(texture.textureId)
                            || !textures.TryGetValue(texture.textureId, out var image))
                            continue;
                        var property = NormalizeMaterialProperty(texture.property);
                        if (!material.HasProperty(property))
                        {
                            if (material.HasProperty("_MainTex"))
                                property = "_MainTex";
                            else
                                continue;
                        }
                        material.SetTexture(property, image);
                        if (texture.scale != null && texture.scale.Length >= 2)
                            material.SetTextureScale(property, new Vector2(texture.scale[0], texture.scale[1]));
                        if (texture.offset != null && texture.offset.Length >= 2)
                            material.SetTextureOffset(property, new Vector2(texture.offset[0], texture.offset[1]));
                    }
                }
                EditorUtility.SetDirty(material);
                result[entry.id] = material;
            }
            AssetDatabase.SaveAssets();
            return result;
        }

        private static string NormalizeMaterialProperty(string property)
        {
            if (string.IsNullOrEmpty(property))
                return "_MainTex";
            if (property == "_BaseColor")
                return "_Color";
            if (property == "_BaseMap")
                return "_MainTex";
            return property;
        }

        private static SceneManifest ReadCompressedSceneManifest()
        {
            var fullPath = ToAbsoluteAssetPath(SceneManifestFile);
            using (var input = new FileStream(fullPath, FileMode.Open, FileAccess.Read, FileShare.Read))
            using (var gzip = new GZipStream(input, CompressionMode.Decompress))
            using (var reader = new StreamReader(gzip, Encoding.UTF8))
            {
                var json = reader.ReadToEnd();
                var result = JsonUtility.FromJson<SceneManifest>(json);
                if (result == null || result.scenes == null || result.scenes.Length == 0)
                    throw new InvalidDataException("The scene manifest did not contain any scenes.");
                return result;
            }
        }

        private static MeshSkinManifest ReadCompressedMeshSkinManifest()
        {
            var fullPath = ToAbsoluteAssetPath(MeshSkinManifestFile);
            using (var input = new FileStream(fullPath, FileMode.Open, FileAccess.Read, FileShare.Read))
            using (var gzip = new GZipStream(input, CompressionMode.Decompress))
            using (var reader = new StreamReader(gzip, Encoding.UTF8))
            {
                var json = reader.ReadToEnd();
                var result = JsonUtility.FromJson<MeshSkinManifest>(json);
                if (result == null || result.formatVersion != 2 || result.meshes == null)
                    throw new InvalidDataException("The mesh skin manifest is missing or has an unsupported format version.");
                return result;
            }
        }

        private static Dictionary<string, MeshSkinData> IndexMeshSkinData(MeshSkinManifest manifest)
        {
            var result = new Dictionary<string, MeshSkinData>(StringComparer.Ordinal);
            if (manifest == null || manifest.meshes == null)
                return result;
            foreach (var entry in manifest.meshes)
            {
                if (entry == null || string.IsNullOrEmpty(entry.meshId))
                    continue;
                if (result.ContainsKey(entry.meshId))
                    throw new InvalidDataException("The mesh skin manifest contains duplicate mesh id " + entry.meshId + ".");
                result[entry.meshId] = entry;
            }
            return result;
        }

        private static T ReadJson<T>(string assetPath) where T : class
        {
            var fullPath = ToAbsoluteAssetPath(assetPath);
            if (!File.Exists(fullPath))
                return null;
            return JsonUtility.FromJson<T>(File.ReadAllText(fullPath, Encoding.UTF8));
        }

        private static void RebuildScenes(
            SceneManifest sceneManifest,
            Dictionary<string, Mesh> meshes,
            Dictionary<string, MeshSkinData> skinDataByMeshId,
            Dictionary<string, Material> materials,
            Dictionary<string, Sprite> sprites,
            Dictionary<string, AudioClip> audioClips,
            Dictionary<string, Font> fonts)
        {
            Directory.CreateDirectory(ToAbsoluteAssetPath(SceneOutputPath));
            var previousActiveScene = SceneManager.GetActiveScene();
            var buildScenes = new List<EditorBuildSettingsScene>();
            var skinSummary = new SkinRendererBuildSummary();
            for (var i = 0; i < sceneManifest.scenes.Length; i++)
            {
                var sceneData = sceneManifest.scenes[i];
                if (sceneData == null || sceneData.objects == null)
                    continue;
                var progress = 0.58f + 0.39f * (i / (float)Math.Max(1, sceneManifest.scenes.Length));
                EditorUtility.DisplayProgressBar("Rage of Fight reconstruction", "Rebuilding " + sceneData.name + "…", progress);
                var path = SceneOutputPath + "/" + sceneData.name + ".unity";
                BuildOneScene(sceneData, path, meshes, skinDataByMeshId, materials, sprites, audioClips, fonts, false, skinSummary);
                buildScenes.Add(new EditorBuildSettingsScene(path, true));
            }
            if (buildScenes.Count > 0)
                EditorBuildSettings.scenes = buildScenes.ToArray();
            if (previousActiveScene.IsValid() && previousActiveScene.isLoaded)
                SceneManager.SetActiveScene(previousActiveScene);
            AssetDatabase.SaveAssets();
            Debug.Log(
                "Rage of Fight skinning: " + skinSummary.skinnedRendererCount + " SkinnedMeshRenderer components bound to scene bones; "
                + skinSummary.staticFallbackCount + " component(s) use static fallback (" + string.Join(", ", skinSummary.staticFallbackMeshIds) + ").");
        }

        private static void RebuildUiPrefabs(
            UiPrefabManifest prefabManifest,
            Dictionary<string, Mesh> meshes,
            Dictionary<string, MeshSkinData> skinDataByMeshId,
            Dictionary<string, Material> materials,
            Dictionary<string, Sprite> sprites,
            Dictionary<string, AudioClip> audioClips,
            Dictionary<string, Font> fonts)
        {
            if (prefabManifest == null || prefabManifest.prefabs == null || prefabManifest.prefabs.Length == 0)
            {
                Debug.LogWarning("No shared-asset UI prefab manifest was found; skipping recovered UI prefab assets.");
                return;
            }

            Directory.CreateDirectory(ToAbsoluteAssetPath(PrefabOutputPath));
            Directory.CreateDirectory(ToAbsoluteAssetPath(MaterialOutputPath));
            for (var i = 0; i < prefabManifest.prefabs.Length; i++)
            {
                var prefab = prefabManifest.prefabs[i];
                if (prefab == null || prefab.objects == null || prefab.objects.Length == 0 || string.IsNullOrEmpty(prefab.id))
                {
                    Debug.LogWarning("Skipping an empty or invalid recovered UI prefab record at index " + i + ".");
                    continue;
                }
                var sceneData = new SceneData
                {
                    key = prefab.id,
                    name = prefab.name ?? prefab.id,
                    objectCount = prefab.objects.Length,
                    objects = prefab.objects
                };
                var path = PrefabOutputPath + "/" + prefab.id + ".prefab";
                BuildOneScene(sceneData, path, meshes, skinDataByMeshId, materials, sprites, audioClips, fonts, true);
            }
        }

        private static void BuildOneScene(
            SceneData sceneData,
            string scenePath,
            Dictionary<string, Mesh> meshes,
            Dictionary<string, MeshSkinData> skinDataByMeshId,
            Dictionary<string, Material> materials,
            Dictionary<string, Sprite> sprites,
            Dictionary<string, AudioClip> audioClips,
            Dictionary<string, Font> fonts,
            bool saveRootAsPrefab = false,
            SkinRendererBuildSummary skinSummary = null)
        {
            var previousActive = SceneManager.GetActiveScene();
            var scene = EditorSceneManager.NewScene(NewSceneSetup.EmptyScene, NewSceneMode.Additive);
            SceneManager.SetActiveScene(scene);
            var objectsById = new Dictionary<int, GameObject>(sceneData.objects.Length);
            var dataById = new Dictionary<int, SceneObject>(sceneData.objects.Length);

            try
            {
                for (var i = 0; i < sceneData.objects.Length; i++)
                {
                    var data = sceneData.objects[i];
                    if (data == null)
                        continue;
                    var isRect = data.transform != null && data.transform.kind == "RectTransform";
                    var go = isRect
                        ? new GameObject(data.name ?? ("Recovered_" + data.id), typeof(RectTransform))
                        : new GameObject(data.name ?? ("Recovered_" + data.id));
                    go.layer = Mathf.Clamp(data.layer, 0, 31);
                    if (!string.IsNullOrEmpty(data.tag) && data.tag != "Untagged")
                    {
                        try { go.tag = data.tag; }
                        catch { /* The original tag may not have been in this project's TagManager. */ }
                    }
                    objectsById[data.id] = go;
                    dataById[data.id] = data;
                    if (i % 1000 == 0)
                    {
                        var fraction = 0.05f + 0.40f * (i / (float)Math.Max(1, sceneData.objects.Length));
                        EditorUtility.DisplayProgressBar("Rage of Fight reconstruction", sceneData.name + ": creating hierarchy…", fraction);
                    }
                }

                // Parent first. Local transforms are applied after parenting so they
                // remain equivalent to the serialized values from the source scene.
                foreach (var pair in dataById)
                {
                    var data = pair.Value;
                    if (data.parent != 0 && objectsById.TryGetValue(data.parent, out var parent))
                        objectsById[pair.Key].transform.SetParent(parent.transform, false);
                }
                foreach (var pair in dataById)
                    ApplyTransform(objectsById[pair.Key].transform, pair.Value.transform);

                var defaultMaterial = GetDefaultMaterial();
                var count = 0;
                foreach (var pair in dataById)
                {
                    var go = objectsById[pair.Key];
                    var data = pair.Value;
                    RestoreVisualComponents(go, data, meshes, skinDataByMeshId, materials, sprites, audioClips, fonts, defaultMaterial, objectsById, skinSummary);
                    if (count % 1000 == 0)
                    {
                        var fraction = 0.47f + 0.48f * (count / (float)Math.Max(1, dataById.Count));
                        EditorUtility.DisplayProgressBar("Rage of Fight reconstruction", sceneData.name + ": adding visuals and UI…", fraction);
                    }
                    count++;
                }

                // Resolve references only after all target components exist, regardless
                // of source ordering within the scene manifest.
                foreach (var pair in dataById)
                    RestoreCanvasCamera(objectsById[pair.Key], pair.Value.canvas, objectsById);
                foreach (var pair in dataById)
                    RestoreButtonReferences(objectsById[pair.Key], pair.Value.uiButtonData, objectsById);
                foreach (var pair in dataById)
                    RestoreCharacterJoint(objectsById[pair.Key], pair.Value.characterJoint, objectsById);

                foreach (var pair in dataById)
                    objectsById[pair.Key].SetActive(pair.Value.active);

                if (saveRootAsPrefab)
                {
                    var rootIds = dataById.Where(pair => pair.Value.parent == 0).Select(pair => pair.Key).ToArray();
                    if (rootIds.Length != 1 || !objectsById.TryGetValue(rootIds[0], out var prefabRoot))
                        throw new InvalidDataException("Recovered UI prefab must contain exactly one root GameObject: " + sceneData.name);
                    var prefabPath = scenePath;
                    Directory.CreateDirectory(Path.GetDirectoryName(ToAbsoluteAssetPath(prefabPath)));
                    if (PrefabUtility.SaveAsPrefabAsset(prefabRoot, prefabPath) == null)
                        throw new IOException("Unity could not save reconstructed UI prefab: " + prefabPath);
                    Debug.Log("Rebuilt UI prefab " + sceneData.name + " with " + sceneData.objects.Length + " GameObjects to " + prefabPath);
                }
                else
                {
                    var fullPath = ToAbsoluteAssetPath(scenePath);
                    Directory.CreateDirectory(Path.GetDirectoryName(fullPath));
                    if (!EditorSceneManager.SaveScene(scene, scenePath))
                        throw new IOException("Unity could not save reconstructed scene: " + scenePath);
                    Debug.Log("Rebuilt " + sceneData.name + " with " + sceneData.objects.Length + " GameObjects to " + scenePath);
                }
            }
            finally
            {
                EditorSceneManager.CloseScene(scene, true);
                if (previousActive.IsValid() && previousActive.isLoaded)
                    SceneManager.SetActiveScene(previousActive);
            }
        }

        private static void ApplyTransform(Transform transform, TransformData data)
        {
            if (transform == null || data == null)
                return;
            transform.localRotation = new Quaternion(data.rotation[0], data.rotation[1], data.rotation[2], data.rotation[3]);
            transform.localScale = new Vector3(data.scale[0], data.scale[1], data.scale[2]);
            var rect = transform as RectTransform;
            if (rect != null && data.kind == "RectTransform")
            {
                rect.anchorMin = new Vector2(data.anchorMin[0], data.anchorMin[1]);
                rect.anchorMax = new Vector2(data.anchorMax[0], data.anchorMax[1]);
                rect.pivot = new Vector2(data.pivot[0], data.pivot[1]);
                rect.sizeDelta = new Vector2(data.sizeDelta[0], data.sizeDelta[1]);
                rect.anchoredPosition3D = new Vector3(
                    data.anchoredPosition[0], data.anchoredPosition[1], data.position[2]);
            }
            else
            {
                transform.localPosition = new Vector3(data.position[0], data.position[1], data.position[2]);
            }
        }

        private static bool TryRestoreSkinnedMeshRenderer(
            GameObject go,
            SceneObject sceneObject,
            RendererData rendererData,
            Dictionary<string, Mesh> meshes,
            Dictionary<string, MeshSkinData> skinDataByMeshId,
            Dictionary<string, Material> materials,
            Material defaultMaterial,
            Dictionary<int, GameObject> objectsById)
        {
            if (go == null || sceneObject == null || rendererData == null
                || string.IsNullOrEmpty(rendererData.meshId)
                || meshes == null || skinDataByMeshId == null || objectsById == null
                || !meshes.TryGetValue(rendererData.meshId, out var mesh) || mesh == null
                || !skinDataByMeshId.TryGetValue(rendererData.meshId, out var skinData) || skinData == null)
                return false;
            if (skinData.geometry == null || mesh.vertexCount != skinData.vertexCount
                || skinData.bindPoseCount <= 0 || mesh.bindposes.Length != skinData.bindPoseCount
                || rendererData.boneCount != skinData.bindPoseCount)
                return false;
            if (rendererData.boneObjects == null || rendererData.boneFileIds == null || rendererData.bonePathIds == null
                || rendererData.boneObjects.Length != skinData.bindPoseCount
                || rendererData.boneFileIds.Length != skinData.bindPoseCount
                || rendererData.bonePathIds.Length != skinData.bindPoseCount)
                return false;

            var bones = new Transform[skinData.bindPoseCount];
            for (var i = 0; i < bones.Length; i++)
            {
                var pathId = rendererData.bonePathIds[i];
                var fileId = rendererData.boneFileIds[i];
                var objectId = rendererData.boneObjects[i];
                if (pathId == 0)
                {
                    if (fileId != 0 || objectId != 0)
                        return false;
                    bones[i] = null;
                    continue;
                }
                if (fileId != 0 || objectId == 0 || !objectsById.TryGetValue(objectId, out var boneObject) || boneObject == null)
                    return false;
                bones[i] = boneObject.transform;
            }

            Transform rootBone = null;
            if (rendererData.rootBonePathId != 0)
            {
                if (rendererData.rootBoneFileId != 0 || rendererData.rootBoneObject == 0
                    || !objectsById.TryGetValue(rendererData.rootBoneObject, out var rootObject) || rootObject == null)
                    return false;
                rootBone = rootObject.transform;
            }

            if (skinData.boneIndices == null || skinData.boneWeights == null
                || skinData.boneIndices.Length != skinData.vertexCount * 4
                || skinData.boneWeights.Length != skinData.vertexCount * 4)
                return false;
            for (var i = 0; i < skinData.boneWeights.Length; i++)
            {
                var weight = skinData.boneWeights[i];
                if (float.IsNaN(weight) || float.IsInfinity(weight) || weight < -0.0000001f)
                    return false;
                if (weight > 0.00000001f)
                {
                    var boneIndex = skinData.boneIndices[i];
                    if (boneIndex < 0 || boneIndex >= bones.Length || bones[boneIndex] == null)
                        return false;
                }
            }

            var renderer = go.GetComponent<SkinnedMeshRenderer>() ?? go.AddComponent<SkinnedMeshRenderer>();
            renderer.sharedMesh = mesh;
            renderer.bones = bones;
            renderer.rootBone = rootBone;
            renderer.sharedMaterials = ResolveMaterials(sceneObject.materials, materials, mesh.subMeshCount, defaultMaterial);
            renderer.updateWhenOffscreen = rendererData.updateWhenOffscreen;
            renderer.skinnedMotionVectors = rendererData.skinnedMotionVectors;
            if (rendererData.quality == (int)SkinQuality.Bone1
                || rendererData.quality == (int)SkinQuality.Bone2
                || rendererData.quality == (int)SkinQuality.Bone4)
                renderer.quality = (SkinQuality)rendererData.quality;
            else
                renderer.quality = SkinQuality.Auto;

            var boundsCenter = ToVector3(rendererData.localBoundsCenter, mesh.bounds.center);
            var boundsExtents = ToVector3(rendererData.localBoundsExtents, mesh.bounds.extents);
            renderer.localBounds = new Bounds(boundsCenter, boundsExtents * 2.0f);
            RestoreRendererSettings(renderer, rendererData);
            return true;
        }

        private static void RestoreVisualComponents(
            GameObject go,
            SceneObject data,
            Dictionary<string, Mesh> meshes,
            Dictionary<string, MeshSkinData> skinDataByMeshId,
            Dictionary<string, Material> materials,
            Dictionary<string, Sprite> sprites,
            Dictionary<string, AudioClip> audioClips,
            Dictionary<string, Font> fonts,
            Material defaultMaterial,
            Dictionary<int, GameObject> objectsById,
            SkinRendererBuildSummary skinSummary)
        {
            var skinnedRendererData = FindRendererSettings(data.renderers, "SkinnedMeshRenderer");
            var restoredAsSkinned = skinnedRendererData != null && TryRestoreSkinnedMeshRenderer(
                go, data, skinnedRendererData, meshes, skinDataByMeshId, materials, defaultMaterial, objectsById);
            if (skinnedRendererData != null && skinSummary != null)
            {
                if (restoredAsSkinned)
                {
                    skinSummary.skinnedRendererCount++;
                }
                else
                {
                    skinSummary.staticFallbackCount++;
                    var meshId = skinnedRendererData.meshId ?? "<missing mesh id>";
                    skinSummary.staticFallbackMeshIds.Add(meshId);
                    Debug.LogWarning("Skinned renderer " + go.name + " uses static fallback because its mesh or scene bones could not be resolved: " + meshId);
                }
            }

            if (!restoredAsSkinned)
            {
                Mesh recoveredMesh = null;
                if (skinnedRendererData != null && !string.IsNullOrEmpty(skinnedRendererData.meshId))
                    meshes.TryGetValue(skinnedRendererData.meshId, out recoveredMesh);
                if (recoveredMesh == null && data.meshes != null)
                {
                    foreach (var id in data.meshes)
                    {
                        if (!string.IsNullOrEmpty(id) && meshes.TryGetValue(id, out recoveredMesh) && recoveredMesh != null)
                            break;
                    }
                }
                if (recoveredMesh != null)
                {
                    var filter = go.GetComponent<MeshFilter>() ?? go.AddComponent<MeshFilter>();
                    var renderer = go.GetComponent<MeshRenderer>() ?? go.AddComponent<MeshRenderer>();
                    filter.sharedMesh = recoveredMesh;
                    renderer.sharedMaterials = ResolveMaterials(data.materials, materials, recoveredMesh.subMeshCount, defaultMaterial);
                    RestoreRendererSettings(renderer, skinnedRendererData ?? FindRendererSettings(data.renderers, "MeshRenderer"));
                }
            }

            if (data.colliders != null)
            {
                foreach (var colliderData in data.colliders)
                {
                    if (colliderData == null)
                        continue;
                    Collider collider = null;
                    if (colliderData.type == "BoxCollider")
                    {
                        var box = go.AddComponent<BoxCollider>();
                        box.center = ToVector3(colliderData.center, Vector3.zero);
                        box.size = ToVector3(colliderData.size, Vector3.one);
                        collider = box;
                    }
                    else if (colliderData.type == "SphereCollider")
                    {
                        var sphere = go.AddComponent<SphereCollider>();
                        sphere.center = ToVector3(colliderData.center, Vector3.zero);
                        sphere.radius = Mathf.Max(0.001f, colliderData.radius);
                        collider = sphere;
                    }
                    else if (colliderData.type == "CapsuleCollider")
                    {
                        var capsule = go.AddComponent<CapsuleCollider>();
                        capsule.center = ToVector3(colliderData.center, Vector3.zero);
                        capsule.radius = Mathf.Max(0.001f, colliderData.radius);
                        capsule.height = Mathf.Max(capsule.radius * 2.0f, colliderData.height);
                        capsule.direction = Mathf.Clamp(colliderData.direction, 0, 2);
                        collider = capsule;
                    }
                    else if (colliderData.type == "MeshCollider")
                    {
                        var meshCollider = go.AddComponent<MeshCollider>();
                        if (!string.IsNullOrEmpty(colliderData.mesh) && meshes.TryGetValue(colliderData.mesh, out var collisionMesh))
                            meshCollider.sharedMesh = collisionMesh;
                        meshCollider.convex = colliderData.convex;
                        collider = meshCollider;
                    }
                    if (collider != null)
                    {
                        collider.enabled = colliderData.enabled;
                        collider.isTrigger = colliderData.isTrigger;
                    }
                }
            }

            if (data.rigidbody != null || Contains(data.components, "Rigidbody"))
            {
                var body = go.GetComponent<Rigidbody>() ?? go.AddComponent<Rigidbody>();
                if (data.rigidbody != null)
                {
                    body.mass = Mathf.Max(0.0001f, data.rigidbody.mass);
                    body.drag = Mathf.Max(0.0f, data.rigidbody.drag);
                    body.angularDrag = Mathf.Max(0.0f, data.rigidbody.angularDrag);
                    body.useGravity = data.rigidbody.useGravity;
                    body.isKinematic = data.rigidbody.isKinematic;
                    body.interpolation = (RigidbodyInterpolation)Mathf.Clamp(data.rigidbody.interpolation, 0, 2);
                    body.constraints = (RigidbodyConstraints)data.rigidbody.constraints;
                    body.collisionDetectionMode = (CollisionDetectionMode)Mathf.Clamp(data.rigidbody.collisionDetection, 0, 3);
                    body.enabled = data.rigidbody.enabled;
                    body.detectCollisions = true;
                    body.maxDepenetrationVelocity = 10.0f;
                }
            }

            if (Contains(data.components, "Animator"))
                GetOrAdd<Animator>(go);
            if (Contains(data.components, "Animation"))
                GetOrAdd<Animation>(go);
            if (Contains(data.components, "ParticleSystem"))
            {
                var particleSystem = GetOrAdd<ParticleSystem>(go);
                particleSystem.playOnAwake = false;
                var particleRenderer = go.GetComponent<ParticleSystemRenderer>();
                if (particleRenderer != null)
                {
                    if (data.materials != null && data.materials.Length > 0)
                        particleRenderer.sharedMaterials = ResolveMaterials(data.materials, materials, data.materials.Length, defaultMaterial);
                    RestoreRendererSettings(particleRenderer, FindRendererSettings(data.renderers, "ParticleSystemRenderer"));
                }
            }
            if (Contains(data.components, "NavMeshAgent"))
            {
                var agent = GetOrAdd<NavMeshAgent>(go);
                if (data.navMeshAgent != null)
                {
                    agent.radius = Mathf.Max(0.01f, data.navMeshAgent.radius);
                    agent.height = Mathf.Max(0.01f, data.navMeshAgent.height);
                    agent.speed = Mathf.Max(0.0f, data.navMeshAgent.speed);
                    agent.acceleration = Mathf.Max(0.0f, data.navMeshAgent.acceleration);
                    agent.angularSpeed = Mathf.Max(0.0f, data.navMeshAgent.angularSpeed);
                    agent.stoppingDistance = Mathf.Max(0.0f, data.navMeshAgent.stoppingDistance);
                    agent.baseOffset = data.navMeshAgent.baseOffset;
                    agent.avoidancePriority = Mathf.Clamp(data.navMeshAgent.avoidancePriority, 0, 99);
                    agent.autoBraking = data.navMeshAgent.autoBraking;
                    agent.autoRepath = data.navMeshAgent.autoRepath;
                }
                // The source NavMeshData is indexed, but not yet rebaked into this project.
                agent.enabled = false;
            }
            if (Contains(data.components, "NavMeshObstacle"))
            {
                var obstacle = GetOrAdd<NavMeshObstacle>(go);
                if (data.navMeshObstacle != null)
                {
                    obstacle.radius = Mathf.Max(0.01f, data.navMeshObstacle.radius);
                    obstacle.height = Mathf.Max(0.01f, data.navMeshObstacle.height);
                    obstacle.carving = data.navMeshObstacle.carving;
                }
                obstacle.enabled = false;
            }
            if (Contains(data.components, "AudioListener"))
                GetOrAdd<AudioListener>(go);

            if (Contains(data.components, "SpriteRenderer") && !string.IsNullOrEmpty(data.sprite))
            {
                if (sprites.TryGetValue(data.sprite, out var sprite) && sprite != null)
                {
                    var renderer = go.GetComponent<SpriteRenderer>() ?? go.AddComponent<SpriteRenderer>();
                    renderer.sprite = sprite;
                    RestoreRendererSettings(renderer, FindRendererSettings(data.renderers, "SpriteRenderer"));
                }
            }

            if (data.uiCanvas || Contains(data.components, "Canvas"))
            {
                var canvas = go.GetComponent<Canvas>() ?? go.AddComponent<Canvas>();
                if (data.canvas != null)
                {
                    canvas.enabled = data.canvas.enabled;
                    canvas.renderMode = (RenderMode)Mathf.Clamp(data.canvas.renderMode, 0, 2);
                    canvas.planeDistance = Mathf.Max(0.01f, data.canvas.planeDistance);
                    canvas.pixelPerfect = data.canvas.pixelPerfect;
                    canvas.overrideSorting = data.canvas.overrideSorting;
                    canvas.sortingLayerID = data.canvas.sortingLayerId;
                    canvas.sortingOrder = data.canvas.sortingOrder;
                    canvas.targetDisplay = Mathf.Clamp(data.canvas.targetDisplay, 0, 7);
                }
                else if (canvas.renderMode == RenderMode.ScreenSpaceOverlay)
                {
                    canvas.pixelPerfect = true;
                }
            }
            if (Contains(data.scripts, "UnityEngine.UI.CanvasScaler"))
            {
                var scaler = go.GetComponent<CanvasScaler>() ?? go.AddComponent<CanvasScaler>();
                if (data.canvasScaler != null)
                {
                    scaler.uiScaleMode = (CanvasScaler.ScaleMode)Mathf.Clamp(data.canvasScaler.uiScaleMode, 0, 2);
                    scaler.referencePixelsPerUnit = Mathf.Max(0.01f, data.canvasScaler.referencePixelsPerUnit);
                    scaler.scaleFactor = Mathf.Max(0.01f, data.canvasScaler.scaleFactor);
                    scaler.screenMatchMode = (CanvasScaler.ScreenMatchMode)Mathf.Clamp(data.canvasScaler.screenMatchMode, 0, 2);
                    scaler.matchWidthOrHeight = Mathf.Clamp01(data.canvasScaler.matchWidthOrHeight);
                    scaler.physicalUnit = (CanvasScaler.Unit)Mathf.Clamp(data.canvasScaler.physicalUnit, 0, 4);
                    scaler.fallbackScreenDPI = Mathf.Max(1.0f, data.canvasScaler.fallbackScreenDPI);
                    scaler.defaultSpriteDPI = Mathf.Max(1.0f, data.canvasScaler.defaultSpriteDPI);
                    scaler.dynamicPixelsPerUnit = Mathf.Max(0.01f, data.canvasScaler.dynamicPixelsPerUnit);
                    if (data.canvasScaler.referenceResolution != null && data.canvasScaler.referenceResolution.Length >= 2)
                        scaler.referenceResolution = new Vector2(data.canvasScaler.referenceResolution[0], data.canvasScaler.referenceResolution[1]);
                }
                else
                {
                    scaler.uiScaleMode = CanvasScaler.ScaleMode.ScaleWithScreenSize;
                    scaler.referenceResolution = new Vector2(1920, 1080);
                    scaler.matchWidthOrHeight = 0.5f;
                }
            }
            if (Contains(data.scripts, "UnityEngine.UI.GraphicRaycaster"))
                GetOrAdd<GraphicRaycaster>(go);

            Image image = null;
            if (data.uiImage)
            {
                image = go.GetComponent<Image>() ?? go.AddComponent<Image>();
                if (!string.IsNullOrEmpty(data.sprite) && sprites.TryGetValue(data.sprite, out var imageSprite))
                    image.sprite = imageSprite;
                if (data.uiImageData != null)
                {
                    image.color = ToColor(data.uiImageData.color, Color.white);
                    image.raycastTarget = data.uiImageData.raycastTarget;
                    image.maskable = data.uiImageData.maskable;
                    image.type = (Image.Type)Mathf.Clamp(data.uiImageData.type, 0, 3);
                    image.preserveAspect = data.uiImageData.preserveAspect;
                    image.fillCenter = data.uiImageData.fillCenter;
                    image.fillMethod = (Image.FillMethod)Mathf.Clamp(data.uiImageData.fillMethod, 0, 4);
                    image.fillAmount = Mathf.Clamp01(data.uiImageData.fillAmount);
                    image.fillClockwise = data.uiImageData.fillClockwise;
                    image.fillOrigin = Mathf.Clamp(data.uiImageData.fillOrigin, 0, 3);
                    image.useSpriteMesh = data.uiImageData.useSpriteMesh;
                    image.pixelsPerUnitMultiplier = Mathf.Max(0.01f, data.uiImageData.pixelsPerUnitMultiplier);
                }
                else
                {
                    image.raycastTarget = data.uiButton;
                }
            }
            if (data.uiText)
            {
                var label = go.GetComponent<Text>() ?? go.AddComponent<Text>();
                label.text = data.text ?? string.Empty;
                if (data.uiTextData != null && !string.IsNullOrEmpty(data.uiTextData.fontId)
                    && fonts.TryGetValue(data.uiTextData.fontId, out var recoveredFont))
                    label.font = recoveredFont;
                else
                {
                    try { label.font = Resources.GetBuiltinResource<Font>("Arial.ttf"); }
                    catch { /* Use Unity's default font if the legacy Arial asset is unavailable. */ }
                }
                if (data.uiTextData != null)
                {
                    label.color = ToColor(data.uiTextData.color, Color.white);
                    label.raycastTarget = data.uiTextData.raycastTarget;
                    label.maskable = data.uiTextData.maskable;
                    label.fontSize = Mathf.Clamp(data.uiTextData.fontSize, 0, 512);
                    label.fontStyle = (FontStyle)Mathf.Clamp(data.uiTextData.fontStyle, 0, 3);
                    label.resizeTextForBestFit = data.uiTextData.bestFit;
                    label.resizeTextMinSize = Mathf.Clamp(data.uiTextData.minSize, 1, 512);
                    label.resizeTextMaxSize = Mathf.Clamp(data.uiTextData.maxSize, label.resizeTextMinSize, 512);
                    label.alignment = (TextAnchor)Mathf.Clamp(data.uiTextData.alignment, 0, 8);
                    label.alignByGeometry = data.uiTextData.alignByGeometry;
                    label.supportRichText = data.uiTextData.richText;
                    label.horizontalOverflow = (HorizontalWrapMode)Mathf.Clamp(data.uiTextData.horizontalOverflow, 0, 1);
                    label.verticalOverflow = (VerticalWrapMode)Mathf.Clamp(data.uiTextData.verticalOverflow, 0, 1);
                    label.lineSpacing = Mathf.Max(0.0f, data.uiTextData.lineSpacing);
                }
                else
                {
                    label.fontSize = 18;
                    label.color = Color.white;
                    label.raycastTarget = false;
                }
            }
            if (data.uiButton)
            {
                var button = go.GetComponent<Button>() ?? go.AddComponent<Button>();
                if (image != null)
                    button.targetGraphic = image;
                RestoreButtonPresentation(button, data.uiButtonData, sprites);
                // Original onClick targets and ad/shop logic are IL2CPP behaviours;
                // they are intentionally not fabricated here.
            }
            if (Contains(data.scripts, "UnityEngine.UI.Outline"))
                GetOrAdd<Outline>(go);
            if (Contains(data.scripts, "UnityEngine.UI.Shadow"))
                GetOrAdd<Shadow>(go);
            if (Contains(data.scripts, "UnityEngine.UI.Mask"))
                GetOrAdd<Mask>(go);
            if (Contains(data.scripts, "UnityEngine.UI.ScrollRect"))
                GetOrAdd<ScrollRect>(go);
            if (Contains(data.scripts, "UnityEngine.UI.VerticalLayoutGroup"))
                GetOrAdd<VerticalLayoutGroup>(go);
            if (Contains(data.scripts, "UnityEngine.UI.HorizontalLayoutGroup"))
                GetOrAdd<HorizontalLayoutGroup>(go);
            if (data.uiEffects != null)
            {
                foreach (var effectData in data.uiEffects)
                {
                    if (effectData == null)
                        continue;
                    Shadow effect;
                    if (effectData.type == "Outline")
                        effect = GetOrAdd<Outline>(go);
                    else if (effectData.type == "Shadow")
                        effect = GetOrAdd<Shadow>(go);
                    else
                        continue;
                    effect.enabled = effectData.enabled;
                    effect.effectColor = ToColor(effectData.color, Color.black);
                    if (effectData.distance != null && effectData.distance.Length >= 2)
                        effect.effectDistance = new Vector2(effectData.distance[0], effectData.distance[1]);
                    effect.useGraphicAlpha = effectData.useGraphicAlpha;
                }
            }
            if (data.canvasGroup != null || Contains(data.components, "CanvasGroup"))
            {
                var canvasGroup = GetOrAdd<CanvasGroup>(go);
                if (data.canvasGroup != null)
                {
                    canvasGroup.enabled = data.canvasGroup.enabled;
                    canvasGroup.alpha = Mathf.Clamp01(data.canvasGroup.alpha);
                    canvasGroup.interactable = data.canvasGroup.interactable;
                    canvasGroup.blocksRaycasts = data.canvasGroup.blocksRaycasts;
                    canvasGroup.ignoreParentGroups = data.canvasGroup.ignoreParentGroups;
                }
            }

            if (Contains(data.components, "Camera"))
            {
                var camera = go.GetComponent<Camera>() ?? go.AddComponent<Camera>();
                if (data.camera != null)
                {
                    camera.enabled = data.camera.enabled;
                    camera.orthographic = data.camera.orthographic;
                    if (data.camera.fieldOfView > 0) camera.fieldOfView = data.camera.fieldOfView;
                    if (data.camera.nearClip > 0) camera.nearClipPlane = data.camera.nearClip;
                    if (data.camera.farClip > data.camera.nearClip) camera.farClipPlane = data.camera.farClip;
                    if (data.camera.orthographicSize > 0) camera.orthographicSize = data.camera.orthographicSize;
                    camera.clearFlags = (CameraClearFlags)Mathf.Clamp(data.camera.clearFlags, 1, 4);
                    camera.backgroundColor = ToColor(data.camera.backgroundColor, Color.black);
                    if (data.camera.viewportRect != null && data.camera.viewportRect.Length >= 4)
                        camera.rect = new Rect(data.camera.viewportRect[0], data.camera.viewportRect[1], data.camera.viewportRect[2], data.camera.viewportRect[3]);
                    camera.depth = data.camera.depth;
                    camera.cullingMask = data.camera.cullingMask;
                    camera.allowHDR = data.camera.allowHDR;
                    camera.allowMSAA = data.camera.allowMSAA;
                    camera.useOcclusionCulling = data.camera.useOcclusionCulling;
                    camera.renderingPath = (RenderingPath)Mathf.Clamp(data.camera.renderingPath, -1, 3);
                }
                if (go.tag == "Untagged")
                {
                    try { go.tag = "MainCamera"; }
                    catch { /* Keep the recovered tag if MainCamera is unavailable. */ }
                }
            }
            if (Contains(data.components, "Light"))
            {
                var light = go.GetComponent<Light>() ?? go.AddComponent<Light>();
                if (data.light != null)
                {
                    light.enabled = data.light.enabled;
                    light.type = data.light.type == 0 ? LightType.Spot
                        : data.light.type == 2 ? LightType.Point
                        : data.light.type == 3 ? LightType.Area
                        : LightType.Directional;
                    light.color = ToColor(data.light.color, Color.white);
                    light.intensity = Mathf.Max(0, data.light.intensity);
                    light.range = Mathf.Max(0.01f, data.light.range);
                    light.spotAngle = Mathf.Clamp(data.light.spotAngle, 1.0f, 179.0f);
                    light.innerSpotAngle = Mathf.Clamp(data.light.innerSpotAngle, 0.0f, light.spotAngle);
                    light.shadows = (LightShadows)Mathf.Clamp(data.light.shadows, 0, 2);
                    light.shadowStrength = Mathf.Clamp01(data.light.shadowStrength);
                    light.shadowBias = Mathf.Max(0.0f, data.light.shadowBias);
                    light.shadowNormalBias = Mathf.Max(0.0f, data.light.shadowNormalBias);
                    light.useColorTemperature = data.light.useColorTemperature;
                    if (data.light.useColorTemperature)
                        light.colorTemperature = Mathf.Clamp(data.light.colorTemperature, 1000.0f, 20000.0f);
                    light.drawHalo = data.light.drawHalo;
                    light.bounceIntensity = Mathf.Max(0.0f, data.light.bounceIntensity);
                    if (light.type == LightType.Area && data.light.areaSize != null && data.light.areaSize.Length >= 2)
                        light.areaSize = new Vector2(data.light.areaSize[0], data.light.areaSize[1]);
                }
            }

            if (Contains(data.components, "AudioSource"))
            {
                // Assign a recovered WAV when it was included by the extractor;
                // clips omitted from the selected export mode stay unassigned.
                var source = GetOrAdd<AudioSource>(go);
                if (data.audioSource != null)
                {
                    source.enabled = data.audioSource.enabled;
                    source.clip = null;
                    if (!string.IsNullOrEmpty(data.audioSource.clip)
                        && audioClips.TryGetValue(data.audioSource.clip, out var recoveredAudio))
                        source.clip = recoveredAudio;
                    source.playOnAwake = data.audioSource.playOnAwake;
                    source.loop = data.audioSource.loop;
                    source.volume = Mathf.Clamp01(data.audioSource.volume);
                    source.pitch = Mathf.Clamp(data.audioSource.pitch, -3.0f, 3.0f);
                    source.priority = Mathf.Clamp(data.audioSource.priority, 0, 256);
                    source.minDistance = Mathf.Max(0.01f, data.audioSource.minDistance);
                    source.maxDistance = Mathf.Max(source.minDistance, data.audioSource.maxDistance);
                }
            }
        }

        private static void RestoreButtonPresentation(
            Button button,
            ButtonData data,
            Dictionary<string, Sprite> sprites)
        {
            if (button == null || data == null)
                return;
            button.enabled = data.enabled;
            button.interactable = data.interactable;
            button.transition = (Selectable.Transition)Mathf.Clamp(data.transition, 0, 3);
            if (data.colors != null)
            {
                var colors = button.colors;
                colors.normalColor = ToColor(data.colors.normal, Color.white);
                colors.highlightedColor = ToColor(data.colors.highlighted, Color.white);
                colors.pressedColor = ToColor(data.colors.pressed, Color.white);
                colors.selectedColor = ToColor(data.colors.selected, Color.white);
                colors.disabledColor = ToColor(data.colors.disabled, Color.white);
                colors.colorMultiplier = Mathf.Max(0.0f, data.colors.colorMultiplier);
                colors.fadeDuration = Mathf.Max(0.0f, data.colors.fadeDuration);
                button.colors = colors;
            }
            if (data.sprites != null)
            {
                var state = button.spriteState;
                if (!string.IsNullOrEmpty(data.sprites.highlighted) && sprites.TryGetValue(data.sprites.highlighted, out var highlighted))
                    state.highlightedSprite = highlighted;
                if (!string.IsNullOrEmpty(data.sprites.pressed) && sprites.TryGetValue(data.sprites.pressed, out var pressed))
                    state.pressedSprite = pressed;
                if (!string.IsNullOrEmpty(data.sprites.selected) && sprites.TryGetValue(data.sprites.selected, out var selected))
                    state.selectedSprite = selected;
                if (!string.IsNullOrEmpty(data.sprites.disabled) && sprites.TryGetValue(data.sprites.disabled, out var disabled))
                    state.disabledSprite = disabled;
                button.spriteState = state;
            }
            if (data.animationTriggers != null)
            {
                var triggers = button.animationTriggers ?? new AnimationTriggers();
                triggers.normalTrigger = data.animationTriggers.normal ?? string.Empty;
                triggers.highlightedTrigger = data.animationTriggers.highlighted ?? string.Empty;
                triggers.pressedTrigger = data.animationTriggers.pressed ?? string.Empty;
                triggers.selectedTrigger = data.animationTriggers.selected ?? string.Empty;
                triggers.disabledTrigger = data.animationTriggers.disabled ?? string.Empty;
                button.animationTriggers = triggers;
            }
        }

        private static void RestoreButtonReferences(GameObject go, ButtonData data, Dictionary<int, GameObject> objectsById)
        {
            if (go == null || data == null)
                return;
            var button = go.GetComponent<Button>();
            if (button == null)
                return;
            button.targetGraphic = null;
            if (data.targetGraphicPresent
                && objectsById.TryGetValue(data.targetGraphicObject, out var targetObject))
                button.targetGraphic = targetObject.GetComponent<Graphic>();
            RestoreSupportedButtonPersistentCalls(button, data.persistentCalls, objectsById);
            if (data.navigation == null)
                return;
            var navigation = button.navigation;
            navigation.mode = (Navigation.Mode)Mathf.Clamp(data.navigation.mode, 0, 4);
            navigation.wrapAround = data.navigation.wrapAround;
            navigation.selectOnUp = FindSelectable(data.navigation.selectOnUpObject, objectsById);
            navigation.selectOnDown = FindSelectable(data.navigation.selectOnDownObject, objectsById);
            navigation.selectOnLeft = FindSelectable(data.navigation.selectOnLeftObject, objectsById);
            navigation.selectOnRight = FindSelectable(data.navigation.selectOnRightObject, objectsById);
            button.navigation = navigation;
        }

        private static void RestoreSupportedButtonPersistentCalls(
            Button button,
            PersistentCallData[] calls,
            Dictionary<int, GameObject> objectsById)
        {
            if (button == null || calls == null || objectsById == null)
                return;
            foreach (var call in calls)
            {
                if (call == null || call.targetObjectId == 0
                    || !objectsById.TryGetValue(call.targetObjectId, out var targetObject))
                    continue;

                if (call.targetType == "AudioSource" && call.methodName == "Play" && call.mode == 1)
                {
                    var audioSource = targetObject.GetComponent<AudioSource>();
                    if (audioSource == null)
                        continue;
                    UnityEventTools.AddVoidPersistentListener(button.onClick, audioSource.Play);
                }
                else if (call.targetType == "GameObject" && call.methodName == "SetActive" && call.mode == 6)
                {
                    UnityEventTools.AddBoolPersistentListener(button.onClick, targetObject.SetActive, call.boolArgument);
                }
                else
                {
                    // Custom IL2CPP methods are kept in the manifest but cannot be
                    // rebound until their original managed scripts are reconstructed.
                    continue;
                }

                var listenerIndex = button.onClick.GetPersistentEventCount() - 1;
                if (listenerIndex >= 0)
                    button.onClick.SetPersistentListenerState(
                        listenerIndex,
                        (UnityEventCallState)Mathf.Clamp(call.callState, 0, 2));
            }
        }

        private static Selectable FindSelectable(int objectId, Dictionary<int, GameObject> objectsById)
        {
            return objectId != 0 && objectsById.TryGetValue(objectId, out var targetObject)
                ? targetObject.GetComponent<Selectable>()
                : null;
        }

        private static RendererData FindRendererSettings(RendererData[] entries, params string[] rendererTypes)
        {
            if (entries == null || rendererTypes == null)
                return null;
            foreach (var entry in entries)
            {
                if (entry != null && Array.IndexOf(rendererTypes, entry.type) >= 0)
                    return entry;
            }
            return null;
        }

        private static void RestoreRendererSettings(Renderer renderer, RendererData data)
        {
            if (renderer == null || data == null)
                return;
            renderer.enabled = data.enabled;
            renderer.shadowCastingMode = (UnityEngine.Rendering.ShadowCastingMode)Mathf.Clamp(data.castShadows, 0, 3);
            renderer.receiveShadows = data.receiveShadows;
            renderer.motionVectorGenerationMode = (UnityEngine.Rendering.MotionVectorGenerationMode)Mathf.Clamp(data.motionVectors, 0, 2);
            renderer.lightProbeUsage = (UnityEngine.Rendering.LightProbeUsage)Mathf.Clamp(data.lightProbeUsage, 0, 3);
            renderer.reflectionProbeUsage = (UnityEngine.Rendering.ReflectionProbeUsage)Mathf.Clamp(data.reflectionProbeUsage, 0, 3);
            renderer.renderingLayerMask = unchecked((uint)data.renderingLayerMask);
            renderer.sortingLayerID = data.sortingLayerId;
            renderer.sortingOrder = data.sortingOrder;

            var spriteRenderer = renderer as SpriteRenderer;
            if (spriteRenderer != null && data.type == "SpriteRenderer")
            {
                spriteRenderer.color = ToColor(data.color, Color.white);
                spriteRenderer.flipX = data.flipX;
                spriteRenderer.flipY = data.flipY;
                spriteRenderer.drawMode = (SpriteDrawMode)Mathf.Clamp(data.drawMode, 0, 2);
                if (data.size != null && data.size.Length >= 2 && spriteRenderer.drawMode != SpriteDrawMode.Simple)
                    spriteRenderer.size = new Vector2(data.size[0], data.size[1]);
                spriteRenderer.tileMode = (SpriteTileMode)Mathf.Clamp(data.spriteTileMode, 0, 1);
                spriteRenderer.maskInteraction = (SpriteMaskInteraction)Mathf.Clamp(data.maskInteraction, 0, 2);
                spriteRenderer.spriteSortPoint = (SpriteSortPoint)Mathf.Clamp(data.spriteSortPoint, 0, 1);
            }
        }

        private static void RestoreCanvasCamera(GameObject go, CanvasData data, Dictionary<int, GameObject> objectsById)
        {
            if (go == null || data == null || data.worldCameraObject == 0)
                return;
            if (go.GetComponent<Canvas>() == null)
                return;
            if (objectsById.TryGetValue(data.worldCameraObject, out var cameraObject))
                go.GetComponent<Canvas>().worldCamera = cameraObject.GetComponent<Camera>();
        }

        private static void RestoreCharacterJoint(GameObject go, CharacterJointData data, Dictionary<int, GameObject> objectsById)
        {
            if (go == null || data == null)
                return;
            var joint = go.GetComponent<CharacterJoint>() ?? go.AddComponent<CharacterJoint>();
            joint.anchor = ToVector3(data.anchor, Vector3.zero);
            joint.axis = ToVector3(data.axis, Vector3.right);
            joint.swingAxis = ToVector3(data.swingAxis, Vector3.up);
            joint.autoConfigureConnectedAnchor = data.autoConfigureConnectedAnchor;
            joint.connectedAnchor = ToVector3(data.connectedAnchor, Vector3.zero);
            joint.enableCollision = data.enableCollision;
            joint.breakForce = Mathf.Max(0.0f, data.breakForce);
            joint.breakTorque = Mathf.Max(0.0f, data.breakTorque);
            joint.massScale = Mathf.Max(0.0001f, data.massScale);
            joint.connectedMassScale = Mathf.Max(0.0001f, data.connectedMassScale);
            if (data.connectedBodyObject != 0 && objectsById.TryGetValue(data.connectedBodyObject, out var connectedObject))
                joint.connectedBody = connectedObject.GetComponent<Rigidbody>();
        }

        private static Vector3 ToVector3(float[] value, Vector3 fallback)
        {
            if (value == null || value.Length < 3)
                return fallback;
            return new Vector3(value[0], value[1], value[2]);
        }

        private static Color ToColor(float[] value, Color fallback)
        {
            if (value == null || value.Length < 4)
                return fallback;
            return new Color(value[0], value[1], value[2], value[3]);
        }

        private static Material[] ResolveMaterials(
            string[] ids,
            Dictionary<string, Material> materials,
            int submeshCount,
            Material fallback)
        {
            var count = Math.Max(1, submeshCount);
            var result = new Material[count];
            for (var i = 0; i < count; i++)
            {
                Material material = null;
                if (ids != null && ids.Length > 0)
                {
                    var id = ids[Math.Min(i, ids.Length - 1)];
                    if (!string.IsNullOrEmpty(id))
                        materials.TryGetValue(id, out material);
                }
                result[i] = material != null ? material : fallback;
            }
            return result;
        }

        private static Material GetDefaultMaterial()
        {
            const string assetPath = MaterialOutputPath + "/RecoveredDefault.mat";
            var existing = AssetDatabase.LoadAssetAtPath<Material>(assetPath);
            if (existing != null)
                return existing;
            var shader = Shader.Find("Standard") ?? Shader.Find("Unlit/Color");
            if (shader == null)
                throw new InvalidOperationException("Could not find a shader for the recovered default material.");
            var material = new Material(shader) { name = "Recovered default material" };
            AssetDatabase.CreateAsset(material, assetPath);
            AssetDatabase.SaveAssets();
            return material;
        }

        private static T GetOrAdd<T>(GameObject go) where T : Component
        {
            return go.GetComponent<T>() ?? go.AddComponent<T>();
        }

        private static bool Contains(string[] array, string value)
        {
            return array != null && Array.IndexOf(array, value) >= 0;
        }

        private static string ToAbsoluteAssetPath(string assetPath)
        {
            var normalized = assetPath.Replace('/', Path.DirectorySeparatorChar);
            var projectRoot = Directory.GetParent(Application.dataPath).FullName;
            return Path.GetFullPath(Path.Combine(projectRoot, normalized));
        }

        [Serializable]
        private class UiPrefabManifest
        {
            public PrefabData[] prefabs;
        }

        [Serializable]
        private class PrefabData
        {
            public string id;
            public string name;
            public string sourceFile;
            public int sourcePathId;
            public int objectCount;
            public SceneObject[] objects;
        }

        [Serializable]
        private class SceneManifest
        {
            public int formatVersion;
            public string source;
            public string unityVersion;
            public SceneData[] scenes;
        }

        [Serializable]
        private class SceneData
        {
            public string key;
            public string name;
            public string buildScene;
            public int objectCount;
            public SceneObject[] objects;
        }

        [Serializable]
        private class SceneObject
        {
            public int id;
            public string name;
            public bool active;
            public int layer;
            public string tag;
            public int parent;
            public TransformData transform;
            public string[] components;
            public string[] scripts;
            public string[] meshes;
            public string[] materials;
            public string sprite;
            public string text;
            public bool uiImage;
            public bool uiText;
            public bool uiButton;
            public ButtonData uiButtonData;
            public bool uiCanvas;
            public ImageData uiImageData;
            public TextData uiTextData;
            public EffectData[] uiEffects;
            public CanvasScalerData canvasScaler;
            public CanvasData canvas;
            public CanvasGroupData canvasGroup;
            public RendererData[] renderers;
            public CameraData camera;
            public LightData light;
            public string audioClip;
            public AudioSourceData audioSource;
            public ColliderData[] colliders;
            public RigidbodyData rigidbody;
            public CharacterJointData characterJoint;
            public NavMeshAgentData navMeshAgent;
            public NavMeshObstacleData navMeshObstacle;
        }

        [Serializable]
        private class TransformData
        {
            public string kind;
            public float[] position;
            public float[] rotation;
            public float[] scale;
            public float[] anchorMin;
            public float[] anchorMax;
            public float[] anchoredPosition;
            public float[] sizeDelta;
            public float[] pivot;
        }

        [Serializable]
        private class ImageData
        {
            public float[] color;
            public bool raycastTarget;
            public float[] raycastPadding;
            public bool maskable;
            public int type;
            public bool preserveAspect;
            public bool fillCenter;
            public int fillMethod;
            public float fillAmount;
            public bool fillClockwise;
            public int fillOrigin;
            public bool useSpriteMesh;
            public float pixelsPerUnitMultiplier;
        }

        [Serializable]
        private class TextData
        {
            public string fontId;
            public float[] color;
            public bool raycastTarget;
            public float[] raycastPadding;
            public bool maskable;
            public int fontSize;
            public int fontStyle;
            public bool bestFit;
            public int minSize;
            public int maxSize;
            public int alignment;
            public bool alignByGeometry;
            public bool richText;
            public int horizontalOverflow;
            public int verticalOverflow;
            public float lineSpacing;
        }

        [Serializable]
        private class ButtonData
        {
            public bool enabled;
            public bool interactable;
            public int transition;
            public NavigationData navigation;
            public ColorBlockData colors;
            public SpriteStateData sprites;
            public AnimationTriggerData animationTriggers;
            public bool targetGraphicPresent;
            public int targetGraphicObject;
            public int persistentCallCount;
            public PersistentCallData[] persistentCalls;
            public bool persistentCallsDecoded;
        }

        [Serializable]
        private class PersistentCallData
        {
            public string targetType;
            public int targetObjectId;
            public string targetScript;
            public string targetAssemblyTypeName;
            public string methodName;
            public int mode;
            public int intArgument;
            public float floatArgument;
            public string stringArgument;
            public bool boolArgument;
            public int callState;
        }

        [Serializable]
        private class NavigationData
        {
            public int mode;
            public bool wrapAround;
            public int selectOnUpObject;
            public int selectOnDownObject;
            public int selectOnLeftObject;
            public int selectOnRightObject;
        }

        [Serializable]
        private class ColorBlockData
        {
            public float[] normal;
            public float[] highlighted;
            public float[] pressed;
            public float[] selected;
            public float[] disabled;
            public float colorMultiplier;
            public float fadeDuration;
        }

        [Serializable]
        private class SpriteStateData
        {
            public string highlighted;
            public string pressed;
            public string selected;
            public string disabled;
        }

        [Serializable]
        private class AnimationTriggerData
        {
            public string normal;
            public string highlighted;
            public string pressed;
            public string selected;
            public string disabled;
        }

        [Serializable]
        private class EffectData
        {
            public string type;
            public bool enabled;
            public float[] color;
            public float[] distance;
            public bool useGraphicAlpha;
        }

        [Serializable]
        private class CanvasScalerData
        {
            public int uiScaleMode;
            public float referencePixelsPerUnit;
            public float scaleFactor;
            public float[] referenceResolution;
            public int screenMatchMode;
            public float matchWidthOrHeight;
            public int physicalUnit;
            public float fallbackScreenDPI;
            public float defaultSpriteDPI;
            public float dynamicPixelsPerUnit;
            public bool presetInfoIsWorld;
        }

        [Serializable]
        private class CanvasData
        {
            public bool enabled;
            public int renderMode;
            public int worldCameraObject;
            public float planeDistance;
            public bool pixelPerfect;
            public bool receivesEvents;
            public bool overrideSorting;
            public int sortingLayerId;
            public int sortingOrder;
            public int targetDisplay;
        }

        [Serializable]
        private class CanvasGroupData
        {
            public bool enabled;
            public float alpha;
            public bool interactable;
            public bool blocksRaycasts;
            public bool ignoreParentGroups;
        }

        [Serializable]
        private class RendererData
        {
            public string type;
            public bool enabled;
            public int castShadows;
            public bool receiveShadows;
            public int motionVectors;
            public int lightProbeUsage;
            public int reflectionProbeUsage;
            public int renderingLayerMask;
            public int sortingLayerId;
            public int sortingOrder;
            public float[] color;
            public bool flipX;
            public bool flipY;
            public int drawMode;
            public float[] size;
            public int spriteTileMode;
            public int maskInteraction;
            public int spriteSortPoint;
            public string meshId;
            public int rootBoneFileId;
            public int rootBonePathId;
            public int rootBoneObject;
            public int[] boneFileIds;
            public int[] bonePathIds;
            public int[] boneObjects;
            public int boneCount;
            public int quality;
            public bool updateWhenOffscreen;
            public bool skinnedMotionVectors;
            public float[] localBoundsCenter;
            public float[] localBoundsExtents;
        }

        [Serializable]
        private class CameraData
        {
            public bool enabled;
            public bool orthographic;
            public float fieldOfView;
            public float nearClip;
            public float farClip;
            public float orthographicSize;
            public int clearFlags;
            public float[] backgroundColor;
            public float[] viewportRect;
            public float depth;
            public int cullingMask;
            public bool allowHDR;
            public bool allowMSAA;
            public bool useOcclusionCulling;
            public int renderingPath;
        }

        [Serializable]
        private class LightData
        {
            public bool enabled;
            public int type;
            public float[] color;
            public float intensity;
            public float range;
            public float spotAngle;
            public float innerSpotAngle;
            public int shadows;
            public float shadowStrength;
            public float shadowBias;
            public float shadowNormalBias;
            public bool drawHalo;
            public float bounceIntensity;
            public bool useColorTemperature;
            public float colorTemperature;
            public float[] areaSize;
        }

        [Serializable]
        private class FontManifest
        {
            public FontEntry[] fonts;
        }

        [Serializable]
        private class FontEntry
        {
            public string id;
            public string name;
            public string assetPath;
            public bool referencedByUiText;
            public bool exported;
        }

        [Serializable]
        private class AudioClipManifest
        {
            public AudioClipEntry[] audioClips;
        }

        [Serializable]
        private class AudioClipEntry
        {
            public string id;
            public string assetPath;
            public bool exported;
        }

        [Serializable]
        private class AudioSourceData
        {
            public bool enabled;
            public string clip;
            public bool playOnAwake;
            public bool loop;
            public float volume;
            public float pitch;
            public int priority;
            public float minDistance;
            public float maxDistance;
        }

        [Serializable]
        private class ColliderData
        {
            public string type;
            public bool enabled;
            public bool isTrigger;
            public float[] center;
            public float[] size;
            public float radius;
            public float height;
            public int direction;
            public bool convex;
            public string mesh;
        }

        [Serializable]
        private class RigidbodyData
        {
            public float mass;
            public float drag;
            public float angularDrag;
            public bool useGravity;
            public bool isKinematic;
            public int interpolation;
            public int constraints;
            public int collisionDetection;
            public bool enabled;
        }

        [Serializable]
        private class CharacterJointData
        {
            public int connectedBodyObject;
            public float[] anchor;
            public float[] axis;
            public float[] swingAxis;
            public float[] connectedAnchor;
            public bool autoConfigureConnectedAnchor;
            public bool enableCollision;
            public float breakForce;
            public float breakTorque;
            public float massScale;
            public float connectedMassScale;
        }

        [Serializable]
        private class NavMeshAgentData
        {
            public bool enabled;
            public float radius;
            public float height;
            public float speed;
            public float acceleration;
            public float angularSpeed;
            public float stoppingDistance;
            public float baseOffset;
            public int avoidancePriority;
            public bool autoBraking;
            public bool autoRepath;
        }

        [Serializable]
        private class NavMeshObstacleData
        {
            public bool enabled;
            public float radius;
            public float height;
            public bool carving;
        }

        [Serializable]
        private class MaterialManifest
        {
            public MaterialEntry[] materials;
        }

        [Serializable]
        private class MaterialEntry
        {
            public string id;
            public string name;
            public string shaderName;
            public ColorEntry[] colors;
            public FloatEntry[] floats;
            public TextureEntry[] textures;
        }

        [Serializable]
        private class ColorEntry
        {
            public string property;
            public float[] value;
        }

        [Serializable]
        private class FloatEntry
        {
            public string property;
            public float value;
        }

        [Serializable]
        private class TextureEntry
        {
            public string property;
            public string textureId;
            public float[] scale;
            public float[] offset;
        }

        [Serializable]
        private class TextureManifest
        {
            public TextureEntryInfo[] textures;
        }

        [Serializable]
        private class TextureEntryInfo
        {
            public string id;
            public string name;
            public string type;
            public string assetPath;
            public int width;
            public int height;
        }

        [Serializable]
        private class SpriteManifest
        {
            public SpriteEntry[] sprites;
        }

        [Serializable]
        private class SpriteEntry
        {
            public string id;
            public string name;
            public string assetPath;
            public int width;
            public int height;
            public float[] pivot;
            public float pixelsPerUnit;
            public float[] originalRect;
        }

        [Serializable]
        private class MeshManifest
        {
            public string archive;
            public MeshEntry[] meshes;
        }

        [Serializable]
        private class MeshEntry
        {
            public string id;
            public string name;
            public string sourceFile;
            public long sourcePathId;
            public string objEntry;
            public string assetPath;
            public int submeshes;
            public bool exported;
        }

        [Serializable]
        private class MeshSkinManifest
        {
            public int formatVersion;
            public MeshSkinData[] meshes;
        }

        [Serializable]
        private class MeshSkinData
        {
            public string id;
            public string meshId;
            public int vertexCount;
            public int bindPoseCount;
            public BindPoseData[] bindPoses;
            public int[] boneIndices;
            public float[] boneWeights;
            public MeshGeometryData geometry;
        }

        [Serializable]
        private class BindPoseData
        {
            public float e00; public float e01; public float e02; public float e03;
            public float e10; public float e11; public float e12; public float e13;
            public float e20; public float e21; public float e22; public float e23;
            public float e30; public float e31; public float e32; public float e33;
        }

        [Serializable]
        private class MeshGeometryData
        {
            public int vertexCount;
            public float[] vertices;
            public float[] normals;
            public float[] tangents;
            public float[] colors;
            public MeshUvChannelData[] uvChannels;
            public MeshSubmeshData[] submeshes;
        }

        [Serializable]
        private class MeshUvChannelData
        {
            public int channel;
            public int dimension;
            public float[] values;
        }

        [Serializable]
        private class MeshSubmeshData
        {
            public string topology;
            public int[] indices;
        }

        private sealed class SkinRendererBuildSummary
        {
            public int skinnedRendererCount;
            public int staticFallbackCount;
            public readonly HashSet<string> staticFallbackMeshIds = new HashSet<string>(StringComparer.Ordinal);
        }
    }
}
#endif
