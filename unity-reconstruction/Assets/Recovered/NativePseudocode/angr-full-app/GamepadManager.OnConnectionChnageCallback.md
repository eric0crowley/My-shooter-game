# Native pseudocode: GamepadManager.OnConnectionChnageCallback

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `GamepadManager.OnConnectionChnageCallback.ctor` — RVA `0xc2d5e0`

- Decompiled symbol: `GamepadManager_OnConnectionChnageCallback_ctor`
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
extern char g_e29574;
extern unsigned long long g_e295bc;
extern unsigned long long g_e295dc;
extern unsigned long long g_e295ec;
extern unsigned long long g_e29618;
extern unsigned long long g_e2969c;
extern unsigned long long g_e296d8;

void GamepadManager_OnConnectionChnageCallback_ctor(struct_2 *ptr, struct_2 *a1, struct_0 *p)
{
    unsigned long long v0;  // x8
    unsigned int flag;  // w22
    unsigned long long v2;  // x8
    struct_2 *v3;  // x9
    unsigned int v5;  // w0
    unsigned long long v6;  // x0

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
            goto LABEL_102d63c;
        v2 = &g_e295dc;
        goto LABEL_102d6b0;
    }
    else
    {
        if (flag)
        {
            if (!a1)
                sub_f7da4c(sub_f7db90(0, &g_84923c), 0);
LABEL_102d63c:
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
                        v2 = &g_e296d8;
                    else
                        v2 = &g_e2969c;
                }
                else
                {
                    if (((char)v6 & 1))
                        v2 = &g_e29618;
                    else
                        v2 = &g_e295ec;
                }
            }
            else
            {
                v2 = &g_e295bc;
            }
LABEL_102d6b0:
            ptr->field_18 = v2;
        }
        *((char **)&ptr->padding_30[8]) = &g_e29574;
        return;
    }
}
```

## `GamepadManager.OnConnectionChnageCallback.Invoke` — RVA `0xc2d6e8`

- Decompiled symbol: `GamepadManager_OnConnectionChnageCallback_Invoke`
- Metadata signature: `public virtual void Invoke(GamepadManager.Gamepad gamepad) { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

void GamepadManager_OnConnectionChnageCallback_Invoke(struct_0 *a0)
{
    goto a0->field_18;
}
```

## `GamepadManager.OnConnectionChnageCallback.BeginInvoke` — RVA `0xc2d6fc`

- Decompiled symbol: `GamepadManager_OnConnectionChnageCallback_BeginInvoke`
- Metadata signature: `public virtual IAsyncResult BeginInvoke(GamepadManager.Gamepad gamepad, AsyncCallback callback, object object) { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
void GamepadManager_OnConnectionChnageCallback_BeginInvoke(unsigned long a0, unsigned long long a1)
{
    unsigned long long v0;  // [bp-0x20]
    unsigned long long flag;  // [bp-0x18]

    flag = 0;
    v0 = a1;
    sub_f7d8e0();
    return;
}
```

## `GamepadManager.OnConnectionChnageCallback.EndInvoke` — RVA `0xc2d71c`

- Decompiled symbol: `GamepadManager_OnConnectionChnageCallback_EndInvoke`
- Metadata signature: `public virtual void EndInvoke(IAsyncResult result) { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
void GamepadManager_OnConnectionChnageCallback_EndInvoke(unsigned long a0, unsigned long a1)
{
    sub_f7d8e4();
    return;
}
```
