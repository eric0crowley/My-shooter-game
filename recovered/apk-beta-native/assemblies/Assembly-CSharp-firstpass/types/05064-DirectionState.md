# `DirectionState` — TypeDefIndex 5064

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `Dir` | `dirCur` |
| `0x14` | `Dir` | `dirPrev` |
| `0x18` | `Dir` | `dirOriginalCur` |
| `0x1C` | `Dir` | `dirOriginalPrev` |

## `DirectionState.ctor` — RVA `0xc5ae6c`

- Lift status: **exact**; input span: 28 bytes; span to next metadata RVA: 28 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong DirectionState_ctor_RVAc5ae6c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x1 = 0x0UL;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((x19) + (0x10UL)))) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((x19) + (0x10UL)))) + (0x8UL))), 0x0UL);
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```

## `DirectionState.Reset` — RVA `0xc5ae88`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public void Reset() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong DirectionState_Reset_RVAc5ae88(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((x0) + (0x10UL)))) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((x0) + (0x10UL)))) + (0x8UL))), 0x0UL);
        return x0;
        return default(ulong);
    }
```

## `DirectionState.GetCur` — RVA `0xc5ae90`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public Dir GetCur() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint DirectionState_GetCur_RVAc5ae90(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x10UL))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `DirectionState.GetPrev` — RVA `0xc5ae98`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public Dir GetPrev() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint DirectionState_GetPrev_RVAc5ae98(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x14UL))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `DirectionState.GetOriginal` — RVA `0xc5aea0`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public Dir GetOriginal() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint DirectionState_GetOriginal_RVAc5aea0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `DirectionState.GetPrevOriginal` — RVA `0xc5aea8`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public Dir GetPrevOriginal() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint DirectionState_GetPrevOriginal_RVAc5aea8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x1CUL))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `DirectionState.JustPressed` — RVA `0xc5aeb0`

- Lift status: **exact**; input span: 36 bytes; span to next metadata RVA: 36 bytes.
- Metadata signature: `public bool JustPressed(Dir dir) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static uint DirectionState_JustPressed_RVAc5aeb0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12955316 = default(uint);
        uint __arm64_flags_left_12955336 = default(uint);
        uint __arm64_flags_right_12955316 = default(uint);
        uint __arm64_flags_right_12955336 = default(uint);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x14UL))))));
        __arm64_flags_left_12955316 = unchecked((uint)(x8));
        __arm64_flags_right_12955316 = unchecked((uint)(x1));
        if ((!((unchecked((uint)((__arm64_flags_left_12955316) - (__arm64_flags_right_12955316))) == unchecked((uint)0x0UL)))))
        {
            label_0xC5AEC4:
            ;
            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x0))))) + (0x10UL))))));
            __arm64_flags_left_12955336 = unchecked((uint)(x8));
            __arm64_flags_right_12955336 = unchecked((uint)(x1));
            x0 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_12955336) - (__arm64_flags_right_12955336))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
            return unchecked((uint)(x0));
        }
        else
        {
            x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
            return unchecked((uint)(x0));
        }
        return default(uint);
    }
```

## `DirectionState.JustReleased` — RVA `0xc5aed4`

- Lift status: **exact**; input span: 36 bytes; span to next metadata RVA: 36 bytes.
- Metadata signature: `public bool JustReleased(Dir dir) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static uint DirectionState_JustReleased_RVAc5aed4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12955352 = default(uint);
        uint __arm64_flags_left_12955364 = default(uint);
        uint __arm64_flags_right_12955352 = default(uint);
        uint __arm64_flags_right_12955364 = default(uint);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x14UL))))));
        __arm64_flags_left_12955352 = unchecked((uint)(x8));
        __arm64_flags_right_12955352 = unchecked((uint)(x1));
        if ((!((unchecked((uint)((__arm64_flags_left_12955352) - (__arm64_flags_right_12955352))) == unchecked((uint)0x0UL)))))
        {
            label_0xC5AEF0:
            ;
            x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
            return unchecked((uint)(x0));
        }
        else
        {
            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x10UL))))));
            __arm64_flags_left_12955364 = unchecked((uint)(x8));
            __arm64_flags_right_12955364 = unchecked((uint)(x1));
            x0 = unchecked((ulong)(((!((unchecked((uint)((__arm64_flags_left_12955364) - (__arm64_flags_right_12955364))) == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
            return unchecked((uint)(x0));
        }
        return default(uint);
    }
```

## `DirectionState.BeginFrame` — RVA `0xc5aef8`

- Lift status: **exact**; input span: 20 bytes; span to next metadata RVA: 20 bytes.
- Metadata signature: `public void BeginFrame() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong DirectionState_BeginFrame_RVAc5aef8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x10UL))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x14UL))), unchecked((uint)(x8)));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x1CUL))), unchecked((uint)(x9)));
        return x0;
        return default(ulong);
    }
```

## `DirectionState.SetDir` — RVA `0xc5af0c`

- Lift status: **partial**; input span: 200 bytes; span to next metadata RVA: 200 bytes.
- Metadata signature: `public void SetDir(Dir dir, DirectionState.OriginalDirResetMode resetMode) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=21 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'cneg' at 0xc5af8c; reason: Unknown IR expression at 0xc5af8c; reason: Unsupported instruction 'csel' at 0xc5afa0; reason: Unknown IR expression at 0xc5afa0

```csharp
public static ulong DirectionState_SetDir_RVAc5af0c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12955424 = default(uint);
        uint __arm64_flags_left_12955520 = default(uint);
        uint __arm64_flags_left_12955536 = default(uint);
        uint __arm64_flags_left_12955544 = default(uint);
        uint __arm64_flags_left_12955556 = default(uint);
        uint __arm64_flags_right_12955424 = default(uint);
        uint __arm64_flags_right_12955520 = default(uint);
        uint __arm64_flags_right_12955536 = default(uint);
        uint __arm64_flags_right_12955544 = default(uint);
        uint __arm64_flags_right_12955556 = default(uint);
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x14UL))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x10UL))), unchecked((uint)(x1)));
        __arm64_flags_left_12955424 = unchecked((uint)(x8));
        __arm64_flags_right_12955424 = unchecked((uint)(x1));
        if ((unchecked((uint)((__arm64_flags_left_12955424) - (__arm64_flags_right_12955424))) == unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x19 = x0;
            if ((unchecked((uint)(x1)) == unchecked((uint)0x0UL)))
            {
                label_0xC5AFB8:
                ;
                RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x18UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
            }
            else
            {
                if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
                {
                    label_0xC5AFC0:
                    ;
                    RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x18UL))), unchecked((uint)(x1)));
                }
                else
                {
                    x20 = unchecked((ulong)(unchecked((uint)(x2))));
                    if ((unchecked((uint)(x2)) == unchecked((uint)0x0UL)))
                    {
                    }
                    else
                    {
                        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x1CUL))))));
                        x0 = RuntimeCalls.InvokeDirect(0xC59650UL /* metadata target: CFUtils.DirDeltaAngle */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
                        x22 = 0x1BAB000UL;
                        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x2CDUL))))))));
                        x21 = unchecked((ulong)(unchecked((uint)(x0))));
                        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
                        {
                        }
                        else
                        {
                            x0 = 0x1A8C000UL;
                            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA60UL))));
                            // Likely IL2CPP class initialization helper (guarded call).
                            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
                            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                            RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x2CDUL))), unchecked((byte)(unchecked((uint)(x8)))));
                        }
                        label_0xC5AF68:
                        ;
                        x8 = 0x1A8C000UL;
                        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA60UL))));
                        x0 = RuntimeMemory.ReadU64(x8);
                        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
                        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
                        {
                        }
                        else
                        {
                            x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
                        }
                        label_0xC5AF80:
                        ;
                        __arm64_flags_left_12955520 = unchecked((uint)(x21));
                        __arm64_flags_right_12955520 = unchecked((uint)0x0UL);
                        x8 = unchecked((ulong)(unchecked((uint)(0xB4UL))));
                        x9 = unchecked((ulong)(unchecked((uint)(0x87UL))));
                        RuntimeCalls.Unsupported("cneg", 0xC5AF8CUL);
                        x10 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)((-(unchecked((uint)(x21)))))) : unchecked((uint)(x21)))));
                        __arm64_flags_left_12955536 = unchecked((uint)(x20));
                        __arm64_flags_right_12955536 = unchecked((uint)0x2UL);
                        x8 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_12955536) - (__arm64_flags_right_12955536))) == unchecked((uint)0x0UL)) ? unchecked((uint)(x9)) : unchecked((uint)(x8)))));
                        __arm64_flags_left_12955544 = unchecked((uint)(x20));
                        __arm64_flags_right_12955544 = unchecked((uint)0x3UL);
                        x9 = unchecked((ulong)(unchecked((uint)(0x5AUL))));
                        RuntimeCalls.Unsupported("csel", 0xC5AFA0UL);
                        x8 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x9)) : unchecked((uint)(x8)))));
                        __arm64_flags_left_12955556 = unchecked((uint)(x10));
                        __arm64_flags_right_12955556 = unchecked((uint)(x8));
                        if ((!((__arm64_flags_left_12955556 >= __arm64_flags_right_12955556))))
                        {
                        }
                        else
                        {
                            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x10UL))))));
                            RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x18UL))), unchecked((uint)(x8)));
                        }
                    }
                }
            }
        }
        label_0xC5AFC4:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```
