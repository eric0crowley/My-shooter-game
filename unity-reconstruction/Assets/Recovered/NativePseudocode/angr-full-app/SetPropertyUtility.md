# Native pseudocode: SetPropertyUtility

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `SetPropertyUtility.SetColor` — RVA `0xccc5bc`

- Decompiled symbol: `SetPropertyUtility_SetColor`
- Metadata signature: `public static bool SetColor(ref Color currentValue, Color newValue) { }`
- Native interval: `72` bytes
- Result: `pseudocode`

```c
unsigned int SetPropertyUtility_SetColor(unsigned int *ptr)
{
    unsigned int v0;  // s4
    unsigned int v1;  // s0
    unsigned int v10;  // s3
    unsigned long long v11;  // 4103
    unsigned long long v2;  // 4103
    unsigned int v3;  // s4
    unsigned int v4;  // s1
    unsigned long long v5;  // 4103
    unsigned int v6;  // s4
    unsigned int v7;  // s2
    unsigned long long v8;  // 4103
    unsigned int v9;  // s4

    v0 = *(ptr);
    v2 = (((CmpF(v0, v1) >> 5 & 3 | CmpF(v0, v1) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v0, v1) >> 5 & 3 | CmpF(v0, v1) & 1) & (CmpF(v0, v1) >> 5 & 3 | CmpF(v0, v1) & 1) >> 1 & 1);
    if ((char)(v2 * 0x10000000 >> 30))
    {
        v3 = ptr[1];
        v5 = (((CmpF(v3, v4) >> 5 & 3 | CmpF(v3, v4) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v3, v4) >> 5 & 3 | CmpF(v3, v4) & 1) & (CmpF(v3, v4) >> 5 & 3 | CmpF(v3, v4) & 1) >> 1 & 1);
        if ((char)(v5 * 0x10000000 >> 30))
        {
            v6 = ptr[2];
            v8 = (((CmpF(v6, v7) >> 5 & 3 | CmpF(v6, v7) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v6, v7) >> 5 & 3 | CmpF(v6, v7) & 1) & (CmpF(v6, v7) >> 5 & 3 | CmpF(v6, v7) & 1) >> 1 & 1);
            if ((char)(v8 * 0x10000000 >> 30))
            {
                v9 = ptr[3];
                v11 = (((CmpF(v9, v10) >> 5 & 3 | CmpF(v9, v10) & 1) ^ 1) * 0x4000000000000000 - 1 >> 61) + 1 - ((CmpF(v9, v10) >> 5 & 3 | CmpF(v9, v10) & 1) & (CmpF(v9, v10) >> 5 & 3 | CmpF(v9, v10) & 1) >> 1 & 1);
                if ((char)(v11 * 0x10000000 >> 30))
                    return 0;
            }
        }
    }
    *(ptr) = v1;
    ptr[1] = v4;
    ptr[2] = v7;
    ptr[3] = v10;
    return 1;
}
```
