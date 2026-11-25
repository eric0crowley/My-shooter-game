# `AdsManager` — TypeDefIndex 3285

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `bool` | `isTest` |
| `0x28` | `string` | `AppOpen_ID` |
| `0x30` | `string` | `Banner_ID` |
| `0x38` | `string` | `Big_Banner_ID` |
| `0x40` | `string` | `interstitial_ID` |
| `0x48` | `string` | `Rewarded_ID` |
| `0x50` | `BannerView` | `bannerView` |
| `0x58` | `BannerView` | `Big_bannerView` |
| `0x60` | `InterstitialAd` | `interstitialAd` |
| `0x68` | `RewardedAd` | `rewardedAd` |
| `0x70` | `Action` | `Successfunction` |

## `AdsManager.Start` — RVA `0xc72a08`

- Lift status: **exact**; input span: 780 bytes; span to next metadata RVA: 780 bytes.
- Metadata signature: `private void Start() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=131 (informational only).

```csharp
public static ulong AdsManager_Start_RVAc72a08(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13053056 = default(uint);
        uint __arm64_flags_right_13053056 = default(uint);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
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
        x20 = 0x1BAB000UL;
        x21 = 0x1A8D000UL;
        x22 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x36CUL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x678UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC72ADC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x680UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x678UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x688UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x690UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x698UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x6A0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x6A8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x6B0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x6B8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x6C0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x6C8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x6D0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x36CUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC72ADC;
        label_0xC72ADC:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179AE80UL /* metadata target: Time.set_timeScale */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x20 = RuntimeMemory.ReadU64(x8);
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC72B04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC72B00UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC72B04;
        label_0xC72B04:
        ;
        x23 = 0x1A8D000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x6C0UL))));
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC72CF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x6A0UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x17961E0UL /* metadata target: MonoBehaviour.print */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x1 = x19;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU64(x8, x19);
        x8 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x20UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC72BC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x6B8UL))));
        x0 = x19;
        x1 = RuntimeMemory.ReadU64(x8);
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x28UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x20 = 0x1A8D000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x6D0UL))));
        x0 = x19;
        x1 = RuntimeMemory.ReadU64(x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x30UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x20);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x38UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x6C8UL))));
        x0 = x19;
        x1 = RuntimeMemory.ReadU64(x8);
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x40UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x6A8UL))));
        x0 = x19;
        x1 = RuntimeMemory.ReadU64(x8);
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x48UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xC72BC8;
        label_0xC72BC8:
        ;
        x24 = 0x1A8D000UL;
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x698UL))));
        x0 = RuntimeMemory.ReadU64(x24);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC72BE4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC72BDCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x24);
        goto label_0xC72BE4;
        label_0xC72BE4:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x8UL))));
        if ((x20 != 0x0UL))
        {
            goto label_0xC72C48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC72C00;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC72BF8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x24);
        goto label_0xC72C00;
        label_0xC72C00:
        ;
        x9 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x680UL))));
        x21 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeMemory.ReadU64(x9);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x690UL))));
        x1 = x21;
        x3 = 0x0UL;
        x20 = x0;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE6041CUL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x24);
        x1 = x20;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x8UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xC72C48;
        label_0xC72C48:
        ;
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x688UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC72C60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC72C5CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC72C60;
        label_0xC72C60:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13AC3E0UL /* metadata target: MobileAds.Initialize */, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x6B0UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x178FAB8UL /* metadata target: PlayerPrefs.GetInt */, x0, x1, x2, x3);
        __arm64_flags_left_13053056 = unchecked((uint)(x0));
        __arm64_flags_right_13053056 = unchecked((uint)0x1UL);
        if ((unchecked((uint)((__arm64_flags_left_13053056) - (__arm64_flags_right_13053056))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC72C90;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC72D14UL /* metadata target: AdsManager.RequestBanner */, x0, x1, x2, x3);
        goto label_0xC72C90;
        label_0xC72C90:
        ;
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC72E30UL /* metadata target: AdsManager.LoadInter */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */, x0, x1, x2, x3);
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC72E9CUL /* metadata target: AdsManager.LoadRewarded */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x22);
        x20 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC72CE4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC72CE4;
        label_0xC72CE4:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798C10UL /* metadata target: Object.DontDestroyOnLoad */, x0, x1, x2, x3);
        goto label_0xC72CF0;
        label_0xC72CF0:
        ;
        x1 = RuntimeMemory.ReadU64(x23);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x40400000UL)), 0)), 0));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x17958A8UL /* metadata target: MonoBehaviour.Invoke */);
        return default(ulong);
    }
```

## `AdsManager.RequestBanner` — RVA `0xc72d14`

- Lift status: **exact**; input span: 284 bytes; span to next metadata RVA: 284 bytes.
- Metadata signature: `private void RequestBanner() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=48 (informational only).

```csharp
public static ulong AdsManager_RequestBanner_RVAc72d14(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x22 = 0x1BAB000UL;
        x20 = 0x1A8D000UL;
        x21 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x371UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x6D8UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x6E0UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC72D78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x6E0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x6E8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x6F0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x6D8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x371UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC72D78;
        label_0xC72D78:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x22 = 0x1A8D000UL;
        x23 = 0x1A8D000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x6E8UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x6F0UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17961E0UL /* metadata target: MonoBehaviour.print */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC72DAC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC72DA4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        goto label_0xC72DAC;
        label_0xC72DAC:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = RuntimeMemory.ReadU64(x22);
        x21 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x3 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x1 = x20;
        x2 = x21;
        x4 = 0x0UL;
        x22 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x13A8E70UL /* metadata target: BannerView.ctor */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x50UL))), x22);
        x0 = x19;
        x1 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(x23);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x13A27ACUL /* metadata target: AdRequest.Builder.ctor */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC72E2C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13A296CUL /* metadata target: AdRequest.Builder.Build */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(x19);
        if ((x8 == 0x0UL))
        {
            goto label_0xC72E2C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = x0;
        x0 = x8;
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x13A9D9CUL /* metadata target: BannerView.LoadAd */);
        label_0xC72E2C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```

## `AdsManager.LoadInter` — RVA `0xc72e30`

- Lift status: **exact**; input span: 108 bytes; span to next metadata RVA: 108 bytes.
- Metadata signature: `private IEnumerator LoadInter() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=16 (informational only).

```csharp
public static ulong AdsManager_LoadInter_RVAc72e30(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x21 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x36FUL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x6F8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8D000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x6F8UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x36FUL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC72E64:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x0 = x20;
        RuntimeMemory.WritePtr(unchecked((ulong)((x20) + (0x10UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x20UL))), x19);
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```

## `AdsManager.LoadRewarded` — RVA `0xc72e9c`

- Lift status: **exact**; input span: 108 bytes; span to next metadata RVA: 108 bytes.
- Metadata signature: `private IEnumerator LoadRewarded() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=16 (informational only).

```csharp
public static ulong AdsManager_LoadRewarded_RVAc72e9c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x21 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x370UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x700UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8D000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x700UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x370UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC72ED0:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x0 = x20;
        RuntimeMemory.WritePtr(unchecked((ulong)((x20) + (0x10UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x20UL))), x19);
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```

## `AdsManager.LoadApOpen` — RVA `0xc72f08`

- Lift status: **exact**; input span: 100 bytes; span to next metadata RVA: 100 bytes.
- Metadata signature: `public void LoadApOpen() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=13 (informational only).

```csharp
public static ulong AdsManager_LoadApOpen_RVAc72f08(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13053764 = default(uint);
        uint __arm64_flags_right_13053764 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x19 = 0x1BAB000UL;
        x20 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x36DUL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x708UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC72F38;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x708UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x36DUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC72F38;
        label_0xC72F38:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x178FAB8UL /* metadata target: PlayerPrefs.GetInt */, x0, x1, x2, x3);
        __arm64_flags_left_13053764 = unchecked((uint)(x0));
        __arm64_flags_right_13053764 = unchecked((uint)0x95UL);
        if ((unchecked((uint)((__arm64_flags_left_13053764) - (__arm64_flags_right_13053764))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC72F60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC72F4CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC72F6CUL /* metadata target: AppOpenAdManager.get_Instance */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC72F60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC72FF4UL /* metadata target: AppOpenAdManager.LoadAppOpenAd */);
        label_0xC72F60:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `AdsManager.loading_Screen` — RVA `0xc73138`

- Lift status: **exact**; input span: 88 bytes; span to next metadata RVA: 88 bytes.
- Metadata signature: `private IEnumerator loading_Screen() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=13 (informational only).

```csharp
public static ulong AdsManager_loading_Screen_RVAc73138(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x19 = 0x1BAB000UL;
        x20 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x36EUL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x738UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8D000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x738UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x36EUL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC73168:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x10UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `AdsManager.Call_Load_Interstitial` — RVA `0xc731b8`

- Lift status: **exact**; input span: 32 bytes; span to next metadata RVA: 32 bytes.
- Metadata signature: `public void Call_Load_Interstitial() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong AdsManager_Call_Load_Interstitial_RVAc731b8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC72E30UL /* metadata target: AdsManager.LoadInter */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */);
        return default(ulong);
    }
```

## `AdsManager.Call_Load_Rewarded` — RVA `0xc731d8`

- Lift status: **exact**; input span: 32 bytes; span to next metadata RVA: 32 bytes.
- Metadata signature: `public void Call_Load_Rewarded() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong AdsManager_Call_Load_Rewarded_RVAc731d8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC72E9CUL /* metadata target: AdsManager.LoadRewarded */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */);
        return default(ulong);
    }
```

## `AdsManager.ShowBanner` — RVA `0xc73248`

- Lift status: **exact**; input span: 4 bytes; span to next metadata RVA: 4 bytes.
- Metadata signature: `public void ShowBanner() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong AdsManager_ShowBanner_RVAc73248(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return RuntimeCalls.InvokeDirect(0xC72D14UL /* metadata target: AdsManager.RequestBanner */);
        return default(ulong);
    }
```

## `AdsManager.DestroyBanner` — RVA `0xc7324c`

- Lift status: **exact**; input span: 28 bytes; span to next metadata RVA: 28 bytes.
- Metadata signature: `public void DestroyBanner() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong AdsManager_DestroyBanner_RVAc7324c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x50UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC73264;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x13A9A98UL /* metadata target: BannerView.Destroy */);
        label_0xC73264:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `AdsManager.Request_Big_Banner` — RVA `0xc73268`

- Lift status: **exact**; input span: 252 bytes; span to next metadata RVA: 252 bytes.
- Metadata signature: `private void Request_Big_Banner() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=42 (informational only).

```csharp
public static ulong AdsManager_Request_Big_Banner_RVAc73268(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x21 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x372UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x6E0UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC732B8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x6E0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x6E8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x6F0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x372UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC732B8;
        label_0xC732B8:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x22 = 0x1A8D000UL;
        x23 = 0x1A8D000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x38UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x6E8UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x6F0UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC732E0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC732D8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        goto label_0xC732E0;
        label_0xC732E0:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = RuntimeMemory.ReadU64(x22);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x3 = unchecked((ulong)(unchecked((uint)(0x5UL))));
        x1 = x20;
        x2 = x21;
        x4 = 0x0UL;
        x22 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x13A8E70UL /* metadata target: BannerView.ctor */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x58UL))), x22);
        x0 = x19;
        x1 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(x23);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x13A27ACUL /* metadata target: AdRequest.Builder.ctor */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC73360;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13A296CUL /* metadata target: AdRequest.Builder.Build */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(x19);
        if ((x8 == 0x0UL))
        {
            goto label_0xC73360;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = x0;
        x0 = x8;
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x13A9D9CUL /* metadata target: BannerView.LoadAd */);
        label_0xC73360:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```

## `AdsManager.Show_Big_Banner` — RVA `0xc73364`

- Lift status: **exact**; input span: 4 bytes; span to next metadata RVA: 4 bytes.
- Metadata signature: `public void Show_Big_Banner() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong AdsManager_Show_Big_Banner_RVAc73364(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return RuntimeCalls.InvokeDirect(0xC73268UL /* metadata target: AdsManager.Request_Big_Banner */);
        return default(ulong);
    }
```

## `AdsManager.Destroy_Big_Banner` — RVA `0xc73368`

- Lift status: **exact**; input span: 28 bytes; span to next metadata RVA: 28 bytes.
- Metadata signature: `public void Destroy_Big_Banner() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong AdsManager_Destroy_Big_Banner_RVAc73368(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x58UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC73380;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x13A9A98UL /* metadata target: BannerView.Destroy */);
        label_0xC73380:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `AdsManager.RequestInterstitial` — RVA `0xc73384`

- Lift status: **exact**; input span: 360 bytes; span to next metadata RVA: 360 bytes.
- Metadata signature: `private void RequestInterstitial() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=61 (informational only).

```csharp
public static ulong AdsManager_RequestInterstitial_RVAc73384(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
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
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x373UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC733FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x740UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x720UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x748UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x398UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x750UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x758UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x760UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x373UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC733FC;
        label_0xC733FC:
        ;
        x21 = x19;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x60UL))));
        x22 = 0x1A8C000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xFFFFFFFFFFFFFFE0UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x398UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC7342C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13AB59CUL /* metadata target: InterstitialAd.Destroy */, x0, x1, x2, x3);
        x0 = x21;
        x1 = 0x0UL;
        RuntimeMemory.WritePtr(x21, 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xC7342C;
        label_0xC7342C:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x22 = 0x1A8D000UL;
        x21 = 0x1A8D000UL;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x760UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x720UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC7344C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC73448UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC7344C;
        label_0xC7344C:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1770B68UL /* metadata target: Debug.Log */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x13A2028UL /* metadata target: AdRequest.ctor */, x0, x1, x2, x3);
        if ((x21 == 0x0UL))
        {
            goto label_0xC734E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC734E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x9 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x758UL))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x750UL))));
        x22 = 0x1A8D000UL;
        x23 = 0x1A8D000UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x2 = RuntimeMemory.ReadU64(x9);
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x740UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x748UL))));
        x0 = RuntimeCalls.InvokeDirect(0xFD6008UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x2 = RuntimeMemory.ReadU64(x23);
        x1 = x19;
        x3 = 0x0UL;
        x22 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xE633ACUL, x0, x1, x2, x3);
        x0 = x20;
        x1 = x21;
        x2 = x22;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13AB0E4UL /* metadata target: InterstitialAd.Load */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x60UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xC734ECUL /* metadata target: AdsManager.RegisterEventHandlers */);
        label_0xC734E8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `AdsManager.RegisterEventHandlers` — RVA `0xc734ec`

- Lift status: **exact**; input span: 1000 bytes; span to next metadata RVA: 1000 bytes.
- Metadata signature: `private void RegisterEventHandlers(InterstitialAd ad) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=173 (informational only).

```csharp
public static ulong AdsManager_RegisterEventHandlers_RVAc734ec(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
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
        x20 = 0x1BAB000UL;
        x22 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x374UL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x698UL))));
        x19 = x1;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC73590;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x768UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x770UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x778UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x780UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x788UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x790UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x798UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x7A0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x698UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x374UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC73590;
        label_0xC73590:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC735A4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC7359CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        goto label_0xC735A4;
        label_0xC735A4:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        if ((x20 != 0x0UL))
        {
            goto label_0xC73608;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC735C0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC735B8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        goto label_0xC735C0;
        label_0xC735C0:
        ;
        x9 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x770UL))));
        x21 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeMemory.ReadU64(x9);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x778UL))));
        x1 = x21;
        x3 = 0x0UL;
        x20 = x0;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE6041CUL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x22);
        x1 = x20;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x10UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xC73608;
        label_0xC73608:
        ;
        if ((x19 == 0x0UL))
        {
            goto label_0xC738D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x1 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13AA944UL /* metadata target: InterstitialAd.add_OnAdPaid */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC73630;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC73628UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        goto label_0xC73630;
        label_0xC73630:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        if ((x20 != 0x0UL))
        {
            goto label_0xC73694;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC7364C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC73644UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        goto label_0xC7364C;
        label_0xC7364C:
        ;
        x9 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x40UL))));
        x21 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeMemory.ReadU64(x9);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x780UL))));
        x1 = x21;
        x3 = 0x0UL;
        x20 = x0;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x14E3EACUL /* metadata target: Action.ctor */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x22);
        x1 = x20;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xC73694;
        label_0xC73694:
        ;
        x0 = x19;
        x1 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13AABDCUL /* metadata target: InterstitialAd.add_OnAdImpressionRecorded */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC736B8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC736B0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        goto label_0xC736B8;
        label_0xC736B8:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x20 != 0x0UL))
        {
            goto label_0xC7371C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC736D4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC736CCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        goto label_0xC736D4;
        label_0xC736D4:
        ;
        x9 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x40UL))));
        x21 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeMemory.ReadU64(x9);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x788UL))));
        x1 = x21;
        x3 = 0x0UL;
        x20 = x0;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x14E3EACUL /* metadata target: Action.ctor */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x22);
        x1 = x20;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x20UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xC7371C;
        label_0xC7371C:
        ;
        x0 = x19;
        x1 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13AAAA4UL /* metadata target: InterstitialAd.add_OnAdClicked */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC73740;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC73738UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        goto label_0xC73740;
        label_0xC73740:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        if ((x20 != 0x0UL))
        {
            goto label_0xC737A4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC7375C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC73754UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        goto label_0xC7375C;
        label_0xC7375C:
        ;
        x9 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x40UL))));
        x21 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeMemory.ReadU64(x9);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x790UL))));
        x1 = x21;
        x3 = 0x0UL;
        x20 = x0;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x14E3EACUL /* metadata target: Action.ctor */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x22);
        x1 = x20;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x28UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xC737A4;
        label_0xC737A4:
        ;
        x0 = x19;
        x1 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13AAD14UL /* metadata target: InterstitialAd.add_OnAdFullScreenContentOpened */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC737C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC737C0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        goto label_0xC737C8;
        label_0xC737C8:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x30UL))));
        if ((x20 != 0x0UL))
        {
            goto label_0xC7382C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC737E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC737DCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        goto label_0xC737E4;
        label_0xC737E4:
        ;
        x9 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x40UL))));
        x21 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeMemory.ReadU64(x9);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x798UL))));
        x1 = x21;
        x3 = 0x0UL;
        x20 = x0;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x14E3EACUL /* metadata target: Action.ctor */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x22);
        x1 = x20;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x30UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xC7382C;
        label_0xC7382C:
        ;
        x0 = x19;
        x1 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13AAE4CUL /* metadata target: InterstitialAd.add_OnAdFullScreenContentClosed */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC73850;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC73848UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        goto label_0xC73850;
        label_0xC73850:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x38UL))));
        if ((x20 != 0x0UL))
        {
            goto label_0xC738B4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC7386C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC73864UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        goto label_0xC7386C;
        label_0xC7386C:
        ;
        x9 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x768UL))));
        x21 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeMemory.ReadU64(x9);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x7A0UL))));
        x1 = x21;
        x3 = 0x0UL;
        x20 = x0;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE6041CUL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x22);
        x1 = x20;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x38UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xC738B4;
        label_0xC738B4:
        ;
        x0 = x19;
        x1 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x13AAF84UL /* metadata target: InterstitialAd.add_OnAdFullScreenContentFailed */);
        label_0xC738D0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `AdsManager.Request_Rewarded` — RVA `0xc738d4`

- Lift status: **exact**; input span: 360 bytes; span to next metadata RVA: 360 bytes.
- Metadata signature: `private void Request_Rewarded() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=61 (informational only).

```csharp
public static ulong AdsManager_Request_Rewarded_RVAc738d4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
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
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x375UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC7394C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x7A8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x720UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x7B0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x398UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x750UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x758UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x7B8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x375UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC7394C;
        label_0xC7394C:
        ;
        x21 = x19;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x68UL))));
        x22 = 0x1A8C000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xFFFFFFFFFFFFFFE0UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x398UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC7397C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13AE954UL /* metadata target: RewardedAd.Destroy */, x0, x1, x2, x3);
        x0 = x21;
        x1 = 0x0UL;
        RuntimeMemory.WritePtr(x21, 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xC7397C;
        label_0xC7397C:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x22 = 0x1A8D000UL;
        x21 = 0x1A8D000UL;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x7B8UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x720UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC7399C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC73998UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC7399C;
        label_0xC7399C:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1770B68UL /* metadata target: Debug.Log */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x13A2028UL /* metadata target: AdRequest.ctor */, x0, x1, x2, x3);
        if ((x21 == 0x0UL))
        {
            goto label_0xC73A38;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC73A38;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x9 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x758UL))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x750UL))));
        x22 = 0x1A8D000UL;
        x23 = 0x1A8D000UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x2 = RuntimeMemory.ReadU64(x9);
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x7A8UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x7B0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xFD6008UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x2 = RuntimeMemory.ReadU64(x23);
        x1 = x19;
        x3 = 0x0UL;
        x22 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xE633ACUL, x0, x1, x2, x3);
        x0 = x20;
        x1 = x21;
        x2 = x22;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13AE320UL /* metadata target: RewardedAd.Load */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x68UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xC73A3CUL /* metadata target: AdsManager.RegisterEventHandlers */);
        label_0xC73A38:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `AdsManager.RegisterEventHandlers` — RVA `0xc73a3c`

- Lift status: **exact**; input span: 1000 bytes; span to next metadata RVA: 1000 bytes.
- Metadata signature: `private void RegisterEventHandlers(RewardedAd ad) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=173 (informational only).

```csharp
public static ulong AdsManager_RegisterEventHandlers_RVAc73a3c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
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
        x20 = 0x1BAB000UL;
        x22 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x376UL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x698UL))));
        x19 = x1;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC73AE0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x768UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x770UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x7C0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x7C8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x7D0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x7D8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x7E0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x7E8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x698UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x376UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC73AE0;
        label_0xC73AE0:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC73AF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC73AECUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        goto label_0xC73AF4;
        label_0xC73AF4:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        if ((x20 != 0x0UL))
        {
            goto label_0xC73B58;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC73B10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC73B08UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        goto label_0xC73B10;
        label_0xC73B10:
        ;
        x9 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x770UL))));
        x21 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeMemory.ReadU64(x9);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x7C0UL))));
        x1 = x21;
        x3 = 0x0UL;
        x20 = x0;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE6041CUL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x22);
        x1 = x20;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x40UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xC73B58;
        label_0xC73B58:
        ;
        if ((x19 == 0x0UL))
        {
            goto label_0xC73E20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x1 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13ADB80UL /* metadata target: RewardedAd.add_OnAdPaid */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC73B80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC73B78UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        goto label_0xC73B80;
        label_0xC73B80:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x48UL))));
        if ((x20 != 0x0UL))
        {
            goto label_0xC73BE4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC73B9C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC73B94UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        goto label_0xC73B9C;
        label_0xC73B9C:
        ;
        x9 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x40UL))));
        x21 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeMemory.ReadU64(x9);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x7C8UL))));
        x1 = x21;
        x3 = 0x0UL;
        x20 = x0;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x14E3EACUL /* metadata target: Action.ctor */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x22);
        x1 = x20;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x48UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xC73BE4;
        label_0xC73BE4:
        ;
        x0 = x19;
        x1 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13ADE18UL /* metadata target: RewardedAd.add_OnAdImpressionRecorded */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC73C08;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC73C00UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        goto label_0xC73C08;
        label_0xC73C08:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x50UL))));
        if ((x20 != 0x0UL))
        {
            goto label_0xC73C6C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC73C24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC73C1CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        goto label_0xC73C24;
        label_0xC73C24:
        ;
        x9 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x40UL))));
        x21 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeMemory.ReadU64(x9);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x7D0UL))));
        x1 = x21;
        x3 = 0x0UL;
        x20 = x0;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x14E3EACUL /* metadata target: Action.ctor */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x22);
        x1 = x20;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x50UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xC73C6C;
        label_0xC73C6C:
        ;
        x0 = x19;
        x1 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13ADCE0UL /* metadata target: RewardedAd.add_OnAdClicked */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC73C90;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC73C88UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        goto label_0xC73C90;
        label_0xC73C90:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x58UL))));
        if ((x20 != 0x0UL))
        {
            goto label_0xC73CF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC73CAC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC73CA4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        goto label_0xC73CAC;
        label_0xC73CAC:
        ;
        x9 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x40UL))));
        x21 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeMemory.ReadU64(x9);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x7D8UL))));
        x1 = x21;
        x3 = 0x0UL;
        x20 = x0;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x14E3EACUL /* metadata target: Action.ctor */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x22);
        x1 = x20;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x58UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xC73CF4;
        label_0xC73CF4:
        ;
        x0 = x19;
        x1 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13ADF50UL /* metadata target: RewardedAd.add_OnAdFullScreenContentOpened */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC73D18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC73D10UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        goto label_0xC73D18;
        label_0xC73D18:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x60UL))));
        if ((x20 != 0x0UL))
        {
            goto label_0xC73D7C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC73D34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC73D2CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        goto label_0xC73D34;
        label_0xC73D34:
        ;
        x9 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x40UL))));
        x21 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeMemory.ReadU64(x9);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x7E0UL))));
        x1 = x21;
        x3 = 0x0UL;
        x20 = x0;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x14E3EACUL /* metadata target: Action.ctor */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x22);
        x1 = x20;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x60UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xC73D7C;
        label_0xC73D7C:
        ;
        x0 = x19;
        x1 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13AE088UL /* metadata target: RewardedAd.add_OnAdFullScreenContentClosed */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC73DA0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC73D98UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        goto label_0xC73DA0;
        label_0xC73DA0:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x68UL))));
        if ((x20 != 0x0UL))
        {
            goto label_0xC73E04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC73DBC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC73DB4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        goto label_0xC73DBC;
        label_0xC73DBC:
        ;
        x9 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x768UL))));
        x21 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeMemory.ReadU64(x9);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x7E8UL))));
        x1 = x21;
        x3 = 0x0UL;
        x20 = x0;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE6041CUL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x22);
        x1 = x20;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x68UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xC73E04;
        label_0xC73E04:
        ;
        x0 = x19;
        x1 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x13AE1C0UL /* metadata target: RewardedAd.add_OnAdFullScreenContentFailed */);
        label_0xC73E20:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `AdsManager.Show_Interstitial` — RVA `0xc73e24`

- Lift status: **exact**; input span: 344 bytes; span to next metadata RVA: 344 bytes.
- Metadata signature: `public void Show_Interstitial() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=54 (informational only).

```csharp
public static ulong AdsManager_Show_Interstitial_RVAc73e24(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13057684 = default(uint);
        uint __arm64_flags_left_13057728 = default(uint);
        uint __arm64_flags_right_13057684 = default(uint);
        uint __arm64_flags_right_13057728 = default(uint);
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
        x21 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x377UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x708UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC73E88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x398UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x708UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x6B0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x7F0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x7F8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x377UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC73E88;
        label_0xC73E88:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x178FAB8UL /* metadata target: PlayerPrefs.GetInt */, x0, x1, x2, x3);
        __arm64_flags_left_13057684 = unchecked((uint)(x0));
        __arm64_flags_right_13057684 = unchecked((uint)0x95UL);
        if ((unchecked((uint)((__arm64_flags_left_13057684) - (__arm64_flags_right_13057684))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC73EC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = 0x1A8D000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x6B0UL))));
        x0 = x19;
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0x70UL))), 0x0UL);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x20);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x178FAB8UL /* metadata target: PlayerPrefs.GetInt */, x0, x1, x2, x3);
        __arm64_flags_left_13057728 = unchecked((uint)(x0));
        __arm64_flags_right_13057728 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13057728) - (__arm64_flags_right_13057728))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC73ED4;
        }
        else
        {
            goto label_0xC73EC8;
        }
        label_0xC73EC8:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC73ED4:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x60UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC73F44;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13AB4C4UL /* metadata target: InterstitialAd.CanShowAd */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC73F44;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x398UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC73F00;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC73EFCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC73F00;
        label_0xC73F00:
        ;
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x7F8UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x1770B68UL /* metadata target: Debug.Log */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x60UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC73F78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13AB4E4UL /* metadata target: InterstitialAd.Show */, x0, x1, x2, x3);
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC72E30UL /* metadata target: AdsManager.LoadInter */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */);
        label_0xC73F44:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x398UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC73F5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC73F58UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC73F5C;
        label_0xC73F5C:
        ;
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x7F0UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x1770F48UL /* metadata target: Debug.LogError */);
        label_0xC73F78:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `AdsManager.Show_Rewarded` — RVA `0xc73f7c`

- Lift status: **exact**; input span: 192 bytes; span to next metadata RVA: 192 bytes.
- Metadata signature: `public void Show_Rewarded(Action RewardedFunction) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=31 (informational only).

```csharp
public static ulong AdsManager_Show_Rewarded_RVAc73f7c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x378UL))))))));
        x20 = x1;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC73FB8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x800UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x808UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x378UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC73FB8;
        label_0xC73FB8:
        ;
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x70UL))), x20);
        x0 = x21;
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xFFFFFFFFFFFFFFF8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC7402C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13AE700UL /* metadata target: RewardedAd.CanShowAd */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC7402C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x68UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x800UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x808UL))));
        x1 = x19;
        x3 = 0x0UL;
        x21 = x0;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE6041CUL, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xC74038;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = x21;
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x13AE720UL /* metadata target: RewardedAd.Show */);
        label_0xC7402C:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC74038:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `AdsManager.ctor` — RVA `0xc7403c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong AdsManager_ctor_RVAc7403c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x1 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */);
        return default(ulong);
    }
```

## `AdsManager.<RequestInterstitial>b__24_0` — RVA `0xc74044`

- Lift status: **exact**; input span: 328 bytes; span to next metadata RVA: 328 bytes.
- Metadata signature: `private void <RequestInterstitial>b__24_0(InterstitialAd ad, LoadAdError error) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=55 (informational only).

```csharp
public static ulong AdsManager__RequestInterstitial_b__24_0_RVAc74044(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
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
        x22 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x379UL))))))));
        x21 = x2;
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC74094;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x398UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x810UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x818UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x379UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC74094;
        label_0xC74094:
        ;
        x22 = 0x1A8C000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x398UL))));
        if ((x19 == 0x0UL))
        {
            goto label_0xC740D4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC740A0UL);
        }
        if ((x21 != 0x0UL))
        {
            goto label_0xC740D4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = 0x1A8D000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x818UL))));
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13AB64CUL /* metadata target: InterstitialAd.GetResponseInfo */, x0, x1, x2, x3);
        x21 = RuntimeMemory.ReadU64(x21);
        if ((x0 == 0x0UL))
        {
            goto label_0xC740FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x168UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x168UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x1 = x0;
        goto label_0xC74100;
        label_0xC740D4:
        ;
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x810UL))));
        x19 = RuntimeMemory.ReadU64(x8);
        if ((x21 == 0x0UL))
        {
            goto label_0xC7414C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x21);
        x0 = x21;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x168UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x168UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x1 = x0;
        goto label_0xC74150;
        label_0xC740FC:
        ;
        x1 = 0x0UL;
        goto label_0xC74100;
        label_0xC74100:
        ;
        x0 = x21;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13ED2C8UL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x22);
        x21 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC74124;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC74124;
        label_0xC74124:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1770B68UL /* metadata target: Debug.Log */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x60UL))), x19);
        x0 = x20;
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xC7414C:
        ;
        x1 = 0x0UL;
        goto label_0xC74150;
        label_0xC74150:
        ;
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13ED2C8UL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x22);
        x19 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC74174;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC74174;
        label_0xC74174:
        ;
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x1770F48UL /* metadata target: Debug.LogError */);
        return default(ulong);
    }
```

## `AdsManager.<Request_Rewarded>b__26_0` — RVA `0xc7418c`

- Lift status: **exact**; input span: 328 bytes; span to next metadata RVA: 328 bytes.
- Metadata signature: `private void <Request_Rewarded>b__26_0(RewardedAd ad, LoadAdError error) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=55 (informational only).

```csharp
public static ulong AdsManager__Request_Rewarded_b__26_0_RVAc7418c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
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
        x22 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x37AUL))))))));
        x21 = x2;
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC741DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x398UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x820UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x828UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x37AUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC741DC;
        label_0xC741DC:
        ;
        x22 = 0x1A8C000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x398UL))));
        if ((x19 == 0x0UL))
        {
            goto label_0xC7421C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC741E8UL);
        }
        if ((x21 != 0x0UL))
        {
            goto label_0xC7421C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = 0x1A8D000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x828UL))));
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13AEA04UL /* metadata target: RewardedAd.GetResponseInfo */, x0, x1, x2, x3);
        x21 = RuntimeMemory.ReadU64(x21);
        if ((x0 == 0x0UL))
        {
            goto label_0xC74244;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x168UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x168UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x1 = x0;
        goto label_0xC74248;
        label_0xC7421C:
        ;
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x820UL))));
        x19 = RuntimeMemory.ReadU64(x8);
        if ((x21 == 0x0UL))
        {
            goto label_0xC74294;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x21);
        x0 = x21;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x168UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x168UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x1 = x0;
        goto label_0xC74298;
        label_0xC74244:
        ;
        x1 = 0x0UL;
        goto label_0xC74248;
        label_0xC74248:
        ;
        x0 = x21;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13ED2C8UL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x22);
        x21 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC7426C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC7426C;
        label_0xC7426C:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1770B68UL /* metadata target: Debug.Log */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x68UL))), x19);
        x0 = x20;
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xC74294:
        ;
        x1 = 0x0UL;
        goto label_0xC74298;
        label_0xC74298:
        ;
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13ED2C8UL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x22);
        x19 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC742BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC742BC;
        label_0xC742BC:
        ;
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x1770F48UL /* metadata target: Debug.LogError */);
        return default(ulong);
    }
```

## `AdsManager.<Show_Rewarded>b__30_0` — RVA `0xc742d4`

- Lift status: **exact**; input span: 256 bytes; span to next metadata RVA: 256 bytes.
- Metadata signature: `private void <Show_Rewarded>b__30_0(Reward reward) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=43 (informational only).

```csharp
public static ulong AdsManager__Show_Rewarded_b__30_0_RVAc742d4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x30UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x37BUL))))))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x398UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8D000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x830UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8D000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x838UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x37BUL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC74320:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x70UL))));
        if ((x8 == 0x0UL))
        {
        }
        else
        {
            x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
            x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
            x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        }
        label_0xC74338:
        ;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC72E9CUL /* metadata target: AdsManager.LoadRewarded */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */, x0, x1, x2, x3);
        if ((x19 == 0x0UL))
        {
            label_0xC743D0:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        }
        else
        {
            x8 = 0x1A8D000UL;
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x830UL))));
            x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
            v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x19) + (0x18UL))))), 0));
            x19 = 0x1A8D000UL;
            x0 = RuntimeMemory.ReadU64(x8);
            x21 = 0x1A8C000UL;
            x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x838UL))));
            x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x398UL))));
            x1 = unchecked((ulong)((sp) + (0x8UL)));
            RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
            x0 = RuntimeCalls.InvokeDirect(0xB7DA64UL, x0, x1, x2, x3);
            x8 = RuntimeMemory.ReadU64(x19);
            x2 = x0;
            x1 = x20;
            x3 = 0x0UL;
            x0 = x8;
            x0 = RuntimeCalls.InvokeDirect(0x13F6D4CUL /* metadata target: String.Format */, x0, x1, x2, x3);
            x8 = RuntimeMemory.ReadU64(x21);
            x19 = x0;
            x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
            if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
            {
            }
            else
            {
                x0 = x8;
                x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
            }
            label_0xC743B4:
            ;
            x0 = x19;
            x1 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0x1770B68UL /* metadata target: Debug.Log */, x0, x1, x2, x3);
            x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
            x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
            x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
            x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
            sp = unchecked((ulong)((sp) + (0x30UL)));
            return x0;
        }
        return default(ulong);
    }
```
