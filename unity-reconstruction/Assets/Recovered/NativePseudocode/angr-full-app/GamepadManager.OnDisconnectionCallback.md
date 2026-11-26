# Native pseudocode: GamepadManager.OnDisconnectionCallback

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `GamepadManager.OnDisconnectionCallback.ctor` — RVA `0xc2d728`

- Decompiled symbol: `GamepadManager_OnDisconnectionCallback_ctor`
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
extern char g_e29764;
extern unsigned long long g_e297bc;
extern unsigned long long g_e297e0;
extern unsigned long long g_e297f4;
extern unsigned long long g_e29824;
extern unsigned long long g_e298b0;
extern unsigned long long g_e298fc;

void GamepadManager_OnDisconnectionCallback_ctor(struct_2 *ptr, struct_2 *a1, struct_0 *p)
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
            goto LABEL_102d7b8;
        v2 = &g_e297e0;
        goto LABEL_102d7fc;
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
                        v2 = &g_e298fc;
                    else
                        v2 = &g_e298b0;
                }
                else
                {
                    if (((char)v4 & 1))
                        v2 = &g_e29824;
                    else
                        v2 = &g_e297f4;
                }
            }
            else
            {
                v2 = &g_e297bc;
            }
LABEL_102d7fc:
            ptr->field_18 = v2;
        }
        else
        {
            if (!a1)
                sub_f7da4c(sub_f7db90(0, &g_84923c), 0);
LABEL_102d7b8:
            v5 = ptr->field_20;
            ptr->field_18 = ptr->field_10;
            ptr->field_40 = v5;
        }
        *((char **)&ptr->padding_30[8]) = &g_e29764;
        return;
    }
}
```

## `GamepadManager.OnDisconnectionCallback.Invoke` — RVA `0xc2d834`

- Decompiled symbol: `GamepadManager_OnDisconnectionCallback_Invoke`
- Metadata signature: `public virtual void Invoke(GamepadManager.Gamepad gamepad, GamepadManager.DisconnectionReason reason) { }`
- Native interval: `20` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

void GamepadManager_OnDisconnectionCallback_Invoke(struct_0 *a0)
{
    goto a0->field_18;
}
```

## `GamepadManager.OnDisconnectionCallback.BeginInvoke` — RVA `0xc2d848`

- Decompiled symbol: `GamepadManager_OnDisconnectionCallback_BeginInvoke`
- Metadata signature: `public virtual IAsyncResult BeginInvoke(GamepadManager.Gamepad gamepad, GamepadManager.DisconnectionReason reason, AsyncCallback callback, object object) { }`
- Native interval: `148` bytes
- Result: `pseudocode`

```c
extern char g_1fab116;

long long GamepadManager_OnDisconnectionCallback_BeginInvoke(long long a0, unsigned long a1, unsigned int a2, long long a3, long long a4)
{
    unsigned long long v4;  // x0
    unsigned long v0;  // [bp-0x58]
    unsigned long long v1;  // [bp-0x50]
    unsigned long long flag;  // [bp-0x48]
    unsigned int v3;  // [bp-0x34]

    v3 = a2;
    if (!(g_1fab116 & 1))
    {
        sub_f7d92c("_j");
        g_1fab116 = 1;
    }
    v1 = 0;
    flag = 0;
    v0 = a1;
    v1 = sub_f7da64(g_1ef31f0, &v3);
    v4 = sub_f7d8e0(a0, &v0, a3, a4);
    return sub_f7d8e0(a0, &v0, a3, a4);
}
```

## `GamepadManager.OnDisconnectionCallback.EndInvoke` — RVA `0xc2d8dc`

- Decompiled symbol: `GamepadManager_OnDisconnectionCallback_EndInvoke`
- Metadata signature: `public virtual void EndInvoke(IAsyncResult result) { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
void GamepadManager_OnDisconnectionCallback_EndInvoke(unsigned long a0, unsigned long a1)
{
    sub_f7d8e4();
    return;
}
```
