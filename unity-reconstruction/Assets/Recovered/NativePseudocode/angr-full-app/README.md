# شبه‌کد C-like angr برای دو اسمبلی برنامه

> **این فایل‌ها سورس اصلی C# نیستند و پروژهٔ Unity قابل‌کامپایل نمی‌سازند.** «C-like» یعنی angr توانسته یک بازنمایی تقریبیِ C تولید کند؛ نام متغیرها، نوع‌ها، layout فیلدها، callها و control flow ممکن است اشتباه باشند. این خروجی برای بررسی دستی/بازنویسی است، نه جایگزین کد اصلی یا اثبات رفتار.

## دامنه و آمار

برای همهٔ **۳٬۵۰۱ RVA یکتای متد** در `Assembly-CSharp.dll` و `Assembly-CSharp-firstpass.dll`، خروجی angr یا C-like است یا fallback اسمبلی:

| نتیجهٔ angr | تعداد |
|---|---:|
| C-like pseudocode | **۳٬۳۸۴** |
| اسمبلی دستوربه‌دستور fallback | **۱۱۷** |
| **جمع RVAهای پوشش‌داده‌شده** | **۳٬۵۰۱** |

این ۳٬۵۰۱ RVA با manifest خروجی native-lift تک‌به‌تک تطبیق داده شدند و هر RVA دقیقاً یک بار در فایل‌های این پوشه وجود دارد. گروه‌بندی در ۴۱۵ فایل type انجام شده است؛ جزئیات هر متد در [`index.json`](./index.json)، فهرست فایل‌ها در [`INDEX.md`](./INDEX.md) و status متنی در [`status.txt`](./status.txt) است.

تطبیق با status ابزار native-lift: ۳٬۰۹۵ متد C-like از ۳٬۱۳۷ متد `exact` و ۲۸۹ متد C-like از ۳۶۴ متد `partial` آمده‌اند. از fallbackها ۴۲ مورد `exact` و ۷۵ مورد `partial` هستند. `exact` فقط کامل‌بودن ترجمهٔ دستورهای native توسط آن lifter را توصیف می‌کند؛ نه صحت معنایی و نه درستی angr را ثابت می‌کند. ابزار native-lift در کل ۲۷۸ متد را `suspect` علامت زده است؛ ۲۲۷ مورد از آن‌ها در این خروجی C-like شده‌اند، ولی همچنان نیازمند بررسی‌اند.

از ۱۱۷ fallback، ۹۰ مورد را decompiler متن C-like نساخت، برای ۲۶ مورد CFG در RVA متد پیدا نشد، و یک متد (`TouchControlSpriteAnimatorBase.GetAnimLerpFactor`, RVA `0xc64640`) پس از توقف طولانی decompiler عمداً به اسمبلی fallback شد. این موارد در `index.json` قابل جست‌وجو هستند.

## روش و محدودیت‌ها

- ابزار: angr 9.2.213 (CFGFast + Decompiler)، با `pycparser 3.0` و compatibility shim محلی برای adapter parser angr؛ ابزار/dependencyها در repository توزیع نشده‌اند.
- اندازهٔ بازهٔ هر متد از manifest native-lift گرفته شد تا فاصلهٔ خالی بین RVAها به‌اشتباه چند مگابایت کد تلقی نشود. metadata و نام‌ها نیز برای برچسب‌گذاری و hintهای field استفاده شدند.
- هنگام کار، angr برای برخی متدها هشدار داد: `Store data lifted to a C type with a different size. Decompilation output will be wrong.` بنابراین حتی متن‌هایی که status آن‌ها `pseudocode` است می‌توانند مشخصاً نادرست باشند. تشخیص `suspect` و خطاهای قابل‌تشخیص در manifest مرجع native-lift هستند؛ نبود هشدار نیز درستی را ثابت نمی‌کند.
- پارامترهای native، `sub_...`ها، globalها و fieldهای `field_xx`/`struct_x` بازنمایی ماشین/heuristic هستند. بعضی fieldها با offset و metadata نام‌گذاری شده‌اند، اما این تطبیق قطعی نیست.
- APK: Unity `2022.3.62f1`, arm64-v8a, metadata 31. هش‌های APK و دو ورودی binary در [`index.json`](./index.json) ثبت شده‌اند؛ فایل اصلی APK و `libil2cpp.so` در repository نیستند.
- خروجی اولیهٔ منتخب ۶۷۱ متدی در `../angr-selected/` نگه داشته شده و داخل همین پوشه با خروجی ۲٬۸۳۰ متد دیگر ادغام شده است؛ آن پوشهٔ قدیمی فقط برای ثبت مرحلهٔ قبلی است و برای پوشش کامل از همین فایل‌ها استفاده کنید.

**هیچ کامپایل C#، build در Unity، اجرای بازی یا آزمون برابری معنایی انجام نشده است.** برای سورس واقعی باید repository/backup اصلی پیدا شود؛ در غیر این صورت، تبدیل این شبه‌کدها به بازی قابل‌اجرا بازنویسی و اعتبارسنجی دستی می‌خواهد.
