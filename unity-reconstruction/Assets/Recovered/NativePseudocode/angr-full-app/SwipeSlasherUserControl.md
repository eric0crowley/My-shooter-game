# Native pseudocode: SwipeSlasherUserControl

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `SwipeSlasherUserControl.OnEnable` — RVA `0xc658b0`

- Decompiled symbol: `SwipeSlasherUserControl_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `176` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[32];
    long long field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1efd0a8;
extern char g_1fab2fa;

long long SwipeSlasherUserControl_OnEnable(struct_1 *ptr)
{
    long long v0;  // x0
    long long v1;  // x0

    if (!(g_1fab2fa & 1))
    {
        sub_f7d92c(&g_1efd0a8);
        sub_f7d92c(&g_1ef0c58);
        g_1fab2fa = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Equality(ptr->field_20, 0, 0);
    if (!((char)v0 & 1))
        return v0;
    ptr->field_20 = sub_1231bc8(ptr, g_1efd0a8);
    v1 = sub_f7d8d0();
    return sub_f7d8d0();
}
```

## `SwipeSlasherUserControl.Update` — RVA `0xc65960`

- Decompiled symbol: `SwipeSlasherUserControl_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `952` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[32];
    unsigned long long field_20;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

extern struct_0 *g_1eeed00;
extern struct_1 *g_1ef0c58;
extern long long g_1f09b50;
extern long long g_1f09b58;
extern long long g_1f0bc98;
extern long long g_1f0bca0;
extern long long g_1f0bca8;
extern long long g_1f0bcb0;
extern long long g_1f0bcb8;
extern long long g_1f0d660;
extern long long g_1f0d668;
extern long long g_1f0d670;
extern long long g_1f0d678;
extern long long g_1f0d680;
extern char g_1fab2fb;

long long SwipeSlasherUserControl_Update(struct_2 *ptr)
{
    long long v0;  // x0
    unsigned long long v1;  // x0
    unsigned int v2;  // w1
    long long v3;  // x0
    long long v4;  // x0

    if (!(g_1fab2fb & 1))
    {
        sub_f7d92c(&g_1eeed00);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f0bca8);
        sub_f7d92c(&g_1f0d680);
        sub_f7d92c(&g_1f0d660);
        sub_f7d92c(&g_1f09b58);
        sub_f7d92c(&g_1f0bca0);
        sub_f7d92c(&g_1f0d678);
        sub_f7d92c(&g_1f0bc98);
        sub_f7d92c(&g_1f0bcb0);
        sub_f7d92c(&g_1f0d668);
        sub_f7d92c(&g_1f09b50);
        sub_f7d92c(&g_1f0d670);
        sub_f7d92c(&g_1f0bcb8);
        g_1fab2fb = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Equality(ptr->field_20, 0, 0);
    if (((char)v0 & 1))
        return v0;
    if (!g_1eeed00->field_e0)
        sub_f7da5c(g_1eeed00);
    if (((char)CF2Input__GetButtonDown(g_1f0bcb8, 0) & 1))
    {
        v1 = ptr->field_20;
        if (!v1)
            sub_f7db74(v1);
        v2 = 0;
    }
    else
    {
        if (!g_1eeed00->field_e0)
            sub_f7da5c(g_1eeed00);
        if (((char)CF2Input__GetButtonDown(g_1f0bcb0, 0) & 1))
        {
            v1 = ptr->field_20;
            if (!v1)
                sub_f7db74(v1);
            v2 = 1;
        }
        else
        {
            if (!g_1eeed00->field_e0)
                sub_f7da5c(g_1eeed00);
            if (((char)CF2Input__GetButtonDown(g_1f0bca8, 0) & 1))
            {
                v1 = ptr->field_20;
                if (!v1)
                    sub_f7db74(v1);
                v2 = 2;
            }
            else
            {
                if (!g_1eeed00->field_e0)
                    sub_f7da5c(g_1eeed00);
                if (((char)CF2Input__GetButtonDown(g_1f0bca0, 0) & 1))
                {
                    v1 = ptr->field_20;
                    if (!v1)
                        sub_f7db74(v1);
                    v2 = 4;
                }
                else
                {
                    if (!g_1eeed00->field_e0)
                        sub_f7da5c(g_1eeed00);
                    if (((char)CF2Input__GetButtonDown(g_1f0bc98, 0) & 1))
                    {
                        v1 = ptr->field_20;
                        if (!v1)
                            sub_f7db74(v1);
                        v2 = 3;
                    }
                    else
                    {
                        if (!g_1eeed00->field_e0)
                            sub_f7da5c(g_1eeed00);
                        if (((char)CF2Input__GetButtonDown(g_1f0d680, 0) & 1))
                        {
                            v1 = ptr->field_20;
                            if (!v1)
                                sub_f7db74(v1);
                            v2 = 5;
                        }
                        else
                        {
                            if (!g_1eeed00->field_e0)
                                sub_f7da5c(g_1eeed00);
                            if (((char)CF2Input__GetButtonDown(g_1f0d678, 0) & 1))
                            {
                                v1 = ptr->field_20;
                                if (!v1)
                                    sub_f7db74(v1);
                                v2 = 6;
                            }
                            else
                            {
                                if (!g_1eeed00->field_e0)
                                    sub_f7da5c(g_1eeed00);
                                if (((char)CF2Input__GetButtonDown(g_1f0d670, 0) & 1))
                                {
                                    v1 = ptr->field_20;
                                    if (!v1)
                                        sub_f7db74(v1);
                                    v2 = 7;
                                }
                                else
                                {
                                    if (!g_1eeed00->field_e0)
                                        sub_f7da5c(g_1eeed00);
                                    if (((char)CF2Input__GetButtonDown(g_1f0d668, 0) & 1))
                                    {
                                        v1 = ptr->field_20;
                                        if (!v1)
                                            sub_f7db74(v1);
                                        v2 = 9;
                                    }
                                    else
                                    {
                                        if (!g_1eeed00->field_e0)
                                            sub_f7da5c(g_1eeed00);
                                        if (((char)CF2Input__GetButtonDown(g_1f0d660, 0) & 1))
                                        {
                                            v1 = ptr->field_20;
                                            if (!v1)
                                                sub_f7db74(v1);
                                            v2 = 8;
                                        }
                                        else
                                        {
                                            if (!g_1eeed00->field_e0)
                                                sub_f7da5c(g_1eeed00);
                                            if (((char)CF2Input__GetButtonDown(g_1f09b58, 0) & 1))
                                            {
                                                v1 = ptr->field_20;
                                                if (!v1)
                                                    sub_f7db74(v1);
                                                v2 = 11;
                                            }
                                            else
                                            {
                                                if (!g_1eeed00->field_e0)
                                                    sub_f7da5c(g_1eeed00);
                                                v3 = CF2Input__GetButtonDown(g_1f09b50, 0);
                                                if (!((char)v3 & 1))
                                                    return v3;
                                                v1 = ptr->field_20;
                                                if (!v1)
                                                    sub_f7db74(v1);
                                                v2 = 10;
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    v4 = SwipeSlasherChara__ExecuteAction(v1, v2);
    return SwipeSlasherChara__ExecuteAction(v1, v2);
}
```

## `SwipeSlasherUserControl.ctor` — RVA `0xc65d18`

- Decompiled symbol: `SwipeSlasherUserControl_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long SwipeSlasherUserControl_ctor(void)
{
    unsigned long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
