# `vfxController` — TypeDefIndex 3293

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `GameObject[]` | `starFx01Prefabs` |
| `0x28` | `GameObject[]` | `starFx02Prefabs` |
| `0x30` | `GameObject[]` | `starFx03Prefabs` |
| `0x38` | `GameObject[]` | `starFx04Prefabs` |
| `0x40` | `GameObject[]` | `starFx05Prefabs` |
| `0x48` | `GameObject[]` | `DesStarFxObjs` |
| `0x50` | `GameObject[]` | `bgFxPrefabs` |
| `0x58` | `int` | `currentStarImage` |
| `0x5C` | `int` | `currentStarFx` |
| `0x60` | `int` | `currentLevel` |
| `0x64` | `int` | `currentBgFx` |

## `vfxController.Start` — RVA `0xc76308`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `private void Start() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong vfxController_Start_RVAc76308(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        x8 = 0x432000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x8) + (0x7E0UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x8) + (0x7E0UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x0) + (0x58UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x0) + (0x58UL))), v0);
#endif
        return x0;
        return default(ulong);
    }
```

## `vfxController.ChangedStarImage` — RVA `0xc76318`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public void ChangedStarImage(int i) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong vfxController_ChangedStarImage_RVAc76318(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x58UL))), unchecked((uint)(x1)));
        return RuntimeCalls.InvokeDirect(0xC76320UL /* metadata target: vfxController.PlayStarFX */);
        return default(ulong);
    }
```

## `vfxController.PlayStarFX` — RVA `0xc76320`

- Lift status: **exact**; input span: 508 bytes; span to next metadata RVA: 508 bytes.
- Metadata signature: `public void PlayStarFX() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=90 (informational only).

```csharp
public static ulong vfxController_PlayStarFX_RVAc76320(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13067184 = default(uint);
        uint __arm64_flags_left_13067196 = default(uint);
        uint __arm64_flags_left_13067268 = default(uint);
        uint __arm64_flags_left_13067304 = default(uint);
        uint __arm64_flags_left_13067352 = default(uint);
        uint __arm64_flags_right_13067184 = default(uint);
        uint __arm64_flags_right_13067196 = default(uint);
        uint __arm64_flags_right_13067268 = default(uint);
        uint __arm64_flags_right_13067304 = default(uint);
        uint __arm64_flags_right_13067352 = default(uint);
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
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
        x20 = 0x1BAB000UL;
        x21 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x3A7UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x9D8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC7637C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x9E0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x9D8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x9D0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x3A7UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC7637C;
        label_0xC7637C:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794E0CUL /* metadata target: GameObject.FindGameObjectsWithTag */, x0, x1, x2, x3);
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x48UL))), x0);
        x1 = x0;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x22 = RuntimeMemory.ReadU64(x20);
        if ((x22 == 0x0UL))
        {
            goto label_0xC76518;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x22) + (0x18UL))))));
        x21 = 0x1A8C000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        __arm64_flags_left_13067184 = unchecked((uint)(x8));
        __arm64_flags_right_13067184 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13067184) - (__arm64_flags_right_13067184))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13067184)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13067184)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13067184) - (__arm64_flags_right_13067184))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13067184)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC7640C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC763BC;
        label_0xC763BC:
        ;
        __arm64_flags_left_13067196 = unchecked((uint)(x23));
        __arm64_flags_right_13067196 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13067196 >= __arm64_flags_right_13067196))
        {
            goto label_0xC76514;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x22) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x23))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC76518;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1795148UL /* metadata target: GameObject.get_gameObject */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x20 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC763F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC763F0;
        label_0xC763F0:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798A20UL /* metadata target: Object.Destroy */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x22) + (0x18UL))))));
        x23 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x23))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13067268 = unchecked((uint)(x23));
        __arm64_flags_right_13067268 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13067268) - (__arm64_flags_right_13067268))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13067268)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13067268)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13067268) - (__arm64_flags_right_13067268))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13067268)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC763BC;
        }
        else
        {
            goto label_0xC7640C;
        }
        label_0xC7640C:
        ;
        x22 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x19) + (0x64UL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x9E0UL))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC76454;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x50UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC76518;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x18UL))))));
        __arm64_flags_left_13067304 = unchecked((uint)(x8));
        __arm64_flags_right_13067304 = unchecked((uint)(x10));
        if ((__arm64_flags_left_13067304 >= __arm64_flags_right_13067304))
        {
            goto label_0xC76514;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)((x9) + (unchecked((ulong)((x8) << (int)(unchecked((int)(0x3UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC76448;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC76444UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC76448;
        label_0xC76448:
        ;
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xD29F50UL, x0, x1, x2, x3);
        goto label_0xC76454;
        label_0xC76454:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x58UL))))));
        __arm64_flags_left_13067352 = unchecked((uint)(x8));
        __arm64_flags_right_13067352 = unchecked((uint)0x4UL);
        if (((__arm64_flags_left_13067352 >= __arm64_flags_right_13067352) && (!((unchecked((uint)((__arm64_flags_left_13067352) - (__arm64_flags_right_13067352))) == unchecked((uint)0x0UL))))))
        {
            goto label_0xC76504;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x452000UL;
        x9 = unchecked((ulong)((x9) + (0x26EUL)));
        x10 = 0xC76478UL;
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (unchecked((ulong)(unchecked((uint)(x8))))))))))));
        x10 = unchecked((ulong)((x10) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) << (int)(unchecked((int)(unchecked((uint)(0x2UL))))))))))));
        return RuntimeCalls.InvokeIndirect(x10);
        label_0xC76504:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC76514:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        goto label_0xC76518;
        label_0xC76518:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `vfxController.ChangedStarFX` — RVA `0xc7651c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public void ChangedStarFX(int i) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong vfxController_ChangedStarFX_RVAc7651c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x5CUL))), unchecked((uint)(x1)));
        return RuntimeCalls.InvokeDirect(0xC76320UL /* metadata target: vfxController.PlayStarFX */);
        return default(ulong);
    }
```

## `vfxController.ChangedLevel` — RVA `0xc76524`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public void ChangedLevel(int i) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong vfxController_ChangedLevel_RVAc76524(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x60UL))), unchecked((uint)(x1)));
        return RuntimeCalls.InvokeDirect(0xC76320UL /* metadata target: vfxController.PlayStarFX */);
        return default(ulong);
    }
```

## `vfxController.ChangedBgFx` — RVA `0xc7652c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public void ChangedBgFx(int i) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong vfxController_ChangedBgFx_RVAc7652c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x64UL))), unchecked((uint)(x1)));
        return RuntimeCalls.InvokeDirect(0xC76320UL /* metadata target: vfxController.PlayStarFX */);
        return default(ulong);
    }
```

## `vfxController.ctor` — RVA `0xc76534`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong vfxController_ctor_RVAc76534(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x1 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */);
        return default(ulong);
    }
```
