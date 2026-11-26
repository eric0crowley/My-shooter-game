# Native pseudocode: CustomGamepadProfileBank

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `CustomGamepadProfileBank.ctor` — RVA `0xc2ae88`

- Decompiled symbol: `CustomGamepadProfileBank_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `140` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    long long field_10;
} struct_0;

extern long long g_1eed620;
extern long long g_1ef7b78;
extern char g_1fab13e;

void CustomGamepadProfileBank_ctor(struct_0 *ptr)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    long long v10;  // x0
    unsigned long long v0;  // [bp-0x30]
    unsigned long long v1;  // [bp-0x20]
    unsigned long long v2;  // [bp-0x18]
    unsigned long long v3;  // [bp-0x10]
    unsigned long long v4;  // [bp-0x8]

    v0 = v5;
    v1 = v6;
    v2 = v7;
    v3 = v8;
    v4 = v9;
    if (!(g_1fab13e & 1))
    {
        sub_f7d92c(&g_1ef7b78);
        sub_f7d92c(&g_1eed620);
        g_1fab13e = 1;
    }
    Object__ctor(ptr, 0);
    v10 = sub_f7db70(g_1eed620);
    sub_14a2bd4(v10, 16, g_1ef7b78);
    ptr->field_10 = v10;
    sub_f7d8d0();
    return;
}
```

## `CustomGamepadProfileBank.Load` — RVA `0xc2b2ec`

- Decompiled symbol: `CustomGamepadProfileBank_Load`
- Metadata signature: `public void Load() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long CustomGamepadProfileBank_Load(unsigned long a0)
{
    unsigned long long v0;  // x0

    v0 = CustomGamepadProfileBank__LoadFromPlayerPrefs();
    return CustomGamepadProfileBank__LoadFromPlayerPrefs();
}
```

## `CustomGamepadProfileBank.GetProfile` — RVA `0xc2d4e8`

- Decompiled symbol: `CustomGamepadProfileBank_GetProfile`
- Metadata signature: `public GamepadProfile GetProfile(string deviceName) { }`
- Native interval: `168` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[24];
    unsigned int field_18;
} struct_2;

typedef struct struct_1 {
    char padding_0[16];
    struct struct_0 *field_10;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

extern long long g_1ef7ba0;
extern long long g_1ef7ba8;
extern char g_1fab141;

struct_2 * CustomGamepadProfileBank_GetProfile(struct_1 *ptr, unsigned long a1)
{
    struct_0 *i;  // x0
    int v1;  // w21

    if (!(g_1fab141 & 1))
    {
        sub_f7d92c(&g_1ef7ba0);
        sub_f7d92c(&g_1ef7ba8);
        g_1fab141 = 1;
    }
    i = ptr->field_10;
    if (i)
    {
        v1 = 0;
        do
        {
            if (i->field_18 <= v1)
                return NULL;
            i = sub_14a30c0();
            if (!i)
                break;
            if (((char)GamepadProfile__IsCompatible() & 1))
                return i;
            i = ptr->field_10;
            v1 += 1;
        } while (i);
    }
    sub_f7db74(i);
    return NULL;
}
```

## `CustomGamepadProfileBank.FindDuplicate` — RVA `0xc333d8`

- Decompiled symbol: `CustomGamepadProfileBank_FindDuplicate`
- Metadata signature: `public int FindDuplicate(GamepadProfile profile) { }`
- Native interval: `164` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    struct struct_0 *field_10;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

extern long long g_1ef7ba0;
extern long long g_1ef7ba8;
extern char g_1fab13f;

int CustomGamepadProfileBank_FindDuplicate(struct_1 *ptr, long long *a1)
{
    struct_0 *i;  // x0
    int v1;  // w21

    if (!(g_1fab13f & 1))
    {
        sub_f7d92c(&g_1ef7ba0);
        sub_f7d92c(&g_1ef7ba8);
        g_1fab13f = 1;
    }
    i = ptr->field_10;
    if (i)
    {
        v1 = 0;
        do
        {
            if (i->field_18 <= v1)
                return -1;
            i = sub_14a30c0();
            if (!i)
                break;
            if (((char)GamepadProfile__IsDuplicateOf(i, a1) & 1))
                return v1;
            i = ptr->field_10;
            v1 += 1;
        } while (i);
    }
    sub_f7db74(i);
    return -1;
}
```

## `CustomGamepadProfileBank.GetProfileById` — RVA `0xc3347c`

- Decompiled symbol: `CustomGamepadProfileBank_GetProfileById`
- Metadata signature: `public GamepadProfile GetProfileById(int i) { }`
- Native interval: `132` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
} struct_0;

extern long long g_1ef7ba0;
extern long long g_1ef7ba8;
extern char g_1fab140;

unsigned int CustomGamepadProfileBank_GetProfileById(struct_0 *a0, unsigned int a1, unsigned long a2)
{
    unsigned long v0;  // x19

    v0 = a1;
    if (!(g_1fab140 & 1))
    {
        sub_f7d92c(&g_1ef7ba0);
        sub_f7d92c(&g_1ef7ba8);
        g_1fab140 = 1;
    }
    if (((char)(v0 >> 31) & 1))
        return 0;
    if (a0->field_10)
    {
        if (*((int *)(a0->field_10 + 24)) > (unsigned int)v0)
            return sub_14a30c0();
        return 0;
    }
    sub_f7db74(0);
}
```

## `CustomGamepadProfileBank.GetCompatibleProfiles` — RVA `0xc33500`

- Decompiled symbol: `CustomGamepadProfileBank_GetCompatibleProfiles`
- Metadata signature: `public void GetCompatibleProfiles(string deviceName, List<GamepadProfile> targetList) { }`
- Native interval: `336` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[16];
    unsigned long long field_10;
} struct_3;

typedef struct struct_5 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_5;

typedef struct struct_4 {
    char padding_0[32];
    unsigned long long field_20;
} struct_4;

typedef struct struct_0 {
    char padding_0[112];
    long long field_70;
} struct_0;

typedef struct struct_1 {
    char padding_0[192];
    struct struct_0 *field_c0;
} struct_1;

typedef struct struct_2 {
    char padding_0[32];
    struct struct_1 *field_20;
} struct_2;

extern struct_2 *g_1ef7b80;
extern long long g_1ef7b88;
extern long long g_1ef7ba0;
extern long long g_1ef7ba8;
extern char g_1fab142;

long long CustomGamepadProfileBank_GetCompatibleProfiles(struct_3 *p, long long a1, struct_5 *ptr)
{
    unsigned long v0;  // x0, Other Possible Types: unsigned long long
    int v1;  // w22
    unsigned long long v2;  // x23
    unsigned long long v3;  // x8
    unsigned long v4;  // x10
    struct_4 *addr;  // x0
    unsigned long v6;  // x0

    if (!(g_1fab142 & 1))
    {
        sub_f7d92c(&g_1ef7b80);
        sub_f7d92c(&g_1ef7b88);
        sub_f7d92c(&g_1ef7ba0);
        sub_f7d92c(&g_1ef7ba8);
        g_1fab142 = 1;
    }
    v0 = p->field_10;
    if (v0)
    {
        v1 = 0;
        do
        {
            if (*((int *)(v0 + 24)) <= v1)
                return v0;
            v0 = sub_14a30c0();
            if (!v0)
                break;
            v2 = v0;
            if (!(GamepadProfile__IsCompatible(v0, a1) & 1))
                continue;
            if (!ptr)
                break;
            if ((sub_14a36c0(ptr, v2, g_1ef7b88) & 1))
                continue;
            v3 = ptr->field_10;
            ptr->field_1c = ptr->field_1c + 1;
            if (!v3)
                break;
            v4 = ptr->field_18;
            if (*((int *)(v3 + 24)) > (unsigned int)v4)
            {
                addr = v3 + v4 * 8;
                ptr->field_18 = (unsigned int)v4 + 1;
                addr->field_20 = v2;
                sub_f7d8d0((struct struct_4 *)&addr->field_20, v2);
            }
            else
            {
                sub_14a3390(ptr, v2, g_1ef7b80->field_20->field_c0->field_70);
            }
        } while ((v0 = p->field_10, v1 = (int)(v1 + 1), v0));
    }
    v6 = sub_f7db74(v0);
    return sub_f7db74(v0);
}
```

## `CustomGamepadProfileBank.AddProfile` — RVA `0xc33650`

- Decompiled symbol: `CustomGamepadProfileBank_AddProfile`
- Metadata signature: `public GamepadProfile AddProfile(GamepadProfile profile) { }`
- Native interval: `276` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    long long field_30;
} struct_0;

typedef struct struct_1 {
    char padding_0[16];
    struct struct_0 *field_10;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

extern long long g_1ef7b90;
extern long long g_1ef7b98;
extern long long g_1ef7ba8;
extern char g_1fab143;

struct_0 * CustomGamepadProfileBank_AddProfile(struct_1 *ptr, struct_0 *a1)
{
    unsigned long long v0;  // x0
    unsigned long v1;  // x8
    unsigned int v2;  // w22
    struct_0 *v3;  // x0
    struct_0 *v4;  // x21

    if (!(g_1fab143 & 1))
    {
        sub_f7d92c(&g_1ef7b90);
        sub_f7d92c(&g_1ef7b98);
        sub_f7d92c(&g_1ef7ba8);
        g_1fab143 = 1;
    }
    if (!a1)
        return a1;
    v0 = CustomGamepadProfileBank__FindDuplicate(ptr, a1);
    v1 = ptr->field_10;
    if (v1)
    {
        v2 = v0;
        if (((char)(v0 >> 31) & 1))
        {
            sub_14a3ed8(v1, 0, a1, g_1ef7b90);
            return a1;
        }
        v3 = sub_14a30c0(v1, v2, g_1ef7ba8);
        if (ptr->field_10)
        {
            v4 = v3;
            sub_14a48fc(ptr->field_10, v2, g_1ef7b98);
            if (ptr->field_10)
            {
                sub_14a3ed8(ptr->field_10, 0, v4, g_1ef7b90);
                if (v4)
                {
                    GamepadProfile__AddSupportedVersion(v4, a1->field_30);
                    return v4;
                }
            }
        }
    }
    sub_f7db74();
}
```

## `CustomGamepadProfileBank.LoadFromPlayerPrefs` — RVA `0xc33764`

- Decompiled symbol: `CustomGamepadProfileBank_LoadFromPlayerPrefs`
- Metadata signature: `private bool LoadFromPlayerPrefs() { }`
- Native interval: `208` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

extern long long g_1ef1920;
extern long long g_1ef29e0;
extern long long g_1f08c30;
extern char g_1fab144;

unsigned long long CustomGamepadProfileBank_LoadFromPlayerPrefs(long long a0)
{
    struct_0 *v0;  // x0
    long long v1;  // x0
    long long v2;  // x0
    unsigned long long v3;  // x0

    if (!(g_1fab144 & 1))
    {
        sub_f7d92c(&g_1ef1920);
        sub_f7d92c(&g_1ef29e0);
        sub_f7d92c(&g_1f08c30);
        g_1fab144 = 1;
    }
    v0 = PlayerPrefs__GetString(g_1f08c30, 0, 0);
    if (!v0)
    {
        return 0;
    }
    else if (v0->field_10)
    {
        v1 = sub_f7db70(g_1ef1920);
        StringReader__ctor(v1, v0, 0);
        v2 = sub_f7db70(g_1ef29e0);
        XmlTextReader__ctor(v2, v1, 0);
        v3 = CustomGamepadProfileBank__LoadFromStream(a0, v2);
        return CustomGamepadProfileBank__LoadFromStream(a0, v2);
    }
    else
    {
        return 0;
    }
}
```

## `CustomGamepadProfileBank.Save` — RVA `0xc33834`

- Decompiled symbol: `CustomGamepadProfileBank_Save`
- Metadata signature: `public void Save() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long CustomGamepadProfileBank_Save(unsigned long a0)
{
    unsigned long long v0;  // x0

    v0 = CustomGamepadProfileBank__SaveToPlayerPrefs();
    return CustomGamepadProfileBank__SaveToPlayerPrefs();
}
```

## `CustomGamepadProfileBank.SaveToPlayerPrefs` — RVA `0xc33838`

- Decompiled symbol: `CustomGamepadProfileBank_SaveToPlayerPrefs`
- Metadata signature: `private bool SaveToPlayerPrefs() { }`
- Native interval: `336` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[360];
    struct struct_1 *field_168;
    unsigned long long field_170;
} struct_0;

typedef struct struct_2 {
    long long field_0;
} struct_2;

typedef struct struct_3 {
    unsigned long long field_0;
} struct_3;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern long long g_1db6f08;
extern long long g_1eef838;
extern long long g_1ef1930;
extern long long g_1ef29f0;
extern long long g_1f08c30;
extern char g_1fab145;

unsigned int CustomGamepadProfileBank_SaveToPlayerPrefs(long long a0)
{
    struct_0 **v0;  // x20
    long long v1;  // x0
    unsigned long long flag;  // x2
    long long v3;  // x1
    struct_0 **v4;  // x0
    unsigned long v5;  // x1
    long long v6;  // x19
    struct_2 **v7;  // x19
    long long v8;  // x0
    struct_3 **ptr;  // x0

    if (!(g_1fab145 & 1))
    {
        sub_f7d92c(&g_1ef1930);
        sub_f7d92c(&g_1ef29f0);
        sub_f7d92c(&g_1f08c30);
        g_1fab145 = 1;
    }
    v0 = sub_f7db70(g_1ef1930);
    StringWriter__ctor(v0, 0);
    v1 = sub_f7db70(g_1ef29f0);
    flag = 0;
    XmlTextWriter__ctor(v1, v0, 0);
    v3 = v1;
    if (!((char)CustomGamepadProfileBank__SaveToStream(a0, v3) & 1))
    {
        return 0;
    }
    else if (v0)
    {
        v4 = v0;
        v5 = *(v0)->field_170;
        *(v0)->field_168();
    }
    else
    {
        v6 = sub_f7db74();
        if ((int)v3 == 1)
        {
            v7 = __cxa_begin_catch(v6);
            v8 = sub_f7d940(&g_1eef838);
            if (((char)sub_f7dfa0(v8, *(v7)->field_0) & 1))
            {
                __cxa_end_catch();
                return 0;
            }
            ptr = __cxa_allocate_exception(8);
            *(ptr) = *(v7);
            v6 = __cxa_throw(ptr, &g_1db6f08, 0);
            __cxa_end_catch(v6, &g_1db6f08, 0);
        }
        sub_e29990(sub_1026098(v6));
    }
}
```

## `CustomGamepadProfileBank.LoadFromStream` — RVA `0xc33988`

- Decompiled symbol: `CustomGamepadProfileBank_LoadFromStream`
- Metadata signature: `private bool LoadFromStream(XmlTextReader stream) { }`
- Native interval: `852` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[304];
    char field_130;
} struct_2;

typedef struct struct_12 {
    struct struct_11 *field_0;
    char padding_8[16];
    int field_18;
} struct_12;

typedef struct struct_6 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    long long field_20;
    struct struct_3 *field_28;
    long long field_30;
    struct struct_4 *field_38;
    long long field_40;
    struct struct_5 *field_48;
    long long field_50;
} struct_6;

typedef struct struct_8 {
    char padding_0[16];
    struct struct_7 *field_10;
} struct_8;

typedef struct struct_10 {
    char padding_0[24];
    struct struct_9 *field_18;
} struct_10;

typedef struct struct_13 {
    long long field_0;
} struct_13;

typedef struct struct_14 {
    unsigned long long field_0;
} struct_14;

typedef struct struct_11 {
    char padding_0[200];
    unsigned long long field_c8;
    char padding_d0[96];
    char field_130;
} struct_11;

typedef struct struct_3 {
    char padding_0[304];
    char field_130;
} struct_3;

typedef struct struct_4 {
    char padding_0[304];
    char field_130;
} struct_4;

typedef struct struct_5 {
    char padding_0[304];
    char field_130;
} struct_5;

typedef struct struct_7 {
    char padding_0[304];
    char field_130;
} struct_7;

typedef struct struct_9 {
    char padding_0[304];
    char field_130;
} struct_9;

typedef struct struct_1 {
    char padding_0[304];
    char field_130;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1db6f08;
extern struct_1 *g_1eed620;
extern struct_0 *g_1eef458;
extern long long g_1eef838;
extern long long g_1ef7ba0;
extern long long g_1ef7ba8;
extern long long g_1f0bdd0;
extern long long g_1f100d8;
extern long long g_1f10140;
extern long long g_1f16088;
extern char g_1fab147;

unsigned int CustomGamepadProfileBank_LoadFromStream(unsigned long a0, struct_2 *a1)
{
    struct_12 *v1;  // x0
    struct_12 *v2;  // x19
    struct_6 *p;  // x0
    struct_8 *addr;  // x0
    struct_6 *ptr3;  // x21
    struct_6 *v14;  // x21
    struct_6 *ptr4;  // x0
    struct_10 *ptr5;  // x0
    struct_6 *ptr6;  // x21
    struct_6 *v18;  // x21
    struct_6 *ptr7;  // x0
    long long v20;  // x0
    unsigned long v3;  // x9
    long long v21;  // x19
    struct_13 **v22;  // x19
    long long v23;  // x0
    struct_14 **ptr;  // x0
    struct_6 *v4;  // x0
    struct_6 *v5;  // x20
    struct_6 *ptr8;  // x21
    struct_6 *v7;  // x21
    struct_2 *v8;  // x0
    struct_6 *ptr9;  // x21
    struct_6 *v10;  // x21
    int i;  // [bp-0x54], Other Possible Types: unsigned int

    if (!(g_1fab147 & 1))
    {
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1ef7ba0);
        sub_f7d92c(&g_1ef7ba8);
        sub_f7d92c(&g_1eed620);
        sub_f7d92c("I)");
        sub_f7d92c(&g_1f16088);
        sub_f7d92c(&g_1f0bdd0);
        sub_f7d92c(&g_1f100d8);
        sub_f7d92c(&g_1f10140);
        g_1fab147 = 1;
    }
    i = 0;
    if (!a1)
        return 0;
    if (CustomGamepadProfileBank__CreateSerializer())
    {
        v1 = XmlSerializer__Deserialize();
        v2 = v1;
        if (!v1)
            goto LABEL_1033c40;
        a1 = g_1eed620;
        v3 = g_1eed620->field_130;
        if (v2->field_0->field_130 >= (unsigned int)v3 && *((long long *)(v2->field_0->field_c8 + v3 * 8 - 8)) == g_1eed620)
        {
            i = 0;
            if (v2->field_18 < 1)
                return 1;
            do
            {
                a1 = 0x7;
                v4 = sub_f7d9d4(g_1eee378, 7);
                if (!v4)
                {
LABEL_1033c30:
                    sub_f7db74();
                    goto LABEL_1033c34;
                }
                v5 = v4;
                if (v4->field_18)
                {
                    ptr8 = v5;
                    ptr8->field_20 = g_1f0bdd0;
                    v7 = &ptr8->field_20;
                    sub_f7d8d0(v7, g_1f0bdd0);
                    a1 = NULL;
                    v8 = Int32__ToString(&i, 0);
                    if (*((int *)&v7->padding_0[8]) <= 1)
                        goto LABEL_1033c2c;
                    ptr9 = v5;
                    ptr9->field_28 = v8;
                    v10 = &ptr9->field_28;
                    a1 = v8;
                    sub_f7d8d0(v10, a1);
                    if (*((int *)&v10->padding_0[16]) <= 2)
                        goto LABEL_1033c2c;
                    p = v5;
                    p->field_30 = g_1f100d8;
                    sub_f7d8d0((struct struct_6 *)&p->field_30, g_1f100d8);
                    a1 = i;
                    addr = sub_14a30c0(v2, a1, g_1ef7ba8);
                    if (!addr)
                        goto LABEL_1033c30;
                    if (v5->field_18 <= 3)
                        goto LABEL_1033c2c;
                    a1 = addr->field_10;
                    ptr3 = v5;
                    ptr3->field_38 = a1;
                    v14 = &ptr3->field_38;
                    sub_f7d8d0(v14, a1);
                    if ((int)v14->field_20 <= 4)
                        goto LABEL_1033c2c;
                    ptr4 = v5;
                    ptr4->field_40 = g_1f10140;
                    sub_f7d8d0((struct struct_6 *)&ptr4->field_40, g_1f10140);
                    a1 = i;
                    ptr5 = sub_14a30c0(v2, a1, g_1ef7ba8);
                    if (!ptr5)
                        goto LABEL_1033c30;
                    if (v5->field_18 <= 5)
                        goto LABEL_1033c2c;
                    a1 = ptr5->field_18;
                    ptr6 = v5;
                    ptr6->field_48 = a1;
                    v18 = &ptr6->field_48;
                    sub_f7d8d0(v18, a1);
                    if ((int)v18->field_30 <= 6)
                        goto LABEL_1033c2c;
                }
                else
                {
LABEL_1033c2c:
                    sub_f7db7c();
                    goto LABEL_1033c30;
                }
                ptr7 = v5;
                ptr7->field_50 = g_1f16088;
                sub_f7d8d0((struct struct_6 *)&ptr7->field_50, g_1f16088);
                v20 = String__Concat(v5, 0);
                if (!g_1eef458->field_e0)
                    sub_f7da5c(g_1eef458);
                Debug__Log(v20, 0);
                i += 1;
            } while (i < v2->field_18);
            return 1;
        }
LABEL_1033c34:
        sub_f7df10(v2);
    }
    v1 = sub_f7db74();
LABEL_1033c40:
    i = 0;
    v21 = sub_f7db74(v1);
    if ((unsigned int)a1 == 1)
    {
        v22 = __cxa_begin_catch(v21);
        v23 = sub_f7d940(&g_1eef838);
        if (((char)sub_f7dfa0(v23, *(v22)->field_0) & 1))
        {
            __cxa_end_catch();
            return 0;
        }
        ptr = __cxa_allocate_exception(8);
        *(ptr) = *(v22);
        v21 = __cxa_throw(ptr, &g_1db6f08, 0);
        __cxa_end_catch(v21, &g_1db6f08, 0);
    }
    sub_e29990(sub_1026098(v21));
}
```

## `CustomGamepadProfileBank.SaveToStream` — RVA `0xc33cdc`

- Decompiled symbol: `CustomGamepadProfileBank_SaveToStream`
- Metadata signature: `private bool SaveToStream(XmlTextWriter stream) { }`
- Native interval: `184` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    long long field_0;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern long long g_1db6f08;
extern long long g_1eef838;

unsigned int CustomGamepadProfileBank_SaveToStream(unsigned long a0, unsigned long long a1)
{
    long long v0;  // x19
    struct_0 **v1;  // x19
    long long v2;  // x0
    struct_1 **ptr;  // x0

    if (!a1)
        return 0;
    if (CustomGamepadProfileBank__CreateSerializer())
    {
        XmlSerializer__Serialize();
        return 1;
    }
    v0 = sub_f7db74();
    if ((unsigned int)a1 == 1)
    {
        v1 = __cxa_begin_catch(v0);
        v2 = sub_f7d940(&g_1eef838);
        if (((char)sub_f7dfa0(v2, *(v1)->field_0) & 1))
        {
            __cxa_end_catch();
            return 0;
        }
        ptr = __cxa_allocate_exception(8);
        *(ptr) = *(v1);
        v0 = __cxa_throw(ptr, &g_1db6f08, 0);
        __cxa_end_catch(v0, &g_1db6f08, 0);
    }
    sub_e29990(sub_1026098(v0));
}
```

## `CustomGamepadProfileBank.CreateSerializer` — RVA `0xc33d94`

- Decompiled symbol: `CustomGamepadProfileBank_CreateSerializer`
- Metadata signature: `private XmlSerializer CreateSerializer() { }`
- Native interval: `504` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    struct struct_1 *field_0;
    char padding_8[16];
    unsigned int field_18;
    char padding_1c[4];
    long long field_20;
    long long field_28;
    long long field_30;
} struct_2;

typedef struct struct_1 {
    char padding_0[64];
    long long field_40;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern long long g_1eeafd8;
extern long long g_1eeb468;
extern long long g_1eebd88;
extern long long g_1eebd90;
extern long long g_1eee3d8;
extern struct_0 *g_1ef1f08;
extern long long g_1ef29a0;
extern char g_1fab146;

long long CustomGamepadProfileBank_CreateSerializer(void)
{
    long long v0;  // x0
    struct_2 *v1;  // x20
    long long v10;  // x0
    long long v2;  // x0
    long long v3;  // x21
    long long v4;  // x0
    struct_2 *ptr;  // x0
    long long v6;  // x21
    struct_2 *p;  // x0
    long long v8;  // x21
    struct_2 *addr;  // x0

    if (!(g_1fab146 & 1))
    {
        sub_f7d92c(&g_1eeb468);
        sub_f7d92c(&g_1eebd88);
        sub_f7d92c(&g_1eebd90);
        sub_f7d92c(&g_1eeafd8);
        sub_f7d92c(&g_1eee3d8);
        sub_f7d92c(&g_1ef1f08);
        sub_f7d92c(&g_1ef29a0);
        g_1fab146 = 1;
    }
    if (!g_1ef1f08->field_e0)
        sub_f7da5c(g_1ef1f08);
    v0 = Type__GetTypeFromHandle(g_1eeafd8, 0);
    v1 = sub_f7d9d4(g_1eee3d8, 3);
    v2 = Type__GetTypeFromHandle(g_1eeb468, 0);
    if (!v1)
        sub_f7db74();
    v3 = v2;
    if (!v2 || !((v4 = sub_f7da60(v3, v1->field_0->field_40), !v4)))
    {
        if (v1->field_18)
        {
            ptr = v1;
            ptr->field_20 = v3;
            sub_f7d8d0((struct struct_2 *)&ptr->field_20, v3);
            v6 = Type__GetTypeFromHandle(g_1eebd88, 0);
            if (!v6 || !((v4 = sub_f7da60(v6, v1->field_0->field_40), !v4)))
            {
                if (v1->field_18 <= 1)
                    goto LABEL_1033f78;
                p = v1;
                p->field_28 = v6;
                sub_f7d8d0((struct struct_2 *)&p->field_28, v6);
                v8 = Type__GetTypeFromHandle(g_1eebd90, 0);
                if (!v8 || (v4 = sub_f7da60(v8, v1->field_0->field_40), v4))
                {
                    if (v1->field_18 > 2)
                    {
                        addr = v1;
                        addr->field_30 = v8;
                        sub_f7d8d0((struct struct_2 *)&addr->field_30, v8);
                        v10 = sub_f7db70(g_1ef29a0);
                        XmlSerializer__ctor(v10, v0, v1, 0);
                        return v10;
                    }
                    goto LABEL_1033f78;
                }
            }
        }
        else
        {
LABEL_1033f78:
            v4 = sub_f7db7c();
        }
    }
    sub_f7da4c(sub_f7db98(v4), 0);
    sub_f7db74();
}
```
