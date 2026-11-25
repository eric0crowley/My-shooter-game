# `PostProcessingBehaviour` — TypeDefIndex 3601

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `PostProcessingProfile` | `profile` |
| `0x28` | `Func<Vector2, Matrix4x4>` | `jitteredMatrixFunc` |
| `0x30` | `Dictionary<Type, KeyValuePair<CameraEvent, CommandBuffer>>` | `m_CommandBuffers` |
| `0x38` | `List<PostProcessingComponentBase>` | `m_Components` |
| `0x40` | `Dictionary<PostProcessingComponentBase, bool>` | `m_ComponentStates` |
| `0x48` | `MaterialFactory` | `m_MaterialFactory` |
| `0x50` | `RenderTextureFactory` | `m_RenderTextureFactory` |
| `0x58` | `PostProcessingContext` | `m_Context` |
| `0x60` | `Camera` | `m_Camera` |
| `0x68` | `PostProcessingProfile` | `m_PreviousProfile` |
| `0x70` | `bool` | `m_RenderingInSceneView` |
| `0x78` | `BuiltinDebugViewsComponent` | `m_DebugViews` |
| `0x80` | `AmbientOcclusionComponent` | `m_AmbientOcclusion` |
| `0x88` | `ScreenSpaceReflectionComponent` | `m_ScreenSpaceReflection` |
| `0x90` | `FogComponent` | `m_FogComponent` |
| `0x98` | `MotionBlurComponent` | `m_MotionBlur` |
| `0xA0` | `TaaComponent` | `m_Taa` |
| `0xA8` | `EyeAdaptationComponent` | `m_EyeAdaptation` |
| `0xB0` | `DepthOfFieldComponent` | `m_DepthOfField` |
| `0xB8` | `BloomComponent` | `m_Bloom` |
| `0xC0` | `ChromaticAberrationComponent` | `m_ChromaticAberration` |
| `0xC8` | `ColorGradingComponent` | `m_ColorGrading` |
| `0xD0` | `UserLutComponent` | `m_UserLut` |
| `0xD8` | `GrainComponent` | `m_Grain` |
| `0xE0` | `VignetteComponent` | `m_Vignette` |
| `0xE8` | `DitheringComponent` | `m_Dithering` |
| `0xF0` | `FxaaComponent` | `m_Fxaa` |
| `0xF8` | `List<PostProcessingComponentBase>` | `m_ComponentsToEnable` |
| `0x100` | `List<PostProcessingComponentBase>` | `m_ComponentsToDisable` |

## `PostProcessingBehaviour.OnEnable` — RVA `0xcdc3bc`

- Lift status: **exact**; input span: 2204 bytes; span to next metadata RVA: 2204 bytes.
- Metadata signature: `private void OnEnable() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=365 (informational only).

```csharp
public static ulong PostProcessingBehaviour_OnEnable_RVAcdc3bc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13487096 = default(uint);
        uint __arm64_flags_right_13487096 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x25 = default(ulong);
        ulong x26 = default(ulong);
        ulong x27 = default(ulong);
        ulong x28 = default(ulong);
        ulong x29 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x80UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x28);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x27);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))), x19);
        x29 = 0x1BAB000UL;
        x28 = 0x1A8F000UL;
        x20 = 0x1A8F000UL;
        x27 = 0x1A8F000UL;
        x26 = 0x1A8F000UL;
        x25 = 0x1A8F000UL;
        x24 = 0x1A8F000UL;
        x21 = 0x1A8F000UL;
        x23 = 0x1A8F000UL;
        x22 = 0x1A8F000UL;
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((x28) + (0x508UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x510UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((x27) + (0x518UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x26) + (0x520UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0x528UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x530UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x538UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x540UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x548UL))));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x29) + (0x616UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDC660;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x550UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x558UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x540UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x560UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x568UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x570UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x578UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x580UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x510UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x588UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x508UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x590UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x598UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x5A0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x5A8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x60UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x5B0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x5B8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x5C0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x5C8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x538UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x530UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x518UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x5D0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x5D8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x5E0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x548UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x5E8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x5F0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x5F8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x600UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x608UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x610UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x618UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x620UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x628UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x630UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x638UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x640UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x648UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x528UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x520UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x650UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x658UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x660UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x668UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x29) + (0x616UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCDC660;
        label_0xCDC660:
        ;
        x0 = RuntimeMemory.ReadU64(x28);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x8UL)))) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x8UL)))) + (0x8UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x18UL))), 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x20);
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xEA53CCUL, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x30UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x27);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCDF364UL /* metadata target: MaterialFactory.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x48UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x26);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCDF6B8UL /* metadata target: RenderTextureFactory.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x50UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x25);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCDE534UL /* metadata target: PostProcessingContext.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x58UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x24);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x21);
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x10A2B64UL, x0, x1, x2, x3);
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x38UL))), x21);
        x0 = x20;
        x1 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x23);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCD0464UL /* metadata target: BuiltinDebugViewsComponent.ctor */, x0, x1, x2, x3);
        x2 = RuntimeMemory.ReadU64(x22);
        x0 = x19;
        x1 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xD2B1ACUL, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x78UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x550UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCCE4F8UL /* metadata target: AmbientOcclusionComponent.ctor */, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5D8UL))));
        x0 = x19;
        x1 = x21;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xD2B1ACUL, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x80UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x650UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCD8E44UL /* metadata target: ScreenSpaceReflectionComponent.ctor */, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x630UL))));
        x0 = x19;
        x1 = x21;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xD2B1ACUL, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x88UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5B0UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCD4C14UL /* metadata target: FogComponent.ctor */, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x610UL))));
        x0 = x19;
        x1 = x21;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xD2B1ACUL, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x90UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5D0UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCD6F68UL /* metadata target: MotionBlurComponent.ctor */, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x628UL))));
        x0 = x19;
        x1 = x21;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xD2B1ACUL, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x98UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x658UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCDA388UL /* metadata target: TaaComponent.ctor */, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x638UL))));
        x0 = x19;
        x1 = x21;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xD2B1ACUL, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0xA0UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x60UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCD44E4UL /* metadata target: EyeAdaptationComponent.ctor */, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x608UL))));
        x0 = x19;
        x1 = x21;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xD2B1ACUL, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0xA8UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x570UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCD300CUL /* metadata target: DepthOfFieldComponent.ctor */, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5F8UL))));
        x0 = x19;
        x1 = x21;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xD2B1ACUL, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0xB0UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x558UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCCF220UL /* metadata target: BloomComponent.ctor */, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5E0UL))));
        x0 = x19;
        x1 = x21;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xD2B1ACUL, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0xB8UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x560UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCD097CUL /* metadata target: ChromaticAberrationComponent.ctor */, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5E8UL))));
        x0 = x19;
        x1 = x21;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xD2B1ACUL, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0xC0UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x568UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCD2178UL /* metadata target: ColorGradingComponent.ctor */, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5F0UL))));
        x0 = x19;
        x1 = x21;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xD2B1ACUL, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0xC8UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x660UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCDA878UL /* metadata target: UserLutComponent.ctor */, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x640UL))));
        x0 = x19;
        x1 = x21;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xD2B1ACUL, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0xD0UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5C0UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCD5524UL /* metadata target: GrainComponent.ctor */, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x620UL))));
        x0 = x19;
        x1 = x21;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xD2B1ACUL, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0xD8UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x668UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCDAC54UL /* metadata target: VignetteComponent.ctor */, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x648UL))));
        x0 = x19;
        x1 = x21;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xD2B1ACUL, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0xE0UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x590UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCD35ACUL /* metadata target: DitheringComponent.ctor */, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x600UL))));
        x0 = x19;
        x1 = x21;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xD2B1ACUL, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0xE8UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5B8UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCD4FF4UL /* metadata target: FxaaComponent.ctor */, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x618UL))));
        x0 = x19;
        x1 = x21;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xD2B1ACUL, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0xF0UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x588UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x580UL))));
        x22 = x0;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xEA78F8UL, x0, x1, x2, x3);
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x40UL))), x22);
        x0 = x21;
        x1 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xCDCBE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5C8UL))));
        x20 = 0x1A8F000UL;
        x23 = 0x1A8F000UL;
        x22 = 0x1A8F000UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x5A0UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x578UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x598UL))));
        x0 = RuntimeCalls.InvokeDirect(0x10A3CF0UL, x0, x1, x2, x3);
        goto label_0xCDCB7C;
        label_0xCDCB7C:
        ;
        x1 = RuntimeMemory.ReadU64(x20);
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        x0 = RuntimeCalls.InvokeDirect(0xF0EA88UL, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDCBA8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x21);
        if ((x0 == 0x0UL))
        {
            goto label_0xCDCBE4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x18UL))));
        x3 = RuntimeMemory.ReadU64(x23);
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xEA7BECUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCDCB7C;
        label_0xCDCBA8:
        ;
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        x0 = RuntimeCalls.InvokeDirect(0xF0EA84UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCDCBB4;
        label_0xCDCBB4:
        ;
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179619CUL /* metadata target: MonoBehaviour.set_useGUILayout */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        return x0;
        label_0xCDCBE4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCDCBE8;
        label_0xCDCBE8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCDCBF4;
        label_0xCDCBF4:
        ;
        x20 = x0;
        __arm64_flags_left_13487096 = unchecked((uint)(x1));
        __arm64_flags_right_13487096 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13487096) - (__arm64_flags_right_13487096))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCDCC28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C00UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x21 = RuntimeMemory.ReadU64(x0);
        x0 = RuntimeCalls.InvokeDirect(0x19B0C10UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        x0 = RuntimeCalls.InvokeDirect(0xF0EA84UL, x0, x1, x2, x3);
        if ((x21 == 0x0UL))
        {
            goto label_0xCDCBB4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB1BD40UL, x0, x1, x2, x3);
        goto label_0xCDCC28;
        label_0xCDCC28:
        ;
        x21 = 0x0UL;
        goto label_0xCDCC34;
        label_0xCDCC34:
        ;
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        x0 = RuntimeCalls.InvokeDirect(0xF0EA84UL, x0, x1, x2, x3);
        if ((x21 != 0x0UL))
        {
            goto label_0xCDCC4C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC26098UL, x0, x1, x2, x3);
        goto label_0xCDCC4C;
        label_0xCDCC4C:
        ;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB1BD40UL, x0, x1, x2, x3);
        x0 = RuntimeCalls.InvokeDirect(0xA29990UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `PostProcessingBehaviour.OnPreCull` — RVA `0xcdcc58`

- Lift status: **exact**; input span: 1428 bytes; span to next metadata RVA: 1428 bytes.
- Metadata signature: `private void OnPreCull() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=220 (informational only).

```csharp
public static ulong PostProcessingBehaviour_OnPreCull_RVAcdcc58(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13488420 = default(uint);
        uint __arm64_flags_left_13488440 = default(uint);
        uint __arm64_flags_left_13488508 = default(uint);
        uint __arm64_flags_result_13488440 = default(uint);
        uint __arm64_flags_right_13488420 = default(uint);
        uint __arm64_flags_right_13488440 = default(uint);
        uint __arm64_flags_right_13488508 = default(uint);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x70UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x20 = 0x1A8D000UL;
        x23 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x617UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x170UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xD8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDCCD8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x170UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x598UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x5A0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x5A8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x5C8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x617UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCDCCD8;
        label_0xCDCCD8:
        ;
        x1 = RuntimeMemory.ReadU64(x20);
        x0 = x19;
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x30UL))), 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x60UL))), x0);
        x1 = x0;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x23);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xFFFFFFFFFFFFFFC0UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDCD14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDCD10UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCDCD14;
        label_0xCDCD14:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDD150;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x23);
        x20 = RuntimeMemory.ReadU64(x20);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDCD3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDCD38UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCDCD3C;
        label_0xCDCD3C:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDD150;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE448UL /* metadata target: PostProcessingContext.Reset */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x21 = x0;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x10UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x50UL))));
        x0 = x21;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x28UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x48UL))));
        x0 = x21;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x20UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x60UL))));
        x20 = x21;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x18UL))), x1);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x78UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        x1 = x21;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x1C8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x9) + (0x1C8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x80UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x30UL))));
        x1 = x21;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x1C8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x9) + (0x1C8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x88UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x38UL))));
        x1 = x21;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x1C8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x9) + (0x1C8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x90UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x1 = x21;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x1C8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x9) + (0x1C8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x98UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x48UL))));
        x1 = x21;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x1C8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x9) + (0x1C8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        x1 = x21;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x1C8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x9) + (0x1C8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x50UL))));
        x1 = x21;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x1C8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x9) + (0x1C8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x1 = x21;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x1C8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x9) + (0x1C8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x58UL))));
        x1 = x21;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x1C8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x9) + (0x1C8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x70UL))));
        x1 = x21;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x1C8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x9) + (0x1C8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x60UL))));
        x1 = x21;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x1C8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x9) + (0x1C8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x68UL))));
        x1 = x21;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x1C8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x9) + (0x1C8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x78UL))));
        x1 = x21;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x1C8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x9) + (0x1C8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x80UL))));
        x1 = x21;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x1C8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x9) + (0x1C8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x88UL))));
        x1 = x21;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x1C8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x9) + (0x1C8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        x1 = x21;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x1C8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x9) + (0x1C8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x21 = x19;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x68UL))));
        x0 = RuntimeMemory.ReadU64(x23);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xFFFFFFFFFFFFFFB8UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDD004;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDD000UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCDD004;
        label_0xCDD004:
        ;
        x0 = x22;
        x1 = x23;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDD030;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xCDD1ECUL /* metadata target: PostProcessingBehaviour.DisableComponents */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x0 = x21;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x68UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xCDD030;
        label_0xCDD030:
        ;
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xCDD360UL /* metadata target: PostProcessingBehaviour.CheckObservers */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176ED24UL /* metadata target: Camera.get_depthTextureMode */, x0, x1, x2, x3);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x38UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5C8UL))));
        x21 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x9;
        x1 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)((sp) + (0x8UL)));
        x0 = RuntimeCalls.InvokeDirect(0x10A3CF0UL, x0, x1, x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x8UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x8UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x18UL))));
        x23 = 0x1A8F000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x20UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x20UL))), v0);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x30UL))), x8);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x5A0UL))));
        goto label_0xCDD084;
        label_0xCDD084:
        ;
        x1 = RuntimeMemory.ReadU64(x23);
        x0 = unchecked((ulong)((sp) + (0x20UL)));
        x0 = RuntimeCalls.InvokeDirect(0xF0EA88UL, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDD0C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        if ((x22 == 0x0UL))
        {
            goto label_0xCDD168;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x22);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x188UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x188UL)))) + (0x8UL))));
        x0 = x22;
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDD084;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x22);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x178UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x178UL)))) + (0x8UL))));
        x0 = x22;
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) | (unchecked((uint)(x21)))))));
        goto label_0xCDD084;
        label_0xCDD0C8:
        ;
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x598UL))));
        x0 = unchecked((ulong)((sp) + (0x20UL)));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xF0EA84UL, x0, x1, x2, x3);
        goto label_0xCDD0DC;
        label_0xCDD0DC:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176ED60UL /* metadata target: Camera.set_depthTextureMode */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x70UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDD150;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x188UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x188UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDD150;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x14UL))))));
        __arm64_flags_left_13488420 = unchecked((uint)(x8));
        __arm64_flags_right_13488420 = unchecked((uint)0x9UL);
        if (((__arm64_flags_left_13488420 >= __arm64_flags_right_13488420) && (!((unchecked((uint)((__arm64_flags_left_13488420) - (__arm64_flags_right_13488420))) == unchecked((uint)0x0UL))))))
        {
            goto label_0xCDD150;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(x8)))))))));
        x9 = unchecked((ulong)(unchecked((uint)(0x3A1UL))));
        __arm64_flags_left_13488440 = unchecked((uint)(x8));
        __arm64_flags_right_13488440 = unchecked((uint)(x9));
        __arm64_flags_result_13488440 = unchecked((uint)((__arm64_flags_left_13488440) & (__arm64_flags_right_13488440)));
        if ((__arm64_flags_result_13488440 == unchecked((uint)0x0UL)))
        {
            goto label_0xCDD150;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDD164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        x0 = RuntimeCalls.InvokeDirect(0xCD95E4UL /* metadata target: TaaComponent.SetProjectionMatrix */, x0, x1, x2, x3);
        goto label_0xCDD150;
        label_0xCDD150:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        sp = unchecked((ulong)((sp) + (0x70UL)));
        return x0;
        label_0xCDD164:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xCDD168;
        label_0xCDD168:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xCDD178;
        label_0xCDD178:
        ;
        x22 = x0;
        __arm64_flags_left_13488508 = unchecked((uint)(x1));
        __arm64_flags_right_13488508 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13488508) - (__arm64_flags_right_13488508))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCDD1B4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C00UL, x0, x1, x2, x3);
        x23 = RuntimeMemory.ReadU64(x0);
        x0 = RuntimeCalls.InvokeDirect(0x19B0C10UL, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x598UL))));
        x0 = unchecked((ulong)((sp) + (0x20UL)));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xF0EA84UL, x0, x1, x2, x3);
        if ((x23 == 0x0UL))
        {
            goto label_0xCDD0DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x23;
        x0 = RuntimeCalls.InvokeDirect(0xB1BD40UL, x0, x1, x2, x3);
        goto label_0xCDD1B4;
        label_0xCDD1B4:
        ;
        x23 = 0x0UL;
        goto label_0xCDD1C0;
        label_0xCDD1C0:
        ;
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x598UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = unchecked((ulong)((sp) + (0x20UL)));
        x0 = RuntimeCalls.InvokeDirect(0xF0EA84UL, x0, x1, x2, x3);
        if ((x23 != 0x0UL))
        {
            goto label_0xCDD1E0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xC26098UL, x0, x1, x2, x3);
        goto label_0xCDD1E0;
        label_0xCDD1E0:
        ;
        x0 = x23;
        x0 = RuntimeCalls.InvokeDirect(0xB1BD40UL, x0, x1, x2, x3);
        x0 = RuntimeCalls.InvokeDirect(0xA29990UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `PostProcessingBehaviour.DisableComponents` — RVA `0xcdd1ec`

- Lift status: **exact**; input span: 372 bytes; span to next metadata RVA: 372 bytes.
- Metadata signature: `private void DisableComponents() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=55 (informational only).

```csharp
public static ulong PostProcessingBehaviour_DisableComponents_RVAcdd1ec(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13488880 = default(uint);
        uint __arm64_flags_right_13488880 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x40UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x61EUL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDD240;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x598UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x5A0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x5A8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x5C8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x61EUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCDD240;
        label_0xCDD240:
        ;
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x8UL)))) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x8UL)))) + (0x8UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x18UL))), 0x0UL);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x38UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDD2DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5C8UL))));
        x21 = 0x1A8F000UL;
        x20 = 0x1A8F000UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x5A0UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x598UL))));
        x8 = unchecked((ulong)((sp) + (0x8UL)));
        x0 = RuntimeCalls.InvokeDirect(0x10A3CF0UL, x0, x1, x2, x3);
        goto label_0xCDD274;
        label_0xCDD274:
        ;
        x1 = RuntimeMemory.ReadU64(x21);
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        x0 = RuntimeCalls.InvokeDirect(0xF0EA88UL, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDD2BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x18UL))));
        if ((x19 == 0x0UL))
        {
            goto label_0xCDD2D8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x19);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1B8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1B8UL)))) + (0x8UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCDD274;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDD274;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x19);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1A8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1A8UL)))) + (0x8UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        goto label_0xCDD274;
        label_0xCDD2BC:
        ;
        x1 = RuntimeMemory.ReadU64(x20);
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        x0 = RuntimeCalls.InvokeDirect(0xF0EA84UL, x0, x1, x2, x3);
        goto label_0xCDD2C8;
        label_0xCDD2C8:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        sp = unchecked((ulong)((sp) + (0x40UL)));
        return x0;
        label_0xCDD2D8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xCDD2DC;
        label_0xCDD2DC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xCDD2EC;
        label_0xCDD2EC:
        ;
        x19 = x0;
        __arm64_flags_left_13488880 = unchecked((uint)(x1));
        __arm64_flags_right_13488880 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13488880) - (__arm64_flags_right_13488880))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCDD328;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C00UL, x0, x1, x2, x3);
        x20 = RuntimeMemory.ReadU64(x0);
        x0 = RuntimeCalls.InvokeDirect(0x19B0C10UL, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x598UL))));
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xF0EA84UL, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCDD2C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB1BD40UL, x0, x1, x2, x3);
        goto label_0xCDD328;
        label_0xCDD328:
        ;
        x20 = 0x0UL;
        goto label_0xCDD334;
        label_0xCDD334:
        ;
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x598UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        x0 = RuntimeCalls.InvokeDirect(0xF0EA84UL, x0, x1, x2, x3);
        if ((x20 != 0x0UL))
        {
            goto label_0xCDD354;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC26098UL, x0, x1, x2, x3);
        goto label_0xCDD354;
        label_0xCDD354:
        ;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB1BD40UL, x0, x1, x2, x3);
        x0 = RuntimeCalls.InvokeDirect(0xA29990UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `PostProcessingBehaviour.CheckObservers` — RVA `0xcdd360`

- Lift status: **partial**; input span: 1056 bytes; span to next metadata RVA: 1056 bytes.
- Metadata signature: `private void CheckObservers() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=152 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.lt' at 0xcdd68c; reason: Unknown IR expression at 0xcdd68c; reason: Unsupported instruction 'b.lt' at 0xcdd6b8; reason: Unknown IR expression at 0xcdd6b8

```csharp
public static ulong PostProcessingBehaviour_CheckObservers_RVAcdd360(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13489324 = default(uint);
        uint __arm64_flags_left_13489332 = default(uint);
        uint __arm64_flags_left_13489392 = default(uint);
        uint __arm64_flags_left_13489472 = default(uint);
        uint __arm64_flags_left_13489588 = default(uint);
        uint __arm64_flags_left_13489692 = default(uint);
        uint __arm64_flags_left_13489796 = default(uint);
        uint __arm64_flags_left_13489840 = default(uint);
        uint __arm64_flags_left_13489952 = default(uint);
        uint __arm64_flags_result_13489332 = default(uint);
        uint __arm64_flags_right_13489324 = default(uint);
        uint __arm64_flags_right_13489332 = default(uint);
        uint __arm64_flags_right_13489392 = default(uint);
        uint __arm64_flags_right_13489472 = default(uint);
        uint __arm64_flags_right_13489588 = default(uint);
        uint __arm64_flags_right_13489692 = default(uint);
        uint __arm64_flags_right_13489796 = default(uint);
        uint __arm64_flags_right_13489840 = default(uint);
        uint __arm64_flags_right_13489952 = default(uint);
        ulong __arm64_pair_address_13489180 = default(ulong);
        ulong __arm64_pair_address_13489264 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x25 = default(ulong);
        ulong x26 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xB0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x60UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x61DUL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDD414;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x670UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x678UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x680UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x688UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x690UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x698UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x6A0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x6A8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x6B0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x6B8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x6C0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x61DUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCDD414;
        label_0xCDD414:
        ;
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x50UL))), 0x0UL);
        __arm64_pair_address_13489180 = unchecked((ulong)((sp) + (0x30UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13489180, v0);
#else
        __WriteVector128(__arm64_pair_address_13489180, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13489180) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13489180) + (0x10UL))), v0);
#endif
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDD670;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x670UL))));
        x21 = 0x1A8F000UL;
        x25 = 0x1A8F000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x688UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0x6A8UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x22 = 0x1A8F000UL;
        x23 = 0x1A8F000UL;
        x24 = 0x1A8F000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x6C0UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x678UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x680UL))));
        x8 = unchecked((ulong)((sp) + (0x8UL)));
        x0 = RuntimeCalls.InvokeDirect(0xEA7FF0UL, x0, x1, x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x8UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x8UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x18UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x18UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x28UL))));
        __arm64_pair_address_13489264 = unchecked((ulong)((sp) + (0x30UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13489264, v0);
#else
        __WriteVector128(__arm64_pair_address_13489264, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13489264) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13489264) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x50UL))), x8);
        goto label_0xCDD478;
        label_0xCDD478:
        ;
        x1 = RuntimeMemory.ReadU64(x21);
        x0 = unchecked((ulong)((sp) + (0x30UL)));
        x0 = RuntimeCalls.InvokeDirect(0xF26DE0UL, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDD598;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xCDD6E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x48UL))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1B8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1B8UL)))) + (0x8UL))));
        x0 = x20;
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCDD6EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x10UL))))))));
        __arm64_flags_left_13489324 = unchecked((uint)(x8));
        __arm64_flags_right_13489324 = unchecked((uint)0x0UL);
        x9 = unchecked((ulong)(((!((unchecked((uint)((__arm64_flags_left_13489324) - (__arm64_flags_right_13489324))) == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        __arm64_flags_left_13489332 = unchecked((uint)(x26));
        __arm64_flags_right_13489332 = unchecked((uint)0xFFUL);
        __arm64_flags_result_13489332 = unchecked((uint)((__arm64_flags_left_13489332) & (__arm64_flags_right_13489332)));
        x10 = unchecked((ulong)(((!((__arm64_flags_result_13489332 == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) ^ (unchecked((uint)(x9)))))));
        if ((unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDD478;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDD4C4UL);
        }
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDD518;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDD6F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x1CUL))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x10UL))));
        x9 = RuntimeMemory.ReadU64(x25);
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x1CUL))), unchecked((uint)(x10)));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDD6F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x0) + (0x18UL))))))));
        x11 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13489392 = unchecked((uint)(x10));
        __arm64_flags_right_13489392 = unchecked((uint)(x11));
        if ((__arm64_flags_left_13489392 >= __arm64_flags_right_13489392))
        {
            goto label_0xCDD568;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x10) << (int)(unchecked((int)(0x3UL))))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x18UL))), unchecked((uint)(x9)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x8) + (0x20UL))), x20);
        x0 = x8;
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xCDD478;
        label_0xCDD518:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x100UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDD6F8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x1CUL))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x10UL))));
        x9 = RuntimeMemory.ReadU64(x25);
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x1CUL))), unchecked((uint)(x10)));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDD6FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x0) + (0x18UL))))))));
        x11 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13489472 = unchecked((uint)(x10));
        __arm64_flags_right_13489472 = unchecked((uint)(x11));
        if ((__arm64_flags_left_13489472 >= __arm64_flags_right_13489472))
        {
            goto label_0xCDD580;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x10) << (int)(unchecked((int)(0x3UL))))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x18UL))), unchecked((uint)(x9)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x8) + (0x20UL))), x20);
        x0 = x8;
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xCDD478;
        label_0xCDD568:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x9))))) + (0x20UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC0UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x70UL))));
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0x10A3390UL, x0, x1, x2, x3);
        goto label_0xCDD478;
        label_0xCDD580:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x9))))) + (0x20UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC0UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x70UL))));
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0x10A3390UL, x0, x1, x2, x3);
        goto label_0xCDD478;
        label_0xCDD598:
        ;
        x1 = RuntimeMemory.ReadU64(x24);
        x0 = unchecked((ulong)((sp) + (0x30UL)));
        x0 = RuntimeCalls.InvokeDirect(0xF26F08UL, x0, x1, x2, x3);
        goto label_0xCDD5A4;
        label_0xCDD5A4:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x100UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDD670;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xCDD5B0;
        label_0xCDD5B0:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        __arm64_flags_left_13489588 = unchecked((uint)(x20));
        __arm64_flags_right_13489588 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13489588) - (__arm64_flags_right_13489588))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13489588)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13489588)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13489588) - (__arm64_flags_right_13489588))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13489588)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCDD60C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(x22);
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDD670;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x3 = RuntimeMemory.ReadU64(x23);
        x21 = x0;
        x0 = x8;
        x1 = x21;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xEA7BD4UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((x21 == 0x0UL))
        {
            goto label_0xCDD670;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x21);
        x0 = x21;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1A8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1A8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x100UL))));
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) + (unchecked((uint)(0x1UL)))))));
        if ((x0 != 0x0UL))
        {
            goto label_0xCDD5B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDD608UL);
        }
        goto label_0xCDD670;
        label_0xCDD60C:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDD670;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xCDD618;
        label_0xCDD618:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        __arm64_flags_left_13489692 = unchecked((uint)(x20));
        __arm64_flags_right_13489692 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13489692) - (__arm64_flags_right_13489692))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13489692)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13489692)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13489692) - (__arm64_flags_right_13489692))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13489692)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCDD674;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(x22);
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDD670;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x3 = RuntimeMemory.ReadU64(x23);
        x21 = x0;
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x8;
        x1 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xEA7BD4UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((x21 == 0x0UL))
        {
            goto label_0xCDD670;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x21);
        x0 = x21;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x198UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x198UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF8UL))));
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) + (unchecked((uint)(0x1UL)))))));
        if ((x0 != 0x0UL))
        {
            goto label_0xCDD618;
        }
        else
        {
            goto label_0xCDD670;
        }
        label_0xCDD670:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCDD674;
        label_0xCDD674:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x100UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDD670;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((unchecked((ulong)((x8) + (0x18UL)))) + (0x4UL))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13489796 = unchecked((uint)(x2));
        __arm64_flags_right_13489796 = unchecked((uint)0x1UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((x8) + (0x18UL)))) + (0x0UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((unchecked((ulong)((x8) + (0x18UL)))) + (0x8UL))), unchecked((uint)(x9)));
        RuntimeCalls.Unsupported("b.lt", 0xCDD68CUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCDD6A8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1568880UL /* metadata target: Array.Clear */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDD670;
        }
        else
        {
            goto label_0xCDD6A8;
        }
        label_0xCDD6A8:
        ;
        x2 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((unchecked((ulong)((x0) + (0x18UL)))) + (0x4UL))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13489840 = unchecked((uint)(x2));
        __arm64_flags_right_13489840 = unchecked((uint)0x1UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((x0) + (0x18UL)))) + (0x0UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((unchecked((ulong)((x0) + (0x18UL)))) + (0x8UL))), unchecked((uint)(x8)));
        RuntimeCalls.Unsupported("b.lt", 0xCDD6B8UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCDD6CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x10UL))));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1568880UL /* metadata target: Array.Clear */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCDD6CC;
        label_0xCDD6CC:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xA0UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x90UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        sp = unchecked((ulong)((sp) + (0xB0UL)));
        return x0;
        label_0xCDD6E8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCDD6EC;
        label_0xCDD6EC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCDD6F0;
        label_0xCDD6F0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCDD6F4;
        label_0xCDD6F4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCDD6F8;
        label_0xCDD6F8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCDD6FC;
        label_0xCDD6FC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCDD71C;
        label_0xCDD71C:
        ;
        x20 = x0;
        __arm64_flags_left_13489952 = unchecked((uint)(x1));
        __arm64_flags_right_13489952 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13489952) - (__arm64_flags_right_13489952))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCDD750;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C00UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x21 = RuntimeMemory.ReadU64(x0);
        x0 = RuntimeCalls.InvokeDirect(0x19B0C10UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = RuntimeMemory.ReadU64(x24);
        x0 = unchecked((ulong)((sp) + (0x30UL)));
        x0 = RuntimeCalls.InvokeDirect(0xF26F08UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((x21 == 0x0UL))
        {
            goto label_0xCDD5A4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB1BD40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCDD750;
        label_0xCDD750:
        ;
        x21 = 0x0UL;
        goto label_0xCDD75C;
        label_0xCDD75C:
        ;
        x1 = RuntimeMemory.ReadU64(x24);
        x0 = unchecked((ulong)((sp) + (0x30UL)));
        x0 = RuntimeCalls.InvokeDirect(0xF26F08UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((x21 != 0x0UL))
        {
            goto label_0xCDD774;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC26098UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCDD774;
        label_0xCDD774:
        ;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB1BD40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeCalls.InvokeDirect(0xA29990UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        return default(ulong);
    }
```

## `PostProcessingBehaviour.OnPreRender` — RVA `0xcdd780`

- Lift status: **exact**; input span: 312 bytes; span to next metadata RVA: 312 bytes.
- Metadata signature: `private void OnPreRender() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=56 (informational only).

```csharp
public static ulong PostProcessingBehaviour_OnPreRender_RVAcdd780(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x20 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x618UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDD7F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x6C8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x6D0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x6D8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x6E0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x6E8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x618UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCDD7F4;
        label_0xCDD7F4:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDD808;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDD804UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCDD808;
        label_0xCDD808:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDD884;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x6D0UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x78UL))));
        x20 = 0x1A8F000UL;
        x21 = 0x1A8F000UL;
        x2 = RuntimeMemory.ReadU64(x8);
        x22 = 0x1A8F000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x6C8UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x6E8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x6D8UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xD2B494UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x80UL))));
        x2 = RuntimeMemory.ReadU64(x20);
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xD2B494UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x88UL))));
        x2 = RuntimeMemory.ReadU64(x21);
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xD2B494UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x90UL))));
        x2 = RuntimeMemory.ReadU64(x22);
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xD2B494UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x70UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDD894;
        }
        else
        {
            goto label_0xCDD884;
        }
        label_0xCDD884:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xCDD894:
        ;
        x8 = 0x1A8F000UL;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x98UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x6E0UL))));
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = RuntimeMemory.ReadU64(x8);
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xD2B494UL);
        return default(ulong);
    }
```

## `PostProcessingBehaviour.OnPostRender` — RVA `0xcdd8b8`

- Lift status: **exact**; input span: 260 bytes; span to next metadata RVA: 260 bytes.
- Metadata signature: `private void OnPostRender() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=37 (informational only).

```csharp
public static ulong PostProcessingBehaviour_OnPostRender_RVAcdd8b8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13490544 = default(uint);
        uint __arm64_flags_left_13490564 = default(uint);
        uint __arm64_flags_result_13490564 = default(uint);
        uint __arm64_flags_right_13490544 = default(uint);
        uint __arm64_flags_right_13490564 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x619UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDD8EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x619UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCDD8EC;
        label_0xCDD8EC:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDD900;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDD8FCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCDD900;
        label_0xCDD900:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDD9AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x60UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDD928;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDD924UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCDD928;
        label_0xCDD928:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDD9AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x70UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDD9AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDD9B8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x188UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x188UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDD9AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDD9B8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDD9B8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x14UL))))));
        __arm64_flags_left_13490544 = unchecked((uint)(x8));
        __arm64_flags_right_13490544 = unchecked((uint)0x9UL);
        if (((__arm64_flags_left_13490544 >= __arm64_flags_right_13490544) && (!((unchecked((uint)((__arm64_flags_left_13490544) - (__arm64_flags_right_13490544))) == unchecked((uint)0x0UL))))))
        {
            goto label_0xCDD9AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(x8)))))))));
        x9 = unchecked((ulong)(unchecked((uint)(0x3A1UL))));
        __arm64_flags_left_13490564 = unchecked((uint)(x8));
        __arm64_flags_right_13490564 = unchecked((uint)(x9));
        __arm64_flags_result_13490564 = unchecked((uint)((__arm64_flags_left_13490564) & (__arm64_flags_right_13490564)));
        if ((__arm64_flags_result_13490564 == unchecked((uint)0x0UL)))
        {
            goto label_0xCDD9AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDD9B8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDD9B8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x176F34CUL /* metadata target: Camera.ResetProjectionMatrix */);
        label_0xCDD9AC:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xCDD9B8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `PostProcessingBehaviour.OnRenderImage` — RVA `0xcdd9bc`

- Lift status: **exact**; input span: 1376 bytes; span to next metadata RVA: 1376 bytes.
- Metadata signature: `private void OnRenderImage(RenderTexture source, RenderTexture destination) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=234 (informational only).

```csharp
public static ulong PostProcessingBehaviour_OnRenderImage_RVAcdd9bc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13491332 = default(uint);
        uint __arm64_flags_right_13491332 = default(uint);
        ulong __arm64_pair_address_13491324 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x25 = default(ulong);
        ulong x26 = default(ulong);
        ulong x27 = default(ulong);
        ulong x28 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFA0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x28);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x27);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x19);
        x22 = 0x1BAB000UL;
        x23 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x61AUL))))))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xD8UL))));
        x19 = x2;
        x21 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDDA98;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC68UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x6F0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x6F8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x700UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x708UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x710UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x718UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x128UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x148UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD68UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x720UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x728UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x61AUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCDDA98;
        label_0xCDDA98:
        ;
        x0 = RuntimeMemory.ReadU64(x23);
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x20UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDDAAC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDDAA8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCDDAAC;
        label_0xCDDAAC:
        ;
        x25 = 0x1A8D000UL;
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0xC68UL))));
        x0 = x22;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDDAF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x23);
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x60UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDDADC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDDAD8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCDDADC;
        label_0xCDDADC:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDDB28;
        }
        else
        {
            goto label_0xCDDAF0;
        }
        label_0xCDDAF0:
        ;
        x0 = RuntimeMemory.ReadU64(x25);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDDB00;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDDAFCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCDDB00;
        label_0xCDDB00:
        ;
        x0 = x21;
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x1778598UL /* metadata target: Graphics.Blit */);
        label_0xCDDB28:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xF0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDDF18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x188UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x188UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xA0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDDF18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(x8);
        x23 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x8;
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x188UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x9) + (0x188UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x10, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDDB68;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x70UL))))))));
        x26 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) ^ (unchecked((uint)(0x1UL)))))));
        goto label_0xCDDB6C;
        label_0xCDDB68:
        ;
        x26 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xCDDB6C;
        label_0xCDDB6C:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xB0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDDF18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x188UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x188UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDDB90;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x70UL))))))));
        x27 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) ^ (unchecked((uint)(0x1UL)))))));
        goto label_0xCDDB94;
        label_0xCDDB90:
        ;
        x27 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xCDDB94;
        label_0xCDDB94:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x48UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDDF18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x728UL))));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xCDF3ECUL /* metadata target: MaterialFactory.Get */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCDDF18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x2 = 0x0UL;
        x22 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x177B0DCUL /* metadata target: Material.set_shaderKeywords */, x0, x1, x2, x3);
        if ((unchecked((uint)(x26)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDDBFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x50UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDDF18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x21;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDF740UL /* metadata target: RenderTextureFactory.Get */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xA0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDDF18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x24 = x0;
        x0 = x8;
        x1 = x21;
        x2 = x24;
        x0 = RuntimeCalls.InvokeDirect(0xCD9E60UL /* metadata target: TaaComponent.Render */, x0, x1, x2, x3);
        x21 = x24;
        goto label_0xCDDBFC;
        label_0xCDDBFC:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDEC64UL /* metadata target: GraphicsUtils.get_whiteTexture */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xA8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDDF18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(x8);
        x24 = x0;
        x0 = x8;
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x188UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x9) + (0x188UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x10, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDDC40;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xA8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDDF18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xCD38D8UL /* metadata target: EyeAdaptationComponent.Prepare */, x0, x1, x2, x3);
        x24 = x0;
        x28 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xCDDC44;
        label_0xCDDC40:
        ;
        x28 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xCDDC44;
        label_0xCDDC44:
        ;
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD68UL))));
        x0 = x22;
        x2 = x24;
        x3 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x177AA8CUL /* metadata target: Material.SetTexture */, x0, x1, x2, x3);
        if ((unchecked((uint)(x27)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDDC9C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xA0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDDF18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xCDDF18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xB0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDDF18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDDC7CUL);
        }
        __arm64_pair_address_13491324 = unchecked((ulong)((x8) + (0x38UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13491324)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13491324) + (0x4UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x9) + (0x28UL))))), 0));
        __arm64_flags_left_13491332 = unchecked((uint)(x26));
        __arm64_flags_right_13491332 = unchecked((uint)0x0UL);
        x3 = unchecked((ulong)(((!((unchecked((uint)((__arm64_flags_left_13491332) - (__arm64_flags_right_13491332))) == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x1 = x21;
        x2 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xCD2860UL /* metadata target: DepthOfFieldComponent.Prepare */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x28 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xCDDC9C;
        label_0xCDDC9C:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xB8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDDF18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x188UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x188UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDDCD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xB8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDDF18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x21;
        x2 = x22;
        x3 = x24;
        x0 = RuntimeCalls.InvokeDirect(0xCCE8A4UL /* metadata target: BloomComponent.Prepare */, x0, x1, x2, x3);
        x28 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xCDDCD0;
        label_0xCDDCD0:
        ;
        x8 = 0x1A8F000UL;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xC0UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x6F0UL))));
        x0 = x20;
        x2 = x22;
        x3 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xD2B560UL, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xC8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x6F8UL))));
        x2 = x22;
        x3 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        x0 = x20;
        x24 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x28))) | (unchecked((uint)(x8)))))));
        x0 = RuntimeCalls.InvokeDirect(0xD2B560UL, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xE0UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x718UL))));
        x2 = x22;
        x3 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        x0 = x20;
        x24 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x24))) | (unchecked((uint)(x8)))))));
        x0 = RuntimeCalls.InvokeDirect(0xD2B560UL, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD0UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x710UL))));
        x2 = x22;
        x3 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        x0 = x20;
        x24 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x24))) | (unchecked((uint)(x8)))))));
        x0 = RuntimeCalls.InvokeDirect(0xD2B560UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        x24 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x24))) | (unchecked((uint)(x8)))))));
        if ((unchecked((uint)((unchecked((uint)(x23))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDDE18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x48UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDDF18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x148UL))));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xCDF3ECUL /* metadata target: MaterialFactory.Get */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCDDF18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x2 = 0x0UL;
        x23 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x177B0DCUL /* metadata target: Material.set_shaderKeywords */, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x708UL))));
        x0 = x20;
        x2 = x23;
        x3 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xD2B560UL, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xE8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x700UL))));
        x0 = x20;
        x2 = x23;
        x3 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xD2B560UL, x0, x1, x2, x3);
        if ((unchecked((uint)(x24)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDDEB4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x50UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDDF18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x21;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDF740UL /* metadata target: RenderTextureFactory.Get */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x25);
        x23 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDDDFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCDDDFC;
        label_0xCDDDFC:
        ;
        x0 = x21;
        x1 = x23;
        x2 = x22;
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177861CUL /* metadata target: Graphics.Blit */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCDDEB8;
        label_0xCDDE18:
        ;
        x8 = 0x1A8F000UL;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x708UL))));
        x0 = x20;
        x2 = x22;
        x3 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xD2B560UL, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xE8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x700UL))));
        x2 = x22;
        x3 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        x0 = x20;
        x23 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x24))) | (unchecked((uint)(x8)))))));
        x0 = RuntimeCalls.InvokeDirect(0xD2B560UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x23))) | (unchecked((uint)(x8)))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDDED0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDEC1CUL /* metadata target: GraphicsUtils.get_isLinearColorSpace */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDDE88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x720UL))));
        x0 = x22;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x177ADF0UL /* metadata target: Material.EnableKeyword */, x0, x1, x2, x3);
        goto label_0xCDDE88;
        label_0xCDDE88:
        ;
        x0 = RuntimeMemory.ReadU64(x25);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDDE98;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDDE94UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCDDE98;
        label_0xCDDE98:
        ;
        x0 = x21;
        x1 = x19;
        x2 = x22;
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177861CUL /* metadata target: Graphics.Blit */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCDDEF0;
        label_0xCDDEB4:
        ;
        x23 = x21;
        goto label_0xCDDEB8;
        label_0xCDDEB8:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xF0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDDF18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x23;
        x2 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xCD4DF4UL /* metadata target: FxaaComponent.Render */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCDDEF0;
        label_0xCDDED0:
        ;
        x0 = RuntimeMemory.ReadU64(x25);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDDEE0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDDEDCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCDDEE0;
        label_0xCDDEE0:
        ;
        x0 = x21;
        x1 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1778598UL /* metadata target: Graphics.Blit */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCDDEF0;
        label_0xCDDEF0:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x50UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDDF18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xCDFA70UL /* metadata target: RenderTextureFactory.ReleaseAll */);
        label_0xCDDF18:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```

## `PostProcessingBehaviour.OnGUI` — RVA `0xcddf1c`

- Lift status: **exact**; input span: 392 bytes; span to next metadata RVA: 392 bytes.
- Metadata signature: `private void OnGUI() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=51 (informational only).

```csharp
public static ulong PostProcessingBehaviour_OnGUI_RVAcddf1c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13492060 = default(uint);
        uint __arm64_flags_left_13492200 = default(uint);
        uint __arm64_flags_left_13492272 = default(uint);
        uint __arm64_flags_left_13492344 = default(uint);
        uint __arm64_flags_right_13492060 = default(uint);
        uint __arm64_flags_right_13492200 = default(uint);
        uint __arm64_flags_right_13492272 = default(uint);
        uint __arm64_flags_right_13492344 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x61BUL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDDF48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x61BUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCDDF48;
        label_0xCDDF48:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17AFBDCUL /* metadata target: Event.get_current */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCDE0A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17AF540UL /* metadata target: Event.get_type */, x0, x1, x2, x3);
        __arm64_flags_left_13492060 = unchecked((uint)(x0));
        __arm64_flags_right_13492060 = unchecked((uint)0x7UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13492060) - (__arm64_flags_right_13492060))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCDE094;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = 0x1A8C000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDDF80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDDF7CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCDDF80;
        label_0xCDDF80:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDE094;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x60UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDDFA8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDDFA4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCDDFA8;
        label_0xCDDFA8:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDE094;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDE0A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x188UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x188UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDE004;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDE0A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDE0A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x14UL))))));
        __arm64_flags_left_13492200 = unchecked((uint)(x8));
        __arm64_flags_right_13492200 = unchecked((uint)0x5UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13492200) - (__arm64_flags_right_13492200))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCDE004;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDE0A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xCD4390UL /* metadata target: EyeAdaptationComponent.OnGUI */);
        label_0xCDE004:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDE0A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x188UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x188UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDE04C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDE0A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDE0A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x14UL))))));
        __arm64_flags_left_13492272 = unchecked((uint)(x8));
        __arm64_flags_right_13492272 = unchecked((uint)0x8UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13492272) - (__arm64_flags_right_13492272))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCDE04C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDE0A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xCD2004UL /* metadata target: ColorGradingComponent.OnGUI */);
        label_0xCDE04C:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDE0A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x188UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x188UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDE094;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDE0A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDE0A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x14UL))))));
        __arm64_flags_left_13492344 = unchecked((uint)(x8));
        __arm64_flags_right_13492344 = unchecked((uint)0x9UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13492344) - (__arm64_flags_right_13492344))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCDE094;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDE0A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xCDA788UL /* metadata target: UserLutComponent.OnGUI */);
        label_0xCDE094:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xCDE0A0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `PostProcessingBehaviour.OnDisable` — RVA `0xcde0a4`

- Lift status: **partial**; input span: 640 bytes; span to next metadata RVA: 640 bytes.
- Metadata signature: `private void OnDisable() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=91 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.lt' at 0xcde24c; reason: Unknown IR expression at 0xcde24c

```csharp
public static ulong PostProcessingBehaviour_OnDisable_RVAcde0a4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13492804 = default(uint);
        uint __arm64_flags_left_13492924 = default(uint);
        uint __arm64_flags_right_13492804 = default(uint);
        uint __arm64_flags_right_13492924 = default(uint);
        ulong __arm64_pair_address_13492556 = default(ulong);
        ulong __arm64_pair_address_13492640 = default(ulong);
        ulong __arm64_pair_address_13492644 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x80UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x40UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x61CUL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDE148;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x730UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x738UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x740UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x748UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x750UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x758UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x760UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x6B0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x768UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x61CUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCDE148;
        label_0xCDE148:
        ;
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        __arm64_pair_address_13492556 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13492556, v0);
#else
        __WriteVector128(__arm64_pair_address_13492556, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13492556) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13492556) + (0x10UL))), v0);
#endif
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDE2A8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x738UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xEA55C4UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCDE2A8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x768UL))));
        x24 = 0x1A8F000UL;
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x748UL))));
        x22 = 0x1A8F000UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x21 = 0x1A8C000UL;
        x23 = 0x1A8F000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x730UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x740UL))));
        x8 = sp;
        x0 = RuntimeCalls.InvokeDirect(0x124EE08UL, x0, x1, x2, x3);
        __arm64_pair_address_13492640 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13492640);
#else
        v0 = __ReadVector128(__arm64_pair_address_13492640);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13492640) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13492640) + (0x10UL))));
#endif
        __arm64_pair_address_13492644 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13492644, v0);
#else
        __WriteVector128(__arm64_pair_address_13492644, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13492644) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13492644) + (0x10UL))), v1);
#endif
        goto label_0xCDE1A8;
        label_0xCDE1A8:
        ;
        x1 = RuntimeMemory.ReadU64(x24);
        x0 = unchecked((ulong)((sp) + (0x20UL)));
        x0 = RuntimeCalls.InvokeDirect(0xF26C24UL, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDE1E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x60UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDE2A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x38UL))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x30UL))))));
        x2 = x20;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176FCE4UL /* metadata target: Camera.RemoveCommandBuffer */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCDE2A4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A7968UL /* metadata target: CommandBuffer.Dispose */, x0, x1, x2, x3);
        goto label_0xCDE1A8;
        label_0xCDE1E8:
        ;
        x1 = RuntimeMemory.ReadU64(x23);
        x0 = unchecked((ulong)((sp) + (0x20UL)));
        x0 = RuntimeCalls.InvokeDirect(0xF26C20UL, x0, x1, x2, x3);
        goto label_0xCDE1F4;
        label_0xCDE1F4:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDE2A8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xEA5850UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDE218;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDE214UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCDE218;
        label_0xCDE218:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDE234;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xCDD1ECUL /* metadata target: PostProcessingBehaviour.DisableComponents */, x0, x1, x2, x3);
        goto label_0xCDE234;
        label_0xCDE234:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x38UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDE2A8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((unchecked((ulong)((x8) + (0x18UL)))) + (0x4UL))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13492804 = unchecked((uint)(x2));
        __arm64_flags_right_13492804 = unchecked((uint)0x1UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((x8) + (0x18UL)))) + (0x0UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((unchecked((ulong)((x8) + (0x18UL)))) + (0x8UL))), unchecked((uint)(x9)));
        RuntimeCalls.Unsupported("b.lt", 0xCDE24CUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCDE260;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1568880UL /* metadata target: Array.Clear */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCDE260;
        label_0xCDE260:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x48UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDE2A8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDF5E0UL /* metadata target: MaterialFactory.Dispose */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x50UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDE2A8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDFB3CUL /* metadata target: RenderTextureFactory.Dispose */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDF31CUL /* metadata target: GraphicsUtils.Dispose */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        sp = unchecked((ulong)((sp) + (0x80UL)));
        return x0;
        label_0xCDE2A0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCDE2A4;
        label_0xCDE2A4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCDE2A8;
        label_0xCDE2A8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCDE2BC;
        label_0xCDE2BC:
        ;
        __arm64_flags_left_13492924 = unchecked((uint)(x1));
        __arm64_flags_right_13492924 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13492924) - (__arm64_flags_right_13492924))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCDE2EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDE2C4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0x19B0C00UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = RuntimeMemory.ReadU64(x0);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x48UL))), x8);
        x0 = RuntimeCalls.InvokeDirect(0x19B0C10UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = RuntimeMemory.ReadU64(x23);
        x0 = unchecked((ulong)((sp) + (0x20UL)));
        x0 = RuntimeCalls.InvokeDirect(0xF26C20UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x48UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDE1F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDE2E8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB1BD40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCDE2EC;
        label_0xCDE2EC:
        ;
        x19 = x0;
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x48UL))), 0x0UL);
        goto label_0xCDE2FC;
        label_0xCDE2FC:
        ;
        x1 = RuntimeMemory.ReadU64(x23);
        x0 = unchecked((ulong)((sp) + (0x20UL)));
        x0 = RuntimeCalls.InvokeDirect(0xF26C20UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x48UL))));
        if ((x8 != 0x0UL))
        {
            goto label_0xCDE318;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC26098UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCDE318;
        label_0xCDE318:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x48UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB1BD40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeCalls.InvokeDirect(0xA29990UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        return default(ulong);
    }
```

## `PostProcessingBehaviour.ResetTemporalEffects` — RVA `0xcde324`

- Lift status: **exact**; input span: 64 bytes; span to next metadata RVA: 64 bytes.
- Metadata signature: `public void ResetTemporalEffects() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=7 (informational only).

```csharp
public static ulong PostProcessingBehaviour_ResetTemporalEffects_RVAcde324(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA0UL))));
        if ((x8 == 0x0UL))
        {
        }
        else
        {
            x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x2CUL))), unchecked((byte)(unchecked((uint)(x9)))));
            x19 = x0;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x98UL))));
            if ((x0 == 0x0UL))
            {
            }
            else
            {
                x0 = RuntimeCalls.InvokeDirect(0xCD58F4UL /* metadata target: MotionBlurComponent.ResetHistory */, x0, x1, x2, x3);
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA8UL))));
                if ((x8 == 0x0UL))
                {
                }
                else
                {
                    x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                    RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x50UL))), unchecked((byte)(unchecked((uint)(x9)))));
                    x30 = RuntimeMemory.ReadU64(sp);
                    x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
                    return x0;
                }
            }
        }
        label_0xCDE360:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `PostProcessingBehaviour.ctor` — RVA `0xcde364`

- Lift status: **exact**; input span: 172 bytes; span to next metadata RVA: 172 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=27 (informational only).

```csharp
public static ulong PostProcessingBehaviour_ctor_RVAcde364(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x22 = 0x1A8F000UL;
        x21 = 0x1A8F000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x61FUL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x530UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x538UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDE3B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x538UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x530UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x61FUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCDE3B0;
        label_0xCDE3B0:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x21);
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x10A2B64UL, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0xF8UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x21);
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x10A2B64UL, x0, x1, x2, x3);
        x0 = unchecked((ulong)((x19) + (0x100UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x100UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */);
        return default(ulong);
    }
```
