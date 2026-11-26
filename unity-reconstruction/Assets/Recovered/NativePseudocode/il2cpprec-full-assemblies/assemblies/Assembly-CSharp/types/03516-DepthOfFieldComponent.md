# `DepthOfFieldComponent` — TypeDefIndex 3516

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `RenderTexture` | `m_CoCHistory` |

## `DepthOfFieldComponent.get_active` — RVA `0xcd25c4`

- Lift status: **exact**; input span: 104 bytes; span to next metadata RVA: 104 bytes.
- Metadata signature: `public override bool get_active() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=13 (informational only).

```csharp
public static uint DepthOfFieldComponent_get_active_RVAcd25c4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13444620 = default(uint);
        uint __arm64_flags_right_13444620 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x5BFUL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD25F0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF88UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x5BFUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCD25F0;
        label_0xCD25F0:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD2628;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCD2618;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD2628;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x30UL))))))));
        __arm64_flags_left_13444620 = unchecked((uint)(x8));
        __arm64_flags_right_13444620 = unchecked((uint)0x0UL);
        x0 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_13444620) - (__arm64_flags_right_13444620))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        goto label_0xCD261C;
        label_0xCD2618:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xCD261C;
        label_0xCD261C:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xCD2628:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `DepthOfFieldComponent.GetCameraFlags` — RVA `0xcd262c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public override DepthTextureMode GetCameraFlags() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint DepthOfFieldComponent_GetCameraFlags_RVAcd262c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `DepthOfFieldComponent.CalculateFocalLength` — RVA `0xcd2634`

- Lift status: **exact**; input span: 156 bytes; span to next metadata RVA: 156 bytes.
- Metadata signature: `private float CalculateFocalLength() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=22 (informational only).

```csharp
public static ulong DepthOfFieldComponent_CalculateFocalLength_RVAcd2634(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x5C0UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD2660;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF88UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x5C0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCD2660;
        label_0xCD2660:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD26CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x20UL))))))));
        if ((unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD2684;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD2670UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x1CUL))))), 0));
        goto label_0xCD26C0;
        label_0xCD2684:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD26CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCD26CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176E71CUL /* metadata target: Camera.get_fieldOfView */, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x3E4UL))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x19B0D00UL, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x3ACUL))))), 0));
        goto label_0xCD26C0;
        label_0xCD26C0:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xCD26CC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `DepthOfFieldComponent.CalculateMaxCoCRadius` — RVA `0xcd26d0`

- Lift status: **exact**; input span: 116 bytes; span to next metadata RVA: 116 bytes.
- Metadata signature: `private float CalculateMaxCoCRadius(int screenHeight) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=19 (informational only).

```csharp
public static ulong DepthOfFieldComponent_CalculateMaxCoCRadius_RVAcd26d0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x5C1UL))))))));
        x19 = unchecked((ulong)(unchecked((uint)(x1))));
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF88UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x5C1UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCD2700:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            label_0xCD2740:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        }
        else
        {
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x24UL))))), 0));
            x8 = 0x432000UL;
            v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x458UL))))), 0));
            x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
            x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
            x30 = RuntimeMemory.ReadU64(sp);
            x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
            return x0;
        }
        return default(ulong);
    }
```

## `DepthOfFieldComponent.CheckHistory` — RVA `0xcd2744`

- Lift status: **exact**; input span: 208 bytes; span to next metadata RVA: 208 bytes.
- Metadata signature: `private bool CheckHistory(int width, int height) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=28 (informational only).

```csharp
public static uint DepthOfFieldComponent_CheckHistory_RVAcd2744(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13445076 = default(uint);
        uint __arm64_flags_left_13445104 = default(uint);
        uint __arm64_flags_right_13445076 = default(uint);
        uint __arm64_flags_right_13445104 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x23 = 0x1BAB000UL;
        x22 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x5C2UL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD8UL))));
        x19 = unchecked((ulong)(unchecked((uint)(x2))));
        x21 = unchecked((ulong)(unchecked((uint)(x1))));
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD2784;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x5C2UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCD2784;
        label_0xCD2784:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x20UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD2798;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCD2794UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCD2798;
        label_0xCD2798:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCD27FC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCD2810;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1782524UL /* metadata target: RenderTexture.IsCreated */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCD27FC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCD2810;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x178UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x178UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        __arm64_flags_left_13445076 = unchecked((uint)(x0));
        __arm64_flags_right_13445076 = unchecked((uint)(x21));
        if ((!((unchecked((uint)((__arm64_flags_left_13445076) - (__arm64_flags_right_13445076))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCD27FC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCD2810;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x198UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x198UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        __arm64_flags_left_13445104 = unchecked((uint)(x0));
        __arm64_flags_right_13445104 = unchecked((uint)(x19));
        x0 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_13445104) - (__arm64_flags_right_13445104))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        goto label_0xCD2800;
        label_0xCD27FC:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xCD2800;
        label_0xCD2800:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xCD2810:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `DepthOfFieldComponent.SelectFormat` — RVA `0xcd2814`

- Lift status: **partial**; input span: 76 bytes; span to next metadata RVA: 76 bytes.
- Metadata signature: `private RenderTextureFormat SelectFormat(RenderTextureFormat primary, RenderTextureFormat secondary) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=10 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'csel' at 0xcd2850; reason: Unknown IR expression at 0xcd2850

```csharp
public static uint DepthOfFieldComponent_SelectFormat_RVAcd2814(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13445192 = default(uint);
        uint __arm64_flags_result_13445192 = default(uint);
        uint __arm64_flags_right_13445192 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = unchecked((ulong)(unchecked((uint)(x1))));
        x0 = unchecked((ulong)(unchecked((uint)(x1))));
        x1 = 0x0UL;
        x19 = unchecked((ulong)(unchecked((uint)(x2))));
        x0 = RuntimeCalls.InvokeDirect(0x179A984UL /* metadata target: SystemInfo.SupportsRenderTextureFormat */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            label_0xCD283C:
            ;
            x0 = unchecked((ulong)(unchecked((uint)(x19))));
            x1 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0x179A984UL /* metadata target: SystemInfo.SupportsRenderTextureFormat */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
            __arm64_flags_left_13445192 = unchecked((uint)(x0));
            __arm64_flags_right_13445192 = unchecked((uint)0x1UL);
            __arm64_flags_result_13445192 = unchecked((uint)((__arm64_flags_left_13445192) & (__arm64_flags_right_13445192)));
            x8 = unchecked((ulong)(unchecked((uint)(0x7UL))));
            RuntimeCalls.Unsupported("csel", 0xCD2850UL);
            x0 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x19)) : unchecked((uint)(x8)))));
        }
        else
        {
            x0 = unchecked((ulong)(unchecked((uint)(x20))));
        }
        label_0xCD2854:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `DepthOfFieldComponent.Prepare` — RVA `0xcd2860`

- Lift status: **partial**; input span: 1836 bytes; span to next metadata RVA: 1836 bytes.
- Metadata signature: `public void Prepare(RenderTexture source, Material uberMaterial, bool antialiasCoC, Vector2 taaJitter, float taaBlending) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=299 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'csel' at 0xcd2958; reason: Unknown IR expression at 0xcd2958; reason: Unsupported instruction 'cinc' at 0xcd2d30; reason: Unknown IR expression at 0xcd2d30; reason: Unsupported instruction 'cinc' at 0xcd2d3c; reason: Unknown IR expression at 0xcd2d3c; reason: Unsupported instruction 'cinc' at 0xcd2df8; reason: Unknown IR expression at 0xcd2df8

```csharp
public static ulong DepthOfFieldComponent_Prepare_RVAcd2860(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13445456 = default(uint);
        uint __arm64_flags_left_13446096 = default(uint);
        uint __arm64_flags_left_13446440 = default(uint);
        uint __arm64_flags_left_13446452 = default(uint);
        uint __arm64_flags_left_13446640 = default(uint);
        uint __arm64_flags_left_13446652 = default(uint);
        uint __arm64_flags_left_13446828 = default(uint);
        uint __arm64_flags_result_13445456 = default(uint);
        uint __arm64_flags_result_13446096 = default(uint);
        uint __arm64_flags_right_13445456 = default(uint);
        uint __arm64_flags_right_13446096 = default(uint);
        uint __arm64_flags_right_13446440 = default(uint);
        uint __arm64_flags_right_13446452 = default(uint);
        uint __arm64_flags_right_13446640 = default(uint);
        uint __arm64_flags_right_13446652 = default(uint);
        uint __arm64_flags_right_13446828 = default(uint);
        float __arm64_float_flags_left_13445476 = default(float);
        float __arm64_float_flags_right_13445476 = default(float);
        ulong __arm64_pair_address_13445220 = default(ulong);
        ulong __arm64_pair_address_13445224 = default(ulong);
        ulong __arm64_pair_address_13445228 = default(ulong);
        ulong __arm64_pair_address_13445232 = default(ulong);
        ulong __arm64_pair_address_13445412 = default(ulong);
        ulong __arm64_pair_address_13447020 = default(ulong);
        ulong __arm64_pair_address_13447024 = default(ulong);
        ulong __arm64_pair_address_13447028 = default(ulong);
        ulong __arm64_pair_address_13447032 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v13 = default(RuntimeVector128);
        RuntimeVector128 v14 = default(RuntimeVector128);
        RuntimeVector128 v15 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
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
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xC0UL)));
        __arm64_pair_address_13445220 = unchecked((ulong)((sp) + (0x20UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13445220, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v15.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13445220) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v14.GetUInt64(0)))));
        __arm64_pair_address_13445224 = unchecked((ulong)((sp) + (0x30UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13445224, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13445224) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13445228 = unchecked((ulong)((sp) + (0x40UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13445228, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13445228) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13445232 = unchecked((ulong)((sp) + (0x50UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13445232, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13445232) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x0UL))), x28);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))), x27);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))), x19);
        x22 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x5C3UL))))))));
        v13 = v2;
        v11 = v1;
        v12 = v0;
        x24 = unchecked((ulong)(unchecked((uint)(x3))));
        x20 = x2;
        x21 = x1;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD291C;
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
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF88UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF90UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF98UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xFA0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xFA8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x5C3UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCD291C;
        label_0xCD291C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD2F88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD2924UL);
        }
        __arm64_pair_address_13445412 = unchecked((ulong)((x8) + (0x14UL)));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13445412)), 0));
        v14 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13445412) + (0x4UL))))), 0));
        x27 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x24UL))))));
        x0 = unchecked((ulong)(unchecked((uint)(0x10UL))));
        x1 = 0x0UL;
        x23 = unchecked((ulong)(unchecked((uint)(0x10UL))));
        x0 = RuntimeCalls.InvokeDirect(0x179A984UL /* metadata target: SystemInfo.SupportsRenderTextureFormat */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD295C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)(unchecked((uint)(0xFUL))));
        x1 = 0x0UL;
        x22 = unchecked((ulong)(unchecked((uint)(0xFUL))));
        x0 = RuntimeCalls.InvokeDirect(0x179A984UL /* metadata target: SystemInfo.SupportsRenderTextureFormat */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        __arm64_flags_left_13445456 = unchecked((uint)(x0));
        __arm64_flags_right_13445456 = unchecked((uint)0x1UL);
        __arm64_flags_result_13445456 = unchecked((uint)((__arm64_flags_left_13445456) & (__arm64_flags_right_13445456)));
        x8 = unchecked((ulong)(unchecked((uint)(0x7UL))));
        RuntimeCalls.Unsupported("csel", 0xCD2958UL);
        x23 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x22)) : unchecked((uint)(x8)))));
        goto label_0xCD295C;
        label_0xCD295C:
        ;
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xCD2634UL /* metadata target: DepthOfFieldComponent.CalculateFocalLength */, x0, x1, x2, x3);
        __arm64_float_flags_left_13445476 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13445476 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_13445476 > __arm64_float_flags_right_13445476) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        if ((x21 == 0x0UL))
        {
            goto label_0xCD2F88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x21);
        x0 = x21;
        v10 = v0;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x178UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x178UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x25 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x21;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x198UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x198UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x26 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x21;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x198UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x198UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x1 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xCD26D0UL /* metadata target: DepthOfFieldComponent.CalculateMaxCoCRadius */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD2F88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCD2F88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xFA0UL))));
        x28 = 0x1A8E000UL;
        x2 = 0x0UL;
        v9 = v0;
        x1 = RuntimeMemory.ReadU64(x8);
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((x28) + (0xF90UL))));
        x0 = RuntimeCalls.InvokeDirect(0xCDF3ECUL /* metadata target: MaterialFactory.Get */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x28);
        x22 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD2A00;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCD2A00;
        label_0xCD2A00:
        ;
        if ((x22 == 0x0UL))
        {
            goto label_0xCD2F88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(x28);
        x8 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x4B4UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xB8UL))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))), 0));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x8UL))))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x25))))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x26))))))), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x0 = x22;
        v0 = v8;
        x2 = 0x0UL;
        v14 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x177B718UL /* metadata target: Material.SetFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x28);
        x0 = x22;
        v0 = v10;
        x2 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xCUL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177B718UL /* metadata target: Material.SetFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x28);
        x0 = x22;
        v0 = v9;
        x2 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x10UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177B718UL /* metadata target: Material.SetFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x28);
        v15 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))))), 0));
        x0 = x22;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x2 = 0x0UL;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x14UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177B718UL /* metadata target: Material.SetFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x28);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0))))), 0));
        x0 = x22;
        x2 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177B718UL /* metadata target: Material.SetFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCD2F88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE4E0UL /* metadata target: PostProcessingContext.get_width */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD2F88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x26 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x8;
        x1 = 0x0UL;
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x1CUL))), unchecked((uint)(x27)));
        x0 = RuntimeCalls.InvokeDirect(0xCDE4FCUL /* metadata target: PostProcessingContext.get_height */, x0, x1, x2, x3);
        if ((x25 == 0x0UL))
        {
            goto label_0xCD2F88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x29 = 0x1A8E000UL;
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((x29) + (0xD40UL))));
        x27 = 0x1A8D000UL;
        x2 = unchecked((ulong)(unchecked((uint)(x0))));
        x5 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x8 = RuntimeMemory.ReadU64(x29);
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((x27) + (0xC68UL))));
        x6 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x7 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x25;
        x1 = unchecked((ulong)(unchecked((uint)(x26))));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x4 = unchecked((ulong)(unchecked((uint)(x23))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x0UL))), x8);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x8UL))), 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0xCDF858UL /* metadata target: RenderTextureFactory.Get */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(x27);
        x25 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD2B48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCD2B48;
        label_0xCD2B48:
        ;
        x0 = 0x0UL;
        x1 = x25;
        x2 = x22;
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177861CUL /* metadata target: Graphics.Blit */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((unchecked((uint)((unchecked((uint)(x24))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCD2CF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x28);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD2B78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD2B70UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(x28);
        goto label_0xCD2B78;
        label_0xCD2B78:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = x22;
        x2 = x25;
        x3 = 0x0UL;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x20UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177AA38UL /* metadata target: Material.SetTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCD2F88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE4E0UL /* metadata target: PostProcessingContext.get_width */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD2F88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x24 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x8;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE4FCUL /* metadata target: PostProcessingContext.get_height */, x0, x1, x2, x3);
        x2 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x24))));
        x0 = RuntimeCalls.InvokeDirect(0xCD2744UL /* metadata target: DepthOfFieldComponent.CheckHistory */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = RuntimeMemory.ReadU64(x28);
        __arm64_flags_left_13446096 = unchecked((uint)(x8));
        __arm64_flags_right_13446096 = unchecked((uint)0x1UL);
        __arm64_flags_result_13446096 = unchecked((uint)((__arm64_flags_left_13446096) & (__arm64_flags_right_13446096)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((!((__arm64_flags_result_13446096 == unchecked((uint)0x0UL)))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD2BEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD2BE4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x28);
        goto label_0xCD2BEC;
        label_0xCD2BEC:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x0 = x22;
        v0 = v12;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x24UL))))));
        v1 = v11;
        v2 = v13;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177B7E8UL /* metadata target: Material.SetVector */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCD2F88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE4E0UL /* metadata target: PostProcessingContext.get_width */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD2F88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x24 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x8;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE4FCUL /* metadata target: PostProcessingContext.get_height */, x0, x1, x2, x3);
        x1 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(x24))));
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = unchecked((ulong)(unchecked((uint)(x23))));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1783E74UL /* metadata target: RenderTexture.GetTemporary */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x24 = x19;
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x20UL))));
        x8 = RuntimeMemory.ReadU64(x27);
        x23 = unchecked((ulong)(unchecked((uint)(x0))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD2C70;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCD2C70;
        label_0xCD2C70:
        ;
        x3 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x26;
        x1 = x23;
        x2 = x22;
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177861CUL /* metadata target: Graphics.Blit */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD2F88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCD2F88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x25;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDF93CUL /* metadata target: RenderTextureFactory.Release */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        x25 = RuntimeMemory.ReadU64(x24);
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD2CC0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD2CBCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCD2CC0;
        label_0xCD2CC0:
        ;
        x0 = x25;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCD2CE0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x24);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1782724UL /* metadata target: RenderTexture.ReleaseTemporary */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCD2CE0;
        label_0xCD2CE0:
        ;
        x0 = x24;
        x1 = x23;
        RuntimeMemory.WriteU64(x24, x23);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCD2CF8;
        label_0xCD2CF4:
        ;
        x23 = x25;
        goto label_0xCD2CF8;
        label_0xCD2CF8:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCD2F88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE4E0UL /* metadata target: PostProcessingContext.get_width */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD2F88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x25 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x8;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE4FCUL /* metadata target: PostProcessingContext.get_height */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x24 == 0x0UL))
        {
            goto label_0xCD2F88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD2D28UL);
        }
        __arm64_flags_left_13446440 = unchecked((uint)(x25));
        __arm64_flags_right_13446440 = unchecked((uint)0x0UL);
        x8 = RuntimeMemory.ReadU64(x29);
        RuntimeCalls.Unsupported("cinc", 0xCD2D30UL);
        x9 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)((unchecked((uint)(x25))) + (unchecked((uint)0x1UL)))) : unchecked((uint)(x25)))));
        __arm64_flags_left_13446452 = unchecked((uint)(x0));
        __arm64_flags_right_13446452 = unchecked((uint)0x0UL);
        x1 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x9))))) >> (int)(unchecked((int)(0x1UL)))))))));
        RuntimeCalls.Unsupported("cinc", 0xCD2D3CUL);
        x9 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)((unchecked((uint)(x0))) + (unchecked((uint)0x1UL)))) : unchecked((uint)(x0)))));
        x2 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x9))))) >> (int)(unchecked((int)(0x1UL)))))))));
        x4 = unchecked((ulong)(unchecked((uint)(0x9UL))));
        x6 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x7 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x24;
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x5 = unchecked((ulong)(unchecked((uint)0x0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x0UL))), x8);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x8UL))), 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0xCDF858UL /* metadata target: RenderTextureFactory.Get */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(x28);
        x24 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD2D80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(x28);
        goto label_0xCD2D80;
        label_0xCD2D80:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = x22;
        x2 = x23;
        x3 = 0x0UL;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x20UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177AA38UL /* metadata target: Material.SetTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(x27);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD2DA8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD2DA4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCD2DA8;
        label_0xCD2DA8:
        ;
        x3 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x0 = x21;
        x1 = x24;
        x2 = x22;
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177861CUL /* metadata target: Graphics.Blit */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCD2F88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE4E0UL /* metadata target: PostProcessingContext.get_width */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD2F88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x25 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x8;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE4FCUL /* metadata target: PostProcessingContext.get_height */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x21 == 0x0UL))
        {
            goto label_0xCD2F88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD2DF0UL);
        }
        __arm64_flags_left_13446640 = unchecked((uint)(x25));
        __arm64_flags_right_13446640 = unchecked((uint)0x0UL);
        x8 = RuntimeMemory.ReadU64(x29);
        RuntimeCalls.Unsupported("cinc", 0xCD2DF8UL);
        x9 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)((unchecked((uint)(x25))) + (unchecked((uint)0x1UL)))) : unchecked((uint)(x25)))));
        __arm64_flags_left_13446652 = unchecked((uint)(x0));
        __arm64_flags_right_13446652 = unchecked((uint)0x0UL);
        x1 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x9))))) >> (int)(unchecked((int)(0x1UL)))))))));
        RuntimeCalls.Unsupported("cinc", 0xCD2E04UL);
        x9 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)((unchecked((uint)(x0))) + (unchecked((uint)0x1UL)))) : unchecked((uint)(x0)))));
        x2 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x9))))) >> (int)(unchecked((int)(0x1UL)))))))));
        x4 = unchecked((ulong)(unchecked((uint)(0x9UL))));
        x6 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x7 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x21;
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x5 = unchecked((ulong)(unchecked((uint)0x0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x0UL))), x8);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x8UL))), 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0xCDF858UL /* metadata target: RenderTextureFactory.Get */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x1CUL))))));
        x21 = x0;
        x0 = x24;
        x1 = x21;
        x3 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)(0x3UL)))))));
        x2 = x22;
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177861CUL /* metadata target: Graphics.Blit */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x3 = unchecked((ulong)(unchecked((uint)(0x7UL))));
        x0 = x21;
        x1 = x24;
        x2 = x22;
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177861CUL /* metadata target: Graphics.Blit */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x20 == 0x0UL))
        {
            goto label_0xCD2F88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x28);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x0 = x20;
        v0 = v8;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v1 = v10;
        v2 = v9;
        x2 = 0x0UL;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x28UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177B7E8UL /* metadata target: Material.SetVector */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD2F88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD2F88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD2F88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x14UL))))));
        __arm64_flags_left_13446828 = unchecked((uint)(x8));
        __arm64_flags_right_13446828 = unchecked((uint)0x6UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13446828) - (__arm64_flags_right_13446828))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCD2EE0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xFA8UL))));
        x0 = x20;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x177ADF0UL /* metadata target: Material.EnableKeyword */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCD2F88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE43CUL /* metadata target: PostProcessingContext.Interrupt */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCD2F40;
        label_0xCD2EE0:
        ;
        x0 = RuntimeMemory.ReadU64(x28);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD2EF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD2EECUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(x28);
        goto label_0xCD2EF4;
        label_0xCD2EF4:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = x20;
        x2 = x24;
        x3 = 0x0UL;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(x8)));
        x0 = RuntimeCalls.InvokeDirect(0x177AA38UL /* metadata target: Material.SetTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x28);
        x0 = x20;
        x2 = x23;
        x3 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x4UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177AA38UL /* metadata target: Material.SetTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xF98UL))));
        x0 = x20;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x177ADF0UL /* metadata target: Material.EnableKeyword */, x0, x1, x2, x3);
        goto label_0xCD2F40;
        label_0xCD2F40:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD2F88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCD2F88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x21;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xB0UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xA0UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x90UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        __arm64_pair_address_13447020 = unchecked((ulong)((sp) + (0x50UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13447020)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13447020) + (0x8UL))))), 0));
        __arm64_pair_address_13447024 = unchecked((ulong)((sp) + (0x40UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13447024)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13447024) + (0x8UL))))), 0));
        __arm64_pair_address_13447028 = unchecked((ulong)((sp) + (0x30UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13447028)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13447028) + (0x8UL))))), 0));
        __arm64_pair_address_13447032 = unchecked((ulong)((sp) + (0x20UL)));
        v15 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13447032)), 0));
        v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13447032) + (0x8UL))))), 0));
        x2 = 0x0UL;
        sp = unchecked((ulong)((sp) + (0xC0UL)));
        return RuntimeCalls.InvokeDirect(0xCDF93CUL /* metadata target: RenderTextureFactory.Release */);
        label_0xCD2F88:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `DepthOfFieldComponent.OnDisable` — RVA `0xcd2f8c`

- Lift status: **exact**; input span: 128 bytes; span to next metadata RVA: 128 bytes.
- Metadata signature: `public override void OnDisable() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=20 (informational only).

```csharp
public static ulong DepthOfFieldComponent_OnDisable_RVAcd2f8c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x5C4UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD2FC0;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x5C4UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCD2FC0;
        label_0xCD2FC0:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD2FD4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD2FD0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCD2FD4;
        label_0xCD2FD4:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCD2FF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x19);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1782724UL /* metadata target: RenderTexture.ReleaseTemporary */, x0, x1, x2, x3);
        goto label_0xCD2FF4;
        label_0xCD2FF4:
        ;
        RuntimeMemory.WritePtr(x19, 0x0UL);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```

## `DepthOfFieldComponent.ctor` — RVA `0xcd300c`

- Lift status: **exact**; input span: 72 bytes; span to next metadata RVA: 72 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=12 (informational only).

```csharp
public static ulong DepthOfFieldComponent_ctor_RVAcd300c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x21 = 0x1A8E000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x5C5UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xFB0UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD3040;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xFB0UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x5C5UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCD3040;
        label_0xCD3040:
        ;
        x1 = RuntimeMemory.ReadU64(x21);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x11689F8UL);
        return default(ulong);
    }
```
