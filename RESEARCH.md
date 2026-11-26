# یادداشت تحقیق فنی

## 2026-11-25 — Milestone M7: تحویل قابل‌اعتماد APK اندروید از CI

### وضعیت/فرض
کد فعلی پروژه شامل اپ Capacitor، افزونهٔ بومی TCP برای LAN، مجوز `INTERNET` در manifest و workflow ساخت APK دیباگ است. ماشین توسعه JDK، Android SDK و `adb` ندارد؛ بنابراین APK این شاخه باید از GitHub Actions ساخته و artifact آن بررسی شود. Build CI نیز آزمون فیزیکی دو گوشی را جایگزین نمی‌کند.

### منابع و نتیجه
- [Capacitor architecture — Ionic Team](https://github.com/ionic-team/capacitor/blob/main/ARCHITECTURE.md) — افزونه‌های Android با `@CapacitorPlugin` کشف/ثبت می‌شوند و رویداد بومی به JavaScript با `notifyListeners` و `addListener` می‌رسد. این الگو با `LanMultiplayerPlugin`, ثبت آن در `MainActivity` و `LanTransport` پروژه هم‌خوان است؛ تغییر کد بومی در این milestone لازم نیست.
- [actions/setup-java — GitHub](https://github.com/actions/setup-java) — action پشتیبانی‌شده cacheهای Gradle و wrapper را با `cache: gradle` فراهم می‌کند. استفاده از آن برای workflow تکراری Android build، زمان انتظار را کم می‌کند.
- [actions/upload-artifact — GitHub](https://github.com/actions/upload-artifact) — workflow فعلی artifact دیباگ را با عمر ۱۴ روز منتشر می‌کند؛ فایل checksum کنار APK به بررسی صحت دانلود کمک می‌کند.

### تصمیم / استفاده
- workflow شاخهٔ فعال حفظ می‌شود؛ به‌جای نصب SDK خارج از میزبان‌های مجاز و نامطمئن، از runner اندروید موجود استفاده می‌شود.
- Gradle dependency/wrapper cache به setup-java افزوده می‌شود و SHA-256 APK همراه artifact بارگذاری می‌شود.
- هیچ کد، تصویر، مدل، تکسچر، صدا یا هویت بصری بازی دیگر کپی نمی‌شود؛ منابع بالا مستندات/ابزار CI هستند، نه دارایی بازی. مجوز assetهای بازیابی‌شده همچنان مستقل و نامشخص است.

### حقوق و محدودیت
منابع GitHub فقط به‌عنوان مستندات فنی استفاده شدند؛ کدشان در مخزن کپی یا vendored نشده است. APK دیباگ برای QA است، نه انتشار فروشگاهی. QA روی گوشی و LAN واقعی همچنان باید جداگانه ثبت شود.
