# Native pseudocode: MapMarker

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `MapMarker.getPosition` — RVA `0xc7ac34`

- Decompiled symbol: `MapMarker_getPosition`
- Metadata signature: `public Vector3 getPosition() { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
void MapMarker_getPosition(void)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    if (Component__get_gameObject() && GameObject__get_transform())
    {
        Transform__get_position();
        return;
    }
    sub_f7db74();
}
```

## `MapMarker.isVisible` — RVA `0xc7ad04`

- Decompiled symbol: `MapMarker_isVisible`
- Metadata signature: `public bool isVisible() { }`
- Native interval: `40` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    long long field_30;
} struct_0;

void MapMarker_isVisible(struct_0 *ptr)
{
    unsigned long long v1;  // x30
    long long v2;  // x0
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    v2 = ptr->field_30;
    if (v2)
    {
        v2 = Component__get_gameObject(v2, 0);
        if (v2)
        {
            GameObject__get_activeSelf();
            return;
        }
    }
    sub_f7db74(v2);
}
```

## `MapMarker.hide` — RVA `0xc7ad2c`

- Decompiled symbol: `MapMarker_hide`
- Metadata signature: `public void hide() { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    long long field_30;
} struct_0;

void MapMarker_hide(struct_0 *ptr)
{
    unsigned long long v1;  // x30
    long long v2;  // x0
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    v2 = ptr->field_30;
    if (v2)
    {
        v2 = Component__get_gameObject(v2, 0);
        if (v2)
        {
            GameObject__SetActive();
            return;
        }
    }
    sub_f7db74(v2);
}
```

## `MapMarker.show` — RVA `0xc7ad58`

- Decompiled symbol: `MapMarker_show`
- Metadata signature: `public void show() { }`
- Native interval: `44` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    long long field_30;
} struct_0;

void MapMarker_show(struct_0 *ptr)
{
    unsigned long long v1;  // x30
    long long v2;  // x0
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    v2 = ptr->field_30;
    if (v2)
    {
        v2 = Component__get_gameObject(v2, 0);
        if (v2)
        {
            GameObject__SetActive();
            return;
        }
    }
    sub_f7db74(v2);
}
```

## `MapMarker.setLocalPos` — RVA `0xc7ad84`

- Decompiled symbol: `MapMarker_setLocalPos`
- Metadata signature: `public void setLocalPos(Vector3 pos) { }`
- Native interval: `80` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    long long field_30;
} struct_0;

void MapMarker_setLocalPos(struct_0 *ptr)
{
    unsigned long long v4;  // d10
    unsigned long long v5;  // d9
    unsigned long long v6;  // d8
    unsigned long long v7;  // x30
    long long v8;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    v8 = ptr->field_30;
    if (v8)
    {
        v8 = Graphic__get_rectTransform(v8, 0);
        if (v8)
        {
            Transform__set_localPosition();
            return;
        }
    }
    sub_f7db74(v8);
}
```

## `MapMarker.setOpacity` — RVA `0xc7add4`

- Decompiled symbol: `MapMarker_setOpacity`
- Metadata signature: `public void setOpacity(float opacity) { }`
- Native interval: `52` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[48];
    struct struct_2 *field_30;
} struct_1;

typedef struct struct_0 {
    char padding_0[680];
    unsigned long long field_2a8;
} struct_0;

typedef struct struct_2 {
    struct struct_0 *field_0;
} struct_2;

void MapMarker_setOpacity(struct_1 *a0)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    if (!a0->field_30)
        sub_f7db74(0);
    goto a0->field_30->field_0->field_2a8;
}
```

## `MapMarker.get_MarkerImage` — RVA `0xc7ae30`

- Decompiled symbol: `MapMarker_get_MarkerImage`
- Metadata signature: `public Image get_MarkerImage() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    unsigned long long field_30;
} struct_0;

long long MapMarker_get_MarkerImage(struct_0 *a0)
{
    return a0->field_30;
}
```

## `MapMarker.Start` — RVA `0xc7ae38`

- Decompiled symbol: `MapMarker_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `748` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[88];
    unsigned long long field_58;
} struct_2;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern long long g_1eefaf0;
extern struct_1 *g_1ef0c58;
extern long long g_1ef22e8;
extern long long g_1efeab8;
extern long long g_1efec00;
extern long long g_1f06608;
extern long long g_1f0c018;
extern char g_1fab1e1;
extern char g_1fab2c9;
extern char g_1fab3d6;

void MapMarker_Start(long long *ptr)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    long long v16;  // x0
    long long v17;  // x0
    long long v18[7];  // x20
    long long v19;  // x21
    long long v20;  // x21
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    long long v12;  // x20
    struct_2 *v13;  // x21
    long long v14;  // x0
    long long v15;  // x22
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x28]
    unsigned long long v2;  // [bp-0x20]
    unsigned long long v3;  // [bp-0x18]
    unsigned long long v4;  // [bp-0x10]
    unsigned long long v5;  // [bp-0x8]

    v0 = v6;
    v1 = v7;
    v2 = v8;
    v3 = v9;
    v4 = v10;
    v5 = v11;
    if (!(g_1fab3d6 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1efeab8);
        sub_f7d92c(&g_1efec00);
        sub_f7d92c(&g_1eefaf0);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f0c018);
        sub_f7d92c(&g_1f06608);
        g_1fab3d6 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Implicit(ptr[4], 0) & 1))
    {
        if (!g_1eef458->field_e0)
            sub_f7da5c(g_1eef458);
        Debug__LogError(g_1f06608, 0);
    }
    v12 = sub_f7db70(g_1eefaf0);
    GameObject__ctor(v12, g_1f0c018, 0);
    if (v12)
    {
        sub_124913c(v12, g_1efeab8);
        v13 = MapCanvasController__get_Instance();
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        if (((char)Object__op_Implicit(v13, 0) & 1))
        {
            v14 = GameObject__get_transform(v12, 0);
            if (v13)
            {
                v15 = v14;
                if (v13->field_58)
                {
                    v16 = MarkerGroup__get_MarkerGroupRect();
                    if (v15)
                    {
                        Transform__SetParent(v15, v16, 0);
                        v17 = sub_1249224(v12, g_1efec00);
                        ptr[6] = v17;
                        v18 = ptr + 6;
                        sub_f7d8d0(v18, v17);
                        if (v18[0])
                        {
                            Image__set_sprite(v18[0], ptr[4], 0);
                            if (ptr[6])
                            {
                                v19 = Graphic__get_rectTransform(ptr[6], 0);
                                if (!g_1fab2c9)
                                {
                                    sub_f7d92c(&g_1ef22e8);
                                    g_1fab2c9 = 1;
                                }
                                if (v19)
                                {
                                    Transform__set_localPosition(v19, 0);
                                    if (v18[0])
                                    {
                                        v20 = Graphic__get_rectTransform(v18[0], 0);
                                        if (!g_1fab1e1)
                                        {
                                            sub_f7d92c(&g_1ef22e8);
                                            g_1fab1e1 = 1;
                                        }
                                        if (v20)
                                        {
                                            Transform__set_localScale(v20, 0);
                                            if (v18[0] && Graphic__get_rectTransform(v18[0], 0))
                                            {
                                                RectTransform__set_sizeDelta();
                                                if (v18[0] && Component__get_gameObject(v18[0], 0))
                                                {
                                                    GameObject__SetActive();
                                                    return;
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
        else
        {
            Component__get_gameObject(ptr, 0);
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            Object__Destroy();
            return;
        }
    }
    sub_f7db74();
}
```

## `MapMarker.Update` — RVA `0xc7b1c8`

- Decompiled symbol: `MapMarker_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `228` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[44];
    char field_2c;
} struct_3;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab2cb;
extern char g_1fab3d7;

long long MapMarker_Update(struct_3 *a0)
{
    long long v0;  // x0
    long long v1;  // x0
    unsigned long v2;  // x0
    unsigned long long v3;  // x0
    unsigned long long v4;  // x0

    if (!(g_1fab3d7 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab3d7 = 1;
    }
    v0 = MapCanvasController__get_Instance();
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v1 = Object__op_Implicit(v0, 0);
    if (!((char)v1 & 1))
        return v1;
    v2 = MapCanvasController__get_Instance();
    if (v2)
    {
        MapCanvasController__checkIn(v2, a0);
        if (*((long long *)&a0[1].padding_0[3]))
        {
            v3 = Graphic__get_rectTransform(*((long long *)&a0[1].padding_0[3]), 0);
            if (!g_1fab2cb)
            {
                sub_f7d92c("-M");
                g_1fab2cb = 1;
            }
            if (v3)
            {
                v4 = Transform__set_rotation();
                return Transform__set_rotation();
            }
        }
    }
    sub_f7db74();
}
```

## `MapMarker.OnDestroy` — RVA `0xc7b2ac`

- Decompiled symbol: `MapMarker_OnDestroy`
- Metadata signature: `private void OnDestroy() { }`
- Native interval: `164` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[48];
    long long field_30;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab3d8;

long long MapMarker_OnDestroy(struct_1 *a0)
{
    long long v0;  // x0
    unsigned long long v1;  // x0

    if (!(g_1fab3d8 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab3d8 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Implicit(a0->field_30, 0);
    if (!((char)v0 & 1))
        return v0;
    if (a0->field_30)
    {
        Component__get_gameObject(a0->field_30, 0);
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v1 = Object__Destroy();
        return Object__Destroy();
    }
    sub_f7db74(0);
}
```

## `MapMarker.ctor` — RVA `0xc7b350`

- Decompiled symbol: `MapMarker_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `24` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MapMarker_Recovered` matched 2 offsets against `MapMarker` metadata (confidence 1.00).

```c
typedef struct MapMarker_Recovered {
    char padding_0[40];
    unsigned int markerSize;
    char isActive;
} MapMarker_Recovered;

long long MapMarker_ctor(struct_0 *ptr)
{
    long long v0;  // x0

    ptr->field_28 = 0x40d00000;
    ptr->field_2c = 1;
    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
