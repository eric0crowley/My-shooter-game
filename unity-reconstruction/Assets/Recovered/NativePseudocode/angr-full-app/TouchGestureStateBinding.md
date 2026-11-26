# Native pseudocode: TouchGestureStateBinding

> **Generated reconstruction, not original C# source.** The bodies below are approximate C-like pseudocode recovered from the APK AArch64 machine code with angr. Names and field layout hints are heuristic; local variables, types, control flow, and call names may be inaccurate. See `../README.md`.

## `TouchGestureStateBinding.ctor` — RVA `0xc5e9e4`

- Decompiled symbol: `TouchGestureStateBinding_ctor`
- Metadata signature: `public void .ctor(InputBindingBase parent) { }`
- Native interval: `1668` bytes
- Result: `pseudocode`

```c
typedef struct struct_0 {
    char padding_0[16];
    char field_10;
    char padding_11[7];
    long long field_18;
} struct_0;

extern long long g_1eef5a0;
extern long long g_1eef6e0;
extern long long g_1ef0558;
extern char g_1fab2dc;

void TouchGestureStateBinding_ctor(struct_0 *ptr, long long a1)
{
    unsigned long long v11;  // x30
    unsigned long long v12;  // x28
    unsigned long long v21;  // x19
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
    if (!(g_1fab2dc & 1))
    {
        sub_f7d92c("g.");
        sub_f7d92c("y7");
        sub_f7d92c(&g_1eef5a0);
        sub_f7d92c(&g_1eef6e0);
        sub_f7d92c(&g_1ef0558);
        sub_f7d92c("7H");
        sub_f7d92c("5Q");
        g_1fab2dc = 1;
    }
    Object__ctor(ptr, 0);
    ptr->field_10 = 0;
    ptr->field_18 = a1;
    sub_f7d8d0((struct struct_0 *)&ptr->field_18, a1);
    ptr->field_10 = 0;
    DigitalBinding__ctor(sub_f7db70(g_1eef590)); /* do not return */
}
```

## `TouchGestureStateBinding.CopyFrom` — RVA `0xc5f068`

- Decompiled symbol: `TouchGestureStateBinding_CopyFrom`
- Metadata signature: `public void CopyFrom(TouchGestureStateBinding b) { }`
- Native interval: `992` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchGestureStateBinding_Recovered` matched 29 offsets against `TouchGestureStateBinding` metadata (confidence 0.97).

```c
typedef struct struct_2 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    struct struct_1 *field_20;
} struct_2;

typedef struct TouchGestureStateBinding_Recovered {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    struct struct_6 *rawPressBinding;
    struct struct_6 *normalPressBinding;
    struct struct_6 *longPressBinding;
    struct struct_6 *tapBinding;
    struct struct_6 *doubleTapBinding;
    struct struct_6 *longTapBinding;
    struct struct_0 *normalPressSwipeDirBinding;
    struct struct_0 *longPressSwipeDirBinding;
    struct struct_0 *normalPressSwipeHorzAxisBinding;
    struct struct_0 *normalPressSwipeVertAxisBinding;
    struct struct_0 *longPressSwipeHorzAxisBinding;
    struct struct_0 *longPressSwipeVertAxisBinding;
    struct struct_0 *normalPressScrollHorzBinding;
    struct struct_0 *normalPressScrollVertBinding;
    struct struct_0 *longPressScrollHorzBinding;
    struct struct_0 *longPressScrollVertBinding;
    struct struct_0 *rawPressMousePosBinding;
    struct struct_1 *normalPressMousePosBinding;
    struct struct_2 *longPressMousePosBinding;
    struct struct_3 *tapMousePosBinding;
    struct struct_4 *doubleTapMousePosBinding;
    struct struct_5 *longTapMousePosBinding;
    struct struct_6 *normalPressSwipeMousePosBinding;
    struct struct_7 *longPressSwipeMousePosBinding;
    struct struct_8 *rawPressEmuTouchBinding;
    struct struct_9 *normalPressEmuTouchBinding;
    struct struct_10 *longPressEmuTouchBinding;
    struct struct_0 *normalPressSwipeJoyBinding;
    struct struct_0 *longPressSwipeJoyBinding;
} TouchGestureStateBinding_Recovered;

typedef struct struct_21 {
    char padding_0[16];
    char field_10;
    char padding_11[7];
    struct struct_21 *field_18;
    unsigned int field_20;
} struct_21;

typedef struct struct_0 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    unsigned int field_20;
} struct_0;

typedef struct struct_12 {
    char padding_0[16];
    char field_10;
    char padding_11[7];
    struct struct_12 *field_18;
    unsigned int field_20;
} struct_12;

typedef struct struct_1 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    unsigned int field_20;
} struct_1;

typedef struct struct_19 {
    char padding_0[16];
    char field_10;
    char padding_11[7];
    struct struct_19 *field_18;
    unsigned int field_20;
} struct_19;

typedef struct struct_22 {
    char padding_0[16];
    char field_10;
    char padding_11[7];
    struct struct_22 *field_18;
    unsigned int field_20;
} struct_22;

typedef struct struct_3 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    unsigned int field_20;
} struct_3;

typedef struct struct_13 {
    char padding_0[16];
    char field_10;
    char padding_11[7];
    struct struct_13 *field_18;
    unsigned int field_20;
} struct_13;

typedef struct struct_4 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    unsigned int field_20;
} struct_4;

typedef struct struct_17 {
    char padding_0[16];
    char field_10;
    char padding_11[7];
    struct struct_17 *field_18;
    unsigned int field_20;
} struct_17;

typedef struct struct_5 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    unsigned int field_20;
} struct_5;

typedef struct struct_20 {
    char padding_0[16];
    char field_10;
    char padding_11[7];
    struct struct_20 *field_18;
    unsigned int field_20;
} struct_20;

typedef struct struct_6 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    unsigned int field_20;
} struct_6;

typedef struct struct_18 {
    char padding_0[16];
    char field_10;
    char padding_11[7];
    struct struct_18 *field_18;
    unsigned int field_20;
} struct_18;

typedef struct struct_7 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    unsigned int field_20;
} struct_7;

typedef struct struct_16 {
    char padding_0[16];
    char field_10;
    char padding_11[7];
    struct struct_16 *field_18;
} struct_16;

typedef struct struct_8 {
    char padding_0[16];
    char field_10;
} struct_8;

typedef struct struct_15 {
    char padding_0[16];
    char field_10;
    char padding_11[7];
    struct struct_15 *field_18;
} struct_15;

typedef struct struct_9 {
    char padding_0[16];
    char field_10;
} struct_9;

typedef struct struct_14 {
    char padding_0[16];
    char field_10;
    char padding_11[7];
    struct struct_14 *field_18;
} struct_14;

typedef struct struct_10 {
    char padding_0[16];
    char field_10;
} struct_10;

typedef struct struct_1 {
    char padding_0[16];
    long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_1;

typedef struct struct_6 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    unsigned long long field_20;
    struct struct_4 *field_28;
} struct_6;

typedef struct struct_0 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    char field_20;
    char padding_21[3];
    unsigned int field_24;
    struct struct_6 *field_28;
    struct struct_6 *field_30;
    struct struct_6 *field_38;
    struct struct_6 *field_40;
    struct struct_6 *field_48;
    struct struct_6 *field_50;
    struct struct_6 *field_58;
    struct struct_6 *field_60;
    struct struct_6 *field_68;
    struct struct_6 *field_70;
} struct_0;

typedef struct struct_0 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    unsigned long long field_20;
} struct_0;

typedef struct struct_0 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    struct struct_0 *field_20;
    struct struct_6 *field_28;
    struct struct_6 *field_30;
} struct_0;

typedef struct struct_2 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    unsigned int field_20;
} struct_2;

typedef struct struct_0 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    struct struct_0 *field_20;
    struct struct_0 *field_28;
    struct struct_0 *field_30;
} struct_0;

typedef struct struct_4 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    struct struct_3 *field_20;
    struct struct_5 *field_28;
} struct_4;

typedef struct struct_3 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
} struct_3;

typedef struct struct_5 {
    char padding_0[24];
    unsigned int field_18;
    unsigned int field_1c;
} struct_5;

struct_2 * TouchGestureStateBinding_CopyFrom(struct_2 *ptr22, struct_11 *p, unsigned long a2, unsigned int a3, unsigned long a4)
{
    unsigned int v0;  // w8
    struct_2 *ptr;  // x20
    struct_1 *ptr23;  // x9
    unsigned int v11;  // w10
    struct_12 *ptr5;  // x11
    struct_19 *ptr14;  // x8
    struct_2 *ptr24;  // x9
    unsigned int v16;  // w10
    struct_19 *ptr6;  // x11
    struct_22 *ptr15;  // x8
    struct_2 *ptr7;  // x9
    struct_3 *ptr25;  // x9
    unsigned int v21;  // w10
    struct_22 *ptr8;  // x11
    struct_13 *ptr16;  // x8
    struct_4 *ptr26;  // x9
    unsigned int v26;  // w10
    struct_13 *ptr9;  // x11
    struct_17 *ptr17;  // x8
    struct_5 *ptr27;  // x9
    unsigned int v31;  // w10
    struct_17 *ptr10;  // x11
    struct_20 *ptr18;  // x8
    struct_6 *ptr28;  // x9
    unsigned int v36;  // w10
    struct_20 *ptr11;  // x11
    struct_18 *ptr19;  // x8
    struct_21 *ptr20;  // x8
    struct_7 *ptr29;  // x9
    unsigned int v41;  // w10
    struct_18 *ptr12;  // x11
    struct_16 *addr;  // x8
    unsigned int v45;  // w9
    struct_15 *ptr3;  // x8
    unsigned int v48;  // w9
    struct_0 *ptr30;  // x9
    struct_14 *ptr4;  // x8
    unsigned int v51;  // w9
    struct_2 *v53;  // x0
    unsigned int v6;  // w10
    struct_21 *ptr13;  // x11
    struct_12 *ptr21;  // x8

    if (p)
    {
        v0 = p->field_10;
        ptr = ptr22;
        ptr22->field_10 = v0;
        if (!v0)
            return ptr22;
        ptr7 = ptr;
        do
        {
            ptr7->field_10 = 1;
            ptr7 = *((long long *)&ptr7->padding_11[7]);
        } while (*((long long *)&ptr7->padding_11[7]));
        if (ptr->field_20)
        {
            DigitalBinding__CopyFrom(ptr->field_20, p->field_20);
            if (*((long long *)&ptr[1].padding_0[0]))
            {
                DigitalBinding__CopyFrom(*((long long *)&ptr[1].padding_0[0]), p->field_28);
                if (*((long long *)&ptr[1].padding_0[8]))
                {
                    DigitalBinding__CopyFrom(*((long long *)&ptr[1].padding_0[8]), p->field_30);
                    if (*((long long *)&ptr[1].field_10))
                    {
                        DigitalBinding__CopyFrom(*((long long *)&ptr[1].field_10), p->field_38);
                        if (*((long long *)&ptr[1].padding_11[7]))
                        {
                            DigitalBinding__CopyFrom(*((long long *)&ptr[1].padding_11[7]), p->field_40);
                            if (ptr[1].field_20)
                            {
                                DigitalBinding__CopyFrom(ptr[1].field_20, p->field_48);
                                if (*((long long *)&ptr[2].padding_0[0]))
                                {
                                    DirectionBinding__CopyFrom(*((long long *)&ptr[2].padding_0[0]), p->field_50, 0, a3);
                                    if (*((long long *)&ptr[2].padding_0[8]))
                                    {
                                        DirectionBinding__CopyFrom(*((long long *)&ptr[2].padding_0[8]), p->field_58, 0, a3);
                                        if (*((long long *)&ptr[2].field_10))
                                        {
                                            AxisBinding__CopyFrom(*((long long *)&ptr[2].field_10), p->field_60);
                                            if (*((long long *)&ptr[2].padding_11[7]))
                                            {
                                                AxisBinding__CopyFrom(*((long long *)&ptr[2].padding_11[7]), p->field_68);
                                                if (ptr[2].field_20)
                                                {
                                                    AxisBinding__CopyFrom(ptr[2].field_20, p->field_70);
                                                    if (*((long long *)&ptr[3].padding_0[0]))
                                                    {
                                                        AxisBinding__CopyFrom(*((long long *)&ptr[3].padding_0[0]), p->field_78);
                                                        if (*((long long *)&ptr[3].padding_0[8]))
                                                        {
                                                            ScrollDeltaBinding__CopyFrom(*((long long *)&ptr[3].padding_0[8]), p->field_80, 0, a3);
                                                            if (*((long long *)&ptr[3].field_10))
                                                            {
                                                                ScrollDeltaBinding__CopyFrom(*((long long *)&ptr[3].field_10), p->field_88, 0, a3);
                                                                if (*((long long *)&ptr[3].padding_11[7]))
                                                                {
                                                                    ScrollDeltaBinding__CopyFrom(*((long long *)&ptr[3].padding_11[7]), p->field_90, 0, a3);
                                                                    if (ptr[3].field_20)
                                                                    {
                                                                        ScrollDeltaBinding__CopyFrom(ptr[3].field_20, p->field_98, 0, a3);
                                                                        ptr20 = *((long long *)&ptr[4].padding_0[0]);
                                                                        if (ptr20)
                                                                        {
                                                                            ptr30 = p->field_a0;
                                                                            if (ptr30)
                                                                            {
                                                                                v6 = ptr30->field_10;
                                                                                ptr20->field_10 = v6;
                                                                                if (v6)
                                                                                {
                                                                                    ptr13 = ptr20;
                                                                                    do
                                                                                    {
                                                                                        ptr13->field_10 = 1;
                                                                                        ptr13 = ptr13->field_18;
                                                                                    } while (ptr13->field_18);
                                                                                    ptr20->field_20 = ptr30->field_20;
                                                                                }
                                                                            }
                                                                            ptr21 = *((long long *)&ptr[4].padding_0[8]);
                                                                            if (ptr21)
                                                                            {
                                                                                ptr23 = p->field_a8;
                                                                                if (ptr23)
                                                                                {
                                                                                    v11 = ptr23->field_10;
                                                                                    ptr21->field_10 = v11;
                                                                                    if (v11)
                                                                                    {
                                                                                        ptr5 = ptr21;
                                                                                        do
                                                                                        {
                                                                                            ptr5->field_10 = 1;
                                                                                            ptr5 = ptr5->field_18;
                                                                                        } while (ptr5->field_18);
                                                                                        ptr21->field_20 = ptr23->field_20;
                                                                                    }
                                                                                }
                                                                                ptr14 = *((long long *)&ptr[4].field_10);
                                                                                if (ptr14)
                                                                                {
                                                                                    ptr24 = p->field_b0;
                                                                                    if (ptr24)
                                                                                    {
                                                                                        v16 = ptr24->field_10;
                                                                                        ptr14->field_10 = v16;
                                                                                        if (v16)
                                                                                        {
                                                                                            ptr6 = ptr14;
                                                                                            do
                                                                                            {
                                                                                                ptr6->field_10 = 1;
                                                                                                ptr6 = ptr6->field_18;
                                                                                            } while (ptr6->field_18);
                                                                                            ptr14->field_20 = (int)ptr24->field_20;
                                                                                        }
                                                                                    }
                                                                                    ptr15 = *((long long *)&ptr[4].padding_11[7]);
                                                                                    if (ptr15)
                                                                                    {
                                                                                        ptr25 = p->field_b8;
                                                                                        if (ptr25)
                                                                                        {
                                                                                            v21 = ptr25->field_10;
                                                                                            ptr15->field_10 = v21;
                                                                                            if (v21)
                                                                                            {
                                                                                                ptr8 = ptr15;
                                                                                                do
                                                                                                {
                                                                                                    ptr8->field_10 = 1;
                                                                                                    ptr8 = ptr8->field_18;
                                                                                                } while (ptr8->field_18);
                                                                                                ptr15->field_20 = ptr25->field_20;
                                                                                            }
                                                                                        }
                                                                                        ptr16 = ptr[4].field_20;
                                                                                        if (ptr16)
                                                                                        {
                                                                                            ptr26 = p->field_c0;
                                                                                            if (ptr26)
                                                                                            {
                                                                                                v26 = ptr26->field_10;
                                                                                                ptr16->field_10 = v26;
                                                                                                if (v26)
                                                                                                {
                                                                                                    ptr9 = ptr16;
                                                                                                    do
                                                                                                    {
                                                                                                        ptr9->field_10 = 1;
                                                                                                        ptr9 = ptr9->field_18;
                                                                                                    } while (ptr9->field_18);
                                                                                                    ptr16->field_20 = ptr26->field_20;
                                                                                                }
                                                                                            }
                                                                                            ptr17 = *((long long *)&ptr[5].padding_0[0]);
                                                                                            if (ptr17)
                                                                                            {
                                                                                                ptr27 = p->field_c8;
                                                                                                if (ptr27)
                                                                                                {
                                                                                                    v31 = ptr27->field_10;
                                                                                                    ptr17->field_10 = v31;
                                                                                                    if (v31)
                                                                                                    {
                                                                                                        ptr10 = ptr17;
                                                                                                        do
                                                                                                        {
                                                                                                            ptr10->field_10 = 1;
                                                                                                            ptr10 = ptr10->field_18;
                                                                                                        } while (ptr10->field_18);
                                                                                                        ptr17->field_20 = ptr27->field_20;
                                                                                                    }
                                                                                                }
                                                                                                ptr18 = *((long long *)&ptr[5].padding_0[8]);
                                                                                                if (ptr18)
                                                                                                {
                                                                                                    ptr28 = p->field_d0;
                                                                                                    if (ptr28)
                                                                                                    {
                                                                                                        v36 = ptr28->field_10;
                                                                                                        ptr18->field_10 = v36;
                                                                                                        if (v36)
                                                                                                        {
                                                                                                            ptr11 = ptr18;
                                                                                                            do
                                                                                                            {
                                                                                                                ptr11->field_10 = 1;
                                                                                                                ptr11 = ptr11->field_18;
                                                                                                            } while (ptr11->field_18);
                                                                                                            ptr18->field_20 = ptr28->field_20;
                                                                                                        }
                                                                                                    }
                                                                                                    ptr19 = *((long long *)&ptr[5].field_10);
                                                                                                    if (ptr19)
                                                                                                    {
                                                                                                        ptr29 = p->field_d8;
                                                                                                        if (ptr29)
                                                                                                        {
                                                                                                            v41 = ptr29->field_10;
                                                                                                            ptr19->field_10 = v41;
                                                                                                            if (v41)
                                                                                                            {
                                                                                                                ptr12 = ptr19;
                                                                                                                do
                                                                                                                {
                                                                                                                    ptr12->field_10 = 1;
                                                                                                                    ptr12 = ptr12->field_18;
                                                                                                                } while (ptr12->field_18);
                                                                                                                ptr19->field_20 = ptr29->field_20;
                                                                                                            }
                                                                                                        }
                                                                                                        addr = *((long long *)&ptr[5].padding_11[7]);
                                                                                                        if (addr)
                                                                                                        {
                                                                                                            if (p->field_e0)
                                                                                                            {
                                                                                                                v45 = p->field_e0->field_10;
                                                                                                                addr->field_10 = v45;
                                                                                                                if (v45)
                                                                                                                {
                                                                                                                    do
                                                                                                                    {
                                                                                                                        addr->field_10 = 1;
                                                                                                                        addr = addr->field_18;
                                                                                                                    } while (addr->field_18);
                                                                                                                }
                                                                                                            }
                                                                                                            ptr3 = ptr[5].field_20;
                                                                                                            if (ptr3)
                                                                                                            {
                                                                                                                if (p->field_e8)
                                                                                                                {
                                                                                                                    v48 = p->field_e8->field_10;
                                                                                                                    ptr3->field_10 = v48;
                                                                                                                    if (v48)
                                                                                                                    {
                                                                                                                        do
                                                                                                                        {
                                                                                                                            ptr3->field_10 = 1;
                                                                                                                            ptr3 = ptr3->field_18;
                                                                                                                        } while (ptr3->field_18);
                                                                                                                    }
                                                                                                                }
                                                                                                                ptr4 = *((long long *)&ptr[6].padding_0[0]);
                                                                                                                if (ptr4)
                                                                                                                {
                                                                                                                    if (p->field_f0)
                                                                                                                    {
                                                                                                                        v51 = p->field_f0->field_10;
                                                                                                                        ptr4->field_10 = v51;
                                                                                                                        if (v51)
                                                                                                                        {
                                                                                                                            do
                                                                                                                            {
                                                                                                                                ptr4->field_10 = 1;
                                                                                                                                ptr4 = ptr4->field_18;
                                                                                                                            } while (ptr4->field_18);
                                                                                                                        }
                                                                                                                    }
                                                                                                                    if (*((long long *)&ptr[6].padding_0[8]))
                                                                                                                    {
                                                                                                                        JoystickStateBinding__CopyFrom(*((long long *)&ptr[6].padding_0[8]), p->field_f8, 0, a3);
                                                                                                                        if (*((long long *)&ptr[6].field_10))
                                                                                                                        {
                                                                                                                            v53 = JoystickStateBinding__CopyFrom(*((long long *)&ptr[6].field_10), p->field_100, 0, a3);
                                                                                                                            return JoystickStateBinding__CopyFrom(*((long long *)&ptr[6].field_10), p->field_100, 0, a3);
                                                                                                                        }
                                                                                                                    }
                                                                                                                }
                                                                                                            }
                                                                                                        }
                                                                                                    }
                                                                                                }
                                                                                            }
                                                                                        }
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    sub_f7db74();
}
```

## `TouchGestureStateBinding.SyncTouchState` — RVA `0xc5f448`

- Decompiled symbol: `TouchGestureStateBinding_SyncTouchState`
- Metadata signature: `public void SyncTouchState(TouchGestureState screenState, TouchGestureState orientedState, JoystickState swipeJoyState, InputRig rig) { }`
- Native interval: `1784` bytes
- Result: `assembly-fallback`
- Note: RuntimeError: Decompiler produced no C-like text

```c
// 0x105f448: sub sp, sp, #0x80
// 0x105f44c: str d12, [sp, #0x10]
// 0x105f450: stp d11, d10, [sp, #0x18]
// 0x105f454: stp d9, d8, [sp, #0x28]
// 0x105f458: str x30, [sp, #0x38]
// 0x105f45c: stp x26, x25, [sp, #0x40]
// 0x105f460: stp x24, x23, [sp, #0x50]
// 0x105f464: stp x22, x21, [sp, #0x60]
// 0x105f468: stp x20, x19, [sp, #0x70]
// 0x105f46c: adrp x24, #0x1fab000
// 0x105f470: ldrb w8, [x24, #0x2dd]
// 0x105f474: mov x19, x4
// 0x105f478: mov x22, x3
// 0x105f47c: mov x23, x2
// 0x105f480: mov x20, x1
// 0x105f484: mov x21, x0
// 0x105f488: tbnz w8, #0, #0x105f4a0
// 0x105f48c: adrp x0, #0x1e8c000
// 0x105f490: ldr x0, [x0, #0xd8]
// 0x105f494: bl #0xf7d92c
// 0x105f498: mov w8, #1
// 0x105f49c: strb w8, [x24, #0x2dd]
// 0x105f4a0: cbz x20, #0x105f4d8
// 0x105f4a4: ldrb w8, [x21, #0x10]
// 0x105f4a8: cbz w8, #0x105f4d8
// 0x105f4ac: adrp x8, #0x1e8c000
// 0x105f4b0: ldr x8, [x8, #0xd8]
// 0x105f4b4: ldr x0, [x8]
// 0x105f4b8: ldr w8, [x0, #0xe0]
// 0x105f4bc: cbnz w8, #0x105f4c4
// 0x105f4c0: bl #0xf7da5c
// 0x105f4c4: mov x0, x19
// 0x105f4c8: mov x1, xzr
// 0x105f4cc: mov x2, xzr
// 0x105f4d0: bl #0x1b9568c
// 0x105f4d4: tbz w0, #0, #0x105f500
// 0x105f4d8: ldp x20, x19, [sp, #0x70]
// 0x105f4dc: ldp x22, x21, [sp, #0x60]
// 0x105f4e0: ldp x24, x23, [sp, #0x50]
// 0x105f4e4: ldp x26, x25, [sp, #0x40]
// 0x105f4e8: ldr x30, [sp, #0x38]
// 0x105f4ec: ldp d9, d8, [sp, #0x28]
// 0x105f4f0: ldp d11, d10, [sp, #0x18]
// 0x105f4f4: ldr d12, [sp, #0x10]
// 0x105f4f8: add sp, sp, #0x80
// 0x105f4fc: ret
// 0x105f500: ldrb w8, [x20, #0x127]
// 0x105f504: cmp x23, #0
// 0x105f508: csel x24, x20, x23, eq
// 0x105f50c: cbz w8, #0x105f598
// 0x105f510: ldr w8, [x20, #0x134]
// 0x105f514: cmp w8, #1
// 0x105f518: b.ne #0x105f55c
// 0x105f51c: ldr x0, [x21, #0x38]
// 0x105f520: cbz x0, #0x105fb3c
// 0x105f524: mov w1, #1
// 0x105f528: mov x2, x19
// 0x105f52c: mov w3, wzr
// 0x105f530: mov x4, xzr
// 0x105f534: bl #0x104f00c
// 0x105f538: ldr x0, [x21, #0xb8]
// 0x105f53c: cbz x0, #0x105fb3c
// 0x105f540: ldr s1, [x20, #0x130]
// 0x105f544: ldr s0, [x20, #0x12c]
// 0x105f548: mov x1, x19
// 0x105f54c: bl #0x105e3a8
// 0x105f550: ldrb w8, [x20, #0x127]
// 0x105f554: cbz w8, #0x105f598
// 0x105f558: ldr w8, [x20, #0x134]
// 0x105f55c: cmp w8, #2
// 0x105f560: b.ne #0x105f598
// 0x105f564: ldr x0, [x21, #0x40]
// 0x105f568: cbz x0, #0x105fb3c
// 0x105f56c: mov w1, #1
// 0x105f570: mov x2, x19
// 0x105f574: mov w3, wzr
// 0x105f578: mov x4, xzr
// 0x105f57c: bl #0x104f00c
// 0x105f580: ldr x0, [x21, #0xc0]
// 0x105f584: cbz x0, #0x105fb3c
// 0x105f588: ldr s1, [x20, #0x130]
// 0x105f58c: ldr s0, [x20, #0x12c]
// 0x105f590: mov x1, x19
// 0x105f594: bl #0x105e3a8
// 0x105f598: ldrb w8, [x20, #0x128]
// 0x105f59c: cbz w8, #0x105f5d4
// 0x105f5a0: ldr x0, [x21, #0x48]
// 0x105f5a4: cbz x0, #0x105fb3c
// 0x105f5a8: mov w1, #1
// 0x105f5ac: mov x2, x19
// 0x105f5b0: mov w3, wzr
// 0x105f5b4: mov x4, xzr
// 0x105f5b8: bl #0x104f00c
// 0x105f5bc: ldr x0, [x21, #0xc8]
// 0x105f5c0: cbz x0, #0x105fb3c
// 0x105f5c4: ldr s1, [x20, #0x130]
// 0x105f5c8: ldr s0, [x20, #0x12c]
// 0x105f5cc: mov x1, x19
// 0x105f5d0: bl #0x105e3a8
// 0x105f5d4: ldrb w8, [x24, #0x106]
// 0x105f5d8: cbz w8, #0x105f5e8
// 0x105f5dc: ldr x0, [x21, #0x58]
// 0x105f5e0: cbnz x0, #0x105f5f8
// 0x105f5e4: b #0x105fb3c
// 0x105f5e8: ldrb w8, [x24, #0x104]
// 0x105f5ec: cbz w8, #0x105f608
// 0x105f5f0: ldr x0, [x21, #0x50]
// 0x105f5f4: cbz x0, #0x105fb3c
// 0x105f5f8: ldr x1, [x24, #0x138]
// 0x105f5fc: mov x2, x19
// 0x105f600: mov x3, xzr
// 0x105f604: bl #0x105cfa0
// 0x105f608: ldrb w8, [x24, #0x1c]
// 0x105f60c: cbz w8, #0x105fad8
// 0x105f610: ldr x0, [x21, #0x20]
// 0x105f614: cbz x0, #0x105fb3c
// 0x105f618: mov w1, #1
// 0x105f61c: mov x2, x19
// 0x105f620: mov w3, wzr
// 0x105f624: mov x4, xzr
// 0x105f628: bl #0x104f00c
// 0x105f62c: ldr x0, [x21, #0xa0]
// 0x105f630: cbz x0, #0x105fb3c
// 0x105f634: ldp s0, s1, [x20, #0x44]
// 0x105f638: mov x1, x19
// 0x105f63c: bl #0x105e3a8
// 0x105f640: ldrb w8, [x20, #0x104]
// 0x105f644: cbz w8, #0x105f678
// 0x105f648: ldr x0, [x21, #0x28]
// 0x105f64c: cbz x0, #0x105fb3c
// 0x105f650: mov w1, #1
// 0x105f654: mov x2, x19
// 0x105f658: mov w3, wzr
// 0x105f65c: mov x4, xzr
// 0x105f660: bl #0x104f00c
// 0x105f664: ldr x0, [x21, #0xa8]
// 0x105f668: cbz x0, #0x105fb3c
// 0x105f66c: ldp s0, s1, [x20, #0x44]
// 0x105f670: mov x1, x19
// 0x105f674: bl #0x105e3a8
// 0x105f678: ldrb w8, [x20, #0x106]
// 0x105f67c: cbz w8, #0x105f6b0
// 0x105f680: ldr x0, [x21, #0x30]
// 0x105f684: cbz x0, #0x105fb3c
// 0x105f688: mov w1, #1
// 0x105f68c: mov x2, x19
// 0x105f690: mov w3, wzr
// 0x105f694: mov x4, xzr
// 0x105f698: bl #0x104f00c
// 0x105f69c: ldr x0, [x21, #0xb0]
// 0x105f6a0: cbz x0, #0x105fb3c
// 0x105f6a4: ldp s0, s1, [x20, #0x44]
// 0x105f6a8: mov x1, x19
// 0x105f6ac: bl #0x105e3a8
// 0x105f6b0: ldp s0, s1, [x24, #0xd8]
// 0x105f6b4: ldp s2, s3, [x24, #0xe0]
// 0x105f6b8: ldp s4, s5, [x24, #0xe8]
// 0x105f6bc: ldp s6, s7, [x24, #0xf0]
// 0x105f6c0: ldrb w8, [x24, #0x106]
// 0x105f6c4: fsub s9, s0, s2
// 0x105f6c8: fsub s8, s1, s3
// 0x105f6cc: fsub s12, s4, s6
// 0x105f6d0: fsub s11, s5, s7
// 0x105f6d4: cbz w8, #0x105f744
// 0x105f6d8: adrp x25, #0x1fab000
// 0x105f6dc: ldrb w8, [x25, #0x242]
// 0x105f6e0: ldr x23, [x21, #0x90]
// 0x105f6e4: cbnz w8, #0x105f6fc
// 0x105f6e8: adrp x0, #0x1e8c000
// 0x105f6ec: ldr x0, [x0, #0xa60]
// 0x105f6f0: bl #0xf7d92c
// 0x105f6f4: mov w8, #1
// 0x105f6f8: strb w8, [x25, #0x242]
// 0x105f6fc: adrp x26, #0x1e8c000
// 0x105f700: ldr x26, [x26, #0xa60]
// 0x105f704: ldr x0, [x26]
// 0x105f708: ldr w8, [x0, #0xe0]
// 0x105f70c: cbnz w8, #0x105f714
// 0x105f710: bl #0xf7da5c
// 0x105f714: fcvt d10, s12
// 0x105f718: add x0, sp, #8
// 0x105f71c: mov v0.16b, v10.16b
// 0x105f720: bl #0x1db0c60
// 0x105f724: fcmp s12, #0.0
// 0x105f728: b.ge #0x105f7b8
// 0x105f72c: fmov d1, #-0.50000000
// 0x105f730: fcmp d0, d1
// 0x105f734: b.ne #0x105f7e0
// 0x105f738: ldr d0, [sp, #8]
// 0x105f73c: fmov d1, #-1.00000000
// 0x105f740: b #0x105f7cc
// 0x105f744: ldrb w8, [x24, #0x104]
// 0x105f748: cbz w8, #0x105fad8
// 0x105f74c: adrp x25, #0x1fab000
// 0x105f750: ldrb w8, [x25, #0x242]
// 0x105f754: ldr x23, [x21, #0x80]
// 0x105f758: cbnz w8, #0x105f770
// 0x105f75c: adrp x0, #0x1e8c000
// 0x105f760: ldr x0, [x0, #0xa60]
// 0x105f764: bl #0xf7d92c
// 0x105f768: mov w8, #1
// 0x105f76c: strb w8, [x25, #0x242]
// 0x105f770: adrp x26, #0x1e8c000
// 0x105f774: ldr x26, [x26, #0xa60]
// 0x105f778: ldr x0, [x26]
// 0x105f77c: ldr w8, [x0, #0xe0]
// 0x105f780: cbnz w8, #0x105f788
// 0x105f784: bl #0xf7da5c
// 0x105f788: fcvt d10, s12
// 0x105f78c: add x0, sp, #8
// 0x105f790: mov v0.16b, v10.16b
// 0x105f794: bl #0x1db0c60
// 0x105f798: fcmp s12, #0.0
// 0x105f79c: b.ge #0x105f7ec
// 0x105f7a0: fmov d1, #-0.50000000
// 0x105f7a4: fcmp d0, d1
// 0x105f7a8: b.ne #0x105f96c
// 0x105f7ac: ldr d0, [sp, #8]
// 0x105f7b0: fmov d1, #-1.00000000
// 0x105f7b4: b #0x105f800
// 0x105f7b8: fmov d1, #0.50000000
// 0x105f7bc: fcmp d0, d1
// 0x105f7c0: b.ne #0x105f814
// 0x105f7c4: ldr d0, [sp, #8]
// 0x105f7c8: fmov d1, #1.00000000
// 0x105f7cc: fcvtzs x8, d0
// 0x105f7d0: fadd d1, d0, d1
// 0x105f7d4: tst x8, #1
// 0x105f7d8: fcsel d0, d0, d1, eq
// 0x105f7dc: b #0x105f81c
// 0x105f7e0: fadd d0, d10, d1
// 0x105f7e4: frintp d0, d0
// 0x105f7e8: b #0x105f81c
// 0x105f7ec: fmov d1, #0.50000000
// 0x105f7f0: fcmp d0, d1
// 0x105f7f4: b.ne #0x105f978
// 0x105f7f8: ldr d0, [sp, #8]
// 0x105f7fc: fmov d1, #1.00000000
// 0x105f800: fcvtzs x8, d0
// 0x105f804: fadd d1, d0, d1
// 0x105f808: tst x8, #1
// 0x105f80c: fcsel d0, d0, d1, eq
// 0x105f810: b #0x105f980
// 0x105f814: fadd d0, d10, d1
// 0x105f818: frintm d0, d0
// 0x105f81c: cbz x23, #0x105fb3c
// 0x105f820: mov x8, #0x7ff0000000000000
// 0x105f824: fmov d1, x8
// 0x105f828: fcvtzs w9, d0
// 0x105f82c: fcmp d0, d1
// 0x105f830: mov w8, #-0x80000000
// 0x105f834: csel w1, w8, w9, eq
// 0x105f838: mov x0, x23
// 0x105f83c: mov x2, x19
// 0x105f840: bl #0x105e7e8
// 0x105f844: ldrb w8, [x25, #0x242]
// 0x105f848: ldr x23, [x21, #0x98]
// 0x105f84c: cbnz w8, #0x105f864
// 0x105f850: adrp x0, #0x1e8c000
// 0x105f854: ldr x0, [x0, #0xa60]
// 0x105f858: bl #0xf7d92c
// 0x105f85c: mov w8, #1
// 0x105f860: strb w8, [x25, #0x242]
// 0x105f864: ldr x0, [x26]
// 0x105f868: ldr w8, [x0, #0xe0]
// 0x105f86c: cbnz w8, #0x105f874
// 0x105f870: bl #0xf7da5c
// 0x105f874: fcvt d10, s11
// 0x105f878: add x0, sp, #8
// 0x105f87c: mov v0.16b, v10.16b
// 0x105f880: bl #0x1db0c60
// 0x105f884: fcmp s11, #0.0
// 0x105f888: b.ge #0x105f8a4
// 0x105f88c: fmov d1, #-0.50000000
// 0x105f890: fcmp d0, d1
// 0x105f894: b.ne #0x105f8cc
// 0x105f898: ldr d0, [sp, #8]
// 0x105f89c: fmov d1, #-1.00000000
// 0x105f8a0: b #0x105f8b8
// 0x105f8a4: fmov d1, #0.50000000
// 0x105f8a8: fcmp d0, d1
// 0x105f8ac: b.ne #0x105f8d8
// 0x105f8b0: ldr d0, [sp, #8]
// 0x105f8b4: fmov d1, #1.00000000
// 0x105f8b8: fcvtzs x8, d0
// 0x105f8bc: fadd d1, d0, d1
// 0x105f8c0: tst x8, #1
// 0x105f8c4: fcsel d0, d0, d1, eq
// 0x105f8c8: b #0x105f8e0
// 0x105f8cc: fadd d0, d10, d1
// 0x105f8d0: frintp d0, d0
// 0x105f8d4: b #0x105f8e0
// 0x105f8d8: fadd d0, d10, d1
// 0x105f8dc: frintm d0, d0
// 0x105f8e0: cbz x23, #0x105fb3c
// 0x105f8e4: mov x8, #0x7ff0000000000000
// 0x105f8e8: fmov d1, x8
// 0x105f8ec: fcvtzs w9, d0
// 0x105f8f0: fcmp d0, d1
// 0x105f8f4: mov w8, #-0x80000000
// 0x105f8f8: csel w1, w8, w9, eq
// 0x105f8fc: mov x0, x23
// 0x105f900: mov x2, x19
// 0x105f904: bl #0x105e7e8
// 0x105f908: ldrb w8, [x20, #0x120]
// 0x105f90c: cbz w8, #0x105f95c
// 0x105f910: ldr x0, [x21, #0xd8]
// 0x105f914: cbz x0, #0x105fb3c
// 0x105f918: ldp s0, s1, [x20, #0x44]
// 0x105f91c: mov x1, x19
// 0x105f920: bl #0x105e3a8
// 0x105f924: ldr x0, [x21, #0x70]
// 0x105f928: cbz x0, #0x105fb3c
// 0x105f92c: mov w1, #3
// 0x105f930: mov v0.16b, v9.16b
// 0x105f934: mov x2, x19
// 0x105f938: mov x3, xzr
// 0x105f93c: bl #0x104f160
// 0x105f940: ldr x0, [x21, #0x78]
// 0x105f944: cbz x0, #0x105fb3c
// 0x105f948: mov w1, #3
// 0x105f94c: mov v0.16b, v8.16b
// 0x105f950: mov x2, x19
// 0x105f954: mov x3, xzr
// 0x105f958: bl #0x104f160
// 0x105f95c: cbz x22, #0x105fad8
// 0x105f960: ldr x0, [x21, #0x100]
// 0x105f964: cbnz x0, #0x105facc
// 0x105f968: b #0x105fb3c
// 0x105f96c: fadd d0, d10, d1
// 0x105f970: frintp d0, d0
// 0x105f974: b #0x105f980
// 0x105f978: fadd d0, d10, d1
// 0x105f97c: frintm d0, d0
// 0x105f980: cbz x23, #0x105fb3c
// 0x105f984: mov x8, #0x7ff0000000000000
// 0x105f988: fmov d1, x8
// 0x105f98c: fcvtzs w9, d0
// 0x105f990: fcmp d0, d1
// 0x105f994: mov w8, #-0x80000000
// 0x105f998: csel w1, w8, w9, eq
// 0x105f99c: mov x0, x23
// 0x105f9a0: mov x2, x19
// 0x105f9a4: bl #0x105e7e8
// 0x105f9a8: ldrb w8, [x25, #0x242]
// 0x105f9ac: ldr x23, [x21, #0x88]
// 0x105f9b0: cbnz w8, #0x105f9c8
// 0x105f9b4: adrp x0, #0x1e8c000
// 0x105f9b8: ldr x0, [x0, #0xa60]
// 0x105f9bc: bl #0xf7d92c
// 0x105f9c0: mov w8, #1
// 0x105f9c4: strb w8, [x25, #0x242]
// 0x105f9c8: ldr x0, [x26]
// 0x105f9cc: ldr w8, [x0, #0xe0]
// 0x105f9d0: cbnz w8, #0x105f9d8
// 0x105f9d4: bl #0xf7da5c
// 0x105f9d8: fcvt d10, s11
// 0x105f9dc: add x0, sp, #8
// 0x105f9e0: mov v0.16b, v10.16b
// 0x105f9e4: bl #0x1db0c60
// 0x105f9e8: fcmp s11, #0.0
// 0x105f9ec: b.ge #0x105fa08
// 0x105f9f0: fmov d1, #-0.50000000
// 0x105f9f4: fcmp d0, d1
// 0x105f9f8: b.ne #0x105fa30
// 0x105f9fc: ldr d0, [sp, #8]
// 0x105fa00: fmov d1, #-1.00000000
// 0x105fa04: b #0x105fa1c
// 0x105fa08: fmov d1, #0.50000000
// 0x105fa0c: fcmp d0, d1
// 0x105fa10: b.ne #0x105fa3c
// 0x105fa14: ldr d0, [sp, #8]
// 0x105fa18: fmov d1, #1.00000000
// 0x105fa1c: fcvtzs x8, d0
// 0x105fa20: fadd d1, d0, d1
// 0x105fa24: tst x8, #1
// 0x105fa28: fcsel d0, d0, d1, eq
// 0x105fa2c: b #0x105fa44
// 0x105fa30: fadd d0, d10, d1
// 0x105fa34: frintp d0, d0
// 0x105fa38: b #0x105fa44
// 0x105fa3c: fadd d0, d10, d1
// 0x105fa40: frintm d0, d0
// 0x105fa44: cbz x23, #0x105fb3c
// 0x105fa48: mov x8, #0x7ff0000000000000
// 0x105fa4c: fmov d1, x8
// 0x105fa50: fcvtzs w9, d0
// 0x105fa54: fcmp d0, d1
// 0x105fa58: mov w8, #-0x80000000
// 0x105fa5c: csel w1, w8, w9, eq
// 0x105fa60: mov x0, x23
// 0x105fa64: mov x2, x19
// 0x105fa68: bl #0x105e7e8
// 0x105fa6c: ldrb w8, [x20, #0x120]
// 0x105fa70: cbz w8, #0x105fac0
// 0x105fa74: ldr x0, [x21, #0xd0]
// 0x105fa78: cbz x0, #0x105fb3c
// 0x105fa7c: ldp s0, s1, [x20, #0x44]
// 0x105fa80: mov x1, x19
// 0x105fa84: bl #0x105e3a8
// 0x105fa88: ldr x0, [x21, #0x60]
// 0x105fa8c: cbz x0, #0x105fb3c
// 0x105fa90: mov w1, #3
// 0x105fa94: mov v0.16b, v9.16b
// 0x105fa98: mov x2, x19
// 0x105fa9c: mov x3, xzr
// 0x105faa0: bl #0x104f160
// 0x105faa4: ldr x0, [x21, #0x68]
// 0x105faa8: cbz x0, #0x105fb3c
// 0x105faac: mov w1, #3
// 0x105fab0: mov v0.16b, v8.16b
// 0x105fab4: mov x2, x19
// 0x105fab8: mov x3, xzr
// 0x105fabc: bl #0x104f160
// 0x105fac0: cbz x22, #0x105fad8
// 0x105fac4: ldr x0, [x21, #0xf8]
// 0x105fac8: cbz x0, #0x105fb3c
// 0x105facc: mov x1, x22
// 0x105fad0: mov x2, x19
// 0x105fad4: bl #0x105dffc
// 0x105fad8: ldr x0, [x21, #0xe0]
// 0x105fadc: cbz x0, #0x105fb3c
// 0x105fae0: mov x1, x20
// 0x105fae4: mov x2, x19
// 0x105fae8: bl #0x105d5b4
// 0x105faec: ldrb w8, [x24, #0x106]
// 0x105faf0: cbz w8, #0x105fb2c
// 0x105faf4: ldr x0, [x21, #0xf0]
// 0x105faf8: cbz x0, #0x105fb3c
// 0x105fafc: mov x1, x20
// 0x105fb00: mov x2, x19
// 0x105fb04: ldp x20, x19, [sp, #0x70]
// 0x105fb08: ldp x22, x21, [sp, #0x60]
// 0x105fb0c: ldp x24, x23, [sp, #0x50]
// 0x105fb10: ldp x26, x25, [sp, #0x40]
// 0x105fb14: ldr x30, [sp, #0x38]
// 0x105fb18: ldp d9, d8, [sp, #0x28]
// 0x105fb1c: ldp d11, d10, [sp, #0x18]
// 0x105fb20: ldr d12, [sp, #0x10]
// 0x105fb24: add sp, sp, #0x80
// 0x105fb28: b #0x105d5b4
// 0x105fb2c: ldrb w8, [x24, #0x104]
// 0x105fb30: cbz w8, #0x105f4d8
// 0x105fb34: ldr x0, [x21, #0xe8]
// 0x105fb38: cbnz x0, #0x105fafc
// 0x105fb3c: bl #0xf7db74
```

## `TouchGestureStateBinding.OnIsBoundToAxis` — RVA `0xc5fb80`

- Decompiled symbol: `TouchGestureStateBinding_OnIsBoundToAxis`
- Metadata signature: `protected override bool OnIsBoundToAxis(string axisName, InputRig rig) { }`
- Native interval: `980` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    struct struct_3 *field_20;
} struct_2;

typedef struct struct_0 {
    char padding_0[488];
    struct struct_1 *field_1e8;
    unsigned long long field_1f0;
} struct_0;

typedef struct struct_3 {
    struct struct_0 *field_0;
} struct_3;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

unsigned int TouchGestureStateBinding_OnIsBoundToAxis(struct_2 *ptr, unsigned long a1, unsigned long a2)
{
    struct_0 **v0;  // x0
    unsigned long long v1;  // x3

    if (!ptr->field_10)
        return 0;
    v0 = ptr->field_20;
    if (!ptr->field_20)
        sub_f7db74(0);
    v1 = ptr->field_20->field_0->field_1f0;
    ptr->field_20->field_0->field_1e8();
}
```

## `TouchGestureStateBinding.OnIsBoundToKey` — RVA `0xc5ff54`

- Decompiled symbol: `TouchGestureStateBinding_OnIsBoundToKey`
- Metadata signature: `protected override bool OnIsBoundToKey(KeyCode keyCode, InputRig rig) { }`
- Native interval: `628` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[16];
    char field_10;
    char padding_11[15];
    struct struct_3 *field_20;
} struct_2;

typedef struct struct_0 {
    char padding_0[472];
    struct struct_1 *field_1d8;
    unsigned long long field_1e0;
} struct_0;

typedef struct struct_3 {
    struct struct_0 *field_0;
} struct_3;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

unsigned int TouchGestureStateBinding_OnIsBoundToKey(struct_2 *ptr, unsigned long a1, unsigned long a2)
{
    struct_0 **v0;  // x0
    unsigned long long v1;  // x3

    if (!ptr->field_10)
        return 0;
    v0 = ptr->field_20;
    if (!ptr->field_20)
        sub_f7db74(0);
    v1 = ptr->field_20->field_0->field_1e0;
    ptr->field_20->field_0->field_1d8();
}
```

## `TouchGestureStateBinding.OnIsEmulatingMousePosition` — RVA `0xc601c8`

- Decompiled symbol: `TouchGestureStateBinding_OnIsEmulatingMousePosition`
- Metadata signature: `protected override bool OnIsEmulatingMousePosition() { }`
- Native interval: `388` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[160];
    struct struct_3 *field_a0;
} struct_2;

typedef struct struct_0 {
    char padding_0[520];
    struct struct_1 *field_208;
    unsigned long long field_210;
} struct_0;

typedef struct struct_3 {
    struct struct_0 *field_0;
} struct_3;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

void TouchGestureStateBinding_OnIsEmulatingMousePosition(struct_2 *ptr)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    struct_0 **v4;  // x0
    unsigned long long v5;  // x1
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr->field_a0;
    if (!ptr->field_a0)
        sub_f7db74(0);
    v5 = ptr->field_a0->field_0->field_210;
    ptr->field_a0->field_0->field_208();
}
```

## `TouchGestureStateBinding.OnIsEmulatingTouches` — RVA `0xc6034c`

- Decompiled symbol: `TouchGestureStateBinding_OnIsEmulatingTouches`
- Metadata signature: `protected override bool OnIsEmulatingTouches() { }`
- Native interval: `336` bytes
- Result: `pseudocode`

```c
typedef struct struct_2 {
    char padding_0[160];
    struct struct_3 *field_a0;
} struct_2;

typedef struct struct_0 {
    char padding_0[504];
    struct struct_1 *field_1f8;
    unsigned long long field_200;
} struct_0;

typedef struct struct_3 {
    struct struct_0 *field_0;
} struct_3;

typedef struct struct_1 {
    unsigned long long field_0;
} struct_1;

void TouchGestureStateBinding_OnIsEmulatingTouches(struct_2 *ptr, unsigned long a1, unsigned long a2, unsigned long a3)
{
    unsigned long long v2;  // x30
    unsigned long long v3;  // x19
    struct_0 **v4;  // x0
    unsigned long long v5;  // x1
    unsigned long long v0;  // [bp-0x10]
    unsigned long long v1;  // [bp-0x8]

    v0 = v2;
    v1 = v3;
    v4 = ptr->field_a0;
    if (!ptr->field_a0)
        sub_f7db74(0);
    v5 = ptr->field_a0->field_0->field_200;
    ptr->field_a0->field_0->field_1f8();
}
```

## `TouchGestureStateBinding.OnGetSubBindingDescriptions` — RVA `0xc6049c`

- Decompiled symbol: `TouchGestureStateBinding_OnGetSubBindingDescriptions`
- Metadata signature: `protected override void OnGetSubBindingDescriptions(BindingDescriptionList descList, Object undoObject, string parentMenuPath) { }`
- Native interval: `1340` bytes
- Result: `pseudocode`
- Heuristic layout hint: `TouchGestureStateBinding_Recovered` matched 2 offsets against `TouchGestureStateBinding` metadata (confidence 0.67).

```c
typedef struct struct_12 {
    char padding_0[16];
    unsigned long long field_10;
    unsigned int field_18;
    unsigned int field_1c;
    char padding_20[8];
    unsigned int field_28;
    char padding_2c[12];
    struct TouchGestureStateBinding_Recovered *field_38;
} struct_12;

typedef struct struct_0 {
    char padding_0[32];
    struct struct_7 **field_20;
} struct_0;

typedef struct TouchGestureStateBinding_Recovered {
    char padding_0[24];
    struct struct_11 *field_18;
    char padding_20[8];
    unsigned long long normalPressBinding;
    char padding_30[16];
    unsigned long long doubleTapBinding;
} TouchGestureStateBinding_Recovered;

typedef struct struct_11 {
    unsigned long long field_0;
} struct_11;

extern long long g_1f09b80;
extern long long g_1f09b88;
extern long long g_1f09df0;
extern long long g_1f09df8;
extern long long g_1f0ab20;
extern long long g_1f0ab28;
extern long long g_1f0ab30;
extern long long g_1f0ab38;
extern long long g_1f0be40;
extern long long g_1f0be48;
extern long long g_1f0be50;
extern long long g_1f0be58;
extern long long g_1f0c770;
extern long long g_1f0d048;
extern long long g_1f0d050;
extern long long g_1f0d298;
extern long long g_1f0de38;
extern long long g_1f0de40;
extern long long g_1f0de48;
extern long long g_1f0de50;
extern long long g_1f0de58;
extern long long g_1f0de60;
extern long long g_1f0e0d8;
extern long long g_1f0e0e0;
extern long long g_1f0f9a0;
extern long long g_1f0f9a8;
extern long long g_1f0f9b0;
extern long long g_1f0f9b8;
extern char g_1fab2de;

void TouchGestureStateBinding_OnGetSubBindingDescriptions(struct_0 *a0, struct_12 *a1, unsigned int a2, long long a3)
{
    unsigned long long v13;  // x30
    unsigned long long v14;  // x28
    unsigned long long v23;  // x19
    unsigned long long v15;  // x27
    unsigned long long v16;  // x26
    unsigned long long v17;  // x25
    unsigned long long v18;  // x24
    unsigned long long v19;  // x23
    unsigned long long v20;  // x22
    unsigned long long v21;  // x21
    unsigned long long v22;  // x20
    char *v0;  // [bp-0x60]
    unsigned long long v1;  // [bp-0x58]
    unsigned long long v2;  // [bp-0x50]
    unsigned long long v3;  // [bp-0x48]
    unsigned long long v4;  // [bp-0x40]
    unsigned long long v5;  // [bp-0x38]
    unsigned long long v6;  // [bp-0x30]
    unsigned long long v7;  // [bp-0x28]
    unsigned long long v8;  // [bp-0x20]
    unsigned long long v9;  // [bp-0x18]
    unsigned long long v10;  // [bp-0x10]
    unsigned long long v11;  // [bp-0x8]
    char v12;  // [bp+0x0]

    v0 = &v12;
    v1 = v13;
    v2 = v14;
    v3 = v15;
    v4 = v16;
    v5 = v17;
    v6 = v18;
    v7 = v19;
    v8 = v20;
    v9 = v21;
    v10 = v22;
    v11 = v23;
    if (!(g_1fab2de & 1))
    {
        sub_f7d92c(&g_1f09df0);
        sub_f7d92c(&g_1f0ab20);
        sub_f7d92c(&g_1f0ab30);
        sub_f7d92c(&g_1f0f9b8);
        sub_f7d92c(&g_1f0de38);
        sub_f7d92c(&g_1f0be50);
        sub_f7d92c(&g_1f0d298);
        sub_f7d92c(&g_1f0be40);
        sub_f7d92c(&g_1f0c770);
        sub_f7d92c(&g_1f0be58);
        sub_f7d92c(&g_1f0d048);
        sub_f7d92c(&g_1f0de40);
        sub_f7d92c(&g_1f0f9a0);
        sub_f7d92c(&g_1f0de48);
        sub_f7d92c(&g_1f0d050);
        sub_f7d92c(&g_1f0e0e0);
        sub_f7d92c(&g_1f0f9b0);
        sub_f7d92c(&g_1f0e0d8);
        sub_f7d92c(&g_1f09df8);
        sub_f7d92c(&g_1f0f9a8);
        sub_f7d92c(&g_1f0ab38);
        sub_f7d92c(&g_1f0de58);
        sub_f7d92c(&g_1f0be48);
        sub_f7d92c(&g_1f0de50);
        sub_f7d92c(&g_1f09b80);
        sub_f7d92c(&g_1f09b88);
        sub_f7d92c(&g_1f0ab28);
        sub_f7d92c(&g_1f0de60);
        g_1fab2de = 1;
    }
    if (a1)
        BindingDescriptionList__Add(a1, a0->field_20, g_1f0d050, a3, a2); /* do not return */
    sub_f7db74();
}
```
