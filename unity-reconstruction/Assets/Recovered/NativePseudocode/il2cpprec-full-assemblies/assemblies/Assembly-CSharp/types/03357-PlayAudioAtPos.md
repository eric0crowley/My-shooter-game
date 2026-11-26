# `PlayAudioAtPos` — TypeDefIndex 3357

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## `PlayAudioAtPos.PlayClipAt` — RVA `0xc8d260`

- Lift status: **exact**; input span: 412 bytes; span to next metadata RVA: 412 bytes.
- Metadata signature: `public static AudioSource PlayClipAt(AudioClip clip, Vector3 pos, float vol, float blend = 1.0, float pitch = 1.0, float minDist = 1.0, float maxDist = 500.0) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=67 (informational only).

```csharp
public static ulong PlayAudioAtPos_PlayClipAt_RVAc8d260(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_13161056 = default(ulong);
        ulong __arm64_pair_address_13161060 = default(ulong);
        ulong __arm64_pair_address_13161064 = default(ulong);
        ulong __arm64_pair_address_13161068 = default(ulong);
        ulong __arm64_pair_address_13161252 = default(ulong);
        ulong __arm64_pair_address_13161256 = default(ulong);
        ulong __arm64_pair_address_13161444 = default(ulong);
        ulong __arm64_pair_address_13161448 = default(ulong);
        ulong __arm64_pair_address_13161452 = default(ulong);
        ulong __arm64_pair_address_13161456 = default(ulong);
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
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v6 = default(RuntimeVector128);
        RuntimeVector128 v7 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_13161056 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFA0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13161056, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v15.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13161056) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v14.GetUInt64(0)))));
        sp = __arm64_pair_address_13161056;
        __arm64_pair_address_13161060 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13161060, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13161060) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13161064 = unchecked((ulong)((sp) + (0x20UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13161064, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13161064) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13161068 = unchecked((ulong)((sp) + (0x30UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13161068, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13161068) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x21 = 0x1A8E000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x43CUL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x30UL))));
        v10 = v7;
        v11 = v6;
        v8 = v5;
        v12 = v4;
        v9 = v3;
        v13 = v2;
        v14 = v1;
        v15 = v0;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x30UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x38UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x43CUL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC8D2D0:
        ;
        x8 = RuntimeMemory.ReadU64(x21);
        x21 = 0x1BAB000UL;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x2CBUL))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x20 = RuntimeMemory.ReadU64(x8);
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD88UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x2CBUL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC8D2FC:
        ;
        if ((x20 == 0x0UL))
        {
        }
        else
        {
            x8 = 0x1A8C000UL;
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD88UL))));
            x0 = x20;
            x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
            x8 = RuntimeMemory.ReadU64(x8);
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
            __arm64_pair_address_13161252 = unchecked((ulong)((x8) + (0x8UL)));
            v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13161252)), 0));
            v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13161252) + (0x4UL))))), 0));
            __arm64_pair_address_13161256 = x8;
            v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13161256)), 0));
            v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13161256) + (0x4UL))))), 0));
            x0 = RuntimeCalls.InvokeDirect(0xC8D3FCUL /* metadata target: AzuObjectPool.SpawnPooledObj */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
            if ((x0 == 0x0UL))
            {
            }
            else
            {
                x8 = 0x1A8E000UL;
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x38UL))));
                x1 = RuntimeMemory.ReadU64(x8);
                x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
                if ((x0 == 0x0UL))
                {
                }
                else
                {
                    x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x20UL))));
                    x20 = x0;
                    if ((x21 == 0x0UL))
                    {
                    }
                    else
                    {
                        x0 = x21;
                        x1 = x19;
                        x2 = 0x0UL;
                        x0 = RuntimeCalls.InvokeDirect(0x176A588UL /* metadata target: AudioSource.set_clip */, x0, x1, x2, x3);
                        x0 = x21;
                        x1 = 0x0UL;
                        x0 = RuntimeCalls.InvokeDirect(0x176AAA8UL /* metadata target: AudioSource.set_spatialBlend */, x0, x1, x2, x3);
                        x0 = x21;
                        x1 = 0x0UL;
                        x0 = RuntimeCalls.InvokeDirect(0x176ADACUL /* metadata target: AudioSource.set_minDistance */, x0, x1, x2, x3);
                        x0 = x21;
                        x1 = 0x0UL;
                        x0 = RuntimeCalls.InvokeDirect(0x176ADF8UL /* metadata target: AudioSource.set_maxDistance */, x0, x1, x2, x3);
                        x0 = x21;
                        x1 = 0x0UL;
                        x0 = RuntimeCalls.InvokeDirect(0x176A478UL /* metadata target: AudioSource.set_volume */, x0, x1, x2, x3);
                        x0 = x21;
                        x1 = 0x0UL;
                        x0 = RuntimeCalls.InvokeDirect(0x176A500UL /* metadata target: AudioSource.set_pitch */, x0, x1, x2, x3);
                        x0 = x21;
                        x1 = 0x0UL;
                        x0 = RuntimeCalls.InvokeDirect(0x176A5CCUL /* metadata target: AudioSource.Play */, x0, x1, x2, x3);
                        x0 = x20;
                        x0 = RuntimeCalls.InvokeDirect(0xC8D5D4UL /* metadata target: TempAudioTimer.DeactivateTimer */, x0, x1, x2, x3);
                        x1 = x0;
                        x0 = x20;
                        x2 = 0x0UL;
                        x0 = RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */, x0, x1, x2, x3);
                        x0 = x21;
                        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
                        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
                        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
                        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
                        __arm64_pair_address_13161444 = unchecked((ulong)((sp) + (0x30UL)));
                        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13161444)), 0));
                        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13161444) + (0x8UL))))), 0));
                        __arm64_pair_address_13161448 = unchecked((ulong)((sp) + (0x20UL)));
                        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13161448)), 0));
                        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13161448) + (0x8UL))))), 0));
                        __arm64_pair_address_13161452 = unchecked((ulong)((sp) + (0x10UL)));
                        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13161452)), 0));
                        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13161452) + (0x8UL))))), 0));
                        __arm64_pair_address_13161456 = sp;
                        v15 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13161456)), 0));
                        v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13161456) + (0x8UL))))), 0));
                        return x0;
                    }
                }
            }
        }
        label_0xC8D3F8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```
