# Native pseudocode: DualStickShooterCharaAnimator

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `DualStickShooterCharaAnimator.OnEnable` — RVA `0xc66900`

- Decompiled symbol: `DualStickShooterCharaAnimator_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `268` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efcf08;
extern long long g_1efcf78;
extern char g_1fab307;

long long DualStickShooterCharaAnimator_OnEnable(long long *ptr)
{
    long long v0;  // x0
    long long v1;  // x0
    long long v2;  // x0

    if (!(g_1fab307 & 1))
    {
        sub_f7d92c(&g_1efcf08);
        sub_f7d92c(&g_1efcf78);
        sub_f7d92c(&g_1ef0c58);
        g_1fab307 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(ptr[5], 0, 0) & 1))
    {
        v0 = sub_1231bc8(ptr, g_1efcf08);
        ptr[5] = v0;
        sub_f7d8d0(ptr + 5, v0);
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v1 = Object__op_Equality(ptr[4], 0, 0);
    if (!((char)v1 & 1))
        return v1;
    ptr[4] = sub_1231bc8(ptr, g_1efcf78);
    v2 = sub_f7d8d0();
    return sub_f7d8d0();
}
```

## `DualStickShooterCharaAnimator.Update` — RVA `0xc66a0c`

- Decompiled symbol: `DualStickShooterCharaAnimator_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `392` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab243;
extern char g_1fab308;

long long DualStickShooterCharaAnimator_Update(long long *ptr)
{
    long long v0;  // x0
    long long v1;  // x0
    long long v2;  // x20
    long long v3;  // x21
    long long v4;  // x0
    unsigned long long v5;  // x0

    if (!(g_1fab308 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab308 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Equality(ptr[5], 0, 0);
    if (((char)v0 & 1))
        return v0;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v1 = Object__op_Equality(ptr[4], 0, 0);
    if (((char)v1 & 1))
        return v1;
    if (ptr[4])
    {
        if (!((char)String__IsNullOrEmpty(ptr[8], 0) & 1))
        {
            v2 = ptr[5];
            v3 = ptr[8];
            if (!g_1fab243)
            {
                sub_f7d92c("_F");
                g_1fab243 = 1;
            }
            if (!g_1ef07e8->field_e0)
                sub_f7da5c(g_1ef07e8);
            if (v2)
            {
                Animator__SetFloat(v2, v3, 0);
                goto LABEL_1066b1c;
            }
        }
        else
        {
LABEL_1066b1c:
            if (((char)String__IsNullOrEmpty(ptr[6], 0) & 1))
            {
LABEL_1066b44:
                v4 = String__IsNullOrEmpty(ptr[7], 0);
                if (((char)v4 & 1))
                    return v4;
                if (ptr[5])
                {
                    v5 = Animator__SetFloat();
                    return Animator__SetFloat();
                }
            }
            else if (ptr[5])
            {
                Animator__SetFloat(ptr[5], ptr[6], 0);
                goto LABEL_1066b44;
            }
        }
    }
    sub_f7db74();
}
```

## `DualStickShooterCharaAnimator.ctor` — RVA `0xc66b94`

- Decompiled symbol: `DualStickShooterCharaAnimator_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `168` bytes
- Result: `pseudocode`

```c
extern long long g_1f0ab18;
extern long long g_1f0dbf8;
extern long long g_1f0f998;
extern char g_1fab309;

void DualStickShooterCharaAnimator_ctor(long long *a0)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    long long ptr[9];  // x0
    long long p[9];  // x0
    long long addr[9];  // x0
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x28]
    unsigned long long v2;  // [bp-0x20]
    unsigned long long v3;  // [bp-0x18]
    unsigned long long v4;  // [bp-0x10]
    unsigned long long v5;  // [bp-0x8]

    v0 = v6;
    v1 = v7;
    v2 = v8;
    v3 = v9;
    v4 = v10;
    v5 = v11;
    if (!(g_1fab309 & 1))
    {
        sub_f7d92c(&g_1f0f998);
        sub_f7d92c(&g_1f0dbf8);
        sub_f7d92c(&g_1f0ab18);
        g_1fab309 = 1;
    }
    ptr = a0;
    ptr[6] = g_1f0f998;
    sub_f7d8d0((long long [9])&ptr[6], g_1f0f998);
    p = a0;
    p[7] = g_1f0ab18;
    sub_f7d8d0((long long [9])&p[7], g_1f0ab18);
    addr = a0;
    addr[8] = g_1f0dbf8;
    sub_f7d8d0((long long [9])&addr[8], g_1f0dbf8);
    MonoBehaviour__ctor();
    return;
}
```
