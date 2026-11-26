# Native pseudocode: LeftRightMenu.OptionSwitchCallback

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `LeftRightMenu.OptionSwitchCallback.ctor` — RVA `0xc5ab80`

- Decompiled symbol: `LeftRightMenu_OptionSwitchCallback_ctor`
- Metadata signature: `public void .ctor(object object, IntPtr method) { }`
- Native interval: `160` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[8];
    unsigned long long field_8;
    char padding_10[66];
    char field_52;
} struct_0;

typedef struct struct_2 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned long long field_18;
    struct struct_2 *field_20;
    struct struct_1 *field_28;
    char padding_30[16];
    struct struct_2 *field_40;
} struct_2;

typedef struct struct_1 {
    char padding_0[8];
    unsigned long long field_8;
    char padding_10[66];
    char field_52;
} struct_1;

extern long long g_84923c;
extern char g_e29bf0;
extern unsigned long long g_e29c38;

void LeftRightMenu_OptionSwitchCallback_ctor(struct_2 *ptr, struct_2 *a1, struct_0 *p)
{
    unsigned long long v0;  // x8
    unsigned int flag;  // w22
    struct_2 *v2;  // x9

    v0 = p->field_8;
    ptr->field_28 = p;
    ptr->field_10 = v0;
    ptr->field_20 = a1;
    sub_f7d8d0((struct struct_2 *)&ptr->field_20);
    flag = p->field_52;
    ptr->field_40 = ptr;
    if (((char)sub_f7d9e4(p) & 1))
    {
        if (flag != 1)
            goto LABEL_105abdc;
        ptr->field_18 = &g_e29c38;
    }
    else
    {
        if (!a1)
            sub_f7da4c(sub_f7db90(0, &g_84923c), 0);
LABEL_105abdc:
        v2 = ptr->field_20;
        ptr->field_18 = ptr->field_10;
        ptr->field_40 = v2;
    }
    *((char **)&ptr->padding_30[8]) = &g_e29bf0;
    return;
}
```

## `LeftRightMenu.OptionSwitchCallback.Invoke` — RVA `0xc5ac20`

- Decompiled symbol: `LeftRightMenu_OptionSwitchCallback_Invoke`
- Metadata signature: `public virtual void Invoke(int dir) { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

void LeftRightMenu_OptionSwitchCallback_Invoke(struct_0 *a0)
{
    goto a0->field_18;
}
```

## `LeftRightMenu.OptionSwitchCallback.BeginInvoke` — RVA `0xc5ac34`

- Decompiled symbol: `LeftRightMenu_OptionSwitchCallback_BeginInvoke`
- Metadata signature: `public virtual IAsyncResult BeginInvoke(int dir, AsyncCallback callback, object object) { }`
- Native interval: `132` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0450;
extern char g_1fab2a4;

long long LeftRightMenu_OptionSwitchCallback_BeginInvoke(long long a0, unsigned int a1, long long a2, long long a3)
{
    unsigned long long v3;  // x0
    unsigned long v0;  // [bp-0x48], Other Possible Types: unsigned long long
    unsigned long long flag;  // [bp-0x40]
    unsigned int v2;  // [bp-0x34]

    v2 = a1;
    if (!(g_1fab2a4 & 1))
    {
        sub_f7d92c(&g_1ef0450);
        g_1fab2a4 = 1;
    }
    v0 = 0;
    flag = 0;
    v0 = sub_f7da64(g_1ef0450, &v2);
    v3 = sub_f7d8e0(a0, &v0, a2, a3);
    return sub_f7d8e0(a0, &v0, a2, a3);
}
```

## `LeftRightMenu.OptionSwitchCallback.EndInvoke` — RVA `0xc5acb8`

- Decompiled symbol: `LeftRightMenu_OptionSwitchCallback_EndInvoke`
- Metadata signature: `public virtual void EndInvoke(IAsyncResult result) { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
void LeftRightMenu_OptionSwitchCallback_EndInvoke(unsigned long a0, unsigned long a1)
{
    sub_f7d8e4();
    return;
}
```
