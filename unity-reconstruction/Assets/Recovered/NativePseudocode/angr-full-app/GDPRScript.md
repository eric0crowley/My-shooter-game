# Native pseudocode: GDPRScript

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `GDPRScript.Start` — RVA `0xc757c0`

- Decompiled symbol: `GDPRScript_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `460` bytes
- Result: `pseudocode`

```c
typedef struct struct_3 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    struct struct_2 *field_18;
} struct_3;

typedef struct struct_1 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_1;

typedef struct struct_0 {
    char padding_0[32];
    unsigned long long field_20;
} struct_0;

typedef struct struct_6 {
    char padding_0[16];
    char field_10;
    char padding_11[7];
    struct struct_5 *field_18;
} struct_6;

typedef struct struct_2 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_2;

typedef struct struct_5 {
    char padding_0[16];
    unsigned int field_10;
    char padding_14[4];
    struct struct_4 *field_18;
} struct_5;

typedef struct struct_4 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_4;

extern long long g_1eed848;
extern long long g_1eeefd8;
extern long long g_1ef8630;
extern long long g_1ef8648;
extern long long g_1efea08;
extern unsigned long long g_1f07d28;
extern char g_1fab399;

void GDPRScript_Start(long long a0)
{
    unsigned long long v6;  // x30
    unsigned long long v7;  // x23
    struct_0 *ptr3;  // x0
    struct_3 *p;  // x0
    struct_6 *ptr4;  // x21
    struct_6 *addr;  // x0
    long long v20;  // x0
    unsigned long long v8;  // x22
    unsigned long long v9;  // x21
    unsigned long long v10;  // x20
    unsigned long long v11;  // x19
    struct_3 *ptr5;  // x20
    struct_1 *ptr;  // x21
    unsigned long long v14;  // x8
    unsigned long v15;  // x10
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
    if (!(g_1fab399 & 1))
    {
        sub_f7d92c("#\t");
        sub_f7d92c(&g_1eeefd8);
        sub_f7d92c(")4");
        sub_f7d92c(&g_1efea08);
        sub_f7d92c(&g_1ef8648);
        sub_f7d92c(&g_1ef8630);
        sub_f7d92c(&g_1eed848);
        sub_f7d92c(&g_1f07d28);
        g_1fab399 = 1;
    }
    ptr5 = sub_f7db70(g_1eeefd8);
    ConsentDebugSettings__ctor(ptr5, 0);
    if (ptr5)
    {
        ptr5->field_10 = 1;
        ptr = sub_f7db70(g_1eed848);
        sub_14a2b64(ptr, g_1ef8630);
        if (ptr)
        {
            v14 = ptr->field_10;
            ptr->field_1c = ptr->field_1c + 1;
            if (v14)
            {
                v15 = ptr->field_18;
                if (*((int *)(v14 + 24)) > (unsigned int)v15)
                {
                    ptr3 = v14 + v15 * 8;
                    ptr->field_18 = (unsigned int)v15 + 1;
                    ptr3->field_20 = g_1f07d28;
                    sub_f7d8d0((struct struct_0 *)&ptr3->field_20);
                }
                else
                {
                    sub_14a3390(ptr);
                }
                p = ptr5;
                p->field_18 = ptr;
                sub_f7d8d0((struct struct_3 *)&p->field_18, ptr);
                ptr4 = sub_f7db70(g_1eef000);
                ConsentRequestParameters__ctor(ptr4, 0);
                if (ptr4)
                {
                    addr = ptr4;
                    ptr4->field_10 = 0;
                    addr->field_18 = ptr5;
                    sub_f7d8d0((struct struct_6 *)&addr->field_18, ptr5);
                    v20 = sub_f7db70(g_1eec008);
                    sub_126041c(v20, a0, g_1efea08, 0);
                }
            }
        }
    }
    sub_f7db74();
}
```

## `GDPRScript.OnConsentInfoUpdated` — RVA `0xc7598c`

- Decompiled symbol: `GDPRScript_OnConsentInfoUpdated`
- Metadata signature: `private void OnConsentInfoUpdated(FormError error) { }`
- Native interval: `136` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern char g_1fab39a;

unsigned long long GDPRScript_OnConsentInfoUpdated(long long a0, unsigned long long a1)
{
    unsigned long long v0;  // x0
    unsigned long long v1;  // x0

    if (!(g_1fab39a & 1))
    {
        sub_f7d92c(&g_1eef458);
        g_1fab39a = 1;
    }
    if (a1)
    {
        if (!g_1eef458->field_e0)
            sub_f7da5c(g_1eef458);
        v0 = Debug__LogError();
        return Debug__LogError();
    }
    else
    {
        v1 = ConsentInformation__IsConsentFormAvailable(0);
        if (!((char)v1 & 1))
            return v1;
        GDPRScript__LoadConsentForm(a0); /* do not return */
    }
}
```

## `GDPRScript.LoadConsentForm` — RVA `0xc75a14`

- Decompiled symbol: `GDPRScript_LoadConsentForm`
- Metadata signature: `private void LoadConsentForm() { }`
- Native interval: `128` bytes
- Result: `pseudocode`

```c
extern long long g_1eec100;
extern long long g_1efea10;
extern char g_1fab39b;

void GDPRScript_LoadConsentForm(long long a0)
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
    if (!(g_1fab39b & 1))
    {
        sub_f7d92c(&g_1eec100);
        sub_f7d92c(&g_1efea10);
        g_1fab39b = 1;
    }
    v10 = sub_f7db70(g_1eec100);
    sub_12633ac(v10, a0, g_1efea10, 0);
}
```

## `GDPRScript.OnLoadConsentForm` — RVA `0xc75a94`

- Decompiled symbol: `GDPRScript_OnLoadConsentForm`
- Metadata signature: `private void OnLoadConsentForm(ConsentForm consentForm, FormError error) { }`
- Native interval: `264` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[32];
    long long field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern long long g_1efea18;
extern char g_1fab39c;

int GDPRScript_OnLoadConsentForm(struct_1 *ptr, long long a1, unsigned long long a2)
{
    unsigned int v0;  // w0
    long long v1;  // x0

    if (!(g_1fab39c & 1))
    {
        sub_f7d92c("#\t");
        sub_f7d92c(&g_1eef458);
        sub_f7d92c(&g_1efea18);
        g_1fab39c = 1;
    }
    if (a2)
    {
        if (g_1eef458->field_e0)
            return Debug__LogError();
        sub_f7da5c(g_1eef458);
        return Debug__LogError();
    }
    else
    {
        ptr->field_20 = a1;
        sub_f7d8d0((struct struct_1 *)&ptr->field_20, a1);
        v0 = ConsentInformation__get_ConsentStatus(0);
        if (v0 != 2)
            return v0;
        v1 = sub_f7db70(g_1eec008);
        sub_126041c(v1, ptr, g_1efea18, 0);
        if (!ptr->field_20)
            sub_f7db74();
    }
}
```

## `GDPRScript.OnShowForm` — RVA `0xc75b9c`

- Decompiled symbol: `GDPRScript_OnShowForm`
- Metadata signature: `private void OnShowForm(FormError error) { }`
- Native interval: `112` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[224];
    unsigned int field_e0;
} struct_0;

extern struct_0 *g_1eef458;
extern char g_1fab39d;

void GDPRScript_OnShowForm(long long a0, unsigned long long a1)
{
    if (!(g_1fab39d & 1))
    {
        sub_f7d92c(&g_1eef458);
        g_1fab39d = 1;
    }
    if (!a1)
        GDPRScript__LoadConsentForm(a0); /* do not return */
    if (!g_1eef458->field_e0)
        sub_f7da5c(g_1eef458);
    Debug__LogError();
    return;
}
```

## `GDPRScript.Update` — RVA `0xc75c0c`

- Decompiled symbol: `GDPRScript_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long GDPRScript_Update(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `GDPRScript.ctor` — RVA `0xc75c10`

- Decompiled symbol: `GDPRScript_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long GDPRScript_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
