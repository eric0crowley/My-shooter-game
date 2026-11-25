# `SplashLoading` — TypeDefIndex 3462

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## `SplashLoading.Start` — RVA `0xcc462c`

- Lift status: **exact**; input span: 32 bytes; span to next metadata RVA: 32 bytes.
- Metadata signature: `private void Start() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong SplashLoading_Start_RVAcc462c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCC464CUL /* metadata target: SplashLoading.LoadMenu */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */);
        return default(ulong);
    }
```

## `SplashLoading.LoadMenu` — RVA `0xcc464c`

- Lift status: **exact**; input span: 88 bytes; span to next metadata RVA: 88 bytes.
- Metadata signature: `private IEnumerator LoadMenu() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=13 (informational only).

```csharp
public static ulong SplashLoading_LoadMenu_RVAcc464c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x20 = 0x1A8E000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x533UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x988UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x988UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x533UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCC467C:
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

## `SplashLoading.ctor` — RVA `0xcc46cc`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong SplashLoading_ctor_RVAcc46cc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x1 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */);
        return default(ulong);
    }
```
