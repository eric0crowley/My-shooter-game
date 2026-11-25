# `PostEffectsHelper` — TypeDefIndex 3635

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## `PostEffectsHelper.OnRenderImage` — RVA `0xce6f38`

- Lift status: **exact**; input span: 104 bytes; span to next metadata RVA: 104 bytes.
- Metadata signature: `private void OnRenderImage(RenderTexture source, RenderTexture destination) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=17 (informational only).

```csharp
public static ulong PostEffectsHelper_OnRenderImage_RVAce6f38(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x19 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x667UL))))))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x398UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE6F74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x398UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB98UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x667UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCE6F74;
        label_0xCE6F74:
        ;
        x0 = RuntimeMemory.ReadU64(x19);
        x19 = 0x1A8F000UL;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB98UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE6F8C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE6F88UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCE6F8C;
        label_0xCE6F8C:
        ;
        x0 = RuntimeMemory.ReadU64(x19);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x1770B68UL /* metadata target: Debug.Log */);
        return default(ulong);
    }
```

## `PostEffectsHelper.DrawLowLevelPlaneAlignedWithCamera` — RVA `0xce6fa0`

- Lift status: **exact**; input span: 576 bytes; span to next metadata RVA: 576 bytes.
- Metadata signature: `private static void DrawLowLevelPlaneAlignedWithCamera(float dist, RenderTexture source, RenderTexture dest, Material material, Camera cameraForProjectionMatrix) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=79 (informational only).

```csharp
public static ulong PostEffectsHelper_DrawLowLevelPlaneAlignedWithCamera_RVAce6fa0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13529256 = default(uint);
        uint __arm64_flags_left_13529516 = default(uint);
        uint __arm64_flags_right_13529256 = default(uint);
        uint __arm64_flags_right_13529516 = default(uint);
        ulong __arm64_pair_address_13529000 = default(ulong);
        ulong __arm64_pair_address_13529004 = default(ulong);
        ulong __arm64_pair_address_13529152 = default(ulong);
        ulong __arm64_pair_address_13529156 = default(ulong);
        ulong __arm64_pair_address_13529168 = default(ulong);
        ulong __arm64_pair_address_13529172 = default(ulong);
        ulong __arm64_pair_address_13529224 = default(ulong);
        ulong __arm64_pair_address_13529544 = default(ulong);
        ulong __arm64_pair_address_13529548 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xE0UL)));
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0x80UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13529000 = unchecked((ulong)((sp) + (0x90UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13529000, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13529000) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13529004 = unchecked((ulong)((sp) + (0xA0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13529004, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13529004) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xD0UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xD0UL)))) + (0x8UL))), x19);
        x23 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x668UL))))))));
        x20 = x3;
        x19 = x2;
        x22 = x1;
        x21 = x0;
        v8 = v0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE6FF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD10UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x668UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCE6FF0;
        label_0xCE6FF0:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1782264UL /* metadata target: RenderTexture.set_active */, x0, x1, x2, x3);
        if ((x19 == 0x0UL))
        {
            goto label_0xCE71DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD10UL))));
        x0 = x19;
        x2 = x21;
        x3 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x177AA8CUL /* metadata target: Material.SetTexture */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1778B44UL /* metadata target: GL.PushMatrix */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1778B94UL /* metadata target: GL.LoadIdentity */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCE71DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176F148UL /* metadata target: Camera.get_projectionMatrix */, x0, x1, x2, x3);
        __arm64_pair_address_13529152 = unchecked((ulong)((sp) + (0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13529152);
#else
        v0 = __ReadVector128(__arm64_pair_address_13529152);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13529152) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13529152) + (0x10UL))));
#endif
        __arm64_pair_address_13529156 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13529156);
#else
        v2 = __ReadVector128(__arm64_pair_address_13529156);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13529156) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13529156) + (0x10UL))));
#endif
        x0 = sp;
        x1 = 0x0UL;
        __arm64_pair_address_13529168 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13529168, v0);
#else
        __WriteVector128(__arm64_pair_address_13529168, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13529168) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13529168) + (0x10UL))), v1);
#endif
        __arm64_pair_address_13529172 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13529172, v2);
#else
        __WriteVector128(__arm64_pair_address_13529172, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13529172) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13529172) + (0x10UL))), v3);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x1778BE4UL /* metadata target: GL.LoadProjectionMatrix */, x0, x1, x2, x3);
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176E71CUL /* metadata target: Camera.get_fieldOfView */, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x3E4UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        x0 = unchecked((ulong)((sp) + (0x8CUL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        x1 = unchecked((ulong)((sp) + (0x88UL)));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C70UL, x0, x1, x2, x3);
        __arm64_pair_address_13529224 = unchecked((ulong)((sp) + (0x88UL)));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13529224)), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13529224) + (0x4UL))))), 0));
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176E9A4UL /* metadata target: Camera.get_aspect */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        v9 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x177AE78UL /* metadata target: Material.get_passCount */, x0, x1, x2, x3);
        __arm64_flags_left_13529256 = unchecked((uint)(x0));
        __arm64_flags_right_13529256 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13529256) - (__arm64_flags_right_13529256))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13529256)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13529256)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13529256) - (__arm64_flags_right_13529256))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13529256)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCE71B4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE70B0UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xBF800000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        x20 = unchecked((ulong)(unchecked((uint)0x0UL)));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)))), 0));
        goto label_0xCE70E8;
        label_0xCE70E8:
        ;
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177AF98UL /* metadata target: Material.SetPass */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = unchecked((ulong)(unchecked((uint)(0x7UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1778D0CUL /* metadata target: GL.Begin */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17788ECUL /* metadata target: GL.TexCoord2 */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177884CUL /* metadata target: GL.Vertex3 */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17788ECUL /* metadata target: GL.TexCoord2 */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177884CUL /* metadata target: GL.Vertex3 */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17788ECUL /* metadata target: GL.TexCoord2 */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177884CUL /* metadata target: GL.Vertex3 */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17788ECUL /* metadata target: GL.TexCoord2 */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177884CUL /* metadata target: GL.Vertex3 */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1778D48UL /* metadata target: GL.End */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) + (unchecked((uint)(0x1UL)))))));
        x0 = RuntimeCalls.InvokeDirect(0x177AE78UL /* metadata target: Material.get_passCount */, x0, x1, x2, x3);
        __arm64_flags_left_13529516 = unchecked((uint)(x20));
        __arm64_flags_right_13529516 = unchecked((uint)(x0));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13529516) - (__arm64_flags_right_13529516))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13529516)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13529516)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13529516) - (__arm64_flags_right_13529516))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13529516)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCE70E8;
        }
        else
        {
            goto label_0xCE71B4;
        }
        label_0xCE71B4:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1778B6CUL /* metadata target: GL.PopMatrix */, x0, x1, x2, x3);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xD0UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xD0UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xC0UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xB0UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))));
        __arm64_pair_address_13529544 = unchecked((ulong)((sp) + (0xA0UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13529544)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13529544) + (0x8UL))))), 0));
        __arm64_pair_address_13529548 = unchecked((ulong)((sp) + (0x90UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13529548)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13529548) + (0x8UL))))), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x80UL))))), 0));
        return x0;
        label_0xCE71DC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `PostEffectsHelper.DrawBorder` — RVA `0xce71e0`

- Lift status: **exact**; input span: 884 bytes; span to next metadata RVA: 884 bytes.
- Metadata signature: `private static void DrawBorder(RenderTexture dest, Material material) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=91 (informational only).

```csharp
public static ulong PostEffectsHelper_DrawBorder_RVAce71e0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13529636 = default(uint);
        uint __arm64_flags_left_13530412 = default(uint);
        uint __arm64_flags_right_13529636 = default(uint);
        uint __arm64_flags_right_13530412 = default(uint);
        ulong __arm64_pair_address_13529568 = default(ulong);
        ulong __arm64_pair_address_13529572 = default(ulong);
        ulong __arm64_pair_address_13530432 = default(ulong);
        ulong __arm64_pair_address_13530440 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_13529568 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFB0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13529568, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13529568) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        sp = __arm64_pair_address_13529568;
        __arm64_pair_address_13529572 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13529572, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13529572) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x20UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x19);
        x19 = x1;
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1782264UL /* metadata target: RenderTexture.set_active */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1778B44UL /* metadata target: GL.PushMatrix */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1778BBCUL /* metadata target: GL.LoadOrtho */, x0, x1, x2, x3);
        if ((x19 == 0x0UL))
        {
            goto label_0xCE7550;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177AE78UL /* metadata target: Material.get_passCount */, x0, x1, x2, x3);
        __arm64_flags_left_13529636 = unchecked((uint)(x0));
        __arm64_flags_right_13529636 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13529636) - (__arm64_flags_right_13529636))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13529636)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13529636)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13529636) - (__arm64_flags_right_13529636))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13529636)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCE7534;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x432000UL;
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x3B8UL))))), 0));
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        goto label_0xCE7240;
        label_0xCE7240:
        ;
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177AF98UL /* metadata target: Material.SetPass */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCE7550;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x0 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x178UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x178UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x0))))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x0 = unchecked((ulong)(unchecked((uint)(0x7UL))));
        x1 = 0x0UL;
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x1778D0CUL /* metadata target: GL.Begin */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17788ECUL /* metadata target: GL.TexCoord2 */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v2 = v8;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177884CUL /* metadata target: GL.Vertex3 */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17788ECUL /* metadata target: GL.TexCoord2 */, x0, x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v0 = v9;
        v2 = v8;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177884CUL /* metadata target: GL.Vertex3 */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17788ECUL /* metadata target: GL.TexCoord2 */, x0, x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v0 = v9;
        v2 = v8;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177884CUL /* metadata target: GL.Vertex3 */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17788ECUL /* metadata target: GL.TexCoord2 */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v2 = v8;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177884CUL /* metadata target: GL.Vertex3 */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        x0 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x178UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x178UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x22 = unchecked((ulong)(unchecked((uint)(x0))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17788ECUL /* metadata target: GL.TexCoord2 */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x22))))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v0 = v9;
        v2 = v8;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177884CUL /* metadata target: GL.Vertex3 */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17788ECUL /* metadata target: GL.TexCoord2 */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v2 = v8;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177884CUL /* metadata target: GL.Vertex3 */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17788ECUL /* metadata target: GL.TexCoord2 */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v2 = v8;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177884CUL /* metadata target: GL.Vertex3 */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17788ECUL /* metadata target: GL.TexCoord2 */, x0, x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v0 = v9;
        v2 = v8;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177884CUL /* metadata target: GL.Vertex3 */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        x0 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x198UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x198UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x0))))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17788ECUL /* metadata target: GL.TexCoord2 */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v2 = v8;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177884CUL /* metadata target: GL.Vertex3 */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17788ECUL /* metadata target: GL.TexCoord2 */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v2 = v8;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177884CUL /* metadata target: GL.Vertex3 */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17788ECUL /* metadata target: GL.TexCoord2 */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v1 = v9;
        v2 = v8;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177884CUL /* metadata target: GL.Vertex3 */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17788ECUL /* metadata target: GL.TexCoord2 */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v1 = v9;
        v2 = v8;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177884CUL /* metadata target: GL.Vertex3 */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        x0 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x198UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x198UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x0))))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17788ECUL /* metadata target: GL.TexCoord2 */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v1 = v9;
        v2 = v8;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177884CUL /* metadata target: GL.Vertex3 */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17788ECUL /* metadata target: GL.TexCoord2 */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v1 = v9;
        v2 = v8;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177884CUL /* metadata target: GL.Vertex3 */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17788ECUL /* metadata target: GL.TexCoord2 */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v2 = v8;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177884CUL /* metadata target: GL.Vertex3 */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17788ECUL /* metadata target: GL.TexCoord2 */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v2 = v8;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177884CUL /* metadata target: GL.Vertex3 */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1778D48UL /* metadata target: GL.End */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        x0 = RuntimeCalls.InvokeDirect(0x177AE78UL /* metadata target: Material.get_passCount */, x0, x1, x2, x3);
        __arm64_flags_left_13530412 = unchecked((uint)(x21));
        __arm64_flags_right_13530412 = unchecked((uint)(x0));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13530412) - (__arm64_flags_right_13530412))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13530412)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13530412)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13530412) - (__arm64_flags_right_13530412))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13530412)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCE7240;
        }
        else
        {
            goto label_0xCE7534;
        }
        label_0xCE7534:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        __arm64_pair_address_13530432 = unchecked((ulong)((sp) + (0x10UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13530432)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13530432) + (0x8UL))))), 0));
        x0 = 0x0UL;
        __arm64_pair_address_13530440 = sp;
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13530440)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13530440) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_13530440) + (0x50UL)));
        return RuntimeCalls.InvokeDirect(0x1778B6CUL /* metadata target: GL.PopMatrix */);
        label_0xCE7550:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `PostEffectsHelper.DrawLowLevelQuad` — RVA `0xce7554`

- Lift status: **exact**; input span: 416 bytes; span to next metadata RVA: 416 bytes.
- Metadata signature: `private static void DrawLowLevelQuad(float x1, float x2, float y1, float y2, RenderTexture source, RenderTexture dest, Material material) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=67 (informational only).

```csharp
public static ulong PostEffectsHelper_DrawLowLevelQuad_RVAce7554(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13530608 = default(uint);
        uint __arm64_flags_left_13530824 = default(uint);
        uint __arm64_flags_right_13530608 = default(uint);
        uint __arm64_flags_right_13530824 = default(uint);
        ulong __arm64_load_address_13530856 = default(ulong);
        ulong __arm64_pair_address_13530456 = default(ulong);
        ulong __arm64_pair_address_13530460 = default(ulong);
        ulong __arm64_pair_address_13530844 = default(ulong);
        ulong __arm64_pair_address_13530848 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFB0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFB0UL)));
        __arm64_pair_address_13530456 = unchecked((ulong)((sp) + (0x8UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13530456, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13530456) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13530460 = unchecked((ulong)((sp) + (0x18UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13530460, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13530460) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x28UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x19);
        x22 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x669UL))))))));
        x19 = x2;
        x21 = x1;
        x20 = x0;
        v8 = v3;
        v9 = v2;
        v10 = v1;
        v11 = v0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE75A8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD10UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x669UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCE75A8;
        label_0xCE75A8:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1782264UL /* metadata target: RenderTexture.set_active */, x0, x1, x2, x3);
        if ((x19 == 0x0UL))
        {
            goto label_0xCE76F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD10UL))));
        x0 = x19;
        x2 = x20;
        x3 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x177AA8CUL /* metadata target: Material.SetTexture */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1778B44UL /* metadata target: GL.PushMatrix */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1778BBCUL /* metadata target: GL.LoadOrtho */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177AE78UL /* metadata target: Material.get_passCount */, x0, x1, x2, x3);
        __arm64_flags_left_13530608 = unchecked((uint)(x0));
        __arm64_flags_right_13530608 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13530608) - (__arm64_flags_right_13530608))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13530608)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13530608)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13530608) - (__arm64_flags_right_13530608))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13530608)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCE76D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x432000UL;
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x3B8UL))))), 0));
        x20 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xCE7604;
        label_0xCE7604:
        ;
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177AF98UL /* metadata target: Material.SetPass */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = unchecked((ulong)(unchecked((uint)(0x7UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1778D0CUL /* metadata target: GL.Begin */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17788ECUL /* metadata target: GL.TexCoord2 */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177884CUL /* metadata target: GL.Vertex3 */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17788ECUL /* metadata target: GL.TexCoord2 */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177884CUL /* metadata target: GL.Vertex3 */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17788ECUL /* metadata target: GL.TexCoord2 */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177884CUL /* metadata target: GL.Vertex3 */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17788ECUL /* metadata target: GL.TexCoord2 */, x0, x1, x2, x3);
        v0 = v11;
        v1 = v8;
        v2 = v12;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177884CUL /* metadata target: GL.Vertex3 */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1778D48UL /* metadata target: GL.End */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) + (unchecked((uint)(0x1UL)))))));
        x0 = RuntimeCalls.InvokeDirect(0x177AE78UL /* metadata target: Material.get_passCount */, x0, x1, x2, x3);
        __arm64_flags_left_13530824 = unchecked((uint)(x20));
        __arm64_flags_right_13530824 = unchecked((uint)(x0));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13530824) - (__arm64_flags_right_13530824))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13530824)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13530824)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13530824) - (__arm64_flags_right_13530824))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13530824)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCE7604;
        }
        else
        {
            goto label_0xCE76D0;
        }
        label_0xCE76D0:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x28UL))));
        __arm64_pair_address_13530844 = unchecked((ulong)((sp) + (0x18UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13530844)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13530844) + (0x8UL))))), 0));
        __arm64_pair_address_13530848 = unchecked((ulong)((sp) + (0x8UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13530848)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13530848) + (0x8UL))))), 0));
        x0 = 0x0UL;
        __arm64_load_address_13530856 = sp;
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_13530856)), 0));
        sp = unchecked((ulong)((__arm64_load_address_13530856) + (0x50UL)));
        return RuntimeCalls.InvokeDirect(0x1778B6CUL /* metadata target: GL.PopMatrix */);
        label_0xCE76F0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `PostEffectsHelper.ctor` — RVA `0xce76f4`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong PostEffectsHelper_ctor_RVAce76f4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x1 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */);
        return default(ulong);
    }
```
