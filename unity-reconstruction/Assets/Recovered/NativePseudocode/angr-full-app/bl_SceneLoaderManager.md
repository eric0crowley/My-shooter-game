# Native pseudocode: bl_SceneLoaderManager

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `bl_SceneLoaderManager.GetSceneInfo` — RVA `0xce8278`

- Decompiled symbol: `bl_SceneLoaderManager_GetSceneInfo`
- Metadata signature: `public bl_SceneLoaderInfo GetSceneInfo(string scene) { }`
- Native interval: `476` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    long long field_10;
} struct_1;

typedef struct struct_2 {
    char padding_0[24];
    long long field_18;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern long long g_1ef65b8;
extern long long g_1ef65c0;
extern long long g_1ef65c8;
extern long long g_1ef8e98;
extern long long g_1f0c828;
extern char g_1fab66d;

struct_1 * bl_SceneLoaderManager_GetSceneInfo(struct_2 *ptr, long long a1)
{
    long long v3;  // x0
    long long v4;  // x1
    long long *v5;  // x23
    struct_0 **v6;  // x22
    long long v7;  // x1
    long long v8;  // x1
    long long v9;  // x20
    long long *v10;  // x0
    long long v11;  // x0
    unsigned long flag;  // [bp-0x58]
    unsigned long long choice;  // [bp-0x50]
    struct_1 *flag2;  // [bp-0x48]

    if (!(g_1fab66d & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1ef65b8);
        sub_f7d92c(&g_1ef65c0);
        sub_f7d92c(&g_1ef65c8);
        sub_f7d92c(&g_1ef8e98);
        sub_f7d92c(&g_1f0c828);
        g_1fab66d = 1;
    }
    flag = 0;
    choice = 0;
    flag2 = NULL;
    v3 = ptr->field_18;
    v4 = a1;
    if (v3)
    {
        v5 = &g_1f0c828;
        v6 = &g_1eef458;
        sub_14a3cf0(v3, g_1ef8e98);
        while (true)
        {
            v7 = g_1ef65c0;
            if (!((char)sub_130ea88(&flag, g_1ef65c0) & 1))
            {
                sub_130ea84(&flag, g_1ef65b8);
LABEL_10e837c:
                v11 = String__Concat(*(v5), a1, 0);
                if (!*(v6)->field_e0)
                    sub_f7da5c(*(v6));
                Debug__Log(v11, 0);
                return NULL;
            }
            if (!flag2)
                break;
            if (((char)String__op_Equality(flag2->field_10, a1, 0) & 1))
            {
                sub_130ea84(&flag, g_1ef65b8);
                return flag2;
            }
        }
        v3 = sub_f7db74();
        v4 = v7;
    }
    v8 = v4;
    v9 = sub_f7db74(v3);
    if ((int)v8 == 1)
    {
        v10 = __cxa_begin_catch(v9);
        __cxa_end_catch(v10);
        sub_130ea84(&flag, g_1ef65b8);
        if (!*(v10))
            goto LABEL_10e837c;
        sub_f1bd40(*(v10));
    }
    sub_130ea84(&flag, g_1ef65b8);
    sub_1026098(v9);
    sub_e29990(sub_f1bd40(0));
}
```

## `bl_SceneLoaderManager.get_HasTips` — RVA `0xce8454`

- Decompiled symbol: `bl_SceneLoaderManager_get_HasTips`
- Metadata signature: `public bool get_HasTips() { }`
- Native interval: `84` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[32];
    struct struct_0 *field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

extern long long g_1ef8688;
extern char g_1fab66e;

unsigned long long bl_SceneLoaderManager_get_HasTips(struct_1 *a0)
{
    unsigned long long v0;  // x0

    if (!(g_1fab66e & 1))
    {
        sub_f7d92c(&g_1ef8688);
        g_1fab66e = 1;
    }
    if (!a0->field_20)
        return 0;
    if (a0->field_20->field_18 <= 0)
        v0 = 0;
    else
        v0 = 1;
    return v0;
}
```

## `bl_SceneLoaderManager.GetSceneNames` — RVA `0xce84a8`

- Decompiled symbol: `bl_SceneLoaderManager_GetSceneNames`
- Metadata signature: `public string[] GetSceneNames() { }`
- Native interval: `288` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_0;

typedef struct struct_2 {
    char padding_0[24];
    long long field_18;
} struct_2;

typedef struct struct_1 {
    long long field_0;
    long long field_8;
} struct_1;

extern long long g_1eed030;
extern struct_0 *g_1ef41b0;
extern long long g_1efe3b8;
extern long long g_1efe408;
extern long long g_1f05530;
extern char g_1fab66f;

void bl_SceneLoaderManager_GetSceneNames(struct_2 *ptr)
{
    unsigned long long v7;  // x30
    unsigned long long v8;  // x24
    long long v17;  // x0
    long long p[2];  // x0
    unsigned long long v9;  // x23
    unsigned long long v10;  // x22
    unsigned long long v11;  // x21
    unsigned long long v12;  // x20
    unsigned long long v13;  // x19
    struct_0 *index;  // x0
    long long v15;  // x19
    long long v16;  // x20
    unsigned long long v0;  // [bp-0x40]
    unsigned long long v1;  // [bp-0x30]
    unsigned long long v2;  // [bp-0x28]
    unsigned long long v3;  // [bp-0x20]
    unsigned long long v4;  // [bp-0x18]
    unsigned long long v5;  // [bp-0x10]
    unsigned long long v6;  // [bp-0x8]

    v0 = v7;
    v1 = v8;
    v2 = v9;
    v3 = v10;
    v4 = v11;
    v5 = v12;
    v6 = v13;
    if (!(g_1fab66f & 1))
    {
        sub_f7d92c(&g_1efe3b8);
        sub_f7d92c(&g_1efe408);
        sub_f7d92c(&g_1eed030);
        sub_f7d92c(&g_1f05530);
        sub_f7d92c(&g_1ef41b0);
        g_1fab66f = 1;
    }
    index = g_1ef41b0;
    v15 = ptr->field_18;
    if (!g_1ef41b0->field_e0)
    {
        sub_f7da5c(g_1ef41b0);
        index = g_1ef41b0;
    }
    v16 = index->field_b8->field_8;
    if (!v16)
    {
        if (!index->field_e0)
        {
            sub_f7da5c();
            index = g_1ef41b0;
        }
        v17 = sub_f7db70(g_1eed030);
        v16 = v17;
        sub_13c1988(v17, index->field_b8->field_0, g_1f05530, 0);
        p = g_1ef41b0->field_b8;
        p[1] = v16;
        sub_f7d8d0((long long [2])&p[1], v16);
    }
    sub_123f3b4(v15, v16, g_1efe3b8);
}
```

## `bl_SceneLoaderManager.AsyncLoadData` — RVA `0xce85c8`

- Decompiled symbol: `bl_SceneLoaderManager_AsyncLoadData`
- Metadata signature: `public static IEnumerator AsyncLoadData() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

extern long long g_1ef41b8;
extern char g_1fab670;

struct_0 * bl_SceneLoaderManager_AsyncLoadData(void)
{
    struct_0 *ptr;  // x0

    if (!(g_1fab670 & 1))
    {
        sub_f7d92c(&g_1ef41b8);
        g_1fab670 = 1;
    }
    ptr = sub_f7db70(g_1ef41b8);
    Object__ctor(ptr, 0);
    ptr->field_10 = 0;
    return ptr;
}
```

## `bl_SceneLoaderManager.<AsyncLoadData>d__6.ctor` — RVA `0xce8620`

- Decompiled symbol: `bl_SceneLoaderManager_AsyncLoadData_d__6_ctor`
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

void bl_SceneLoaderManager_AsyncLoadData_d__6_ctor(struct_0 *ptr, unsigned int a1)
{
    Object__ctor();
    ptr->field_10 = a1;
    return;
}
```

## `bl_SceneLoaderManager.get_Instance` — RVA `0xce8648`

- Decompiled symbol: `bl_SceneLoaderManager_get_Instance`
- Metadata signature: `public static bl_SceneLoaderManager get_Instance() { }`
- Native interval: `220` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    long long field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    char padding_0[184];
    struct struct_2 *field_b8;
} struct_1;

extern struct_0 *g_1ef0c58;
extern struct_1 *g_1ef2b08;
extern long long g_1f00c68;
extern long long g_1f0d800;
extern char g_1fab671;

long long bl_SceneLoaderManager_get_Instance(void)
{
    long long v0;  // x0

    if (!(g_1fab671 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f00c68);
        sub_f7d92c(&g_1f0d800);
        sub_f7d92c(&g_1ef2b08);
        g_1fab671 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Equality(g_1ef2b08->field_b8->field_0, 0, 0) & 1))
    {
        v0 = sub_11328ac(g_1f0d800, g_1f00c68);
        g_1ef2b08->field_b8->field_0 = v0;
        sub_f7d8d0(g_1ef2b08->field_b8, v0);
    }
    return g_1ef2b08->field_b8->field_0;
}
```

## `bl_SceneLoaderManager.ctor` — RVA `0xce8724`

- Decompiled symbol: `bl_SceneLoaderManager_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `220` bytes
- Result: `pseudocode`

```c
extern long long g_1eed848;
extern long long g_1eed990;
extern long long g_1ef8630;
extern long long g_1ef8e90;
extern char g_1fab672;

void bl_SceneLoaderManager_ctor(long long *a0)
{
    unsigned long long v7;  // x30
    unsigned long long v8;  // x24
    long long ptr[5];  // x0
    unsigned long long v9;  // x23
    unsigned long long v10;  // x22
    unsigned long long v11;  // x21
    unsigned long long v12;  // x20
    unsigned long long v13;  // x19
    long long v14;  // x20
    long long p[5];  // x0
    long long v16;  // x20
    unsigned long long v0;  // [bp-0x40]
    unsigned long long v1;  // [bp-0x30]
    unsigned long long v2;  // [bp-0x28]
    unsigned long long v3;  // [bp-0x20]
    unsigned long long v4;  // [bp-0x18]
    unsigned long long v5;  // [bp-0x10]
    unsigned long long v6;  // [bp-0x8]

    v0 = v7;
    v1 = v8;
    v2 = v9;
    v3 = v10;
    v4 = v11;
    v5 = v12;
    v6 = v13;
    if (!(g_1fab672 & 1))
    {
        sub_f7d92c(&g_1ef8e90);
        sub_f7d92c(&g_1ef8630);
        sub_f7d92c(&g_1eed990);
        sub_f7d92c(&g_1eed848);
        g_1fab672 = 1;
    }
    v14 = sub_f7db70(g_1eed990);
    sub_14a2b64(v14, g_1ef8e90);
    p = a0;
    p[3] = v14;
    sub_f7d8d0((long long [5])&p[3], v14);
    v16 = sub_f7db70(g_1eed848);
    sub_14a2b64(v16, g_1ef8630);
    ptr = a0;
    ptr[4] = v16;
    sub_f7d8d0((long long [5])&ptr[4], v16);
}
```

## `bl_SceneLoaderManager.<>c.cctor` — RVA `0xce8800`

- Decompiled symbol: `bl_SceneLoaderManager_c_cctor`
- Metadata signature: `private static void .cctor() { }`
- Native interval: `104` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    long long field_0;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

extern struct_0 *g_1ef41b0;
extern char g_1fab673;

void bl_SceneLoaderManager_c_cctor(void)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    long long v6;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab673 & 1))
    {
        sub_f7d92c(&g_1ef41b0);
        g_1fab673 = 1;
    }
    v6 = sub_f7db70(g_1ef41b0);
    Object__ctor(v6, 0);
    g_1ef41b0->field_b8->field_0 = v6;
    sub_f7d8d0();
    return;
}
```

## `bl_SceneLoaderManager.<>c.ctor` — RVA `0xce8868`

- Decompiled symbol: `bl_SceneLoaderManager_c_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long bl_SceneLoaderManager_c_ctor(void)
{
    long long v0;  // x0

    v0 = Object__ctor();
    return Object__ctor();
}
```

## `bl_SceneLoaderManager.<>c.<GetSceneNames>b__5_0` — RVA `0xce8870`

- Decompiled symbol: `bl_SceneLoaderManager_c_GetSceneNames_b__5_0`
- Metadata signature: `internal string <GetSceneNames>b__5_0(bl_SceneLoaderInfo x) { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
} struct_0;

long long bl_SceneLoaderManager_c_GetSceneNames_b__5_0(unsigned long a0, struct_0 *a1)
{
    if (a1)
        return a1->field_10;
    sub_f7db74();
}
```

## `bl_SceneLoaderManager.<AsyncLoadData>d__6.Dispose` — RVA `0xce8888`

- Decompiled symbol: `bl_SceneLoaderManager_AsyncLoadData_d__6_Dispose`
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long bl_SceneLoaderManager_AsyncLoadData_d__6_Dispose(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `bl_SceneLoaderManager.<AsyncLoadData>d__6.MoveNext` — RVA `0xce888c`

- Decompiled symbol: `bl_SceneLoaderManager_AsyncLoadData_d__6_MoveNext`
- Metadata signature: `private bool MoveNext() { }`
- Native interval: `544` bytes
- Result: `pseudocode`

```c
typedef struct struct_7 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    unsigned long long field_18;
    long long field_20;
} struct_7;

typedef struct struct_6 {
    char padding_0[200];
    unsigned long long field_c8;
    char padding_d0[96];
    char field_130;
} struct_6;

typedef struct struct_3 {
    struct struct_2 *field_0;
} struct_3;

typedef struct struct_2 {
    char padding_0[200];
    unsigned long long field_c8;
    char padding_d0[96];
    char field_130;
} struct_2;

typedef struct struct_5 {
    struct struct_3 *field_0;
} struct_5;

typedef struct struct_4 {
    char padding_0[184];
    struct struct_5 *field_b8;
    char padding_c0[112];
    char field_130;
} struct_4;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

extern long long g_1eebcd8;
extern struct_0 *g_1ef0c58;
extern struct_1 *g_1ef1f08;
extern struct_4 *g_1ef2b08;
extern long long g_1f0d800;
extern char g_1fab674;

unsigned int bl_SceneLoaderManager_AsyncLoadData_d__6_MoveNext(struct_7 *ptr)
{
    long long v0;  // x0
    long long v1;  // x1
    struct_3 **v10;  // x8
    struct_7 *ptr4;  // x19
    struct_7 *addr;  // x0
    struct_7 *ptr3;  // x20
    long long v4;  // x0
    struct_7 *p;  // x20
    struct_6 **v6;  // x0
    unsigned long v7;  // x11
    struct_6 **v8;  // x10
    unsigned long v9;  // x11

    if (!(g_1fab674 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1ef1f08);
        sub_f7d92c(&g_1f0d800);
        sub_f7d92c(&g_1eebcd8);
        sub_f7d92c(&g_1ef2b08);
        g_1fab674 = 1;
    }
    if (ptr->field_10 != 1)
    {
        if (ptr->field_10)
            return 0;
        ptr->field_10 = 4294967295;
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (((char)Object__op_Equality(g_1ef2b08->field_b8->field_0, 0, 0) & 1))
        {
            if (!g_1ef1f08->field_e0)
                sub_f7da5c(g_1ef1f08);
            v0 = Type__GetTypeFromHandle(g_1eebcd8, 0);
            v1 = Resources__LoadAsync(g_1f0d800, v0, 0);
            addr = ptr;
            addr->field_20 = v1;
            sub_f7d8d0((struct struct_7 *)&addr->field_20, v1);
LABEL_10e89a8:
            ptr3 = ptr;
            v4 = ptr3->field_20;
            p = &ptr3->field_20;
            if (!v4)
            {
                sub_f7db74(v4);
            }
            else if (((char)AsyncOperation__get_isDone(v4, 0) & 1))
            {
                v4 = *((long long *)&p->padding_0[0]);
                if (!v4)
                    sub_f7db74(v4);
                v6 = ResourceRequest__get_asset(v4, 0);
                if (v6)
                {
                    v7 = g_1ef2b08->field_130;
                    if ((unsigned int)v7 > *(v6)->field_130)
                    {
                        v8 = NULL;
                    }
                    else if (*((long long *)(*(v6)->field_c8 + v7 * 8 - 8)) == g_1ef2b08)
                    {
                        v8 = v6;
                    }
                    else
                    {
                        v8 = NULL;
                    }
                    g_1ef2b08->field_b8->field_0 = v8;
                    v9 = g_1ef2b08->field_130;
                    v10 = g_1ef2b08->field_b8;
                    if ((unsigned int)v9 > *(v6)->field_130)
                        goto LABEL_10e8a64;
                }
                else
                {
                    g_1ef2b08->field_b8->field_0 = NULL;
                    v10 = g_1ef2b08->field_b8;
LABEL_10e8a64:
                }
                sub_f7d8d0(v10);
                *((long long *)&p->padding_0[0]) = 0;
                sub_f7d8d0(p, 0);
            }
            else
            {
                ptr->field_18 = 0;
                ptr4 = &ptr->field_18;
                sub_f7d8d0(ptr4, 0);
                *((unsigned int *)&ptr4->padding_0[8]) = 1;
                return 1;
            }
        }
        return 0;
    }
    ptr->field_10 = 4294967295;
    goto LABEL_10e89a8;
}
```

## `bl_SceneLoaderManager.<AsyncLoadData>d__6.get_Current` — RVA `0xce8aac`

- Decompiled symbol: `bl_SceneLoaderManager_AsyncLoadData_d__6_get_Current`
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long bl_SceneLoaderManager_AsyncLoadData_d__6_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```

## `bl_SceneLoaderManager.<AsyncLoadData>d__6.Reset` — RVA `0xce8ab4`

- Decompiled symbol: `bl_SceneLoaderManager_AsyncLoadData_d__6_Reset`
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
extern long long g_1ef0bd8;
extern long long g_1f05538;

void bl_SceneLoaderManager_AsyncLoadData_d__6_Reset(void)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = sub_f7db70(sub_f7d940(&g_1ef0bd8));
    NotSupportedException__ctor(v4, 0);
    sub_f7da4c(v4, sub_f7d940(&g_1f05538));
}
```

## `bl_SceneLoaderManager.<AsyncLoadData>d__6.get_Current` — RVA `0xce8aec`

- Decompiled symbol: `bl_SceneLoaderManager_AsyncLoadData_d__6_get_Current`
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long bl_SceneLoaderManager_AsyncLoadData_d__6_get_Current(struct_0 *a0)
{
    return a0->field_18;
}
```
