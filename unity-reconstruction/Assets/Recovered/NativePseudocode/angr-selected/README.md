# خروجی منتخب اولیه — pseudocode با angr

> **این پوشه خروجی مرحلهٔ قبلی و زیرمجموعهٔ ۶۷۱‌متدی است؛ خروجی کامل‌ترِ هر ۳٬۵۰۱ RVA اکنون در [`../angr-full-app/`](../angr-full-app/README.md) قرار دارد.**
>
> **این فایل‌ها سورس اصلی C# نیستند و پروژهٔ قابل‌کامپایل Unity نمی‌سازند.** بدنه‌ها C-like pseudocode حاصل تحلیل باینری ARM64 هستند. آن‌ها می‌توانند control flow، type، نام call و layout فیلد را اشتباه بازسازی کنند؛ از آن‌ها فقط به‌عنوان راهنمای مهندسی معکوس استفاده کنید.

## آمار

- دامنه: ۶۷۱ RVA یکتا، ۴۷ گروه/type منتخب از `Assembly-CSharp.dll` و `Assembly-CSharp-firstpass.dll`؛ این subset با ۱۹ از ۶۹ نوع برنامه‌ایِ متصل به scene/prefab هم‌پوشانی دارد.
- نتیجهٔ angr: ۶۴۸ بدنهٔ C-like و ۲۳ fallback به اسمبلی دستوربه‌دستور.
- این مجموعه subset خروجی `../il2cpprec-full-assemblies/` است؛ فهرست هر type در [`INDEX.md`](./INDEX.md)، آمار و status هر متد در [`index.json`](./index.json) است.
- مقایسهٔ status RVA با lifter دیگر: ۵۹۳ مورد C-like از ۵۹۵ موردی آمده که ابزار native آن‌ها را `exact` برچسب زده؛ ۵۵ مورد C-like از ۷۶ `partial`؛ ۲ `exact` و ۲۱ `partial` در fallback اسمبلی مانده‌اند. `exact` فقط completeness ترجمهٔ دستور native در آن ابزار را می‌سنجد و **هیچ statusی صحت معنایی را ثابت نمی‌کند**.

## روش و caveatها

خروجی با angr 9.2.213 (CFGFast + Decompiler) روی `libil2cpp.so` تولید شد. محیط اولیه `pycparser 3.12` ناسازگار بود؛ در اجرای موفق، `pycparser 3.0` و یک compatibility shim محلی در adapter angr استفاده شد. نسخهٔ ابزار و جزئیات per-method در `index.json` ثبت شده‌اند؛ خود tool/dependencyها داخل پروژه کپی نشده‌اند.

نام تابع metadata و چند نام field با تطبیق heuristic RVA/offset بازگردانده شده‌اند؛ فیلدهای دیگر به شکل `field_xx` و توابع native به شکل `sub_xxx` می‌مانند. خود angr در برخی روش‌ها هشدار «Store data lifted to a C type with a different size» داد؛ در این موارد خروجی ممکن است مشخصاً نادرست باشد. ۲۳ بدنه‌ای که decompiler C-like نداد یا CFG در RVA هدف function پیدا نکرد، در فایل‌ها با برچسب `assembly-fallback` و علت ثبت‌شده در `index.json` نگه داشته شده‌اند.

هیچ‌کدام از این بدنه‌ها با C# compiler، Unity Editor یا اجرای بازی اعتبارسنجی نشده‌اند. فایل‌های `*.md` در این پوشه گزارش/شبه‌کد هستند، نه سورس قابل‌استفاده در `Assets/` به‌عنوان Script.
