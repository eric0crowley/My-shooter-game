# Native pseudocode: WeaponSelection

> Metadata source-path string: `Assets/Script/WeaponSelection.cs`. This is a path string from the APK metadata, not recovered source text.

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `WeaponSelection.Start` — RVA `0xcc4b6c`

- Decompiled symbol: `WeaponSelection_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `644` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WeaponSelection_Recovered` matched 8 offsets against `WeaponSelection` metadata (confidence 1.00).

```c
typedef struct struct_10 {
    char padding_0[32];
    char field_20;
    char padding_21[7];
    struct struct_11 *field_28;
    char padding_30[56];
    long long field_68;
    char padding_70[16];
    struct struct_9 *field_80;
    char padding_88[8];
    unsigned long long field_90;
    unsigned long long field_98;
    unsigned long long field_a0;
    unsigned long long field_a8;
} struct_10;

typedef struct struct_9 {
    char padding_0[24];
    unsigned int field_18;
} struct_9;

typedef struct struct_5 {
    struct WeaponSelection_Recovered *field_0;
    long long field_8;
    unsigned int field_10;
} struct_5;

typedef struct struct_12 {
    char padding_0[32];
    long long field_20;
} struct_12;

typedef struct struct_13 {
    char padding_0[32];
    long long field_20;
} struct_13;

typedef struct struct_14 {
    char padding_0[32];
    long long field_20;
} struct_14;

typedef struct struct_15 {
    char padding_0[32];
    long long field_20;
} struct_15;

typedef struct struct_7 {
    char padding_0[1512];
    struct struct_8 *field_5e8;
    unsigned long long field_5f0;
} struct_7;

typedef struct struct_11 {
    struct struct_7 *field_0;
} struct_11;

typedef struct WeaponSelection_Recovered {
    char padding_0[32];
    char isbuy;
    char padding_21[7];
    struct struct_4 *totalEarningTxt2;
    char padding_30[56];
    unsigned long long SkinBuyButton;
    char padding_70[16];
    struct struct_2 *WeaponPrice;
    char padding_88[8];
    unsigned long long OnetimeGun;
    unsigned long long VideoBtn;
    unsigned long long OnetimeGun2;
    unsigned long long VideoBtn2;
} WeaponSelection_Recovered;

typedef struct struct_8 {
    unsigned long long field_0;
} struct_8;

typedef struct struct_4 {
    struct struct_0 *field_0;
} struct_4;

typedef struct struct_2 {
    char padding_0[24];
    unsigned int field_18;
} struct_2;

typedef struct struct_0 {
    char padding_0[1512];
    struct struct_1 *field_5e8;
    unsigned long long field_5f0;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern unsigned long long g_1f06220;
extern long long g_1f0dab0;
extern char g_1fab538;

void WeaponSelection_Start(struct_10 *ptr)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x21
    unsigned long long v15;  // x8
    unsigned long v16;  // x9
    struct_13 *v17;  // x8
    unsigned long long v18;  // x8
    unsigned long v19;  // x9
    struct_14 *v20;  // x8
    unsigned long long v21;  // x8
    unsigned long v22;  // x9
    struct_15 *v23;  // x8
    long long v24;  // x0
    unsigned long long v7;  // x20
    long long v25;  // x0
    struct_7 **v26;  // x19
    unsigned long v27;  // x0
    unsigned long long v28;  // x2
    unsigned long long v29;  // x1
    struct_7 **v30;  // x0
    unsigned long long v8;  // x19
    long long v9;  // x0
    struct_5 *p;  // x8
    unsigned long v11;  // x0
    unsigned long long v12;  // x8
    unsigned long v13;  // x9
    struct_12 *v14;  // x8
    unsigned int v0;  // [bp-0x24]
    unsigned long long v1;  // [bp-0x20]
    unsigned long long v2;  // [bp-0x18]
    unsigned long long v3;  // [bp-0x10]
    unsigned long long v4;  // [bp-0x8]

    v1 = v5;
    v2 = v6;
    v3 = v7;
    v4 = v8;
    if (!(g_1fab538 & 1))
    {
        sub_f7d92c("Y'");
        sub_f7d92c("U^");
        sub_f7d92c("a&");
        sub_f7d92c(")#");
        sub_f7d92c(&g_1f0dab0);
        sub_f7d92c(&g_1f06220);
        g_1fab538 = 1;
    }
    if (ptr->field_80)
    {
        v9 = sub_f7d9d4(g_1eedff0, ptr->field_80->field_18);
        p = g_1ef2480->field_b8;
        p->field_8 = v9;
        v11 = sub_f7d8d0(&p->field_8, v9);
        v12 = ptr->field_90;
        if (v12)
        {
            v13 = g_1ef2480->field_b8->field_10;
            if (*((int *)(v12 + 24)) <= (unsigned int)v13)
                goto LABEL_10c4dec;
            v14 = v12 + v13 * 8;
            if (v14->field_20 && !((v11 = (unsigned long)GameObject__SetActive(v14->field_20, 1, 0), v15 = ptr->field_98, !v15)))
            {
                v16 = g_1ef2480->field_b8->field_10;
                if (*((int *)(v15 + 24)) <= (unsigned int)v16)
                    goto LABEL_10c4dec;
                v17 = v15 + v16 * 8;
                if (v17->field_20 && !((v11 = (unsigned long)GameObject__SetActive(v17->field_20, 1, 0), v18 = ptr->field_a0, !v18)))
                {
                    v19 = g_1ef2480->field_b8->field_10;
                    if (*((int *)(v18 + 24)) <= (unsigned int)v19)
                        goto LABEL_10c4dec;
                    v20 = v18 + v19 * 8;
                    if (v20->field_20 && !((v11 = (unsigned long)GameObject__SetActive(v20->field_20, 1, 0), v21 = ptr->field_a8, !v21)))
                    {
                        v22 = g_1ef2480->field_b8->field_10;
                        if (*((int *)(v21 + 24)) <= (unsigned int)v22)
                            goto LABEL_10c4dec;
                        v23 = v21 + v22 * 8;
                        if (v23->field_20)
                        {
                            GameObject__SetActive(v23->field_20, 1, 0);
                            g_1ef2480->field_b8->field_0 = ptr;
                            sub_f7d8d0(g_1ef2480->field_b8, ptr);
                            Time__set_timeScale(0);
                            if (PlayerPrefs__GetInt(g_1f0dab0, 0) != 1)
                            {
LABEL_10c4d4c:
                                ptr->field_20 = 0;
                                v24 = Int32__ToString((struct struct_10 *)&ptr->padding_70[8], 0);
                                v25 = String__Concat(g_1f0fb70, v24, 0);
                                PlayerPrefs__SetInt(v25, 1, 0);
                                v26 = ptr->field_28;
                                v0 = PlayerPrefs__GetInt(g_1f0ee98, 0);
                                v27 = Int32__ToString(&v0, 0);
                                if (v26)
                                {
                                    v28 = *(v26)->field_5f0;
                                    if (!v27)
                                        v29 = g_1f06220;
                                    else
                                        v29 = v27;
                                    v30 = v26;
                                    *(v26)->field_5e8();
                                }
                            }
                            else if (ptr->field_68)
                            {
                                GameObject__SetActive(ptr->field_68, 0, 0);
                                goto LABEL_10c4d4c;
                            }
                        }
                    }
                }
            }
        }
    }
    v11 = sub_f7db74();
LABEL_10c4dec:
    sub_f7db7c(v11);
}
```

## `WeaponSelection.Update` — RVA `0xcc4df0`

- Decompiled symbol: `WeaponSelection_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long WeaponSelection_Update(unsigned long a0)
{
    WeaponSelection__setLocks(); /* do not return */
}
```

## `WeaponSelection.setLocks` — RVA `0xcc4df4`

- Decompiled symbol: `WeaponSelection_setLocks`
- Metadata signature: `private void setLocks() { }`
- Native interval: `600` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WeaponSelection_Recovered` matched 3 offsets against `WeaponSelection` metadata (confidence 1.00).

```c
typedef struct WeaponSelection_Recovered {
    char padding_0[32];
    char isbuy;
    char padding_21[15];
    struct struct_3 *PriceOfCurrentWeapon;
    char padding_38[8];
    struct struct_3 *WeaponBuyButton;
} WeaponSelection_Recovered;

typedef struct struct_4 {
    char padding_0[1512];
    struct struct_5 *field_5e8;
    unsigned long long field_5f0;
} struct_4;

typedef struct struct_3 {
    struct struct_0 *field_0;
} struct_3;

typedef struct struct_5 {
    unsigned long long field_0;
} struct_5;

typedef struct struct_0 {
    char padding_0[1512];
    struct struct_1 *field_5e8;
    unsigned long long field_5f0;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern long long g_1f06220;
extern unsigned long long g_1f064e0;
extern long long g_1f08408;
extern char g_1fab53a;

void WeaponSelection_setLocks(struct_2 *ptr)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    struct_4 **v10;  // x0
    unsigned long v11;  // x2
    unsigned long long v12;  // x1
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
    if (!(g_1fab53a & 1))
    {
        sub_f7d92c("U^");
        sub_f7d92c(&g_1f08408);
        sub_f7d92c(&g_1f064e0);
        sub_f7d92c("a&");
        sub_f7d92c(&g_1f06220);
        g_1fab53a = 1;
    }
    v10 = ptr->field_40;
    if (v10)
    {
        GameObject__SetActive(v10, 0, 0);
        v10 = ptr->field_30;
        ptr->field_20 = 0;
        if (v10)
        {
            v11 = *(v10)->field_5f0;
            v12 = g_1f064e0;
            *(v10)->field_5e8();
        }
    }
    sub_f7db7c(sub_f7db74(v10));
}
```

## `WeaponSelection.BuyWeapon` — RVA `0xcc504c`

- Decompiled symbol: `WeaponSelection_BuyWeapon`
- Metadata signature: `public void BuyWeapon() { }`
- Native interval: `396` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WeaponSelection_Recovered` matched 4 offsets against `WeaponSelection` metadata (confidence 1.00).

```c
typedef struct WeaponSelection_Recovered {
    char padding_0[40];
    struct struct_3 *totalEarningTxt2;
    char padding_30[24];
    long long insuficientCash;
    char padding_50[40];
    unsigned int Weaponindex;
    char padding_7c[4];
    unsigned long long WeaponPrice;
} WeaponSelection_Recovered;

typedef struct struct_0 {
    char padding_0[1512];
    struct struct_1 *field_5e8;
    unsigned long long field_5f0;
} struct_0;

typedef struct struct_3 {
    struct struct_0 *field_0;
} struct_3;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern unsigned long long g_1f06220;
extern char g_1fab539;

long long WeaponSelection_BuyWeapon(struct_2 *ptr)
{
    unsigned long v1;  // x0
    unsigned long v2;  // x8
    struct_0 **v11;  // x0
    unsigned long long v3;  // x9
    unsigned long v4;  // x0
    unsigned long long v5;  // x8
    unsigned long v6;  // x9
    struct_0 **v7;  // x21
    unsigned long v8;  // x0
    unsigned long long v9;  // x2
    unsigned long long v10;  // x1
    unsigned int v0;  // [bp-0x24]

    if (!(g_1fab539 & 1))
    {
        sub_f7d92c("a&");
        sub_f7d92c(")#");
        sub_f7d92c(&g_1f06220);
        g_1fab539 = 1;
    }
    v0 = 0;
    v1 = PlayerPrefs__GetInt(g_1f0ee98, 0);
    v2 = ptr->field_78;
    v3 = ptr->field_80;
    if (v3)
    {
        if (*((int *)(v3 + 24)) <= (unsigned int)v2)
        {
            sub_f7db7c(v1);
        }
        else if (*((int *)(v3 + v2 * 4 + 32)) <= (unsigned int)v1)
        {
            v1 = PlayerPrefs__GetInt(g_1f0ee98, 0);
            v5 = ptr->field_80;
            if (v5)
            {
                v6 = ptr->field_78;
                if (*((int *)(v5 + 24)) <= (unsigned int)v6)
                    sub_f7db7c(v1);
                PlayerPrefs__SetInt(g_1f0ee98, v1 - *((int *)(v5 + v6 * 4 + 32)), 0);
                v7 = ptr->field_28;
                v0 = PlayerPrefs__GetInt(g_1f0ee98, 0);
                v8 = Int32__ToString(&v0, 0);
                if (v7)
                {
                    v9 = *(v7)->field_5f0;
                    if (!v8)
                        v10 = g_1f06220;
                    else
                        v10 = v8;
                    v11 = v7;
                    *(v7)->field_5e8();
                }
            }
        }
        else if (ptr->field_48)
        {
            v4 = GameObject__SetActive(ptr->field_48, 1, 0);
            return GameObject__SetActive(ptr->field_48, 1, 0);
        }
    }
    sub_f7db7c(sub_f7db74());
}
```

## `WeaponSelection.Weapons` — RVA `0xcc51d8`

- Decompiled symbol: `WeaponSelection_Weapons`
- Metadata signature: `public void Weapons(int Gunsindex) { }`
- Native interval: `196` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WeaponSelection_Recovered` matched 3 offsets against `WeaponSelection` metadata (confidence 1.00).

```c
typedef struct WeaponSelection_Recovered {
    char padding_0[32];
    char isbuy;
    char padding_21[15];
    struct struct_3 *PriceOfCurrentWeapon;
    char padding_38[8];
    struct struct_3 *WeaponBuyButton;
} WeaponSelection_Recovered;

typedef struct struct_3 {
    struct struct_0 *field_0;
} struct_3;

typedef struct struct_0 {
    char padding_0[1512];
    struct struct_1 *field_5e8;
    unsigned long long field_5f0;
} struct_0;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

void WeaponSelection_Weapons(struct_2 *ptr, unsigned int a1)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x21
    unsigned long long v6;  // x20
    unsigned long long v7;  // x19
    unsigned long long cur[5];  // x8
    struct_2 *p;  // x19
    unsigned long v10;  // x20
    unsigned long long v11;  // x21
    unsigned int v12;  // w9
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x18]
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v0 = v4;
    v1 = v5;
    v2 = v6;
    v3 = v7;
    cur = ptr[1].field_40;
    *((unsigned int *)&ptr[1].field_30) = a1;
    if (cur)
    {
        p = ptr;
        v10 = a1;
        v11 = 0;
        while (true)
        {
            v12 = cur[3];
            if (v12 > (unsigned int)v11)
                break;
            if (v12 <= (unsigned int)v11)
                goto LABEL_10c5298;
            cur = &cur[v11];
            if (!cur[4] || (GameObject__SetActive(cur[4], 0, 0), cur = (unsigned long long [5])p[1].field_40, v11 += 1, !cur))
                break;
        }
    }
    while (true)
    {
        sub_f7db74();
        if (v12 <= (unsigned int)v10)
            break;
        cur = &cur[v10 & 4294967295];
        if (cur[4])
        {
            GameObject__SetActive(cur[4], 1, 0);
            WeaponSelection__setLocks(p); /* do not return */
        }
    }
LABEL_10c5298:
    sub_f7db7c();
}
```

## `WeaponSelection.SelectButtonFunction` — RVA `0xcc529c`

- Decompiled symbol: `WeaponSelection_SelectButtonFunction`
- Metadata signature: `public void SelectButtonFunction() { }`
- Native interval: `76` bytes
- Result: `pseudocode`

```c
extern char g_1fab53b;

void WeaponSelection_SelectButtonFunction(unsigned long a0)
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
    if (!(g_1fab53b & 1))
    {
        sub_f7d92c("_&");
        g_1fab53b = 1;
    }
    PlayerPrefs__SetInt();
    return;
}
```

## `WeaponSelection.CloseInsufficientPanel` — RVA `0xcc52e8`

- Decompiled symbol: `WeaponSelection_CloseInsufficientPanel`
- Metadata signature: `public void CloseInsufficientPanel() { }`
- Native interval: `32` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[72];
    unsigned long long field_48;
} struct_0;

void WeaponSelection_CloseInsufficientPanel(struct_0 *a0)
{
    unsigned long long v1;  // x30
    unsigned long long v0;  // [bp-0x10]

    v0 = v1;
    if (a0->field_48)
    {
        GameObject__SetActive();
        return;
    }
    sub_f7db74(0);
}
```

## `WeaponSelection.pistolskin` — RVA `0xcc5308`

- Decompiled symbol: `WeaponSelection_pistolskin`
- Metadata signature: `public void pistolskin() { }`
- Native interval: `72` bytes
- Result: `pseudocode`

```c
extern char g_1fab53c;

void WeaponSelection_pistolskin(void)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab53c & 1))
    {
        sub_f7d92c("\t:");
        g_1fab53c = 1;
    }
    PlayerPrefs__SetInt();
    return;
}
```

## `WeaponSelection.pistolskinBuy` — RVA `0xcc5350`

- Decompiled symbol: `WeaponSelection_pistolskinBuy`
- Metadata signature: `public void pistolskinBuy() { }`
- Native interval: `296` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WeaponSelection_Recovered` matched 2 offsets against `WeaponSelection` metadata (confidence 1.00).

```c
typedef struct WeaponSelection_Recovered {
    char padding_0[40];
    struct struct_3 *totalEarningTxt2;
    char padding_30[24];
    unsigned long long insuficientCash;
} WeaponSelection_Recovered;

typedef struct struct_0 {
    char padding_0[1512];
    struct struct_1 *field_5e8;
    unsigned long long field_5f0;
} struct_0;

typedef struct struct_3 {
    struct struct_0 *field_0;
} struct_3;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern unsigned long long g_1f06220;
extern long long g_1f0dab0;
extern char g_1fab53d;

long long WeaponSelection_pistolskinBuy(struct_2 *ptr)
{
    unsigned int v1;  // w0
    unsigned long long v2;  // x0
    unsigned long v3;  // x0
    unsigned long long v4;  // x0
    struct_0 **v5;  // x20
    unsigned long long v6;  // x2
    unsigned long long v7;  // x1
    struct_0 **v8;  // x0
    unsigned int v0;  // [bp-0x24]

    if (!(g_1fab53d & 1))
    {
        sub_f7d92c(")#");
        sub_f7d92c(&g_1f0dab0);
        sub_f7d92c(&g_1f06220);
        g_1fab53d = 1;
    }
    v1 = PlayerPrefs__GetInt(g_1f0ee98, 0);
    if (*((int *)((char *)&ptr[1].field_28 + 4)) > v1)
    {
        v2 = ptr->field_48;
        if (v2)
        {
            v3 = GameObject__SetActive();
            return GameObject__SetActive();
        }
    }
    else
    {
        v4 = PlayerPrefs__GetInt(g_1f0ee98, 0);
        PlayerPrefs__SetInt(g_1f0ee98, v4 - *((int *)((char *)&ptr[1].field_28 + 4)), 0);
        v5 = ptr->field_28;
        v0 = PlayerPrefs__GetInt(g_1f0ee98, 0);
        v2 = Int32__ToString(&v0, 0);
        if (v5)
        {
            v6 = *(v5)->field_5f0;
            if (!v2)
                v7 = g_1f06220;
            else
                v7 = v2;
            v8 = v5;
            *(v5)->field_5e8();
        }
    }
    sub_f7db74(v2);
}
```

## `WeaponSelection.pistolskinPanel` — RVA `0xcc5478`

- Decompiled symbol: `WeaponSelection_pistolskinPanel`
- Metadata signature: `public void pistolskinPanel() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
void WeaponSelection_pistolskinPanel(unsigned long long *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr[12];
    if (v4)
    {
        GameObject__SetActive(v4, 1, 0);
        v4 = ptr[11];
        if (ptr[11])
        {
            GameObject__SetActive();
            return;
        }
    }
    sub_f7db74(v4);
}
```

## `WeaponSelection.pistolMain` — RVA `0xcc54b0`

- Decompiled symbol: `WeaponSelection_pistolMain`
- Metadata signature: `public void pistolMain() { }`
- Native interval: `72` bytes
- Result: `pseudocode`

```c
extern char g_1fab53e;

void WeaponSelection_pistolMain(void)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab53e & 1))
    {
        sub_f7d92c("\t:");
        g_1fab53e = 1;
    }
    PlayerPrefs__SetInt();
    return;
}
```

## `WeaponSelection.pistolMainPanel` — RVA `0xcc54f8`

- Decompiled symbol: `WeaponSelection_pistolMainPanel`
- Metadata signature: `public void pistolMainPanel() { }`
- Native interval: `56` bytes
- Result: `pseudocode`

```c
void WeaponSelection_pistolMainPanel(unsigned long long *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr[12];
    if (v4)
    {
        GameObject__SetActive(v4, 0, 0);
        v4 = ptr[11];
        if (ptr[11])
        {
            GameObject__SetActive();
            return;
        }
    }
    sub_f7db74(v4);
}
```

## `WeaponSelection.FreeReward` — RVA `0xcc5530`

- Decompiled symbol: `WeaponSelection_FreeReward`
- Metadata signature: `public void FreeReward() { }`
- Native interval: `72` bytes
- Result: `pseudocode`

```c
extern long long g_1f145b8;
extern char g_1fab53f;

void WeaponSelection_FreeReward(void)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    if (!(g_1fab53f & 1))
    {
        sub_f7d92c(&g_1f145b8);
        g_1fab53f = 1;
    }
    PlayerPrefs__SetInt();
    return;
}
```

## `WeaponSelection.FreeRewardfun` — RVA `0xcc5578`

- Decompiled symbol: `WeaponSelection_FreeRewardfun`
- Metadata signature: `public void FreeRewardfun() { }`
- Native interval: `236` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[40];
    struct struct_3 *field_28;
} struct_2;

typedef struct struct_0 {
    char padding_0[1512];
    struct struct_1 *field_5e8;
    unsigned long long field_5f0;
} struct_0;

typedef struct struct_3 {
    struct struct_0 *field_0;
} struct_3;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

extern unsigned long long g_1f06220;
extern char g_1fab540;

void WeaponSelection_FreeRewardfun(struct_2 *ptr)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x21
    unsigned long long v7;  // x20
    unsigned long long v8;  // x19
    unsigned int v9;  // w0
    struct_0 **v10;  // x20
    unsigned long v11;  // x0
    unsigned long long v12;  // x2
    unsigned long long v13;  // x1
    struct_0 **v14;  // x0
    unsigned int v0;  // [bp-0x24]
    unsigned long long v1;  // [bp-0x20]
    unsigned long long v2;  // [bp-0x18]
    unsigned long long v3;  // [bp-0x10]
    unsigned long long v4;  // [bp-0x8]

    v1 = v5;
    v2 = v6;
    v3 = v7;
    v4 = v8;
    if (!(g_1fab540 & 1))
    {
        sub_f7d92c(")#");
        sub_f7d92c(&g_1f06220);
        g_1fab540 = 1;
    }
    v9 = PlayerPrefs__GetInt(g_1f0ee98, 0);
    PlayerPrefs__SetInt(g_1f0ee98, v9 + 500, 0);
    v10 = ptr->field_28;
    v0 = PlayerPrefs__GetInt(g_1f0ee98, 0);
    v11 = Int32__ToString(&v0, 0);
    if (!v10)
        sub_f7db74();
    v12 = *(v10)->field_5f0;
    if (!v11)
        v13 = g_1f06220;
    else
        v13 = v11;
    v14 = v10;
    *(v10)->field_5e8();
}
```

## `WeaponSelection.OnTimeReward` — RVA `0xcc5664`

- Decompiled symbol: `WeaponSelection_OnTimeReward`
- Metadata signature: `public void OnTimeReward(int thisGun) { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[120];
    unsigned int field_78;
} struct_0;

struct_0 * WeaponSelection_OnTimeReward(struct_0 *ptr, unsigned int a1)
{
    ptr->field_78 = a1;
    return ptr;
}
```

## `WeaponSelection.GiveReward` — RVA `0xcc566c`

- Decompiled symbol: `WeaponSelection_GiveReward`
- Metadata signature: `public void GiveReward() { }`
- Native interval: `828` bytes
- Result: `pseudocode`
- Heuristic layout hint: `WeaponSelection_Recovered` matched 3 offsets against `WeaponSelection` metadata (confidence 1.00).

```c
typedef struct WeaponSelection_Recovered {
    char padding_0[120];
    unsigned int Weaponindex;
    char padding_7c[20];
    struct struct_5 *OnetimeGun;
    char padding_98[24];
    long long OnetimePanel;
} WeaponSelection_Recovered;

typedef struct struct_5 {
    char padding_0[24];
    unsigned int field_18;
} struct_5;

typedef struct struct_2 {
    char padding_0[24];
    unsigned int field_18;
} struct_2;

typedef struct struct_0 {
    char padding_0[184];
    struct struct_1 *field_b8;
    char padding_c0[32];
    unsigned int field_e0;
} struct_0;

typedef struct struct_1 {
    struct struct_0 *field_0;
} struct_1;

typedef struct struct_0 {
    char padding_0[72];
    long long field_48;
    char padding_50[32];
    long long field_70;
    long long field_78;
    long long field_80;
    long long field_88;
    char padding_90[8];
    long long field_98;
    long long field_a0;
    long long field_a8;
    char padding_b0[196];
    unsigned int field_174;
} struct_0;

extern struct_0 *g_1ef0750;
extern long long g_1f06220;
extern char g_1fab541;

void WeaponSelection_GiveReward(struct_6 *ptr)
{
    unsigned long long v5;  // x30
    unsigned long long v6;  // x22
    unsigned long long v7;  // x21
    unsigned long long v8;  // x20
    unsigned long long v9;  // x19
    unsigned int v10;  // w8
    unsigned long v11;  // x0
    struct_2 *v12;  // x8
    unsigned long v13;  // x9
    struct_0 *v14;  // x0
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
    if (!(g_1fab541 & 1))
    {
        sub_f7d92c(&g_1ef0750);
        sub_f7d92c("U^");
        sub_f7d92c(")#");
        sub_f7d92c(&g_1f06220);
        g_1fab541 = 1;
    }
    if (ptr->field_90)
    {
        if (ptr->field_90->field_18 - 1 <= g_1ef2480->field_b8->field_10)
            v10 = 0;
        else
            v10 = g_1ef2480->field_b8->field_10 + 1;
        g_1ef2480->field_b8->field_10 = v10;
        if (ptr->field_b0)
        {
            v11 = GameObject__SetActive(ptr->field_b0, 0, 0);
            v12 = g_1ef2480->field_b8->field_8;
            if (v12)
            {
                v13 = ptr->field_78;
                if (v12->field_18 <= (unsigned int)v13)
                    sub_f7db7c(v11);
                v12[1].padding_0[4 + v13] = 1;
                v14 = g_1ef0750;
                if (!g_1ef0750->field_e0)
                {
                    sub_f7da5c(g_1ef0750);
                    v14 = g_1ef0750;
                }
                if (v14->field_b8->field_0)
                    MainMenuController__PrimaryWeapon(v14->field_b8->field_0); /* do not return */
            }
        }
    }
    v11 = sub_f7db74();
    sub_f7db7c(v11);
}
```

## `WeaponSelection.ctor` — RVA `0xcc59a8`

- Decompiled symbol: `WeaponSelection_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[120];
    unsigned int field_78;
} struct_0;

long long WeaponSelection_ctor(struct_0 *ptr)
{
    ptr->field_78 = 1;
}
```
