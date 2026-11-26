# Native pseudocode: MeshContainer

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `MeshContainer.ctor` — RVA `0xce1e20`

- Decompiled symbol: `MeshContainer_ctor`
- Metadata signature: `public void .ctor(Mesh m) { }`
- Native interval: `112` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MeshContainer_Recovered` matched 3 offsets against `MeshContainer` metadata (confidence 1.00).

```c
typedef struct MeshContainer_Recovered {
    char padding_0[16];
    long long mesh;
    long long vertices;
    unsigned long long normals;
} MeshContainer_Recovered;

void MeshContainer_ctor(struct_0 *addr, long long a1)
{
    unsigned long long v3;  // x30
    unsigned long long v4;  // x20
    unsigned long long v5;  // x19
    struct_0 *ptr;  // x0
    long long v7;  // x1
    struct_0 *p;  // x0
    unsigned long long v0;  // [bp-0x20]
    unsigned long long v1;  // [bp-0x10]
    unsigned long long v2;  // [bp-0x8]

    v0 = v3;
    v1 = v4;
    v2 = v5;
    Object__ctor();
    ptr = addr;
    ptr->field_10 = a1;
    sub_f7d8d0((struct MeshContainer_Recovered *)&ptr->field_10, a1);
    if (a1)
    {
        v7 = Mesh__get_vertices(a1, 0);
        p = addr;
        p->field_18 = v7;
        sub_f7d8d0((struct MeshContainer_Recovered *)&p->field_18, v7);
        addr->field_20 = Mesh__get_normals(a1, 0);
        sub_f7d8d0();
        return;
    }
    sub_f7db74();
}
```

## `MeshContainer.Update` — RVA `0xce1e90`

- Decompiled symbol: `MeshContainer_Update`
- Metadata signature: `public void Update() { }`
- Native interval: `56` bytes
- Result: `pseudocode`
- Heuristic layout hint: `MeshContainer_Recovered` matched 2 offsets against `MeshContainer` metadata (confidence 1.00).

```c
typedef struct MeshContainer_Recovered {
    char padding_0[16];
    unsigned long long mesh;
    long long vertices;
} MeshContainer_Recovered;

void MeshContainer_Update(struct_0 *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    unsigned long long v4;  // x0
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr->field_10;
    if (v4)
    {
        Mesh__set_vertices(v4, ptr->field_18, 0);
        v4 = ptr->field_10;
    }
    sub_f7db74(v4);
}
```
