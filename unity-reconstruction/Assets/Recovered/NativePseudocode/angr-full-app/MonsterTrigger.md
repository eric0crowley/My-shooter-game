# Native pseudocode: MonsterTrigger

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `MonsterTrigger.Start` — RVA `0xc85374`

- Decompiled symbol: `MonsterTrigger_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `204` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[32];
    struct struct_1 *field_20;
} struct_2;

typedef struct struct_3 {
    char padding_0[24];
    unsigned int field_18;
} struct_3;

typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab418;

struct_2 * MonsterTrigger_Start(struct_2 *ptr, unsigned long a1)
{
    struct_2 *v0;  // x0
    struct_2 *v1;  // x0
    struct_2 *v2;  // x0
    struct_3 *p;  // x8
    unsigned long long v4;  // x22
    unsigned long v5;  // x9
    unsigned long long v6;  // x23
    struct_3 *v7;  // x8
    unsigned long v8;  // x0

    v0 = ptr;
    if (!(g_1fab418 & 1))
    {
        v1 = sub_f7d92c(&g_1ef0c58);
        g_1fab418 = 1;
        v0 = v1;
    }
    p = ptr->field_20;
    if (ptr->field_20)
    {
        v4 = 4;
        do
        {
            v5 = p->field_18;
            v6 = v4 - 4;
            if ((v5 & 4294967295) <= v6)
                return v2;
            if (v5 <= v6)
                sub_f7db7c();
            if (!g_1ef0c58->field_e0)
                sub_f7da5c(g_1ef0c58);
            if (!(Object__op_Implicit(*((long long *)&p->padding_0[8 * v4]), 0) & 1))
                continue;
            v7 = ptr->field_20;
            if (!v7)
                break;
            if (v7->field_18 <= v6)
                sub_f7db7c();
            if (!*((long long *)&v7->padding_0[8 * v4]))
                break;
            v2 = GameObject__SetActive(*((long long *)&v7->padding_0[8 * v4]), 0, 0);
        } while ((p = (struct_3 *)ptr->field_20, v4 += 1, p));
    }
    v8 = sub_f7db74();
    return sub_f7db74();
}
```

## `MonsterTrigger.OnTriggerEnter` — RVA `0xc85440`

- Decompiled symbol: `MonsterTrigger_OnTriggerEnter`
- Metadata signature: `private void OnTriggerEnter(Collider col) { }`
- Native interval: `344` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[32];
    struct struct_1 *field_20;
} struct_2;

typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1f0cf98;
extern char g_1fab419;

long long MonsterTrigger_OnTriggerEnter(struct_2 *ptr, long long a1)
{
    long long v0;  // x0
    unsigned long v1;  // x0
    struct_1 *p;  // x8
    unsigned long long v3;  // x22
    unsigned long v4;  // x9
    unsigned long long v5;  // x23
    struct_1 *v6;  // x8
    unsigned long long v7;  // x0
    unsigned long v8;  // x0

    if (!(g_1fab419 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f0cf98);
        g_1fab419 = 1;
    }
    if (a1 && Component__get_gameObject(a1, 0))
    {
        v0 = GameObject__get_tag();
        v1 = String__op_Equality(v0, g_1f0cf98, 0);
        if (!((char)v1 & 1))
            return v1;
        p = ptr->field_20;
        if (ptr->field_20)
        {
            v3 = 4;
            do
            {
                v4 = p->field_18;
                v5 = v3 - 4;
                if ((v4 & 4294967295) > v5)
                {
                    if (v4 <= v5)
                        sub_f7db7c();
                    if (!g_1ef0c58->field_e0)
                        sub_f7da5c(g_1ef0c58);
                    if (!(Object__op_Implicit(*((long long *)&p->padding_0[8 * v3]), 0) & 1))
                        continue;
                    v6 = ptr->field_20;
                    if (!v6)
                        break;
                    if (v6->field_18 <= v5)
                        sub_f7db7c();
                    if (!*((long long *)&v6->padding_0[8 * v3]))
                        break;
                    GameObject__SetActive(*((long long *)&v6->padding_0[8 * v3]), 1, 0);
                }
                else
                {
                    if (Component__get_transform(ptr, 0))
                    {
                        Component__get_gameObject();
                        if (!g_1ef0c58->field_e0)
                            sub_f7da5c(g_1ef0c58);
                        v7 = Object__Destroy();
                        return Object__Destroy();
                    }
                    break;
                }
            } while ((p = (struct_1 *)ptr->field_20, v3 += 1, p));
        }
    }
    v8 = sub_f7db74();
    return sub_f7db74();
}
```

## `MonsterTrigger.ctor` — RVA `0xc85598`

- Decompiled symbol: `MonsterTrigger_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long MonsterTrigger_ctor(void)
{
}
```
