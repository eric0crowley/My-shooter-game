# Native pseudocode: DigitalBinding

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `DigitalBinding.ctor` — RVA `0xc4eaa8`

- Decompiled symbol: `DigitalBinding_ctor`
- Metadata signature: `public void .ctor(InputBindingBase parent) { }`
- Native interval: `28` bytes
- Result: `pseudocode`

```c
void DigitalBinding_ctor(unsigned long a0)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    InputBindingBase__ctor(); /* do not return */
}
```

## `DigitalBinding.Sync` — RVA `0xc4f00c`

- Decompiled symbol: `DigitalBinding_Sync`
- Metadata signature: `public void Sync(bool state, InputRig rig, bool skipIfTargetIsMuted = false) { }`
- Native interval: `340` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    char field_10;
    char padding_11[7];
    int field_18;
    char padding_1c[4];
    struct struct_1 *field_20;
    struct struct_1 *field_28;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1ef7f38;
extern long long g_1ef7f40;
extern long long g_1ef8f88;
extern long long g_1ef8f90;
extern char g_1fab2b9;

struct_1 * DigitalBinding_Sync(struct_1 *ptr, unsigned int a1, unsigned long a2, unsigned long a3)
{
    struct_1 *v0;  // x0
    struct_1 *v1;  // x0
    struct_1 *v2;  // x0
    struct_1 *v3;  // x0
    struct_1 *v4;  // x0
    unsigned int v5;  // w22
    int v6;  // w22
    unsigned long v7;  // x0

    v0 = ptr;
    if (!(g_1fab2b9 & 1))
    {
        sub_f7d92c(&g_1ef8f88);
        sub_f7d92c(&g_1ef7f38);
        sub_f7d92c(&g_1ef8f90);
        sub_f7d92c(&g_1ef7f40);
        v1 = sub_f7d92c(&g_1ef0c58);
        g_1fab2b9 = 1;
        v0 = v1;
    }
    v2 = v0;
    if (!((char)a1 & 1))
        return v2;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v3 = Object__op_Equality(a2, 0, 0);
    if (((char)v3 & 1))
    {
        return v3;
    }
    else if (ptr->field_10)
    {
        v4 = ptr->field_28;
        if (v4)
        {
            v5 = 0;
            do
            {
                if (v4->field_18 <= v5)
                {
                    v4 = ptr->field_20;
                    if (v4)
                    {
                        v6 = 0;
                        do
                        {
                            if (v4->field_18 <= v6)
                                return v4;
                        } while ((v4 = (struct_1 *)(unsigned long long)sub_14a30c0(), (unsigned long long)sub_14a30c0() && (DigitalBinding_AxisElem__ApplyToRig(), v4 = (struct_1 *)ptr->field_20, v6 = (int)(v6 + 1), v4)));
                    }
                }
            } while ((v4 = (struct_1 *)(unsigned long long)sub_1491d6c(), a2 && (InputRig__SetKeyCode(a2, (unsigned int)v4), v4 = (struct_1 *)ptr->field_28, v5 += 1, v4)));
        }
        v7 = sub_f7db74(v4);
        return sub_f7db74(v4);
    }
    else
    {
        return v3;
    }
}
```

## `DigitalBinding.ctor` — RVA `0xc56dec`

- Decompiled symbol: `DigitalBinding_ctor`
- Metadata signature: `public void .ctor(KeyCode key, bool bindToAxis, string axisName, bool axisNegSide, bool enabled, InputBindingBase parent) { }`
- Native interval: `164` bytes
- Result: `pseudocode`

```c
void DigitalBinding_ctor(unsigned long a0, unsigned long a1, unsigned long a2, unsigned long a3, unsigned long a4, unsigned long a5, unsigned long a6)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
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
    InputBindingBase__ctor(); /* do not return */
}
```

## `DigitalBinding.BasicConstructor` — RVA `0xc5be6c`

- Decompiled symbol: `DigitalBinding_BasicConstructor`
- Metadata signature: `private void BasicConstructor() { }`
- Native interval: `220` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DigitalBinding_Recovered` matched 2 offsets against `DigitalBinding` metadata (confidence 0.67).

```c
typedef struct DigitalBinding_Recovered {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    long long axisList;
    long long keyList;
} DigitalBinding_Recovered;

extern long long g_1eed6d0;
extern long long g_1eed9c0;
extern long long g_1ef7f10;
extern long long g_1ef8f60;
extern char g_1fab2b7;

void DigitalBinding_BasicConstructor(struct_0 *ptr)
{
    unsigned long long v7;  // x30
    unsigned long long v8;  // x24
    unsigned long long v9;  // x23
    unsigned long long v10;  // x22
    unsigned long long v11;  // x21
    unsigned long long v12;  // x20
    unsigned long long v13;  // x19
    long long v14;  // x20
    long long v15;  // x0
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
    if (!(g_1fab2b7 & 1))
    {
        sub_f7d92c(&g_1ef7f10);
        sub_f7d92c(&g_1ef8f60);
        sub_f7d92c(&g_1eed9c0);
        sub_f7d92c(&g_1eed6d0);
        g_1fab2b7 = 1;
    }
    ptr->field_10 = 0;
    v14 = sub_f7db70(g_1eed6d0);
    sub_1491880(v14, 1, g_1ef7f10);
    ptr->field_28 = v14;
    sub_f7d8d0((struct DigitalBinding_Recovered *)&ptr->field_28, v14);
    v15 = sub_f7db70(g_1eed9c0);
    sub_14a2bd4(v15, 1, g_1ef8f60);
    ptr->field_20 = v15;
    sub_f7d8d0();
    return;
}
```

## `DigitalBinding.AddKey` — RVA `0xc5bf48`

- Decompiled symbol: `DigitalBinding_AddKey`
- Metadata signature: `public void AddKey(KeyCode code) { }`
- Native interval: `164` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_0;

typedef struct struct_2 {
    char padding_0[40];
    struct struct_1 *field_28;
} struct_2;

typedef struct struct_1 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_1;

extern long long g_1ef7f18;
extern char g_1fab2bc;

struct_0 * DigitalBinding_AddKey(struct_2 *p, unsigned int a1)
{
    struct_1 *ptr;  // x0
    unsigned long long v1;  // x8
    unsigned long v2;  // x10

    if (!(g_1fab2bc & 1))
    {
        sub_f7d92c(&g_1ef7f18);
        g_1fab2bc = 1;
    }
    ptr = p->field_28;
    if (ptr)
    {
        v1 = ptr->field_10;
        ptr->field_1c = ptr->field_1c + 1;
        if (v1)
        {
            v2 = ptr->field_18;
            if (*((int *)(v1 + 24)) > (unsigned int)v2)
            {
                ptr->field_18 = (unsigned int)v2 + 1;
                *((unsigned int *)(v1 + v2 * 4 + 32)) = a1;
                return ptr;
            }
        }
    }
    sub_f7db74(ptr);
}
```

## `DigitalBinding.AddAxis` — RVA `0xc5bfec`

- Decompiled symbol: `DigitalBinding_AddAxis`
- Metadata signature: `public DigitalBinding.AxisElem AddAxis() { }`
- Native interval: `208` bytes
- Result: `pseudocode`

```c
long long DigitalBinding_AddAxis(void)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
}
```

## `DigitalBinding.ctor` — RVA `0xc5c0e8`

- Decompiled symbol: `DigitalBinding_ctor`
- Metadata signature: `public void .ctor(KeyCode key, string axisName, bool enabled, InputBindingBase parent) { }`
- Native interval: `156` bytes
- Result: `pseudocode`

```c
void DigitalBinding_ctor(unsigned long a0, unsigned long a1, unsigned long a2, unsigned long a3, unsigned long a4)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
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
    InputBindingBase__ctor(); /* do not return */
}
```

## `DigitalBinding.ctor` — RVA `0xc5c184`

- Decompiled symbol: `DigitalBinding_ctor`
- Metadata signature: `public void .ctor(KeyCode key, bool enabled, InputBindingBase parent) { }`
- Native interval: `92` bytes
- Result: `pseudocode`

```c
void DigitalBinding_ctor(unsigned long a0, unsigned long a1, unsigned long a2, unsigned long a3)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    InputBindingBase__ctor(); /* do not return */
}
```

## `DigitalBinding.CopyFrom` — RVA `0xc5c1e0`

- Decompiled symbol: `DigitalBinding_CopyFrom`
- Metadata signature: `public void CopyFrom(DigitalBinding b) { }`
- Native interval: `596` bytes
- Result: `pseudocode`
- Heuristic layout hint: `DigitalBinding_Recovered` matched 2 offsets against `DigitalBinding` metadata (confidence 0.67).

```c
typedef struct struct_2 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    struct struct_0 *field_20;
    struct struct_1 *field_28;
} struct_2;

typedef struct DigitalBinding_Recovered {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    unsigned long long axisList;
    struct struct_4 *keyList;
} DigitalBinding_Recovered;

typedef struct struct_7 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_7;

typedef struct struct_4 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    struct struct_3 *field_20;
    struct struct_5 *field_28;
} struct_4;

typedef struct struct_0 {
    char padding_0[16];
    long long field_10;
    int field_18;
    unsigned int field_1c;
} struct_0;

typedef struct struct_1 {
    char padding_0[24];
    int field_18;
    unsigned int field_1c;
} struct_1;

typedef struct struct_3 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_3;

typedef struct struct_5 {
    char padding_0[24];
    unsigned int field_18;
    unsigned int field_1c;
} struct_5;

extern long long g_1ef7f20;
extern long long g_1ef7f38;
extern long long g_1ef7f40;
extern long long g_1ef7f48;
extern long long g_1ef8f70;
extern long long g_1ef8f88;
extern long long g_1ef8f90;
extern char g_1fab2b8;

struct_2 * DigitalBinding_CopyFrom(struct_2 *addr, struct_6 *ptr)
{
    struct_2 *v0;  // x0
    struct_2 *v1;  // x0
    unsigned int ptr3[8];  // x8
    struct_4 *i;  // x0
    unsigned int v12;  // w21
    unsigned int v13;  // w0
    struct_4 *v14;  // x0
    unsigned int v15;  // w21
    unsigned int v16;  // w9
    struct_2 *v2;  // x0
    unsigned int v3;  // w8
    struct_7 *p;  // x9
    unsigned long long v5;  // x8
    unsigned int v6;  // w2
    unsigned int v7;  // w10
    unsigned int v8;  // w21
    unsigned long v9;  // x0

    v0 = addr;
    if (!(g_1fab2b8 & 1))
    {
        sub_f7d92c(&g_1ef8f70);
        sub_f7d92c(&g_1ef7f20);
        sub_f7d92c(&g_1ef8f88);
        sub_f7d92c(&g_1ef7f38);
        sub_f7d92c(&g_1ef8f90);
        sub_f7d92c(&g_1ef7f40);
        v1 = sub_f7d92c(&g_1ef7f48);
        g_1fab2b8 = 1;
        v0 = v1;
    }
    v2 = v0;
    if (!ptr)
        return v2;
    v3 = ptr->field_10;
    addr->field_10 = v3;
    if (!v3)
        return v2;
    InputBindingBase__Enable(addr, 0);
    p = addr->field_20;
    if (p && (v5 = ptr->field_20, v5))
    {
        v6 = p->field_18;
        if (v6 == *((int *)(v5 + 24)))
        {
LABEL_105c29c:
            v8 = 0;
            do
            {
                if (*((int *)(v5 + 24)) <= v8)
                {
                    ptr3 = addr->field_28;
                    if (ptr3)
                    {
                        i = ptr->field_28;
                        if (i)
                        {
                            if (ptr3[6] != *((int *)&i->padding_11[7]))
                            {
                                v15 = 0;
                                v16 = ptr3[7] + 1;
                                ptr3[6] = 0;
                                ptr3[7] = v16;
                                do
                                {
                                    if (*((int *)&i->padding_11[7]) <= v15)
                                        return i;
                                    DigitalBinding__AddKey(addr, sub_1491d6c());
                                    i = ptr->field_28;
                                    v15 += 1;
                                } while (i);
                            }
                            else if (ptr3[6] >= 1)
                            {
                                v12 = 0;
                                while (true)
                                {
                                    v13 = sub_1491d6c();
                                    if (!addr->field_28 || !((sub_1491dc0(addr->field_28, (unsigned long long)v12, (unsigned long long)v13, g_1ef7f48), v14 = (struct_4 *)ptr->field_28, v14)))
                                        break;
                                    v12 += 1;
                                    if (v12 >= *((int *)&v14->padding_11[7]))
                                        return v14;
                                }
                            }
                            else
                            {
                                return i;
                            }
                        }
                    }
                }
            } while (addr->field_20 && (v9 = (unsigned long)sub_14a30c0(addr->field_20, (unsigned long long)v8, g_1ef8f90), ptr->field_20 && (sub_14a30c0(ptr->field_20, (unsigned long long)v8, g_1ef8f90), v9 && (DigitalBinding_AxisElem__CopyFrom(), v5 = ptr->field_20, v8 += 1, v5))));
        }
        else
        {
            v7 = p->field_1c + 1;
            p->field_18 = 0;
            p->field_1c = v7;
            if (v6 < 1 || (Array__Clear(p->field_10, 0), v5 = ptr->field_20, v5))
            {
                if (*((int *)(v5 + 24)) > 0)
                    DigitalBinding__AddAxis(); /* do not return */
                goto LABEL_105c29c;
            }
        }
    }
    sub_f7db74();
}
```

## `DigitalBinding.Clear` — RVA `0xc5c4d0`

- Decompiled symbol: `DigitalBinding_Clear`
- Metadata signature: `public void Clear() { }`
- Native interval: `24` bytes
- Result: `pseudocode`

```c
long long DigitalBinding_Clear(long long a0)
{
    unsigned long long v0;  // x0

    DigitalBinding__ClearKeys();
    v0 = DigitalBinding__ClearAxes(a0);
    return DigitalBinding__ClearAxes(a0);
}
```

## `DigitalBinding.ClearKeys` — RVA `0xc5c4e8`

- Decompiled symbol: `DigitalBinding_ClearKeys`
- Metadata signature: `public void ClearKeys() { }`
- Native interval: `80` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    struct struct_1 *field_28;
} struct_0;

typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
    unsigned int field_1c;
} struct_1;

extern long long g_1ef7f20;
extern char g_1fab2ba;

struct_0 * DigitalBinding_ClearKeys(struct_0 *p)
{
    struct_0 *v0;  // x0
    struct_0 *v1;  // x0
    struct_0 *v2;  // x0
    unsigned int ptr[8];  // x8
    unsigned int v4;  // w9

    v0 = p;
    if (!(g_1fab2ba & 1))
    {
        v1 = sub_f7d92c(&g_1ef7f20);
        g_1fab2ba = 1;
        v0 = v1;
    }
    v2 = v0;
    ptr = p->field_28;
    if (ptr)
    {
        v4 = ptr[7];
        ptr[6] = 0;
        ptr[7] = v4 + 1;
        return v2;
    }
    sub_f7db74();
}
```

## `DigitalBinding.ClearAxes` — RVA `0xc5c538`

- Decompiled symbol: `DigitalBinding_ClearAxes`
- Metadata signature: `public void ClearAxes() { }`
- Native interval: `112` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[32];
    struct struct_0 *field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
    unsigned int field_1c;
} struct_0;

extern long long g_1ef8f70;
extern char g_1fab2bb;

void DigitalBinding_ClearAxes(struct_1 *p)
{
    struct_0 *ptr;  // x8
    int v1;  // w2
    unsigned int v2;  // w9

    if (!(g_1fab2bb & 1))
    {
        sub_f7d92c(&g_1ef8f70);
        g_1fab2bb = 1;
    }
    ptr = p->field_20;
    if (ptr)
    {
        v1 = ptr->field_18;
        v2 = ptr->field_1c;
        ptr->field_18 = 0;
        ptr->field_1c = v2 + 1;
        if (v1 < 1)
            return;
        Array__Clear();
        return;
    }
    sub_f7db74();
}
```

## `DigitalBinding.RemoveLastKey` — RVA `0xc5c5a8`

- Decompiled symbol: `DigitalBinding_RemoveLastKey`
- Metadata signature: `public void RemoveLastKey() { }`
- Native interval: `116` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

typedef struct struct_2 {
    char padding_0[40];
    struct struct_1 *field_28;
} struct_2;

typedef struct struct_1 {
    char padding_0[24];
    int field_18;
} struct_1;

extern long long g_1ef7f30;
extern long long g_1ef7f38;
extern char g_1fab2bd;

struct_0 * DigitalBinding_RemoveLastKey(struct_2 *ptr, unsigned long a1, unsigned long a2)
{
    struct_1 *v0;  // x0

    if (!(g_1fab2bd & 1))
    {
        sub_f7d92c(&g_1ef7f30);
        sub_f7d92c(&g_1ef7f38);
        g_1fab2bd = 1;
    }
    v0 = ptr->field_28;
    if (!v0)
    {
        sub_f7db74(0);
    }
    else if (v0->field_18 < 1)
    {
        return v0;
    }
}
```

## `DigitalBinding.ReplaceKey` — RVA `0xc5c61c`

- Decompiled symbol: `DigitalBinding_ReplaceKey`
- Metadata signature: `public void ReplaceKey(int keyElemId, KeyCode key) { }`
- Native interval: `148` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[40];
    struct struct_0 *field_28;
} struct_0;

extern long long g_1ef7f38;
extern long long g_1ef7f48;
extern char g_1fab2be;

struct_0 * DigitalBinding_ReplaceKey(struct_0 *ptr, unsigned int a1, unsigned long a2)
{
    unsigned long v0;  // x20
    struct_0 *v1;  // x0
    struct_0 *v2;  // x0
    struct_0 *v3;  // x0
    struct_0 *v4;  // x0
    unsigned long long v5;  // x0

    v0 = a1;
    v1 = ptr;
    if (!(g_1fab2be & 1))
    {
        sub_f7d92c(&g_1ef7f38);
        v2 = sub_f7d92c(&g_1ef7f48);
        g_1fab2be = 1;
        v1 = v2;
    }
    v3 = v1;
    if (((char)(v0 >> 31) & 1))
        return v3;
    v4 = ptr->field_28;
    if (v4)
    {
        if (*((int *)&v4->padding_0[24]) > (unsigned int)v0)
        {
            v5 = sub_1491dc0();
            return sub_1491dc0();
        }
        return v4;
    }
    sub_f7db74(0);
}
```

## `DigitalBinding.GetAxisElem` — RVA `0xc5c718`

- Decompiled symbol: `DigitalBinding_GetAxisElem`
- Metadata signature: `public DigitalBinding.AxisElem GetAxisElem(int id) { }`
- Native interval: `132` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned long long field_20;
} struct_0;

extern long long g_1ef8f88;
extern long long g_1ef8f90;
extern char g_1fab2c0;

unsigned int DigitalBinding_GetAxisElem(struct_0 *a0, unsigned int a1)
{
    unsigned long v0;  // x19

    v0 = a1;
    if (!(g_1fab2c0 & 1))
    {
        sub_f7d92c(&g_1ef8f88);
        sub_f7d92c(&g_1ef8f90);
        g_1fab2c0 = 1;
    }
    if (((char)(v0 >> 31) & 1))
        return 0;
    if (a0->field_20)
    {
        if (*((int *)(a0->field_20 + 24)) > (unsigned int)v0)
            return sub_14a30c0();
        return 0;
    }
    sub_f7db74(0);
}
```

## `DigitalBinding.RemoveLastAxis` — RVA `0xc5c79c`

- Decompiled symbol: `DigitalBinding_RemoveLastAxis`
- Metadata signature: `public void RemoveLastAxis() { }`
- Native interval: `116` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[24];
    unsigned int field_18;
} struct_2;

typedef struct struct_1 {
    char padding_0[32];
    struct struct_0 *field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

extern long long g_1ef8f80;
extern long long g_1ef8f88;
extern char g_1fab2c1;

struct_2 * DigitalBinding_RemoveLastAxis(struct_1 *ptr, unsigned long a1)
{
    struct_0 *v0;  // x0
    long long v1;  // x0

    if (!(g_1fab2c1 & 1))
    {
        sub_f7d92c(&g_1ef8f80);
        sub_f7d92c(&g_1ef8f88);
        g_1fab2c1 = 1;
    }
    v0 = ptr->field_20;
    if (v0)
    {
        if (v0->field_18 >= 1)
        {
            v1 = sub_14a48fc();
            return sub_14a48fc();
        }
        return v0;
    }
    sub_f7db74(0);
}
```

## `DigitalBinding.OnIsBoundToKey` — RVA `0xc5c810`

- Decompiled symbol: `DigitalBinding_OnIsBoundToKey`
- Metadata signature: `protected override bool OnIsBoundToKey(KeyCode keycode, InputRig rig) { }`
- Native interval: `140` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[16];
    char field_10;
    char padding_11[23];
    struct struct_0 *field_28;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

extern long long g_1ef7f28;
extern long long g_1ef7f38;
extern char g_1fab2c2;

unsigned int DigitalBinding_OnIsBoundToKey(struct_1 *a0, unsigned long a1)
{
    unsigned int v0;  // w8

    if (!(g_1fab2c2 & 1))
    {
        sub_f7d92c(&g_1ef7f28);
        sub_f7d92c(&g_1ef7f38);
        g_1fab2c2 = 1;
    }
    if (a0->field_10)
    {
        if (!a0->field_28)
        {
            sub_f7db74(0);
        }
        else if (a0->field_28->field_18 >= 1)
        {
            v0 = ~((unsigned int)sub_1492a70());
            return (v0 * 2 | v0 >> 31) & 1;
        }
    }
    return 0;
}
```

## `DigitalBinding.OnIsBoundToAxis` — RVA `0xc5c89c`

- Decompiled symbol: `DigitalBinding_OnIsBoundToAxis`
- Metadata signature: `protected override bool OnIsBoundToAxis(string axisName, InputRig rig) { }`
- Native interval: `280` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    long long field_10;
} struct_0;

typedef struct struct_2 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    struct struct_1 *field_20;
} struct_2;

typedef struct struct_1 {
    char padding_0[24];
    int field_18;
} struct_1;

extern long long g_1eedbf8;
extern long long g_1ef8f78;
extern long long g_1ef8f88;
extern long long g_1f044c8;
extern char g_1fab2c3;

unsigned int DigitalBinding_OnIsBoundToAxis(struct_2 *ptr, long long a1)
{
    struct_0 *v0;  // x21
    struct_0 *p;  // x0
    struct_1 *v2;  // x19
    long long v3;  // x0
    unsigned int v4;  // w8

    if (!(g_1fab2c3 & 1))
    {
        sub_f7d92c(&g_1ef8f78);
        sub_f7d92c(&g_1ef8f88);
        sub_f7d92c(&g_1eedbf8);
        sub_f7d92c(&g_1f044c8);
        sub_f7d92c("-h");
        g_1fab2c3 = 1;
    }
    v0 = sub_f7db70(g_1ef2f80);
    Object__ctor(v0, 0);
    if (v0)
    {
        p = v0;
        p->field_10 = a1;
        sub_f7d8d0((struct struct_0 *)&p->field_10, a1);
        if (!ptr->field_10)
            return 0;
        v2 = ptr->field_20;
        if (!v2)
        {
            sub_f7db74();
        }
        else if (v2->field_18 >= 1)
        {
            v3 = sub_f7db70(g_1eedbf8);
            sub_156a5b4(v3, v0, g_1f044c8, 0);
            v4 = ~((int)sub_14a3b4c(v2, v3, g_1ef8f78));
            return (v4 * 2 | v4 >> 31) & 1;
        }
        return 0;
    }
    sub_f7db74();
}
```

## `DigitalBinding.<>c__DisplayClass20_0.ctor` — RVA `0xc5c9b4`

- Decompiled symbol: `DigitalBinding_c__DisplayClass20_0_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long DigitalBinding_c__DisplayClass20_0_ctor(void)
{
    long long v0;  // x0

    v0 = Object__ctor();
    return Object__ctor();
}
```

## `DigitalBinding.<>c__DisplayClass20_0.<OnIsBoundToAxis>b__0` — RVA `0xc5c9c8`

- Decompiled symbol: `DigitalBinding_c__DisplayClass20_0_OnIsBoundToAxis_b__0`
- Metadata signature: `internal bool <OnIsBoundToAxis>b__0(DigitalBinding.AxisElem x) { }`
- Native interval: `36` bytes
- Result: `pseudocode`

```c
void DigitalBinding_c__DisplayClass20_0_OnIsBoundToAxis_b__0(unsigned long a0, unsigned long long a1)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    if (a1)
    {
        String__op_Equality();
        return;
    }
    sub_f7db74();
}
```
