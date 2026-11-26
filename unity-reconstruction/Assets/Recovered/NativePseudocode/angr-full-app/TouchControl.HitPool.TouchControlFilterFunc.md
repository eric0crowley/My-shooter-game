# Native pseudocode: TouchControl.HitPool.TouchControlFilterFunc

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `TouchControl.HitPool.TouchControlFilterFunc.ctor` — RVA `0xc53a78`

- Decompiled symbol: `TouchControl_HitPool_TouchControlFilterFunc_ctor`
- Metadata signature: `public void .ctor(object object, IntPtr method) { }`
- Native interval: `264` bytes
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
extern char g_e299f4;
extern unsigned long long g_e29a48;
extern unsigned long long g_e29a68;
extern unsigned long long g_e29a78;
extern unsigned long long g_e29aa4;
extern unsigned long long g_e29b28;
extern unsigned long long g_e29b64;

void TouchControl_HitPool_TouchControlFilterFunc_ctor(struct_2 *ptr, struct_2 *a1, struct_0 *p)
{
    unsigned long long v0;  // x8
    unsigned int flag;  // w22
    unsigned long long v2;  // x8
    struct_2 *v3;  // x9
    unsigned int v5;  // w0
    unsigned long v6;  // x0

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
            goto LABEL_1053ad4;
        v2 = &g_e29a68;
        goto LABEL_1053b48;
    }
    else
    {
        if (flag)
        {
            if (!a1)
                sub_f7da4c(sub_f7db90(0, &g_84923c), 0);
LABEL_1053ad4:
            v3 = ptr->field_20;
            ptr->field_18 = ptr->field_10;
            ptr->field_40 = v3;
        }
        else
        {
            if (ptr->field_70)
            {
                v5 = sub_f7d9dc(p);
                v6 = sub_f7df68(p);
                if (((char)v5 & 1))
                {
                    if (((char)v6 & 1))
                        v2 = &g_e29b64;
                    else
                        v2 = &g_e29b28;
                }
                else
                {
                    if (((char)v6 & 1))
                        v2 = &g_e29aa4;
                    else
                        v2 = &g_e29a78;
                }
            }
            else
            {
                v2 = &g_e29a48;
            }
LABEL_1053b48:
            ptr->field_18 = v2;
        }
        *((char **)&ptr->padding_30[8]) = &g_e299f4;
        return;
    }
}
```

## `TouchControl.HitPool.TouchControlFilterFunc.Invoke` — RVA `0xc53b80`

- Decompiled symbol: `TouchControl_HitPool_TouchControlFilterFunc_Invoke`
- Metadata signature: `public virtual bool Invoke(TouchControl c) { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

void TouchControl_HitPool_TouchControlFilterFunc_Invoke(struct_0 *a0)
{
    goto a0->field_18;
}
```

## `TouchControl.HitPool.TouchControlFilterFunc.BeginInvoke` — RVA `0xc53b94`

- Decompiled symbol: `TouchControl_HitPool_TouchControlFilterFunc_BeginInvoke`
- Metadata signature: `public virtual IAsyncResult BeginInvoke(TouchControl c, AsyncCallback callback, object object) { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
void TouchControl_HitPool_TouchControlFilterFunc_BeginInvoke(unsigned long a0, unsigned long long a1)
{
    unsigned long long v0;  // [bp-0x20]
    unsigned long long flag;  // [bp-0x18]

    flag = 0;
    v0 = a1;
    sub_f7d8e0();
    return;
}
```

## `TouchControl.HitPool.TouchControlFilterFunc.EndInvoke` — RVA `0xc53bb4`

- Decompiled symbol: `TouchControl_HitPool_TouchControlFilterFunc_EndInvoke`
- Metadata signature: `public virtual bool EndInvoke(IAsyncResult result) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
long long TouchControl_HitPool_TouchControlFilterFunc_EndInvoke(unsigned long a0, long long a1)
{
    if (sub_f7d8e4(a1, 0))
        return *((char *)sub_f7da68());
    sub_f7db74();
}
```
