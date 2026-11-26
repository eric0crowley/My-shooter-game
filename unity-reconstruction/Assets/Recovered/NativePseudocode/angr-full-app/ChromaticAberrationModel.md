# Native pseudocode: ChromaticAberrationModel

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `ChromaticAberrationModel.get_settings` — RVA `0xcdb344`

- Decompiled symbol: `ChromaticAberrationModel_get_settings`
- Metadata signature: `public ChromaticAberrationModel.Settings get_settings() { }`
- Native interval: `12` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned long long field_18;
} struct_0;

long long ChromaticAberrationModel_get_settings(struct_0 *a0)
{
    return a0->field_18;
}
```

## `ChromaticAberrationModel.set_settings` — RVA `0xcdb350`

- Decompiled symbol: `ChromaticAberrationModel_set_settings`
- Metadata signature: `public void set_settings(ChromaticAberrationModel.Settings value) { }`
- Native interval: `16` bytes
- Result: `pseudocode`

```c
long long ChromaticAberrationModel_set_settings(unsigned long long *ptr, unsigned long a1, unsigned long a2)
{
    long long v0;  // x0

    ptr[3] = a1;
    ptr[4] = a2;
    v0 = sub_f7d8d0();
    return sub_f7d8d0();
}
```

## `ChromaticAberrationModel.Reset` — RVA `0xcdb360`

- Decompiled symbol: `ChromaticAberrationModel_Reset`
- Metadata signature: `public override void Reset() { }`
- Native interval: `76` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned long long field_20;
} struct_0;

long long ChromaticAberrationModel_Reset(struct_0 *ptr)
{
    struct_0 *p;  // x19
    unsigned long v3;  // x0
    unsigned long flag;  // [bp-0x20]
    unsigned long v1;  // [bp-0x18], Other Possible Types: unsigned long long

    flag = 0;
    v1 = 0;
    sub_f7d8d0(&flag, 0);
    *((unsigned int *)&v1) = 1036831949;
    *((unsigned long *)&ptr->padding_0[24]) = flag;
    p = &ptr->padding_0[24];
    *((unsigned long *)&p->padding_0[8]) = v1;
    v3 = sub_f7d8d0(p, 0);
    return sub_f7d8d0(p, 0);
}
```

## `ChromaticAberrationModel.ctor` — RVA `0xcdb3e0`

- Decompiled symbol: `ChromaticAberrationModel_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `88` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned long long field_20;
} struct_0;

long long ChromaticAberrationModel_ctor(struct_0 *ptr)
{
    unsigned long long v4;  // x30
    unsigned long long v5;  // x19
    unsigned long flag;  // [bp-0x20]
    unsigned long v1;  // [bp-0x18], Other Possible Types: unsigned long long
    unsigned long long v2;  // [bp-0x10]
    unsigned long long v3;  // [bp-0x8]

    v2 = v4;
    v3 = v5;
    flag = 0;
    v1 = 0;
    sub_f7d8d0(&flag, 0);
    *((unsigned int *)&v1) = 1036831949;
    *((unsigned long *)&ptr->padding_0[24]) = flag;
    ptr->field_20 = v1;
    sub_f7d8d0((struct struct_0 *)&ptr->padding_0[24], 0);
    PostProcessingModel__ctor(ptr, 0); /* do not return */
}
```
