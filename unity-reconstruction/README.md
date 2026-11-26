# Rage of Fight — Unity reconstruction project

این پوشه یک پروژهٔ Unity جدا از پروتوتایپ Three.js ریشهٔ مخزن است. پروژه از داده‌های APK اصلی استخراج و بازسازی می‌شود و با Unity **2022.3.62f1** تنظیم شده است.

> **محدودیت مهم:** APK با IL2CPP ساخته شده است. فایل‌های APK داده‌های بازی، نام کلاس‌ها، صحنه‌ها و دارایی‌ها را حفظ می‌کنند، اما سورس اصلی C# و پروژهٔ دقیق Unity را تضمین نمی‌کنند. این پوشه یک بازسازی قابل‌ویرایش از داده‌های در دسترس است؛ سورس اصلی یا نسخهٔ کامل/آزموده‌شدهٔ بازی نیست. اکنون شبه‌کد native برای بررسی در `Assets/Recovered/NativePseudocode/` نگهداری می‌شود، اما آن خروجی‌ها سورس اصلی یا کامپوننت‌های C# قابل‌اجرا نیستند و رفتار gameplay هنوز بازسازی نشده است.

## ساخت صحنه‌ها در Unity

1. Unity Hub را باز کن و **همین پوشهٔ `unity-reconstruction`** را با Unity `2022.3.62f1` باز کن.
2. پس از پایان Import و نصب UGUI، از منو انتخاب کن:
   **Tools → Rage of Fight → Prepare assets and rebuild scenes**
3. ابزار Editor مش‌های OBJ فشرده را باز می‌کند، دارایی‌ها و متریال‌های پایه را وارد می‌کند و چهار صحنهٔ بازسازی‌شده را می‌سازد:
   - `Assets/Scenes/00 - Splash.unity`
   - `Assets/Scenes/01 - MainMenu.unity`
   - `Assets/Scenes/02 - GamePlay.unity`
   - `Assets/Scenes/03 - Z-GamePlay.unity`
4. پس از بازسازی، از **Tools → Rage of Fight → Validate rebuilt skinning** استفاده کن. این بررسی صحنه‌های ذخیره‌شده را باز می‌کند، تطابق رأس‌ها/ویژگی‌ها، submeshها، وزن‌ها و bind poseهای Meshهای native با آرشیو منبع را می‌سنجد و اتصال boneها و تعداد rendererهای بازسازی‌شده را کنترل می‌کند؛ تغییر یا ذخیره‌ای در صحنه‌ها ایجاد نمی‌کند.
5. برای اجرای صحنه‌ها، آن‌ها را در Build Settings فعال کن؛ ابزار بازسازی این فهرست را هم در صورت موفقیت تنظیم می‌کند.
6. برای بازسازی جداگانهٔ UI prefabهای استخراج‌شده، از **Tools → Rage of Fight → Rebuild shared UI prefabs only** استفاده کن؛ خروجی در `Assets/Recovered/Prefabs/` قرار می‌گیرد.

ساخت صحنه‌ها ممکن است چند دقیقه طول بکشد: دو صحنهٔ بازی ده‌ها هزار GameObject دارند. Builder، hierarchy و transformها، مدل‌های static و ۷۱۴ مش weighted را به‌صورت `SkinnedMeshRenderer` با boneهای محلی و bind poseهای متناظر می‌سازد؛ متریال‌های پایه، رنگ و fill mode تصویرهای UI، فونت، رنگ و اندازه/سبک/تراز متن، حالت transition و ColorBlock/navigation دکمه‌ها، Canvas/CanvasScaler/CanvasGroup، تنظیمات sorting/shadow rendererها، دوربین‌ها و نورها را هم بازسازی می‌کند؛ همچنین colliderها، rigidbodyها و CharacterJointهای پایه را می‌سازد. دو نمونهٔ `Tube` به‌دلیل نبود bone weight قابل‌بازیابی عمداً به‌صورت static fallback ساخته می‌شوند. اگر فایل‌های صدا (WAV/MP3) با یکی از گزینه‌های صوتی زیر استخراج شده باشند، Builder آن‌ها را به AudioSourceهای متناظر وصل می‌کند؛ کلیپ‌هایی که عمداً از export حذف شده‌اند بدون clip می‌مانند. همچنین سه ریشهٔ UI prefab باقی‌مانده در `sharedassets2.assets` (خارج از چهار scene اصلی) را با تمام ۷ GameObject درخت، چهار Image، دو Text، یک Button، دو افکت Shadow/Outline و اسپرایت‌هایشان به prefabهای قابل‌ویرایش تبدیل می‌کند. وضعیت بصری و navigation هر ۲۸۹ Button ثبت و توسط Builder اعمال می‌شود. هر ۵۵۱ persistent onClick call نیز با target، method، mode، argument و call state استخراج شده است؛ Builder تعداد ۱۲۳ فراخوانی استاندارد `AudioSource.Play` و ۶۳ فراخوانی `GameObject.SetActive` را دوباره متصل می‌کند. ۳۶۵ handler باقی‌مانده به اسکریپت‌های IL2CPP اصلی وابسته‌اند و فقط به‌صورت metadata حفظ می‌شوند. NavMeshAgentها به‌صورت غیرفعال وارد می‌شوند چون NavMesh این پروژه هنوز bake نشده است. دادهٔ رمزگشایی‌شدهٔ muscle clip، stateهای AnimatorController و skeleton/human mappingهای Avatar اکنون در manifestهای فشرده نگه‌داری می‌شوند، اما هنوز به AnimationClip یا AnimatorController قابل‌اجرا تبدیل نشده‌اند. منطق اختصاصی eventهای دکمه‌ها، تبلیغات، networking و رفتار AI هم بازسازی نشده‌اند؛ GameObjectهای دارای اسکریپت اصلی با نام و metadata در manifest ثبت می‌شوند، ولی کد IL2CPP آن‌ها به کامپوننت C# قابل‌اجرا تبدیل نشده است.

> **روش بازسازی skinning:** OBJ به‌تنهایی نگاشت قابل‌اعتماد vertex-index به weight را تضمین نمی‌کند؛ واردکننده می‌تواند vertexها را به‌خاطر seamهای UV/normal تکثیر یا مرتب کند. برای جلوگیری از اتصال اشتباه weightها، extractor نسخهٔ ۲ آرشیو `mesh-skin-data.json.gz` علاوه بر bind poseها و چهار influence هر vertex، vertex/normal/tangent/UV، submesh و triangle index اصلی Mesh را در همان ترتیب Unity ذخیره می‌کند. Builder از این داده‌ها Mesh assetهای بومی می‌سازد، `BoneWeight[]` و `bindposes` را روی همان vertexها می‌گذارد و `m_Bones`/`rootBone` را با ترتیب PPtrهای همان scene وصل می‌کند. Validator آفلاین تطابق `boneCount` با bind poseها، weight indexهای فعال با boneهای محلی و طول/دامنهٔ تمام streamهای geometry را بررسی می‌کند. پس از ساخت در Editor، فرمان **Validate rebuilt skinning** محتوای Meshهای native را دوباره با آرشیو نسخهٔ ۲ مقایسه می‌کند و rigهای صحنهٔ ذخیره‌شده را می‌سنجد. ۲۵ مش weighted شامل ۷۹٬۳۹۰ vertex، ۹۰۲ bind pose و ۱۰۴٬۸۶۲ مثلث‌اند؛ `Tube` یک bind poseٔ اضافه ولی هیچ weight قابل‌استفاده‌ای ندارد، پس شمار کل bind poseهای index مش‌ها ۹۰۳ است. ۱۲٬۸۷۳ weight چهارمِ فشرده‌شده که UnityPy 1.25.4 اشتباه محاسبه می‌کند با باقیماندهٔ نرمال‌شده اصلاح شده‌اند. **Validator آفلاین PASS می‌دهد، اما Unity Editor در این محیط در دسترس نیست؛ بنابراین compile، شکل‌دهیِ دیداری هنگام چرخش bone و ظاهر meshها پس از ساخت هنوز باید در Unity 2022.3.62f1 نهایی بررسی شوند.**

## داده‌های واردشده

- `Assets/Recovered/Compressed/mesh-exports.zip` — مش‌های OBJ فشرده؛ ابزار Editor آن‌ها را برای Unity باز می‌کند. یک mesh ارجاع‌شده با نام `power_line` در دادهٔ APK خالی/غیرقابل‌صدور است، پس عمداً جایگزین حدسی ندارد و validator همین یک هشدار را گزارش می‌کند.
- `Assets/Recovered/Manifests/mesh-skin-data.json.gz` — آرشیو نسخهٔ ۲ شامل bind pose، four-influence bone weights و geometry فلت/vertex-aligned برای ۲۵ مش weighted؛ Builder آن‌ها را به Mesh asset بومی با `boneWeights`، `bindposes`، submeshها و کانال‌های vertex تبدیل می‌کند. Validator ساختار ماتریس‌ها، تعداد vertex/indexها، وزن‌ها و سازگاری bone PPtrهای scene با bind poseهای فعال را کنترل می‌کند.
- `Assets/Recovered/Textures/` — تکسچرهای مورد استفادهٔ متریال‌های صحنه‌ها.
- `Assets/Recovered/Sprites/` — اسپرایت‌های استفاده‌شده در صحنه‌های بازی و رابط کاربری.
- `Assets/Recovered/Manifests/scene-data.json.gz` — hierarchy و transformها، component/script names، SpriteRenderer/renderer و bone/rootBone PPtrهای `SkinnedMeshRenderer`، UGUI image/text/Button style، navigation و persistent onClick call metadata، Shadow/Outline effect data، CanvasScaler/Canvas/CanvasGroup، Camera/Light و داده‌های پایهٔ physics.
- `Assets/Recovered/Manifests/ui-prefabs.json` — سه ریشهٔ سلسله‌مراتبی UI prefab که در shared assets خارج از صحنه‌ها ذخیره شده‌اند.
- `Assets/Recovered/Manifests/fonts.json` و `Assets/Recovered/Fonts/` — هر چهار فونت TTF/OTF تعبیه‌شده در APK؛ ۵۵۰ ارجاع Text حل شده‌اند: ۵۴۸ به `BebasNeue-Regular` و یکی‌یکی به `Purista Light` و `LegacyRuntime`. فونت `TAHOMABD` هم استخراج شده ولی در Textهای صحنه/Prefab ارجاع نشده است.
- `Assets/Recovered/Manifests/materials.json` — نام Shader و مقادیر سادهٔ متریال‌ها؛ Shaderهای اصلی بازی به Shader استاندارد Unity نگاشت می‌شوند.
- `Assets/Recovered/Manifests/audio-index.json` — نام، مدت، مشخصات، فرمت و وضعیت export برای ۱۵۱ AudioClip؛ snapshot فعلی همهٔ فایل‌ها را دارد: ۱۴۹ WAV و ۲ MP3 اصلی (حدود ۱۶٫۷ MiB) در `Assets/Recovered/Audio/` که Builder به AudioSourceهای متناظر وصل می‌کند.
- `Assets/Recovered/Manifests/animation-index.json` — فهرست ۱۷۷ AnimationClip با زمان شروع/پایان استخراج‌شده از `m_MuscleClip`، منحنی‌های streamed/dense، تعداد نمونه‌ها، bindingها و eventها. در snapshot فعلی: ۵٬۰۶۴ streamed curves، ۷۷۹٬۹۶۱ streamed words، ۲٬۷۲۵ dense curves، ۱۲٬۴۲۲ dense frames، ۲۱۲٬۳۲۷ dense values، ۷٬۷۰۶ constant values و ۱۱٬۶۰۶ generic bindings.
- `Assets/Recovered/Manifests/animation-curve-data.json.gz` — دادهٔ رمزگشایی‌شدهٔ muscle clip، binding constant و eventها برای بازرسی و اعتبارسنجی؛ این‌ها هنوز به AnimationClip قابل‌اجرا در Unity تبدیل نشده‌اند.
- `Assets/Recovered/Manifests/animator-controller-index.json` و `avatar-index.json` — metadata فهرست‌شدهٔ ۵۶ controller (۲۵۰ state، ۲۲۵ transition record و ۲۲۷ blend tree) و ۲۰ Avatar (۱٬۱۰۵ skeleton node، ۴۷۸ human mapping و ۱٬۱۰۵ transform-name entry).
- `Assets/Recovered/Manifests/animator-controller-data.json.gz` و `avatar-data.json.gz` — typetreeهای کامل رمزگشایی‌شدهٔ controller و Avatar؛ این‌ها آرشیوهای بازرسی‌اند، نه فایل‌های Unity قابل‌اجرا یا بازسازی rig کامل.
- `Assets/Recovered/Manifests/il2cpp-script-metadata.json` و `il2cpp-script-metadata.md` — نمایهٔ metadata باینری IL2CPP برای ۸۲ نوع اسکریپت متصل به صحنه‌ها و UI prefabها: ۲٬۳۴۹ اعلان فیلد و ۱٬۱۳۵ امضای متد. این‌ها کد C# نیستند؛ بدنه‌های خالی `dump.cs` فقط placeholder هستند.
- `Assets/Recovered/NativePseudocode/README.md` — راهنمای خروجی مهندسی معکوس: شبه‌کد native برای ۳٬۵۰۱ RVA در دو اسمبلی برنامه (۳٬۱۳۷ `exact` و ۳۶۴ `partial` از دید ترجمهٔ دستورها) و خروجی angr برای همهٔ همان ۳٬۵۰۱ RVA (۳٬۳۸۴ C-like و ۱۱۷ اسمبلی fallback). این فایل‌ها سورس C# اصلی، کد قابل‌کامپایل یا اثبات رفتار نیستند؛ محدودیت‌ها، هش‌های ورودی و لینک فایل‌های هر نوع در همان پوشه مستند شده‌اند.
- `Assets/Recovered/Manifests/extraction-report.md` — آمار و هشدارهای استخراج.
- `Assets/Branding/rage-of-fight-icon.png` — کپی بدون تغییر از آیکن تأییدشدهٔ موجود در workspace.

## استخراج مجدد از APK

نیازمندی: Python 3.10+ و pip.

```bash
python -m pip install -r Tools/requirements.txt
python Tools/extract_from_apk.py /path/to/original.apk
```

برای بررسی آفلاین سازگاری manifestها و ارجاع assetها، تطابق AnimationClipهای فهرست‌شده با داده‌های `m_MuscleClip`، اتصال Animator/Avatar/Animation به فهرست‌هایشان، سلامت فایل‌های WAV و فریم‌های MP3 (شامل تعداد نمونه/مدت در برابر manifest) و سلامت آرشیو OBJ، بدون نیاز به Unity:

```bash
python Tools/validate_reconstruction.py
```

این بررسی، کامپایل یا اجرای Builder در Unity را جایگزین نمی‌کند. ورودی extractor می‌تواند APK، خروجی APKTool یا مسیر `assets/bin/Data` باشد. داده‌های split Unity به‌صورت خودکار به هم پیوسته می‌شوند. برای خروجی WAV سبک‌تر (کلیپ‌های حداکثر ۲ MiB؛ مناسب افکت‌های صدا که Builder به AudioSourceها وصل می‌کند):

```bash
python Tools/extract_from_apk.py /path/to/original.apk --include-audio-sfx
```

برای همهٔ ۱۵۱ AudioClip از `--include-audio` استفاده کن. دو track بلندِ موسیقی/voice در APK داخل FSB5 با فریم‌های MP3 اصلی ذخیره شده‌اند؛ extractor آن‌ها را بدون decode یا رمزگذاریِ دوباره به MP3 بازمی‌گرداند و بایت‌های صفرِ padding برای هم‌ترازی چهاربایتی FSB5 میان فریم‌ها را حذف می‌کند. این اصلاح برای `MilitaryVoice` ضروری است: ۳٬۳۵۵ فریم MPEG-1 Layer III با ۱٬۱۵۲ نمونه در هر فریم، ۳٬۸۶۴٬۹۶۰ نمونه و مدت ۸۷٫۶۴۰۸۱۶ ثانیه را بازسازی می‌کنند و اکنون با metadata منبع و خوانش Mutagen تطابق دارد. دو MP3 در مجموع حدود ۱٫۱ MiB هستند و بقیهٔ کلیپ‌ها WAV صادر می‌شوند. در نتیجه حالت کامل ۱۵۱ فایل (۱۴۹ WAV و ۲ MP3) می‌دهد و هر ۴۶ ارجاع AudioSource صحنه‌ها فایل خواهد داشت، بدون افزایش حدود ۶۵ MiB ناشی از WAVهای PCM طولانی. در حالت سبک `--include-audio-sfx`، این دو track عمداً حذف می‌شوند و ۴۱ از ۴۶ ارجاع صحنه فایل خواهند داشت.

### نمایه‌سازی metadata اسکریپت‌های IL2CPP (مرحلهٔ جداگانه)

APK شامل `global-metadata.dat` (metadata نسخهٔ IL2CPP 31) و `libil2cpp.so` برای ARM64 است. برای تولید دوبارهٔ این نمایه، از [Il2CppDumper-Python](https://github.com/springmusk026/Il2CppDumper-Python) استفاده کن و سپس ابزار فهرست‌سازی محلی را اجرا کن؛ فایل APK و `dump.cs` حجیم را داخل پروژه قرار نده:

```bash
git clone https://github.com/springmusk026/Il2CppDumper-Python.git /tmp/Il2CppDumper-Python
git -C /tmp/Il2CppDumper-Python checkout 126b6c9db3c9f67649f5c4645cada55763f0a0e1
unzip -p /path/to/original.apk 'lib/arm64-v8a/libil2cpp.so' > /tmp/libil2cpp.so
unzip -p /path/to/original.apk 'assets/bin/Data/Managed/Metadata/global-metadata.dat' > /tmp/global-metadata.dat
PYTHONPATH=/tmp/Il2CppDumper-Python python -m il2cpp_dumper_py /tmp/libil2cpp.so /tmp/global-metadata.dat /tmp/il2cpp-dump
python Tools/extract_il2cpp_script_metadata.py /tmp/il2cpp-dump/dump.cs --metadata-version 31.0
```

در آخرین اجرای extractor → فهرست‌ساز IL2CPP → validator، هر ۸۲ نوعِ مورد استفادهٔ صحنه‌ها و UI prefabها، ۲٬۳۴۹ اعلان فیلد و ۱٬۱۳۵ امضای method فهرست شدند؛ validator نتیجهٔ `PASS` داد. حل `MonoBehaviour.m_Script` اکنون PPtr را از فایل asset خود component dereference می‌کند، از جمله ارجاع به asset خارجی؛ استخراج کامل و تطبیق مجدد این مسیر را آزمودند. از ۳۶۵ فراخوانی MonoBehaviour، نام نوع و method برای ۳۴۴ مورد تطبیق دارد. ۲۱ مورد عمداً حل‌نشده می‌ماند: ۱۵ callback روی GameObject با نام `IAP_Manager` دارای `m_Script` تهی‌اند؛ ۶ callback هم به methodهای `scrollrec` (دو بار)، `Withoutscrollrec` (دو بار)، `GrenadekitButt` و `HealthKitButt` در `MainMenuController` اشاره می‌کنند که در metadata موجود نیستند. حل نام، overload درست یا رفتار زمان اجرا را ثابت نمی‌کند. `dump.cs` بدنهٔ methodها را ندارد؛ بنابراین منطق gameplay از این راه بازیابی نشده است.

این پروژه assetها و manifestها را بازتولید می‌کند و دو نوع شبه‌کد native را فقط برای بازرسی نگه می‌دارد؛ **سورس اصلی C# و کامپوننت‌های رفتاری قابل‌اجرای بازیابی نشده‌اند**. فایل‌های حجیم و فایل‌های ساخته‌شده در Editor برای جلوگیری از دادهٔ تکراری در `.gitignore` قرار دارند؛ ابزارها و manifestهای بازسازی در همین پروژه نگه داشته شده‌اند.
