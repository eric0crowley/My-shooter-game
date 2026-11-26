# Native pseudocode: InputRig.VirtualJoystickConfigCollection

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `InputRig.VirtualJoystickConfigCollection.ctor` — RVA `0xc40a54`

- Decompiled symbol: `InputRig_VirtualJoystickConfigCollection_ctor`
- Metadata signature: `public void .ctor(InputRig rig, int capacity) { }`
- Native interval: `96` bytes
- Result: `pseudocode`

```c
extern long long g_1ef9888;
extern char g_1fab1f7;

void InputRig_VirtualJoystickConfigCollection_ctor(unsigned long a0, unsigned long a1, unsigned long a2)
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
    if (!(g_1fab1f7 & 1))
    {
        sub_f7d92c(&g_1ef9888);
        g_1fab1f7 = 1;
    }
}
```

## `InputRig.VirtualJoystickConfigCollection.Add` — RVA `0xc40ab4`

- Decompiled symbol: `InputRig_VirtualJoystickConfigCollection_Add`
- Metadata signature: `public InputRig.VirtualJoystickConfig Add(string name, bool undoable) { }`
- Native interval: `296` bytes
- Result: `pseudocode`

```c
extern long long g_1ef3370;
extern long long g_1ef9120;
extern long long g_1ef9890;
extern char g_1fab1f8;

long long InputRig_VirtualJoystickConfigCollection_Add(long long a0, long long a1)
{
    long long v0;  // x0
    unsigned long v1;  // x0

    if (!(g_1fab1f8 & 1))
    {
        sub_f7d92c(&g_1ef9120);
        sub_f7d92c(&g_1ef9890);
        sub_f7d92c(&g_1ef3370);
        g_1fab1f8 = 1;
    }
    v0 = sub_1526618(a0, a1, g_1ef9890);
    if (v0)
        return v0;
    v1 = sub_f7db70(g_1ef3370);
    Object__ctor(v1, 0);
    InputRig_VirtualJoystickConfig__BasicConstructor(v1); /* do not return */
}
```
