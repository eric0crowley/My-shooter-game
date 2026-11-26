# شبه‌کد Native بازیابی‌شده از APK

> **هیچ‌یک از فایل‌های این درخت سورس اصلی C# یا پروژهٔ قابل‌کامپایل Unity نیست.** بازی با IL2CPP ساخته شده؛ APK شامل کد ماشین ARM64 و metadata است، نه متن C# اولیه، نام متغیرهای محلی، کامنت‌ها یا ساختار دقیق برنامه. این‌ها خروجی‌های مهندسی معکوس‌اند و ممکن است نوع‌ها، جریان کنترل، فراخوانی‌ها یا رفتار را اشتباه بازسازی کنند. آن‌ها را به‌عنوان مرجع برای بازنویسی/بررسی استفاده کنید، نه جایگزین سورس اصلی.

## ورودی و provenance

- APK: `بازی شوتر نمونه.apk`؛ Unity `2022.3.62f1`، معماری `arm64-v8a`، IL2CPP metadata نسخهٔ 31.
- SHA-256 فایل APK: `972a874cdfdf89415f04ab4b62517a96b91df50c5f964f8d000a336c6ab6aa9c` (65,955,104 بایت).
- SHA-256 `libil2cpp.so`: `7e0219d08e799ec959fb1aceda3503d5b342a6df745eab412d79bdf12eff47c3` (28,965,488 بایت).
- SHA-256 `global-metadata.dat`: `c1c4ede19665421f89ff46157a05f5e5c8a0207dee163a7f1c0f271fca1f980e` (5,089,464 بایت).
- خود APK، باینری native، metadata خام و executable ابزار decompiler عمداً در Git قرار نگرفته‌اند. هش‌ها و جزئیات روش در manifestها نگه داشته شده‌اند.

## خروجی‌ها

### ۱) پوشش کامل دو اسمبلی کد برنامه — `il2cpprec-full-assemblies/`

برای **۳٬۵۰۱ RVA یکتای متد** از `Assembly-CSharp.dll` و `Assembly-CSharp-firstpass.dll`، شبه‌کد low-level ساخته شده است:

| اسمبلی | متدها | ترجمهٔ دستورهای native کامل (`exact`) | ناقص (`partial`) |
|---|---:|---:|---:|
| `Assembly-CSharp.dll` | ۱٬۹۲۳ | ۱٬۷۴۱ | ۱۸۲ |
| `Assembly-CSharp-firstpass.dll` | ۱٬۵۷۸ | ۱٬۳۹۶ | ۱۸۲ |
| **جمع** | **۳٬۵۰۱** | **۳٬۱۳۷** | **۳۶۴** |

`exact` فقط یعنی lifter همهٔ دستورهای native آن بدنه را به IR خودش ترجمه کرده؛ **معنای C#، صحت رفتار، کامل‌بودن بدنه یا کامپایل‌پذیری را ثابت نمی‌کند**. ابزار ۲۷۸ متد را `suspect` علامت زده و برای ۳٬۲۰۸ متد در مجموع ۱۰۵٬۳۴۲ دستور unmapped ثبت شده است. صفر خطای file mapping گزارش شده، ولی این هم آزمون معنایی نیست. همهٔ شمارش‌ها و تشخیص‌های per-method در `il2cpprec-full-assemblies/manifest.json` هستند؛ فهرست و فایل‌های هر نوع در `il2cpprec-full-assemblies/INDEX.md` قرار دارند.

بدنه‌ها C# نیستند: پارامترهای ABI مثل `ulong x0…x7`، نام‌هایی مثل `RuntimeMemory`/`RuntimeCalls` و برچسب‌های پرش بازنمایی سطح پایین ابزارند. کد به Unity وارد یا کامپایل/اجرا نشده است. `Assembly-CSharp-firstpass.dll` ممکن است کد plugin یا asset شخص ثالث داشته باشد؛ پیش از استفادهٔ مجدد مجوز هر جزء را جداگانه بررسی کنید.

### ۲) شبه‌کد C-like برای همهٔ RVAهای دو اسمبلی — `angr-full-app/`

پس از حل ناسازگاری `pycparser` و گسترش تحلیل از زیرمجموعه به کل دو اسمبلی، **هر ۳٬۵۰۱ RVA** اکنون یک خروجی دارد: **۳٬۳۸۴ C-like pseudocode** و **۱۱۷ اسمبلی fallback**، در ۴۱۵ فایل گروه/type. فهرست methodها و statusها در `angr-full-app/index.json` و فایل‌های گروه در `angr-full-app/INDEX.md` است. خروجی اولیهٔ ۶۷۱‌متدی در `angr-selected/` برای ثبت مرحلهٔ قبلی نگه داشته شده؛ از آن برای پوشش کامل استفاده نکن.

تطبیق status با lifter native: ۳٬۰۹۵ مورد C-like از ۳٬۱۳۷ مورد `exact` و ۲۸۹ مورد C-like از ۳۶۴ مورد `partial` آمده‌اند؛ ۴۲ fallback از گروه `exact` و ۷۵ fallback از گروه `partial` هستند. این فقط تطبیق RVA و وضعیت ابزارهاست، نه اثبات درستی یا برابری معنایی. از ۱۱۷ fallback، ۹۰ مورد C-like تولید نکردند، ۲۶ مورد در RVA هدف CFG function نداشتند و یک متد (`GetAnimLerpFactor`, RVA `0xc64640`) پس از توقف قبلی decompiler عمداً به اسمبلی fallback شد.

خروجی angr نیز سورس C# نیست: نوع/چیدمان field و نام بعضی callها heuristic است؛ متغیرهای محلی و control flow ممکن است اشتباه باشند. angr در تعدادی از بدنه‌ها هشدار داده که اندازهٔ type تولیدشده با store واقعی فرق دارد. ابزار native-lift نیز ۲۷۸ متد را `suspect` علامت زده است. هیچ‌یک از این فایل‌ها کامپایل یا با اجرای بازی اعتبارسنجی نشده‌اند. Source-pathهایی مثل `Assets/Script/GameController.cs` فقط رشتهٔ path بازیابی‌شده از metadata هستند، نه فایل‌های منبع موجود.

## دامنه و چیزهایی که هنوز بازیابی نشده‌اند

- این دو خروجی **سورس اصلی C# را برنمی‌گردانند**. راه دقیق برای داشتن همان سورس، پیدا کردن repository/backup اصلی یا دریافت سورس از سازنده است؛ تبدیل native code به کد high-level یکتا نیست.
- خروجی کامل فقط دو اسمبلی نام‌برده را پوشش می‌دهد، نه Unity/.NET runtime، همهٔ DLLهای ثالث یا همهٔ متدهای metadata بدون RVA. ۱۳ نوع `UnityEngine.UI.dll` مرتبط با scene/prefab در این batch نیستند. پروژهٔ بازسازی‌شده در `Packages/manifest.json` وابستگی `com.unity.ugui` نسخهٔ `1.0.0` را اعلام می‌کند تا Unity Package Manager کد/assembly رابط را resolve کند؛ این نسخه انتخاب پروژهٔ بازسازی است و تطابق دقیق آن با APK اثبات نشده. کد UGUI زیرساخت Unity است، نه سورس gameplay.
- برای نسخهٔ C#-recovery از `il2cpprec_cli --binary --metadata --output-dir` هم تلاش شد، ولی tool برای metadata نسخهٔ 31 پیام `native source layout is unsupported or provisional` داد؛ گزینهٔ layout نیز با تشخیص raw/precise conflict داشت. بنابراین پروژهٔ C# تولید نشد.
- مستندات Cpp2IL شاخهٔ development آن را WIP و خروجی CIL را فعلاً نامرتب توصیف می‌کنند؛ آخرین release قابل‌مشاهده `2022.0.7` بود. دانلود executable به‌علت محدودیت دسترسی به host فایل release ناموفق ماند و در محیط `dotnet` وجود ندارد. Il2CppDumper برای restore کردن DLLهای metadata مفید است، اما طبق مستندات خودش **کد متدها را برنمی‌گرداند**؛ Il2CppInspector نیز سال‌هاست معلق است. منابع: [Cpp2IL](https://github.com/SamboyCoding/Cpp2IL)، [Il2CppDumper](https://github.com/Perfare/Il2CppDumper)، [Il2CppInspector](https://github.com/djkaty/Il2CppInspector).
- پروژهٔ Unity هنوز به Unity Editor `2022.3.62f1` برای compile، ساخت صحنه‌ها و آزمون دیداری skinning نیاز دارد. Validator آفلاین PASS است، اما کامپایل/اجرای Unity انجام نشده؛ `power_line` صادر نشده و دو `Tube` بدون وزن کامل ایستا می‌مانند. جزئیات در [`unity-reconstruction/README.md`](../../../README.md) و manifestهای `Assets/Recovered/Manifests/` است.

این‌ها بیشترین بازیابی قابل‌اتکایی هستند که از باینری موجود در این محیط تولید شد. هر تلاش بعدی برای decompile باید با سورس اصلی واقعی، شبه‌کد C-like، اسمبلی fallback و محدودیت معنایی جداگانه برچسب بخورد.
