# Native pseudocode: SimpleInteractiveObject

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `SimpleInteractiveObject.OnCharacterAction` — RVA `0xc662fc`

- Decompiled symbol: `SimpleInteractiveObject_OnCharacterAction`
- Metadata signature: `public override void OnCharacterAction(CharacterAction chara) { }`
- Native interval: `276` bytes
- Result: `pseudocode`
- Heuristic layout hint: `SimpleInteractiveObject_Recovered` matched 3 offsets against `SimpleInteractiveObject` metadata (confidence 1.00).

```c
typedef struct SimpleInteractiveObject_Recovered {
    char padding_0[56];
    long long targetRenderer;
    long long soundEffect;
    char isActivated;
} SimpleInteractiveObject_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab302;

long long SimpleInteractiveObject_OnCharacterAction(struct_1 *ptr)
{
    long long v0;  // x20
    long long v1;  // x0
    long long v2;  // x0

    if (!(g_1fab302 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab302 = 1;
    }
    v0 = ptr->field_38;
    ptr->field_48 = ptr->field_48 ^ 1;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (((char)Object__op_Inequality(v0, 0, 0) & 1))
    {
        v1 = ptr->field_38;
        if (v1)
        {
            v1 = Renderer__get_material(v1, 0);
            if (ptr->field_48)
            {
                if (v1)
                    goto LABEL_10663a0;
            }
            else
            {
                if (v1)
                {
LABEL_10663a0:
                    Material__set_color();
                    goto LABEL_10663a8;
                }
            }
        }
    }
    else
    {
LABEL_10663a8:
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v2 = Object__op_Inequality(ptr->field_40, 0, 0);
        if (!((char)v2 & 1))
            return v2;
        v1 = Component__get_transform(ptr, 0);
        if (v1)
            Transform__get_position();
    }
    sub_f7db74(v1);
}
```

## `SimpleInteractiveObject.ctor` — RVA `0xc66410`

- Decompiled symbol: `SimpleInteractiveObject_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    uint128_t field_20;
    unsigned int field_30;
} struct_0;

long long SimpleInteractiveObject_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_30 = 0x3f800000;
    ptr->field_20 = 0x3f8000000000000040000000;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
