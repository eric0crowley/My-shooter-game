# Native pseudocode: ObjectShow

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `ObjectShow.Start` — RVA `0xcc4560`

- Decompiled symbol: `ObjectShow_Start`
- Metadata signature: `private void Start() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long ObjectShow_Start(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `ObjectShow.Update` — RVA `0xcc4564`

- Decompiled symbol: `ObjectShow_Update`
- Metadata signature: `private void Update() { }`
- Native interval: `4` bytes
- Result: `pseudocode`

```c
long long ObjectShow_Update(void)
{
    unsigned long v0;  // x0

    return v0;
}
```

## `ObjectShow.OnTriggerEnter` — RVA `0xcc4568`

- Decompiled symbol: `ObjectShow_OnTriggerEnter`
- Metadata signature: `private void OnTriggerEnter(Collider other) { }`
- Native interval: `188` bytes
- Result: `pseudocode`

```c
typedef struct struct_1 {
    char padding_0[32];
    struct struct_0 *field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

typedef struct struct_2 {
    char padding_0[32];
    long long field_20;
} struct_2;

extern long long g_1f0cf98;
extern char g_1fab532;

long long ObjectShow_OnTriggerEnter(struct_1 *ptr, long long a1)
{
    long long v0;  // x0
    unsigned long v1;  // x0
    struct_0 *v2;  // x8
    unsigned long long v3;  // x20
    struct_2 *v4;  // x8
    unsigned long v5;  // x0

    if (!(g_1fab532 & 1))
    {
        sub_f7d92c(&g_1f0cf98);
        g_1fab532 = 1;
    }
    if (a1 && Component__get_gameObject(a1, 0))
    {
        v0 = GameObject__get_tag();
        v1 = String__op_Equality(v0, g_1f0cf98, 0);
        if (!((char)v1 & 1))
            return v1;
        v2 = ptr->field_20;
        if (ptr->field_20)
        {
            v3 = 0;
            do
            {
                if (v2->field_18 <= (unsigned int)v3)
                    return v1;
                if (v2->field_18 <= (unsigned int)v3)
                    sub_f7db7c();
                v4 = &v2->padding_0[8 * v3];
            } while (v4->field_20 && (v1 = (unsigned long)GameObject__SetActive(v4->field_20, 1, 0), v2 = (struct_0 *)ptr->field_20, v3 += 1, v2));
        }
    }
    v5 = sub_f7db74();
    return sub_f7db74();
}
```

## `ObjectShow.ctor` — RVA `0xcc4624`

- Decompiled symbol: `ObjectShow_ctor`
- Metadata signature: `public void .ctor() { }`
- Native interval: `8` bytes
- Result: `pseudocode`

```c
long long ObjectShow_ctor(void)
{
    long long v0;  // x0

    v0 = MonoBehaviour__ctor();
    return MonoBehaviour__ctor();
}
```
