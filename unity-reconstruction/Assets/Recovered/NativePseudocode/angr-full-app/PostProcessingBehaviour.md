# Native pseudocode: PostProcessingBehaviour

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `PostProcessingBehaviour.OnEnable` — RVA `0xcdc3bc`

- Decompiled symbol: `PostProcessingBehaviour_OnEnable`
- Metadata signature: `private void OnEnable() { }`
- Native interval: `2204` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[48];
    long long field_30;
} struct_0;

extern long long g_1eec608;
extern long long g_1eed790;
extern long long g_1eee740;
extern long long g_1eeebd8;
extern long long g_1eeec90;
extern long long g_1eeeef8;
extern long long g_1eef5e0;
extern long long g_1ef0a08;
extern long long g_1ef12a0;
extern long long g_1ef1530;
extern long long g_1ef1ae0;
extern long long g_1ef21d8;
extern long long g_1ef2388;
extern long long g_1ef57a0;
extern long long g_1ef57a8;
extern long long g_1ef5c28;
extern long long g_1ef6308;
extern long long g_1ef6310;
extern long long g_1ef6318;
extern long long g_1ef8290;
extern long long g_1ef82a8;
extern long long g_1f005d0;
extern long long g_1f005d8;
extern long long g_1f005e0;
extern long long g_1f005e8;
extern long long g_1f005f0;
extern long long g_1f005f8;
extern long long g_1f00600;
extern long long g_1f00608;
extern long long g_1f00610;
extern long long g_1f00618;
extern long long g_1f00620;
extern long long g_1f00628;
extern long long g_1f00630;
extern long long g_1f00638;
extern long long g_1f00640;
extern long long g_1f00648;
extern char g_1fab616;

long long PostProcessingBehaviour_OnEnable(struct_0 *ptr)
{
    unsigned long long v16;  // x30
    unsigned long long v17;  // x28
    unsigned long long v26;  // x19
    long long v27;  // x20
    unsigned long long v18;  // x27
    unsigned long long v19;  // x26
    unsigned long long v20;  // x25
    unsigned long long v21;  // x24
    unsigned long long v22;  // x23
    unsigned long long v23;  // x22
    unsigned long long v24;  // x21
    unsigned long long v25;  // x20
    unsigned long long flag;  // [bp-0x78]
    unsigned long long choice;  // [bp-0x70]
    unsigned long long flag2;  // [bp-0x68]
    char *v3;  // [bp-0x60]
    unsigned long long v4;  // [bp-0x58]
    unsigned long long v5;  // [bp-0x50]
    unsigned long long v6;  // [bp-0x48]
    unsigned long long v7;  // [bp-0x40]
    unsigned long long v8;  // [bp-0x38]
    unsigned long long v9;  // [bp-0x30]
    unsigned long long v10;  // [bp-0x28]
    unsigned long long v11;  // [bp-0x20]
    unsigned long long v12;  // [bp-0x18]
    unsigned long long v13;  // [bp-0x10]
    unsigned long long v14;  // [bp-0x8]
    char v15;  // [bp+0x0]

    v3 = &v15;
    v4 = v16;
    v5 = v17;
    v6 = v18;
    v7 = v19;
    v8 = v20;
    v9 = v21;
    v10 = v22;
    v11 = v23;
    v12 = v24;
    v13 = v25;
    v14 = v26;
    if (!(g_1fab616 & 1))
    {
        sub_f7d92c(&g_1eee740);
        sub_f7d92c(&g_1eeebd8);
        sub_f7d92c(&g_1eeec90);
        sub_f7d92c("E2");
        sub_f7d92c(&g_1eeeef8);
        sub_f7d92c("A7");
        sub_f7d92c(&g_1ef57a8);
        sub_f7d92c(&g_1ef57a0);
        sub_f7d92c(&g_1ef5c28);
        sub_f7d92c(&g_1eec608);
        sub_f7d92c("\r{");
        sub_f7d92c(&g_1eef5e0);
        sub_f7d92c(&g_1ef6308);
        sub_f7d92c(&g_1ef6310);
        sub_f7d92c(&g_1ef6318);
        sub_f7d92c("e:");
        sub_f7d92c("O;");
        sub_f7d92c("5<");
        sub_f7d92c("O=");
        sub_f7d92c(&g_1ef82a8);
        sub_f7d92c(&g_1ef8290);
        sub_f7d92c(&g_1eed790);
        sub_f7d92c("KF");
        sub_f7d92c(&g_1ef0a08);
        sub_f7d92c(&g_1f005d0);
        sub_f7d92c(&g_1f005d8);
        sub_f7d92c(&g_1f005e0);
        sub_f7d92c(&g_1f005e8);
        sub_f7d92c(&g_1f005f0);
        sub_f7d92c(&g_1f005f8);
        sub_f7d92c(&g_1f00600);
        sub_f7d92c(&g_1f00608);
        sub_f7d92c(&g_1f00610);
        sub_f7d92c(&g_1f00618);
        sub_f7d92c(&g_1f00620);
        sub_f7d92c(&g_1f00628);
        sub_f7d92c(&g_1f00630);
        sub_f7d92c(&g_1f00638);
        sub_f7d92c(&g_1f00640);
        sub_f7d92c(&g_1f00648);
        sub_f7d92c("oL");
        sub_f7d92c(&g_1ef12a0);
        sub_f7d92c(&g_1ef1530);
        sub_f7d92c(&g_1ef1ae0);
        sub_f7d92c(&g_1ef21d8);
        sub_f7d92c(&g_1ef2388);
        g_1fab616 = 1;
    }
    flag = 0;
    choice = 0;
    flag2 = 0;
    v27 = sub_f7db70(g_1eec730);
    sub_12a53cc(v27, g_1ef5c28);
    ptr->field_30 = v27;
    sub_f7d8d0((struct struct_0 *)&ptr->field_30, v27);
    MaterialFactory__ctor(sub_f7db70(g_1ef07c8), 0); /* do not return */
}
```

## `PostProcessingBehaviour.OnPreCull` — RVA `0xcdcc58`

- Decompiled symbol: `PostProcessingBehaviour_OnPreCull`
- Metadata signature: `private void OnPreCull() { }`
- Native interval: `1428` bytes
- Result: `pseudocode`
- Heuristic layout hint: `PostProcessingBehaviour_Recovered` matched 8 offsets against `PostProcessingBehaviour` metadata (confidence 1.00).

```c
typedef struct PostProcessingBehaviour_Recovered {
    char padding_0[32];
    struct struct_8 *profile;
    char padding_28[32];
    long long m_MaterialFactory;
    long long m_RenderTextureFactory;
    struct struct_8 *m_Context;
    struct struct_9 *m_Camera;
    char padding_68[8];
    char m_RenderingInSceneView;
    char padding_71[7];
    struct struct_8 *m_DebugViews;
    char padding_80[32];
    struct struct_8 *m_Taa;
} PostProcessingBehaviour_Recovered;

typedef struct struct_14 {
    struct struct_11 *field_0;
    char padding_8[8];
    struct struct_14 *field_10;
    struct struct_15 *field_18;
    unsigned long long field_20;
    unsigned long long field_28;
} struct_14;

typedef struct struct_8 {
    struct struct_5 *field_0;
    char padding_8[8];
    struct struct_8 *field_10;
    struct struct_9 *field_18;
    long long field_20;
    long long field_28;
} struct_8;

typedef struct struct_20 {
    struct struct_17 *field_0;
    char padding_8[8];
    struct struct_20 *field_10;
    struct struct_21 *field_18;
    unsigned long long field_20;
    unsigned long long field_28;
} struct_20;

typedef struct struct_9 {
    struct struct_8 *field_0;
} struct_9;

typedef struct struct_11 {
    char padding_0[392];
    struct struct_12 *field_188;
    unsigned long long field_190;
    char padding_198[48];
    struct struct_13 *field_1c8;
    unsigned long long field_1d0;
} struct_11;

typedef struct struct_15 {
    struct struct_14 *field_0;
} struct_15;

typedef struct struct_5 {
    char padding_0[392];
    struct struct_6 *field_188;
    unsigned long long field_190;
    char padding_198[48];
    struct struct_7 *field_1c8;
    unsigned long long field_1d0;
} struct_5;

typedef struct struct_17 {
    char padding_0[392];
    struct struct_18 *field_188;
    unsigned long long field_190;
    char padding_198[48];
    struct struct_19 *field_1c8;
    unsigned long long field_1d0;
} struct_17;

typedef struct struct_21 {
    struct struct_20 *field_0;
} struct_21;

typedef struct struct_12 {
    unsigned long long field_0;
} struct_12;

typedef struct struct_13 {
    unsigned long long field_0;
} struct_13;

typedef struct struct_6 {
    unsigned long long field_0;
} struct_6;

typedef struct struct_7 {
    unsigned long long field_0;
} struct_7;

typedef struct struct_18 {
    unsigned long long field_0;
} struct_18;

typedef struct struct_19 {
    unsigned long long field_0;
} struct_19;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

typedef struct struct_0 {
    char padding_0[392];
    struct struct_1 *field_188;
    unsigned long long field_190;
    char padding_198[48];
    struct struct_2 *field_1c8;
    unsigned long long field_1d0;
} struct_0;

typedef struct struct_3 {
    struct struct_0 *field_0;
    char padding_8[8];
    struct struct_3 *field_10;
    struct struct_4 *field_18;
    unsigned long long field_20;
    unsigned long long field_28;
} struct_3;

typedef struct struct_16 {
    char padding_0[224];
    unsigned int field_e0;
} struct_16;

typedef struct struct_4 {
    struct struct_3 *field_0;
} struct_4;

extern struct_16 *g_1ef0c58;
extern struct_4 *g_1ef6308;
extern long long g_1ef6310;
extern long long g_1ef6318;
extern long long g_1ef82a8;
extern long long g_1efcf30;
extern char g_1fab617;

long long PostProcessingBehaviour_OnPreCull(struct_10 *ptr)
{
    struct_14 **v3;  // x0
    struct_10 *p;  // x20
    struct_8 *addr;  // x0
    unsigned long v14;  // x1
    struct_8 *ptr3;  // x0
    struct_8 *ptr4;  // x20
    struct_8 **v17;  // x2
    struct_8 *v18;  // x1
    unsigned long v19;  // x3
    long long v20;  // x22
    long long *v21;  // x0
    unsigned long long flag;  // x2
    struct_8 *v5;  // x21
    long long v23;  // x0
    unsigned long v24;  // x1
    long long v6;  // x0
    struct_14 **ptr5;  // x20
    struct_14 **v8;  // x1
    long long v9;  // x0
    struct_20 *ptr6;  // x0
    struct_8 *v11;  // x1
    unsigned long v12;  // x1
    unsigned long choice;  // [bp-0x50]
    unsigned long long flag2;  // [bp-0x48]
    unsigned long long flag3;  // [bp-0x40]

    if (!(g_1fab617 & 1))
    {
        sub_f7d92c(&g_1efcf30);
        sub_f7d92c(&g_1ef6308);
        sub_f7d92c(&g_1ef6310);
        sub_f7d92c(&g_1ef6318);
        sub_f7d92c(&g_1ef82a8);
        sub_f7d92c(&g_1ef0c58);
        g_1fab617 = 1;
    }
    choice = 0;
    flag2 = 0;
    flag3 = 0;
    v3 = sub_1231bc8(ptr, g_1efcf30);
    ptr->field_60 = v3;
    p = &ptr->field_60;
    sub_f7d8d0(p, v3);
    v5 = *((long long *)&p->padding_28[24]);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v6 = Object__op_Equality(v5, 0, 0);
    if (((char)v6 & 1))
        return v6;
    ptr5 = *((long long *)&p->padding_0[0]);
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v8 = NULL;
    v9 = Object__op_Equality(ptr5, 0, 0);
    if (((char)v9 & 1))
        return v9;
    ptr6 = ptr->field_58;
    if (ptr6)
    {
        v8 = NULL;
        ptr6 = PostProcessingContext__Reset(ptr6, 0);
        if (ptr6)
        {
            v11 = ptr->field_20;
            v5 = ptr6;
            ptr6->field_10 = v11;
            sub_f7d8d0((struct struct_20 *)&ptr6->field_10, v11);
            v12 = ptr->field_50;
            addr = v5;
            addr->field_28 = v12;
            sub_f7d8d0((struct struct_8 *)&addr->field_28, v12);
            v14 = ptr->field_48;
            ptr3 = v5;
            ptr3->field_20 = v14;
            sub_f7d8d0((struct struct_8 *)&ptr3->field_20, v14);
            v8 = ptr->field_60;
            ptr4 = v5;
            ptr4->field_18 = v8;
            ptr5 = &ptr4->field_18;
            ptr6 = sub_f7d8d0(ptr5, v8);
            if (ptr->field_20)
            {
                ptr6 = ptr->field_78;
                if (ptr6)
                {
                    v17 = ptr->field_20->field_18;
                    v18 = v5;
                    v19 = ptr6->field_0->field_1d0;
                    ptr6->field_0->field_1c8();
                }
            }
        }
    }
    while (true)
    {
        v20 = sub_f7db74(sub_f7db74(ptr6));
        if ((unsigned int)v8 == 1)
        {
            v21 = __cxa_begin_catch(v20);
            __cxa_end_catch(v21);
            v8 = g_1ef6308;
            sub_130ea84(&choice, g_1ef6308);
            if (!*(v21))
            {
                ptr6 = *(ptr5);
                if (ptr6)
                {
                    v8 = v5 & 4294967295;
                    flag = 0;
                    v23 = Camera__set_depthTextureMode(ptr6, v8, 0);
                    if (ptr->field_70)
                        return v23;
                    ptr6 = ptr->field_a0;
                    if (ptr6)
                    {
                        v24 = ptr6->field_0->field_190;
                        ptr6->field_0->field_188();
                    }
                }
            }
            else
            {
                sub_f1bd40(*(v21));
                goto LABEL_10dd1b4;
            }
        }
        else
        {
LABEL_10dd1b4:
            sub_130ea84(&choice, g_1ef6308);
            sub_1026098(v20);
            break;
        }
    }
    sub_e29990(sub_f1bd40(0));
}
```

## `PostProcessingBehaviour.DisableComponents` — RVA `0xcdd1ec`

- Decompiled symbol: `PostProcessingBehaviour_DisableComponents`
- Metadata signature: `private void DisableComponents() { }`
- Native interval: `372` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[440];
    struct struct_1 *field_1b8;
    unsigned long long field_1c0;
} struct_0;

typedef struct struct_2 {
    char padding_0[56];
    long long field_38;
} struct_2;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern long long g_1ef6308;
extern long long g_1ef6310;
extern long long g_1ef6318;
extern long long g_1ef82a8;
extern char g_1fab61e;

unsigned long long PostProcessingBehaviour_DisableComponents(struct_2 *ptr, unsigned int flag3)
{
    long long v3;  // x0
    struct_0 **v4;  // x19
    unsigned long v5;  // x1
    struct_0 **v6;  // x0
    unsigned long long v7;  // x0
    long long v8;  // x19
    long long *v9;  // x0
    unsigned long long v10;  // x0
    unsigned long flag;  // [bp-0x38]
    unsigned long long choice;  // [bp-0x30]
    struct_0 **flag2;  // [bp-0x28]

    if (!(g_1fab61e & 1))
    {
        sub_f7d92c(&g_1ef6308);
        sub_f7d92c(&g_1ef6310);
        sub_f7d92c(&g_1ef6318);
        sub_f7d92c(&g_1ef82a8);
        g_1fab61e = 1;
    }
    flag = 0;
    choice = 0;
    flag2 = NULL;
    v3 = ptr->field_38;
    if (v3)
    {
        sub_14a3cf0(v3, g_1ef82a8);
        flag3 = g_1ef6310;
        if (!((char)sub_130ea88(&flag, g_1ef6310) & 1))
        {
            v7 = sub_130ea84(&flag, g_1ef6308);
            return sub_130ea84(&flag, g_1ef6308);
        }
        v4 = flag2;
        if (v4)
        {
            v5 = *(v4)->field_1c0;
            v6 = v4;
            *(v6)->field_1b8();
        }
        v3 = sub_f7db74();
    }
    v8 = sub_f7db74(v3);
    if (flag3 == 1)
    {
        v9 = __cxa_begin_catch(v8);
        __cxa_end_catch(v9);
        v10 = sub_130ea84(&flag, g_1ef6308);
        if (!*(v9))
            return v10;
        sub_f1bd40(*(v9));
    }
    sub_130ea84(&flag, g_1ef6308);
    sub_1026098(v8);
    sub_e29990(sub_f1bd40(0));
}
```

## `PostProcessingBehaviour.CheckObservers` — RVA `0xcdd360`

- Decompiled symbol: `PostProcessingBehaviour_CheckObservers`
- Metadata signature: `private void CheckObservers() { }`
- Native interval: `1056` bytes
- Result: `pseudocode`

```c
typedef struct struct_7 {
    struct struct_4 *field_0;
    char padding_8[8];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_7;

typedef struct struct_3 {
    struct struct_0 *field_0;
    char padding_8[8];
    long long field_10;
    int field_18;
    unsigned int field_1c;
} struct_3;

typedef struct struct_8 {
    char padding_0[440];
    struct struct_9 *field_1b8;
    unsigned long long field_1c0;
} struct_8;

typedef struct struct_4 {
    char padding_0[408];
    struct struct_5 *field_198;
    unsigned long long field_1a0;
    struct struct_6 *field_1a8;
    unsigned long long field_1b0;
} struct_4;

typedef struct struct_0 {
    char padding_0[408];
    struct struct_1 *field_198;
    unsigned long long field_1a0;
    struct struct_2 *field_1a8;
    unsigned long long field_1b0;
} struct_0;

typedef struct struct_9 {
    unsigned long long field_0;
} struct_9;

typedef struct struct_5 {
    unsigned long long field_0;
} struct_5;

typedef struct struct_6 {
    unsigned long long field_0;
} struct_6;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

extern long long g_1ef57b0;
extern long long g_1ef57b8;
extern long long g_1ef67d8;
extern long long g_1ef67e0;
extern long long g_1ef67e8;
extern long long g_1ef70a8;
extern long long g_1ef70b0;
extern long long g_1ef8298;
extern long long g_1ef82a0;
extern long long g_1ef82b0;
extern long long g_1ef82b8;
extern char g_1fab61d;

struct_7 * PostProcessingBehaviour_CheckObservers(struct_3 **ptr)
{
    struct_3 *p;  // x0
    struct_8 **v7;  // x20
    struct_3 *v16;  // x21
    unsigned long long choice;  // x2
    struct_3 *v18;  // x0
    unsigned long long v19;  // x1
    long long v20;  // x3
    struct_3 *v21;  // x21
    unsigned long long flag2;  // x2
    struct_3 *v23;  // x0
    unsigned long long v24;  // x1
    struct_7 *addr;  // x8
    unsigned long v8;  // x1
    int v26;  // w2
    unsigned int v27;  // w9
    int v28;  // w2
    unsigned int v29;  // w8
    struct_8 **v9;  // x0
    unsigned long v10;  // x0
    unsigned long v11;  // x0
    long long v12;  // x20
    long long *v13;  // x0
    long long v15;  // x3
    char v0;  // [bp-0xa8]
    uint128_t v1;  // [bp-0x98]
    unsigned long long v2;  // [bp-0x88]
    char flag;  // [bp-0x80], Other Possible Types: uint128_t
    uint128_t v4;  // [bp-0x70]
    unsigned long long v5;  // [bp-0x60]

    if (!(g_1fab61d & 1))
    {
        sub_f7d92c(&g_1ef57b0);
        sub_f7d92c(&g_1ef57b8);
        sub_f7d92c(&g_1ef67d8);
        sub_f7d92c(&g_1ef67e0);
        sub_f7d92c(&g_1ef67e8);
        sub_f7d92c(&g_1ef70a8);
        sub_f7d92c(&g_1ef70b0);
        sub_f7d92c(&g_1ef8298);
        sub_f7d92c(&g_1ef82a0);
        sub_f7d92c(&g_1ef82b0);
        sub_f7d92c(&g_1ef82b8);
        g_1fab61d = 1;
    }
    v5 = 0;
    flag = 0;
    v4 = 0;
    p = ptr[8];
    if (p)
    {
        sub_12a7ff0(p, g_1ef57b0);
        memcpy(&flag, &v0, 16);
        v4 = v1;
        v5 = v2;
        if (((char)sub_1326de0(&flag, g_1ef67e0) & 1))
        {
            v7 = (unsigned long long)v4;
            if (v7)
            {
                v8 = *(v7)->field_1c0;
                v9 = v7;
                *(v9)->field_1b8();
            }
            v10 = sub_f7db74(sub_f7db74());
            v11 = sub_f7db74(sub_f7db74(v10));
            v12 = sub_f7db74(sub_f7db74(v11));
            if ((int)g_1ef67e0 == 1)
            {
                v13 = __cxa_begin_catch(v12);
                __cxa_end_catch(v13);
                sub_1326f08(&flag, g_1ef67d8);
                if (!*(v13))
                    goto LABEL_10dd5a4;
                sub_f1bd40(*(v13));
            }
            sub_1326f08(&flag, g_1ef67d8);
            sub_1026098(v12);
            sub_e29990(sub_f1bd40(0));
        }
        else
        {
            sub_1326f08(&flag, g_1ef67d8);
LABEL_10dd5a4:
            p = ptr[32];
            if (p)
            {
                if (p->field_18 > 0)
                {
                    p = sub_14a30c0();
                    if (ptr[8])
                    {
                        v15 = g_1ef57b8;
                        v16 = p;
                        choice = 0;
                        p = sub_12a7bd4(ptr[8], v16, 0, g_1ef57b8);
                        if (v16)
                        {
                            v18 = v16;
                            v19 = v16->field_0->field_1b0;
                            v16->field_0->field_1a8();
                        }
                    }
                }
                else
                {
                    p = ptr[31];
                    if (p && p->field_18 > 0)
                    {
                        p = sub_14a30c0();
                        if (ptr[8])
                        {
                            v20 = g_1ef57b8;
                            v21 = p;
                            flag2 = 1;
                            p = sub_12a7bd4(ptr[8], v21, 1, g_1ef57b8);
                            if (v21)
                            {
                                v23 = v21;
                                v24 = v21->field_0->field_1a0;
                                v21->field_0->field_198();
                            }
                        }
                    }
                }
            }
        }
    }
    do
    {
        do
        {
            p = sub_f7db74(p);
        } while ((addr = (struct_7 *)ptr[32], !ptr[32]));
    } while ((v26 = (int)addr->field_18, v27 = addr->field_1c + 1, addr->field_18 = (unsigned int)0, addr->field_1c = v27, v26 >= 1 && (Array__Clear(addr->field_10, 0), p = ptr[31], !p)));
    v28 = p->field_18;
    v29 = p->field_1c;
    p->field_18 = 0;
    p->field_1c = v29 + 1;
    if (v28 >= 1)
        p = Array__Clear(p->field_10, 0);
    return p;
}
```

## `PostProcessingBehaviour.OnPreRender` — RVA `0xcdd780`

- Decompiled symbol: `PostProcessingBehaviour_OnPreRender`
- Metadata signature: `private void OnPreRender() { }`
- Native interval: `312` bytes
- Result: `pseudocode`
- Heuristic layout hint: `PostProcessingBehaviour_Recovered` matched 6 offsets against `PostProcessingBehaviour` metadata (confidence 1.00).

```c
typedef struct PostProcessingBehaviour_Recovered {
    char padding_0[32];
    long long profile;
    char padding_28[72];
    char m_RenderingInSceneView;
    char padding_71[7];
    long long m_DebugViews;
    long long m_AmbientOcclusion;
    long long m_ScreenSpaceReflection;
    long long m_FogComponent;
} PostProcessingBehaviour_Recovered;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern long long g_1f00650;
extern long long g_1f00658;
extern long long g_1f00660;
extern long long g_1f00668;
extern long long g_1f00670;
extern char g_1fab618;

long long PostProcessingBehaviour_OnPreRender(struct_1 *a0)
{
    long long v0;  // x0
    long long v1;  // x0
    unsigned long long v2;  // x0

    if (!(g_1fab618 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f00650);
        sub_f7d92c(&g_1f00658);
        sub_f7d92c(&g_1f00660);
        sub_f7d92c(&g_1f00668);
        sub_f7d92c(&g_1f00670);
        g_1fab618 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Equality(a0->field_20, 0, 0);
    if (((char)v0 & 1))
        return v0;
    sub_112b494(a0, a0->field_78, g_1f00658);
    sub_112b494(a0, a0->field_80, g_1f00650);
    sub_112b494(a0, a0->field_88, g_1f00670);
    v1 = sub_112b494(a0, a0->field_90, g_1f00660);
    if (!a0->field_70)
    {
        v2 = sub_112b494();
        return sub_112b494();
    }
    return v1;
}
```

## `PostProcessingBehaviour.OnPostRender` — RVA `0xcdd8b8`

- Decompiled symbol: `PostProcessingBehaviour_OnPostRender`
- Metadata signature: `private void OnPostRender() { }`
- Native interval: `260` bytes
- Result: `pseudocode`
- Heuristic layout hint: `PostProcessingBehaviour_Recovered` matched 4 offsets against `PostProcessingBehaviour` metadata (confidence 1.00).

```c
typedef struct PostProcessingBehaviour_Recovered {
    char padding_0[32];
    long long profile;
    char padding_28[56];
    long long m_Camera;
    char padding_68[8];
    char m_RenderingInSceneView;
    char padding_71[47];
    struct struct_4 *m_Taa;
} PostProcessingBehaviour_Recovered;

typedef struct struct_1 {
    char padding_0[392];
    struct struct_2 *field_188;
    unsigned long long field_190;
} struct_1;

typedef struct struct_4 {
    struct struct_1 *field_0;
} struct_4;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab619;

long long PostProcessingBehaviour_OnPostRender(struct_3 *ptr)
{
    long long v0;  // x0
    unsigned long long flag;  // x2
    long long v2;  // x0
    struct_1 **v3;  // x0
    unsigned long long v4;  // x1

    if (!(g_1fab619 & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab619 = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    v0 = Object__op_Equality(ptr->field_20, 0, 0);
    if (((char)v0 & 1))
        return v0;
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    flag = 0;
    v2 = Object__op_Equality(ptr->field_60, 0, 0);
    if (((char)v2 & 1))
    {
        return v2;
    }
    else if (!ptr->field_70)
    {
        v3 = ptr->field_a0;
        if (!ptr->field_a0)
            sub_f7db74(0);
        v4 = ptr->field_a0->field_0->field_190;
        ptr->field_a0->field_0->field_188();
    }
    else
    {
        return v2;
    }
}
```

## `PostProcessingBehaviour.OnRenderImage` — RVA `0xcdd9bc`

- Decompiled symbol: `PostProcessingBehaviour_OnRenderImage`
- Metadata signature: `private void OnRenderImage(RenderTexture source, RenderTexture destination) { }`
- Native interval: `1376` bytes
- Result: `pseudocode`
- Heuristic layout hint: `PostProcessingBehaviour_Recovered` matched 3 offsets against `PostProcessingBehaviour` metadata (confidence 1.00).

```c
typedef struct PostProcessingBehaviour_Recovered {
    char padding_0[32];
    long long profile;
    char padding_28[56];
    long long m_Camera;
    char padding_68[136];
    struct struct_5 *m_Fxaa;
} PostProcessingBehaviour_Recovered;

typedef struct struct_2 {
    char padding_0[392];
    struct struct_3 *field_188;
    unsigned long long field_190;
} struct_2;

typedef struct struct_5 {
    struct struct_2 *field_0;
} struct_5;

typedef struct struct_3 {
    unsigned long long field_0;
} struct_3;

typedef struct struct_1 {
    char padding_0[224];
    unsigned int field_e0;
} struct_1;

extern struct_1 *g_1ef0c58;
extern long long g_1efa0c0;
extern long long g_1f00678;
extern long long g_1f00680;
extern long long g_1f00688;
extern long long g_1f00690;
extern long long g_1f00698;
extern long long g_1f006a0;
extern long long g_1f0aa78;
extern long long g_1f0aab0;
extern long long g_1f10260;
extern char g_1fab61a;

void PostProcessingBehaviour_OnRenderImage(struct_4 *ptr, unsigned long a1, unsigned long a2)
{
    unsigned long long v11;  // x30
    unsigned long long v12;  // x28
    unsigned long long v21;  // x19
    unsigned long long flag;  // x2
    struct_2 **v23;  // x0
    unsigned long long v24;  // x1
    unsigned long long v13;  // x27
    unsigned long long v14;  // x26
    unsigned long long v15;  // x25
    unsigned long long v16;  // x24
    unsigned long long v17;  // x23
    unsigned long long v18;  // x22
    unsigned long long v19;  // x21
    unsigned long long v20;  // x20
    unsigned long long v0;  // [bp-0x60]
    unsigned long long v1;  // [bp-0x50]
    unsigned long long v2;  // [bp-0x48]
    unsigned long long v3;  // [bp-0x40]
    unsigned long long v4;  // [bp-0x38]
    unsigned long long v5;  // [bp-0x30]
    unsigned long long v6;  // [bp-0x28]
    unsigned long long v7;  // [bp-0x20]
    unsigned long long v8;  // [bp-0x18]
    unsigned long long v9;  // [bp-0x10]
    unsigned long long v10;  // [bp-0x8]

    v0 = v11;
    v1 = v12;
    v2 = v13;
    v3 = v14;
    v4 = v15;
    v5 = v16;
    v6 = v17;
    v7 = v18;
    v8 = v19;
    v9 = v20;
    v10 = v21;
    if (!(g_1fab61a & 1))
    {
        sub_f7d92c("g=");
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1f00678);
        sub_f7d92c(&g_1f00680);
        sub_f7d92c(&g_1f00688);
        sub_f7d92c(&g_1f00690);
        sub_f7d92c(&g_1f00698);
        sub_f7d92c(&g_1f006a0);
        sub_f7d92c(&g_1efa0c0);
        sub_f7d92c(&g_1f0aa78);
        sub_f7d92c(&g_1f10260);
        sub_f7d92c("#$");
        sub_f7d92c(&g_1f0aab0);
        g_1fab61a = 1;
    }
    if (!g_1ef0c58->field_e0)
        sub_f7da5c(g_1ef0c58);
    if (!((char)Object__op_Equality(ptr->field_20, 0, 0) & 1))
    {
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        flag = 0;
        if (!((char)Object__op_Equality(ptr->field_60, 0, 0) & 1))
        {
            v23 = ptr->field_f0;
            if (!ptr->field_f0)
                sub_f7db74(0);
            v24 = ptr->field_f0->field_0->field_190;
            ptr->field_f0->field_0->field_188();
        }
    }
    if (!g_1eefbb8->field_e0)
        sub_f7da5c(g_1eefbb8);
    Graphics__Blit();
    return;
}
```

## `PostProcessingBehaviour.OnGUI` — RVA `0xcddf1c`

- Decompiled symbol: `PostProcessingBehaviour_OnGUI`
- Metadata signature: `private void OnGUI() { }`
- Native interval: `392` bytes
- Result: `pseudocode`
- Heuristic layout hint: `PostProcessingBehaviour_Recovered` matched 3 offsets against `PostProcessingBehaviour` metadata (confidence 1.00).

```c
typedef struct PostProcessingBehaviour_Recovered {
    char padding_0[32];
    long long profile;
    char padding_28[56];
    long long m_Camera;
    char padding_68[64];
    struct struct_4 *m_EyeAdaptation;
} PostProcessingBehaviour_Recovered;

typedef struct struct_1 {
    char padding_0[392];
    struct struct_2 *field_188;
    unsigned long long field_190;
} struct_1;

typedef struct struct_4 {
    struct struct_1 *field_0;
} struct_4;

typedef struct struct_2 {
    unsigned long long field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1ef0c58;
extern char g_1fab61b;

long long PostProcessingBehaviour_OnGUI(struct_3 *ptr)
{
    long long v0;  // x0
    long long v1;  // x0
    unsigned long long flag;  // x2
    long long v3;  // x0
    struct_1 **v4;  // x0
    unsigned long long v5;  // x1

    if (!(g_1fab61b & 1))
    {
        sub_f7d92c(&g_1ef0c58);
        g_1fab61b = 1;
    }
    if (Event__get_current(0))
    {
        v0 = Event__get_type();
        if ((int)v0 != 7)
            return v0;
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        v1 = Object__op_Equality(ptr->field_20, 0, 0);
        if (((char)v1 & 1))
            return v1;
        if (!g_1ef0c58->field_e0)
            sub_f7da5c(g_1ef0c58);
        flag = 0;
        v3 = Object__op_Equality(ptr->field_60, 0, 0);
        if (((char)v3 & 1))
            return v3;
        v4 = ptr->field_a8;
        if (v4)
        {
            v5 = *(v4)->field_190;
            *(v4)->field_188();
        }
    }
    sub_f7db74();
}
```

## `PostProcessingBehaviour.OnDisable` — RVA `0xcde0a4`

- Decompiled symbol: `PostProcessingBehaviour_OnDisable`
- Metadata signature: `private void OnDisable() { }`
- Native interval: `640` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[56];
    long long field_38;
} struct_2;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_1;

extern struct_0 *g_1ef0c58;
extern long long g_1ef5c38;
extern long long g_1ef5c50;
extern long long g_1ef68a8;
extern long long g_1ef68b0;
extern long long g_1ef68b8;
extern long long g_1ef7048;
extern long long g_1ef7050;
extern long long g_1ef82a0;
extern long long g_1efb6f8;
extern char g_1fab61c;

int PostProcessingBehaviour_OnDisable(struct_2 *ptr, long long a1)
{
    unsigned long i;  // x0
    long long *v7;  // x22
    unsigned int v16;  // w9
    struct_0 **v8;  // x21
    long long *addr;  // x23
    unsigned long v10;  // x20
    unsigned long v11;  // x0
    unsigned long v12;  // x0
    unsigned long long *ptr3;  // x0
    struct_1 *p;  // x8
    unsigned int v15;  // w2
    char v0;  // [bp-0x80]
    uint128_t v1;  // [bp-0x70]
    int flag;  // [bp-0x60]
    char v3;  // [bp-0x60]
    uint128_t v4;  // [bp-0x50]
    long long v5;  // [bp-0x38], Other Possible Types: unsigned long long

    if (!(g_1fab61c & 1))
    {
        sub_f7d92c(&g_1ef5c38);
        sub_f7d92c(&g_1ef5c50);
        sub_f7d92c(&g_1ef68a8);
        sub_f7d92c(&g_1ef68b0);
        sub_f7d92c(&g_1ef68b8);
        sub_f7d92c(&g_1ef7048);
        sub_f7d92c(&g_1ef7050);
        sub_f7d92c(&g_1ef82a0);
        sub_f7d92c(&g_1ef0c58);
        sub_f7d92c(&g_1efb6f8);
        g_1fab61c = 1;
    }
    flag = 0;
    v4 = 0;
    i = *((long long *)&ptr->padding_0[48]);
    if (i)
    {
        a1 = g_1ef5c50;
        i = sub_12a55c4(i, g_1ef5c50);
        if (i)
        {
            v7 = &g_1ef5c38;
            v8 = &g_1ef0c58;
            addr = &g_1ef68a8;
            sub_164ee08();
            memcpy(&v3, &v0, 16);
            v4 = v1;
            while (true)
            {
                a1 = g_1ef68b0;
                if (!((char)sub_1326c24(&v3, g_1ef68b0) & 1))
                {
                    a1 = g_1ef68a8;
                    sub_1326c20(&v3, g_1ef68a8);
                }
                if (*((long long *)&ptr[1].padding_0[32]))
                {
                    v10 = *((unsigned long long *)((void*)&v4 + 8));
                    a1 = (unsigned int)v4;
                    v11 = Camera__RemoveCommandBuffer(*((long long *)&ptr[1].padding_0[32]), a1, v10, 0);
                    if (!v10)
                        goto LABEL_10de2a4;
                    CommandBuffer__Dispose(v10, 0);
                }
                else
                {
                    v11 = sub_f7db74(0);
LABEL_10de2a4:
                    i = sub_f7db74(v11);
                    break;
                }
            }
        }
    }
    do
    {
        do
        {
            do
            {
                do
                {
                    v12 = sub_f7db74(i);
                    if ((int)a1 == 1)
                    {
                        ptr3 = __cxa_begin_catch();
                        v5 = *(ptr3);
                        __cxa_end_catch(ptr3);
                        sub_1326c20(&flag, *(addr));
                        if (v5)
                        {
                            v12 = sub_f1bd40(v5);
                            goto LABEL_10de2ec;
                        }
                    }
                    else
                    {
LABEL_10de2ec:
                        v5 = 0;
                        sub_1326c20(&flag, *(addr));
                        if (!v5)
                            sub_1026098(v12);
                        sub_e29990(sub_f1bd40(v5));
                    }
                } while ((i = (unsigned long)*((long long *)&ptr->padding_0[48]), !i));
                sub_12a5850(i, *(v7));
                if (!*(v8)->field_e0)
                    sub_f7da5c(*(v8));
                a1 = 0;
                if (((char)Object__op_Inequality(*((long long *)&ptr->padding_0[32]), 0, 0) & 1))
                    i = PostProcessingBehaviour__DisableComponents(ptr, 0);
            } while ((p = (struct_1 *)ptr->field_38, !p));
            v15 = p->field_18;
            v16 = p->field_1c + 1;
            p->field_18 = 0;
            p->field_1c = v16;
            if (v15 >= 1)
            {
                a1 = 0;
                Array__Clear(p->field_10, 0);
            }
            i = *((long long *)&ptr[1].padding_0[8]);
        } while (!i);
    } while ((a1 = 0, MaterialFactory__Dispose(i, 0), i = (unsigned long)*((long long *)&ptr[1].padding_0[16]), !i));
    RenderTextureFactory__Dispose(i, 0);
    return GraphicsUtils__Dispose(0);
}
```

## `PostProcessingBehaviour.ResetTemporalEffects` — RVA `0xcde324`

- Decompiled symbol: `PostProcessingBehaviour_ResetTemporalEffects`
- Metadata signature: `public void ResetTemporalEffects() { }`
- Native interval: `64` bytes
- Result: `pseudocode`
- Heuristic layout hint: `PostProcessingBehaviour_Recovered` matched 2 offsets against `PostProcessingBehaviour` metadata (confidence 1.00).

```c
typedef struct PostProcessingBehaviour_Recovered {
    char padding_0[152];
    struct struct_0 *m_MotionBlur;
    struct struct_0 *m_Taa;
} PostProcessingBehaviour_Recovered;

typedef struct struct_0 {
    char padding_0[44];
    char field_2c;
} struct_0;

typedef struct struct_0 {
    char padding_0[40];
    long long field_28;
} struct_0;

void PostProcessingBehaviour_ResetTemporalEffects(struct_1 *idx)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    if (idx->field_a0)
    {
        idx->field_a0->field_2c = 1;
        if (idx->field_98)
            MotionBlurComponent__ResetHistory(idx->field_98); /* do not return */
    }
    sub_f7db74();
}
```

## `PostProcessingBehaviour.ctor` — RVA `0xcde364`

- Decompiled symbol: `PostProcessingBehaviour_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `172` bytes
- Result: `pseudocode`

```c
extern long long g_1eed790;
extern long long g_1ef8290;
extern char g_1fab61f;

void PostProcessingBehaviour_ctor(long long *ptr)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    long long v10;  // x20
    long long v11;  // x20
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
    if (!(g_1fab61f & 1))
    {
        sub_f7d92c(&g_1ef8290);
        sub_f7d92c(&g_1eed790);
        g_1fab61f = 1;
    }
    v10 = sub_f7db70(g_1eed790);
    sub_14a2b64(v10, g_1ef8290);
    ptr[31] = v10;
    sub_f7d8d0(ptr + 31, v10);
    v11 = sub_f7db70(g_1eed790);
    sub_14a2b64(v11, g_1ef8290);
    ptr[32] = v11;
    sub_f7d8d0(ptr + 32, v11);
    MonoBehaviour__ctor();
    return;
}
```
