# Native pseudocode: Enemyspawner

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `Enemyspawner.Start` — RVA `0xc75e7c`

- Decompiled symbol: `Enemyspawner_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long Enemyspawner_Start(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `Enemyspawner.SpawnNewEnemy` — RVA `0xc75e80`

- Decompiled symbol: `Enemyspawner_SpawnNewEnemy`
- Metadata signature: `public void SpawnNewEnemy() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long Enemyspawner_SpawnNewEnemy(void)
{
    unsigned long v0;  // x0

    return v0;
}
```


## `Enemyspawner.Update` — RVA `0xc75e84`

- Decompiled symbol: `Enemyspawner_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `608` bytes
- Result: `pseudocode`
- Heuristic layout hint: `Enemyspawner_Recovered` matched 4 offsets against `Enemyspawner` metadata (confidence 1.00).

```c
typedef struct Enemyspawner_Recovered {
    char padding_0[32];
    unsigned long long Enemypositions;
    unsigned long long Terrorists;
    unsigned int a;
    unsigned int RandomPosition;
} Enemyspawner_Recovered;

typedef struct struct_3 {
    char padding_0[32];
    long long field_20;
} struct_3;

typedef struct struct_4 {
    char padding_0[32];
    long long field_20;
} struct_4;

typedef struct struct_5 {
    char padding_0[32];
    long long field_20;
} struct_5;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
} struct_0;

typedef struct struct_2 {
    char padding_0[224];
    unsigned int field_e0;
} struct_2;

extern struct_0 *g_1eef750;
extern struct_2 *g_1ef0c58;
extern long long g_1f00260;
extern char g_1fab2cb;
extern char g_1fab3a4;

struct_6 * Enemyspawner_Update(struct_6 *ptr)
{
    struct_6 *v0;  // x0
    struct_6 *v1;  // x0
    unsigned long v10;  // x9
    struct_4 *v11;  // x8
    unsigned long v12;  // x8
    unsigned long v13;  // x9
    struct_5 *v14;  // x8
    unsigned int v15;  // w21
    struct_6 *v16;  // x0
    long long v3;  // x0
    unsigned long v4;  // x8
    unsigned long v5;  // x21
    unsigned long v6;  // x9
    struct_3 *v7;  // x9
    unsigned long v8;  // x20
    unsigned long v9;  // x8

    v0 = ptr;
    if (!(g_1fab3a4 & 1))
    {
        sub_f7d92c(&g_1eef750);
        sub_f7d92c(&g_1f00260);
        v1 = sub_f7d92c(&g_1ef0c58);
        g_1fab3a4 = 1;
        v0 = v1;
    }
    if (g_1eef750->field_b8->field_0 != 1)
        return v0;
    g_1eef750->field_b8->field_0 = 0;
    v3 = Random__Range(0, 8, 0);
    v4 = ptr->field_28;
    ptr->field_34 = v3;
    if (v4)
    {
        v5 = ptr->field_30;
        if (*((int *)(v4 + 24)) <= (unsigned int)v5)
            sub_f7db7c(v3);
        v6 = ptr->field_20;
        if (v6)
        {
            if (*((int *)(v6 + 24)) > (int)v3)
            {
                v7 = v6 + (v3 & 4294967295) * 8;
                if (v7->field_20)
                {
                    v8 = *((long long *)(v4 + v5 * 8 + 32));
                    if (GameObject__get_transform(v7->field_20, 0))
                    {
                        v3 = Transform__get_position();
                        v9 = ptr->field_20;
                        if (v9)
                        {
                            v10 = ptr->field_34;
                            if (*((int *)(v9 + 24)) <= (unsigned int)v10)
                                sub_f7db7c(v3);
                            v11 = v9 + v10 * 8;
                            if (v11->field_20 && GameObject__get_transform(v11->field_20, 0))
                            {
                                v3 = Transform__get_position();
                                v12 = ptr->field_20;
                                if (v12)
                                {
                                    v13 = ptr->field_34;
                                    if (*((int *)(v12 + 24)) <= (unsigned int)v13)
                                        sub_f7db7c(v3);
                                    v14 = v12 + v13 * 8;
                                    if (v14->field_20 && GameObject__get_transform(v14->field_20, 0))
                                    {
                                        Transform__get_position();
                                        if ((unsigned int)v5)
                                        {
                                            if (!g_1fab2cb)
                                            {
                                                sub_f7d92c("-M");
                                                g_1fab2cb = 1;
                                            }
                                            if (!g_1ef0c58->field_e0)
                                                sub_f7da5c(g_1ef0c58);
                                            v15 = 0;
                                        }
                                        else
                                        {
                                            if (!g_1fab2cb)
                                            {
                                                sub_f7d92c("-M");
                                                g_1fab2cb = 1;
                                            }
                                            if (!g_1ef0c58->field_e0)
                                                sub_f7da5c(g_1ef0c58);
                                            v15 = 1;
                                        }
                                        v16 = sub_112a1ac(v8, g_1f00260);
                                        ptr->field_30 = v15;
                                        return v16;
                                    }
                                }
                            }
                        }
                    }
                }
            }
            else
            {
                sub_f7db7c(v3);
            }
        }
    }
    sub_f7db7c(sub_f7db74());
}
```


## `Enemyspawner.ctor` — RVA `0xc760e4`

- Decompiled symbol: `Enemyspawner_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long Enemyspawner_ctor(void)
{
}
```
