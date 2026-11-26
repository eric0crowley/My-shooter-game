# Native pseudocode: WaypointGroup

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `WaypointGroup.Start` — RVA `0xc8875c`

- Decompiled symbol: `WaypointGroup_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `320` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WaypointGroup_Recovered` matched 2 offsets against `WaypointGroup` metadata (confidence 1.00).

```c
typedef struct WaypointGroup_Recovered {
    char padding_0[40];
    struct struct_0 *wayPoints;
    long long myTransform;
} WaypointGroup_Recovered;

typedef struct struct_0 {
    char padding_0[16];
    unsigned long long field_10;
    int field_18;
    unsigned int field_1c;
} struct_0;

typedef struct struct_2 {
    char padding_0[32];
    unsigned long long field_20;
} struct_2;

extern long long g_1ef8a80;
extern long long g_1ef8a88;
extern char g_1fab42f;

long long WaypointGroup_Start(struct_1 *addr)
{
    long long v0;  // x0
    struct_1 *ptr3;  // x20
    unsigned long v10;  // x10
    struct_2 *ptr4;  // x0
    unsigned long v12;  // x0
    struct_0 *ptr;  // x8
    int v3;  // w2
    unsigned int v4;  // w9
    int v5;  // w21
    unsigned long v6;  // x0
    struct_0 *p;  // x22
    unsigned long long v8;  // x0
    unsigned long long v9;  // x8

    if (!(g_1fab42f & 1))
    {
        sub_f7d92c(&g_1ef8a80);
        sub_f7d92c(&g_1ef8a88);
        g_1fab42f = 1;
    }
    v0 = Component__get_transform(addr, 0);
    addr->field_30 = v0;
    ptr3 = &addr->field_30;
    sub_f7d8d0(ptr3, v0);
    ptr = *((long long *)&ptr3->padding_0[8]);
    if (ptr)
    {
        v3 = ptr->field_18;
        v4 = ptr->field_1c + 1;
        ptr->field_18 = 0;
        ptr->field_1c = v4;
        if (v3 >= 1)
            Array__Clear(ptr->field_10, 0);
        if (*((long long *)&ptr3->padding_0[0]))
        {
            v5 = 0;
            do
            {
                v6 = Transform__get_childCount();
                if ((unsigned int)v6 <= v5)
                    return v6;
                if (!addr->field_30 || !((p = (struct_0 *)addr->field_28, v8 = (unsigned long long)Transform__GetChild(addr->field_30, v5, 0), p && (v9 = p->field_10, p->field_1c = p->field_1c + 1, v9))))
                    break;
                v10 = p->field_18;
                if (*((int *)(v9 + 24)) > (unsigned int)v10)
                {
                    ptr4 = v9 + v10 * 8;
                    p->field_18 = (unsigned int)v10 + 1;
                    ptr4->field_20 = Transform__GetChild(addr->field_30, v5, 0);
                    sub_f7d8d0((struct struct_2 *)&ptr4->field_20);
                }
                else
                {
                    sub_14a3390(p);
                }
                v5 += 1;
            } while (*((long long *)&ptr3->padding_0[0]));
        }
    }
    v12 = sub_f7db74();
    return sub_f7db74();
}
```

## `WaypointGroup.OnDrawGizmos` — RVA `0xc8889c`

- Decompiled symbol: `WaypointGroup_OnDrawGizmos`
- Metadata signature: `private void OnDrawGizmos() { }`
- Native interval: `1000` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[16];
    unsigned long long field_10;
    int field_18;
    unsigned int field_1c;
    char field_20;
    char padding_21[7];
    struct struct_2 *field_28;
    long long field_30;
} struct_2;

typedef struct struct_3 {
    char padding_0[32];
    unsigned long long field_20;
} struct_3;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

extern struct_0 *g_1ef0c58;
extern struct_1 *g_1ef0e48;
extern long long g_1ef8a80;
extern long long g_1ef8a88;
extern long long g_1ef8a98;
extern long long g_1ef8aa0;
extern char g_1fab430;

struct_2 * WaypointGroup_OnDrawGizmos(struct_2 *ptr)
{
    struct_2 *v0;  // x0
    struct_2 *v1;  // x0
    struct_2 *p;  // x22
    unsigned long long v11;  // x0
    unsigned long v12;  // x8
    unsigned long v13;  // x10
    struct_3 *ptr3;  // x0
    unsigned int v15;  // w20
    long long v16;  // x0
    struct_2 *v17;  // x0
    unsigned int v18;  // w21
    struct_2 *v2;  // x0
    long long v3;  // x0
    struct_2 *ptr4;  // x20
    struct_2 *addr;  // x8
    unsigned int v6;  // w2
    unsigned int v7;  // w9
    int v8;  // w21
    struct_2 *v9;  // x0

    v0 = ptr;
    if (!(g_1fab430 & 1))
    {
        sub_f7d92c(&g_1ef8a80);
        sub_f7d92c(&g_1ef8a88);
        sub_f7d92c(&g_1ef8a98);
        sub_f7d92c(&g_1ef8aa0);
        sub_f7d92c(&g_1ef0c58);
        v1 = sub_f7d92c(&g_1ef0e48);
        g_1fab430 = 1;
        v0 = v1;
    }
    v2 = v0;
    if (!ptr->field_20)
        return v2;
    v3 = Component__get_transform(ptr, 0);
    ptr->field_30 = v3;
    ptr4 = &ptr->field_30;
    sub_f7d8d0(ptr4, v3);
    addr = *((long long *)&ptr4->padding_0[8]);
    if (addr)
    {
        v6 = addr->field_18;
        v7 = addr->field_1c + 1;
        addr->field_18 = 0;
        addr->field_1c = v7;
        if (v6 >= 1)
            Array__Clear(addr->field_10, 0);
        if (*((long long *)&ptr4->padding_0[0]))
        {
            v8 = 0;
            do
            {
                v9 = Transform__get_childCount();
                p = ptr->field_28;
                if ((unsigned int)v9 <= v8 || !*((long long *)&ptr4->padding_0[0]) || !((v11 = (unsigned long long)Transform__GetChild(*((long long *)&ptr4->padding_0[0]), v8, 0), p && (v12 = (unsigned long)p->field_10, p->field_1c = p->field_1c + 1, v12))))
                    break;
                v13 = p->field_18;
                if (*((int *)(v12 + 24)) > (unsigned int)v13)
                {
                    ptr3 = v12 + v13 * 8;
                    p->field_18 = (unsigned int)v13 + 1;
                    ptr3->field_20 = Transform__GetChild(*((long long *)&ptr4->padding_0[0]), v8, 0);
                    sub_f7d8d0((struct struct_3 *)&ptr3->field_20);
                }
                else
                {
                    sub_14a3390(p);
                }
                v8 += 1;
            } while (*((long long *)&ptr4->padding_0[0]));
        }
    }
    while (true)
    {
        v9 = sub_f7db74();
        if (!p)
        {
            return v9;
        }
        else if (p->field_18 >= 1)
        {
            v15 = 0;
            while (true)
            {
                v16 = sub_14a30c0(p, v15, g_1ef8aa0);
                if (!g_1ef0c58->field_e0)
                    sub_f7da5c(g_1ef0c58);
                v17 = Object__op_Inequality(v16, 0, 0);
                if (((char)v17 & 1))
                {
                    Gizmos__set_color(0);
                    if (!ptr->field_28 || !sub_14a30c0(ptr->field_28, v15, g_1ef8aa0))
                        break;
                    Transform__get_position();
                    Gizmos__DrawWireSphere(0);
                    v17 = ptr->field_28;
                    if (!v17)
                        break;
                    if (v15 != v17->field_18 - 1)
                    {
                        v18 = v15 + 1;
                        p = sub_14a30c0();
                        if (!g_1ef0c58->field_e0)
                            sub_f7da5c(g_1ef0c58);
                        v17 = Object__op_Inequality(p, 0, 0);
                        if (((char)v17 & 1))
                        {
                            v17 = ptr->field_28;
                            if (!v17)
                                break;
                            if (v17->field_18 >= 2)
                            {
                                if (!sub_14a30c0() || !((Transform__get_position(), ptr->field_28 && sub_14a30c0(ptr->field_28, (unsigned long long)v18, g_1ef8aa0))))
                                    break;
                                Transform__get_position();
                                if (!g_1ef0e48->field_e0)
                                    sub_f7da5c(g_1ef0e48);
                                Gizmos__set_color(0);
                                if (!ptr->field_28 || !sub_14a30c0(ptr->field_28, v15, g_1ef8aa0) || !((Transform__get_position(), ptr->field_28 && sub_14a30c0(ptr->field_28, (unsigned long long)v18, g_1ef8aa0))))
                                    break;
                                Transform__get_position();
                                v17 = Gizmos__DrawLine(0);
                            }
                        }
                    }
                }
                p = ptr->field_28;
                if (!p)
                    break;
                v15 += 1;
                if (v15 >= p->field_18)
                    return v17;
            }
        }
        else
        {
            return v9;
        }
    }
}
```

## `WaypointGroup.ctor` — RVA `0xc88c84`

- Decompiled symbol: `WaypointGroup_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `144` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WaypointGroup_Recovered` matched 2 offsets against `WaypointGroup` metadata (confidence 1.00).

```c
typedef struct WaypointGroup_Recovered {
    char padding_0[32];
    char drawWaypoints;
    char padding_21[7];
    long long wayPoints;
} WaypointGroup_Recovered;

extern long long g_1eed8e0;
extern long long g_1ef8a70;
extern char g_1fab431;

void WaypointGroup_ctor(struct_0 *ptr)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    long long v10;  // x20
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
    if (!(g_1fab431 & 1))
    {
        sub_f7d92c(&g_1ef8a70);
        sub_f7d92c(&g_1eed8e0);
        g_1fab431 = 1;
    }
    ptr->field_20 = 1;
    v10 = sub_f7db70(g_1eed8e0);
    sub_14a2b64(v10, g_1ef8a70);
    ptr->field_28 = v10;
    sub_f7d8d0((struct WaypointGroup_Recovered *)&ptr->field_28, v10);
    MonoBehaviour__ctor();
    return;
}
```
