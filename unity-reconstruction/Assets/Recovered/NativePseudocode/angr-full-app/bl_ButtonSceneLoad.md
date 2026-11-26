# Native pseudocode: bl_ButtonSceneLoad

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `bl_ButtonSceneLoad.OnPointerClick` — RVA `0xceb768`

- Decompiled symbol: `bl_ButtonSceneLoad_OnPointerClick`
- Metadata signature: `public void OnPointerClick(PointerEventData eventData) { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long bl_ButtonSceneLoad_OnPointerClick(unsigned long a0)
{
    unsigned long long v0;  // x0

    v0 = bl_ButtonSceneLoad__LoadScene();
    return bl_ButtonSceneLoad__LoadScene();
}
```

## `bl_ButtonSceneLoad.LoadScene` — RVA `0xceb76c`

- Decompiled symbol: `bl_ButtonSceneLoad_LoadScene`
- Metadata signature: `public void LoadScene() { }`
- Native interval: `172` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[24];
    long long field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[16];
    long long field_10;
} struct_0;

extern long long g_1ef8ea0;
extern char g_1fab67d;

long long bl_ButtonSceneLoad_LoadScene(void* ptr)
{
    void* v0;  // x19
    long long v1;  // x0
    struct_1 *v2;  // x0
    struct_0 *p;  // x0
    long long v4;  // x1
    unsigned long v5;  // x0
    long long v6;  // x0

    if (!(g_1fab67d & 1))
    {
        sub_f7d92c(&g_1ef8ea0);
        g_1fab67d = 1;
    }
    if ((char)ptr[32])
    {
        v0 = ptr + 40;
        v1 = String__IsNullOrEmpty((long long)ptr[40], 0);
        if (((char)v1 & 1))
            return v1;
    }
    else
    {
        v2 = bl_SceneLoaderManager__get_Instance();
        if (!v2)
        {
            sub_f7db74();
        }
        else if (v2->field_18)
        {
            p = sub_14a30c0(v2->field_18, (int)ptr[48], g_1ef8ea0);
            if (!p)
                sub_f7db74();
            v4 = p->field_10;
            *((long long *)&ptr[40]) = v4;
            v0 = ptr + 40;
            sub_f7d8d0(v0, v4);
        }
        else
        {
            sub_f7db74();
        }
    }
    v5 = bl_SceneLoaderUtils__get_GetLoader();
    if (v5)
    {
        v6 = bl_SceneLoader__LoadLevel(v5, *((long long *)v0));
        return bl_SceneLoader__LoadLevel(v5, *((long long *)v0));
    }
    sub_f7db74();
}
```

## `bl_ButtonSceneLoad.ctor` — RVA `0xceb818`

- Decompiled symbol: `bl_ButtonSceneLoad_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    char field_20;
} struct_0;

long long bl_ButtonSceneLoad_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_20 = 1;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
