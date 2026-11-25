# `NPCSpawner` — TypeDefIndex 3345

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `WaveManager` | `WaveManager` |
| `0x28` | `GameObject` | `NPCPrefab` |
| `0x30` | `float` | `spawnDelay` |
| `0x34` | `float` | `spawnTime` |
| `0x38` | `GameObject` | `NPCInstance` |
| `0x40` | `List<AI>` | `Npcs` |
| `0x48` | `float` | `timeLeft` |
| `0x50` | `WaypointGroup` | `waypointGroup` |
| `0x58` | `int` | `firstWaypoint` |
| `0x60` | `AI` | `AIcomponent` |
| `0x68` | `bool` | `unlimitedSpawning` |
| `0x69` | `bool` | `huntPlayer` |
| `0x6C` | `int` | `maxActiveNpcs` |
| `0x70` | `int` | `NpcsToSpawn` |
| `0x74` | `int` | `spawnedNpcAmt` |
| `0x78` | `bool` | `pauseSpawning` |

## `NPCSpawner.UnregisterSpawnedNPC` — RVA `0xc83f28`

- Lift status: **partial**; input span: 372 bytes; span to next metadata RVA: 372 bytes.
- Metadata signature: `public void UnregisterSpawnedNPC(AI NpcAI) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=57 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ge' at 0xc84060; reason: Unknown IR expression at 0xc84060

```csharp
public static ulong NPCSpawner_UnregisterSpawnedNPC_RVAc83f28(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13123492 = default(uint);
        uint __arm64_flags_left_13123672 = default(uint);
        uint __arm64_flags_right_13123492 = default(uint);
        uint __arm64_flags_right_13123672 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x427UL))))))));
        x20 = x1;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC83F84;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE58UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD88UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD90UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x427UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC83F84;
        label_0xC83F84:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC83FF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x24 = 0x1A8D000UL;
        x23 = 0x1A8C000UL;
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xD90UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xD8UL))));
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC83FA0;
        label_0xC83FA0:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        __arm64_flags_left_13123492 = unchecked((uint)(x21));
        __arm64_flags_right_13123492 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13123492) - (__arm64_flags_right_13123492))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13123492)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13123492)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13123492) - (__arm64_flags_right_13123492))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13123492)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC84064;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(x24);
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x23);
        x22 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC83FD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC83FD0;
        label_0xC83FD0:
        ;
        x0 = x22;
        x1 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC83FF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        if ((x0 != 0x0UL))
        {
            goto label_0xC83FA0;
        }
        else
        {
            goto label_0xC83FF0;
        }
        label_0xC83FF0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC83FF4;
        label_0xC83FF4:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC83FF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE58UL))));
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x10A48FCUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(x23);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC84024;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC84020UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC84024;
        label_0xC84024:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC84064;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC83FF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1791624UL /* metadata target: Behaviour.get_enabled */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC84064;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC83FF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x44UL))))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((unchecked((ulong)((x0) + (0x44UL)))) + (0x4UL))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13123672 = unchecked((uint)(x8));
        __arm64_flags_right_13123672 = unchecked((uint)(x9));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x48UL))), unchecked((uint)(x8)));
        RuntimeCalls.Unsupported("b.ge", 0xC84060UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC84078;
        }
        else
        {
            goto label_0xC84064;
        }
        label_0xC84064:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC84078:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xC87770UL /* metadata target: WaveManager.StartWave */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */);
        return default(ulong);
    }
```

## `NPCSpawner.Start` — RVA `0xc873b0`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `private void Start() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong NPCSpawner_Start_RVAc873b0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFC4800000UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x34UL))), unchecked((uint)(x8)));
        return x0;
        return default(ulong);
    }
```

## `NPCSpawner.Update` — RVA `0xc873bc`

- Lift status: **exact**; input span: 168 bytes; span to next metadata RVA: 168 bytes.
- Metadata signature: `private void Update() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=19 (informational only).

```csharp
public static ulong NPCSpawner_Update_RVAc873bc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13136900 = default(uint);
        uint __arm64_flags_left_13136920 = default(uint);
        uint __arm64_flags_right_13136900 = default(uint);
        uint __arm64_flags_right_13136920 = default(uint);
        float __arm64_float_flags_left_13136944 = default(float);
        float __arm64_float_flags_right_13136944 = default(float);
        ulong __arm64_pair_address_13136828 = default(ulong);
        ulong __arm64_pair_address_13136928 = default(ulong);
        ulong __arm64_pair_address_13136968 = default(ulong);
        ulong __arm64_pair_address_13136984 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_13136828 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13136828, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13136828) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = __arm64_pair_address_13136828;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x10UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x425UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC873EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD88UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x425UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC873EC;
        label_0xC873EC:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x78UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC87450;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC87460;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x6CUL))))));
        __arm64_flags_left_13136900 = unchecked((uint)(x8));
        __arm64_flags_right_13136900 = unchecked((uint)(x9));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13136900) - (__arm64_flags_right_13136900))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13136900)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13136900)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13136900) - (__arm64_flags_right_13136900))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13136900)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC87450;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x68UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC87420;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x70UL))))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((unchecked((ulong)((x19) + (0x70UL)))) + (0x4UL))))));
        __arm64_flags_left_13136920 = unchecked((uint)(x8));
        __arm64_flags_right_13136920 = unchecked((uint)(x9));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13136920) - (__arm64_flags_right_13136920))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13136920)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13136920)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13136920) - (__arm64_flags_right_13136920))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13136920)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC87450;
        }
        else
        {
            goto label_0xC87420;
        }
        label_0xC87420:
        ;
        __arm64_pair_address_13136928 = unchecked((ulong)((x19) + (0x30UL)));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13136928)), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13136928) + (0x4UL))))), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179AD30UL /* metadata target: Time.get_time */, x0, x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_13136944 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13136944 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13136944 >= __arm64_float_flags_right_13136944) || ((__arm64_float_flags_left_13136944 != __arm64_float_flags_left_13136944) || (__arm64_float_flags_right_13136944 != __arm64_float_flags_right_13136944))))
        {
            goto label_0xC87450;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        __arm64_pair_address_13136968 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13136968)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13136968) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_13136968) + (0x30UL)));
        return RuntimeCalls.InvokeDirect(0xC87464UL /* metadata target: NPCSpawner.Spawn */);
        label_0xC87450:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        __arm64_pair_address_13136984 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13136984)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13136984) + (0x8UL))))), 0));
        return x0;
        label_0xC87460:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `NPCSpawner.Spawn` — RVA `0xc87464`

- Lift status: **exact**; input span: 780 bytes; span to next metadata RVA: 780 bytes.
- Metadata signature: `private void Spawn(GameObject NpcPrefab) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=111 (informational only).

```csharp
public static ulong NPCSpawner_Spawn_RVAc87464(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13137404 = default(uint);
        uint __arm64_flags_right_13137404 = default(uint);
        ulong __arm64_load_address_13137764 = default(ulong);
        ulong __arm64_pair_address_13137000 = default(ulong);
        ulong __arm64_pair_address_13137004 = default(ulong);
        ulong __arm64_pair_address_13137008 = default(ulong);
        ulong __arm64_pair_address_13137752 = default(ulong);
        ulong __arm64_pair_address_13137756 = default(ulong);
        ulong __arm64_pair_address_13137760 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v13 = default(RuntimeVector128);
        RuntimeVector128 v14 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x12 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFA0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v14.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFA0UL)));
        __arm64_pair_address_13137000 = unchecked((ulong)((sp) + (0x8UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13137000, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13137000) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13137004 = unchecked((ulong)((sp) + (0x18UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13137004, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13137004) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13137008 = unchecked((ulong)((sp) + (0x28UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13137008, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13137008) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x38UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x22 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x426UL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD8UL))));
        x20 = x1;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC874EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF18UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCE0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCF0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD60UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x9C8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x426UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC874EC;
        label_0xC874EC:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC87500;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC874FCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC87500;
        label_0xC87500:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8774C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC8776C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        v8 = v0;
        v9 = v1;
        v10 = v2;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC8776C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D6F0UL /* metadata target: Transform.get_rotation */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        v11 = v0;
        v12 = v1;
        v13 = v2;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        v14 = v3;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC8756C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC87568UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC8756C;
        label_0xC8756C:
        ;
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x9C8UL))));
        x0 = x20;
        v0 = v8;
        v1 = v9;
        x1 = RuntimeMemory.ReadU64(x8);
        v2 = v10;
        x0 = RuntimeCalls.InvokeDirect(0xD2A1ACUL, x0, x1, x2, x3);
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x38UL))), x0);
        x1 = x0;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xC8776C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCE0UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8776C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = 0x1A8D000UL;
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xCF0UL))));
        x11 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x1CUL))))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        x10 = RuntimeMemory.ReadU64(x10);
        x11 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0x1CUL))), unchecked((uint)(x11)));
        if ((x9 == 0x0UL))
        {
            goto label_0xC8776C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x11 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x8) + (0x18UL))))))));
        x12 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x18UL))))));
        x20 = x0;
        __arm64_flags_left_13137404 = unchecked((uint)(x11));
        __arm64_flags_right_13137404 = unchecked((uint)(x12));
        if ((__arm64_flags_left_13137404 >= __arm64_flags_right_13137404))
        {
            goto label_0xC87620;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) + (unchecked((uint)(0x1UL)))))));
        x0 = unchecked((ulong)((x9) + (unchecked((ulong)((x11) << (int)(unchecked((int)(0x3UL))))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0x18UL))), unchecked((uint)(x10)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x20UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xC87638;
        label_0xC87620:
        ;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x10))))) + (0x20UL))));
        x0 = x8;
        x1 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xC0UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x70UL))));
        x0 = RuntimeCalls.InvokeDirect(0x10A3390UL, x0, x1, x2, x3);
        goto label_0xC87638;
        label_0xC87638:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC8776C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xF18UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xC8776C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x0;
        x0 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x78UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x69UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8767C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x114UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC8767C;
        label_0xC8767C:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x20UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x50UL))));
        x21 = unchecked((ulong)((x20) + (0x120UL)));
        x0 = x21;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x120UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x58UL))))));
        x0 = x20;
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x116UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x12CUL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0x128UL))), unchecked((uint)(x8)));
        x0 = RuntimeCalls.InvokeDirect(0xC7D2A0UL /* metadata target: AI.SpawnNPC */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179AD30UL /* metadata target: Time.get_time */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x69UL))))))));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x34UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC876EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8776C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        if ((x0 != 0x0UL))
        {
            goto label_0xC87720;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC876E8UL);
        }
        goto label_0xC8776C;
        label_0xC876EC:
        ;
        x8 = RuntimeMemory.ReadU64(x21);
        if ((x8 == 0x0UL))
        {
            goto label_0xC8776C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8776C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x58UL))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD60UL))));
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC8776C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC8776C;
        }
        else
        {
            goto label_0xC87720;
        }
        label_0xC87720:
        ;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteF32(unchecked((ulong)((x20) + (0x144UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x20) + (0x148UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x130UL))), unchecked((byte)(unchecked((uint)(x8)))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x25EUL))), unchecked((byte)(unchecked((uint)(x8)))));
        RuntimeMemory.WriteF32(unchecked((ulong)((x20) + (0x14CUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x74UL))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x74UL))), unchecked((uint)(x8)));
        goto label_0xC8774C;
        label_0xC8774C:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x38UL))));
        __arm64_pair_address_13137752 = unchecked((ulong)((sp) + (0x28UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13137752)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13137752) + (0x8UL))))), 0));
        __arm64_pair_address_13137756 = unchecked((ulong)((sp) + (0x18UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13137756)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13137756) + (0x8UL))))), 0));
        __arm64_pair_address_13137760 = unchecked((ulong)((sp) + (0x8UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13137760)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13137760) + (0x8UL))))), 0));
        __arm64_load_address_13137764 = sp;
        v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_13137764)), 0));
        return x0;
        label_0xC8776C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `NPCSpawner.ctor` — RVA `0xc877dc`

- Lift status: **exact**; input span: 168 bytes; span to next metadata RVA: 168 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=25 (informational only).

```csharp
public static ulong NPCSpawner_ctor_RVAc877dc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
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
        x22 = 0x1BAB000UL;
        x21 = 0x1A8D000UL;
        x20 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x428UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xF08UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xF10UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC87828;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF10UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF08UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x428UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC87828;
        label_0xC87828:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0x41F00000UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x30UL))), unchecked((uint)(x8)));
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x20);
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x10A2B64UL, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x40UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = 0x431000UL;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0xD88UL))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x58UL))), unchecked((uint)(x8)));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x68UL))), unchecked((byte)(unchecked((uint)(x8)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x6CUL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
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
