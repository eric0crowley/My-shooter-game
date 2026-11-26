# Native pseudocode: WaterBase

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `WaterBase.UpdateShader` — RVA `0xce5700`

- Decompiled symbol: `WaterBase_UpdateShader`
- Metadata signature: `public void UpdateShader() { }`
- Native interval: `376` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WaterBase_Recovered` matched 2 offsets against `WaterBase` metadata (confidence 1.00).

```c
typedef struct WaterBase_Recovered {
    char padding_0[32];
    unsigned long long sharedMaterial;
    char padding_28[4];
    char edgeBlend;
} WaterBase_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab656;

long long WaterBase_UpdateShader(struct_1 *ptr, unsigned long a1, unsigned long a2)
{
    unsigned long long v0;  // x0
    long long v1;  // x0
    long long v2;  // x0
    long long v3;  // x0
    unsigned long long v4;  // x0

    if (!(g_1fab656 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c("7&");
        sub_f7d92c("9&");
        g_1fab656 = 1;
    }
    if (2 > ptr->padding_28)
    {
        v0 = ptr->field_20;
        if (v0 && (v0 = (unsigned long long)Material__get_shader(v0, 0), v0))
        {
            if (ptr->padding_28 == 1)
                goto LABEL_10e5794;
            else
                goto LABEL_10e5794;
        }
    }
    else
    {
        v0 = ptr->field_20;
        if (v0 && (v0 = (unsigned long long)Material__get_shader(v0, 0), v0))
        {
LABEL_10e5794:
            Shader__set_maximumLOD();
            if (!((char)SystemInfo__SupportsRenderTextureFormat(1, 0) & 1))
            {
                ptr->field_2c = 0;
LABEL_10e5848:
                Shader__EnableKeyword(g_1f0fac8, 0);
                v4 = Shader__DisableKeyword();
                return Shader__DisableKeyword();
            }
            if (!ptr->field_2c)
                goto LABEL_10e5848;
            Shader__EnableKeyword(g_1f0fad0, 0);
            Shader__DisableKeyword(g_1f0fac8, 0);
            v1 = Camera__get_main(0);
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            v2 = Object__op_Implicit(v1, 0);
            if (!((char)v2 & 1))
                return v2;
            v0 = Camera__get_main(0);
            if (v0)
            {
                Camera__get_depthTextureMode();
                v3 = Camera__set_depthTextureMode();
                return Camera__set_depthTextureMode();
            }
        }
    }
    sub_f7db74(v0);
}
```

## `WaterBase.WaterTileBeingRendered` — RVA `0xce5878`

- Decompiled symbol: `WaterBase_WaterTileBeingRendered`
- Metadata signature: `public void WaterTileBeingRendered(Transform tr, Camera currentCam) { }`
- Native interval: `164` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[44];
    char field_2c;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab657;

long long WaterBase_WaterTileBeingRendered(struct_1 *a0, unsigned long a1, long long a2)
{
    long long v0;  // x0
    long long v1;  // x0

    if (!(g_1fab657 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab657 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Implicit(a2, 0);
    if (!((char)v0 & 1))
    {
        return v0;
    }
    else if (a0->field_2c)
    {
        if (a2)
        {
            Camera__get_depthTextureMode(a2, 0);
            v1 = Camera__set_depthTextureMode();
            return Camera__set_depthTextureMode();
        }
        sub_f7db74();
    }
    else
    {
        return v0;
    }
}
```

## `WaterBase.Update` — RVA `0xce591c`

- Decompiled symbol: `WaterBase_Update`
- Metadata signature: `public void Update() { }`
- Native interval: `116` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WaterBase_Recovered` matched 2 offsets against `WaterBase` metadata (confidence 1.00).

```c
typedef struct WaterBase_Recovered {
    char padding_0[32];
    unsigned long long sharedMaterial;
    char padding_28[4];
    char edgeBlend;
} WaterBase_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab658;

long long WaterBase_Update(struct_1 *a0)
{
    long long v0;  // x0
    unsigned int v1;  // x2
    long long v2;  // x0

    if (!(g_1fab658 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab658 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Implicit(a0->field_20, 0);
    if (!((char)v0 & 1))
        return v0;
    v2 = WaterBase__UpdateShader(a0, 0, v1);
    return WaterBase__UpdateShader(a0, 0, v1);
}
```

## `WaterBase.ctor` — RVA `0xce5990`

- Decompiled symbol: `WaterBase_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `24` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WaterBase_Recovered` matched 2 offsets against `WaterBase` metadata (confidence 1.00).

```c
typedef struct WaterBase_Recovered {
    char padding_0[40];
    unsigned int waterQuality;
    char edgeBlend;
} WaterBase_Recovered;

long long WaterBase_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_28 = 2;
    ptr->field_2c = 1;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
