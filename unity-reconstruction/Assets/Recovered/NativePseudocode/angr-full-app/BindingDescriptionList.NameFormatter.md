# Native pseudocode: BindingDescriptionList.NameFormatter

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `BindingDescriptionList.NameFormatter.ctor` — RVA `0xc5dc9c`

- Decompiled symbol: `BindingDescriptionList_NameFormatter_ctor`
- Metadata signature: `public void .ctor(object object, IntPtr method) { }`
- Native interval: `268` bytes
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
    char padding_48[40];
    char field_70;
} struct_2;

typedef struct struct_1 {
    char padding_0[8];
    unsigned long long field_8;
    char padding_10[66];
    char field_52;
} struct_1;

extern long long g_84923c;
extern char g_e29d18;
extern unsigned long long g_e29d78;
extern unsigned long long g_e29d9c;
extern unsigned long long g_e29db0;
extern unsigned long long g_e29de0;
extern unsigned long long g_e29e6c;
extern unsigned long long g_e29eb8;

void BindingDescriptionList_NameFormatter_ctor(struct_2 *ptr, struct_2 *a1, struct_0 *p)
{
    unsigned long long v0;  // x8
    unsigned int flag;  // w22
    unsigned long long v2;  // x8
    unsigned int v3;  // w0
    unsigned long v4;  // x0
    struct_2 *v5;  // x9

    v0 = p->field_8;
    ptr->field_28 = p;
    ptr->field_10 = v0;
    ptr->field_20 = a1;
    sub_f7d8d0((struct struct_2 *)&ptr->field_20);
    flag = p->field_52;
    ptr->field_40 = ptr;
    if (((char)sub_f7d9e4(p) & 1))
    {
        if (flag != 2)
            goto LABEL_105dd2c;
        v2 = &g_e29d9c;
        goto LABEL_105dd70;
    }
    else
    {
        if (flag == 1)
        {
            if (ptr->field_70)
            {
                v3 = sub_f7d9dc(p);
                v4 = sub_f7df68(p);
                if (((char)v3 & 1))
                {
                    if (((char)v4 & 1))
                        v2 = &g_e29eb8;
                    else
                        v2 = &g_e29e6c;
                }
                else
                {
                    if (((char)v4 & 1))
                        v2 = &g_e29de0;
                    else
                        v2 = &g_e29db0;
                }
            }
            else
            {
                v2 = &g_e29d78;
            }
LABEL_105dd70:
            ptr->field_18 = v2;
        }
        else
        {
            if (!a1)
                sub_f7da4c(sub_f7db90(0, &g_84923c), 0);
LABEL_105dd2c:
            v5 = ptr->field_20;
            ptr->field_18 = ptr->field_10;
            ptr->field_40 = v5;
        }
        *((char **)&ptr->padding_30[8]) = &g_e29d18;
        return;
    }
}
```

## `BindingDescriptionList.NameFormatter.Invoke` — RVA `0xc5dda8`

- Decompiled symbol: `BindingDescriptionList_NameFormatter_Invoke`
- Metadata signature: `public virtual string Invoke(InputBindingBase bind, string name) { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

void BindingDescriptionList_NameFormatter_Invoke(struct_0 *a0)
{
    goto a0->field_18;
}
```

## `BindingDescriptionList.NameFormatter.BeginInvoke` — RVA `0xc5ddbc`

- Decompiled symbol: `BindingDescriptionList_NameFormatter_BeginInvoke`
- Metadata signature: `public virtual IAsyncResult BeginInvoke(InputBindingBase bind, string name, AsyncCallback callback, object object) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
void BindingDescriptionList_NameFormatter_BeginInvoke(unsigned long a0, unsigned long long a1, unsigned long long a2, unsigned long a3, unsigned long a4)
{
    unsigned long long v0;  // [bp-0x28]
    unsigned long long v1;  // [bp-0x20]
    unsigned long long flag;  // [bp-0x18]

    flag = 0;
    v0 = a1;
    v1 = a2;
    sub_f7d8e0();
    return;
}
```

## `BindingDescriptionList.NameFormatter.EndInvoke` — RVA `0xc5dde4`

- Decompiled symbol: `BindingDescriptionList_NameFormatter_EndInvoke`
- Metadata signature: `public virtual string EndInvoke(IAsyncResult result) { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
void BindingDescriptionList_NameFormatter_EndInvoke(unsigned long a0, unsigned long a1)
{
    sub_f7d8e4();
    return;
}
```
