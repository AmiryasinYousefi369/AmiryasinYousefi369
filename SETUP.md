# راهنمای راه‌اندازی پروژه‌ی پروفایل گیت‌هاب

این پروژه شامل ۴ بخشه:
```
├── README.md                          ← فایلی که توی پروفایلت نمایش داده می‌شه
├── assets/
│   ├── contrib-heatmap.svg            ← گراف مشارکت (هر روز خودکار آپدیت می‌شه)
│   ├── wordmark.svg                   ← اسم AMIRYASIN به‌صورت ASCII سبز
│   └── verbose-card.svg               ← کارت اطلاعات (whoami --verbose)
├── scripts/
│   ├── generate_heatmap.py            ← گراف مشارکت رو از روی داده‌ی واقعی گیت‌هاب می‌سازه
│   ├── generate_wordmark.py           ← وردمارک رو می‌سازه
│   └── generate_info_card.py          ← کارت whoami --verbose رو می‌سازه
└── .github/workflows/update-profile.yml   ← Action که هر روز heatmap رو تازه می‌کنه
```

## مرحله ۱: ساخت ریپو
1. یه ریپوی Public جدید بساز با اسم **دقیقاً** `AmiryasinYousefi369`.
2. تمام فایل‌ها و پوشه‌های همین پروژه (از جمله پوشه‌ی مخفی `.github`) رو توی ریپو آپلود کن — ساختار پوشه‌ها باید عیناً همین باشه.

> ⚠️ پوشه‌ی `.github` با نقطه شروع می‌شه و ممکنه توی بعضی فایل‌منیجرها مخفی باشه؛ مطمئن شو که آپلودش می‌کنی.

## مرحله ۲: فعال کردن دسترسی نوشتن برای Action
چون Action قراره خودش commit بزنه، باید بهش اجازه بدی:
1. برو به ریپو → **Settings** → **Actions** → **General**
2. پایین صفحه، بخش **Workflow permissions** رو پیدا کن
3. گزینه‌ی **"Read and write permissions"** رو انتخاب و Save کن

## مرحله ۳: اجرای اولین بار Action
1. برو به تب **Actions** توی ریپو
2. روی workflow به اسم **"Update profile assets"** کلیک کن
3. دکمه‌ی **"Run workflow"** رو بزن تا همین الان heatmap واقعیت ساخته بشه (به‌جای منتظر موندن تا نیمه‌شب)

## مرحله ۴: شخصی‌سازی محتوا
### الف) لینک لینکدین
توی `README.md` دنبال این خط بگرد و لینک واقعیت رو جایگزین کن:
```
https://www.linkedin.com/in/REPLACE-WITH-YOUR-LINKEDIN-USERNAME
```

### ب) متن‌های Now / Prev / Stack / Highlights
فایل `scripts/generate_info_card.py` رو باز کن، بالای فایل یه دیکشنری به اسم `FIELDS` هست:
```python
FIELDS = [
    ("Now:", "..."),
    ("Prev:", "..."),
    ("Stack:", "..."),
    ("Highlights:", "..."),
    ("Learning:", "Full-Stack Development"),
    ("Reach:", "shop.ario-co.ir - tonystarkicu1@gmail.com"),
]
```
متن هر خط رو با متن واقعی خودت عوض کن، بعد این دستور رو (روی سیستم خودت یا توی Codespace گیت‌هاب) اجرا کن:
```bash
python3 scripts/generate_info_card.py
```
این کار فایل `assets/verbose-card.svg` رو بازسازی می‌کنه؛ فایل جدید رو commit و push کن.

### پ) اضافه کردن پرتره‌ی ASCII (اختیاری)
این نسخه پرتره نداره چون عکس شخصی نفرستادی. هر وقت یه عکس واقعی از خودت داشتی، بفرست تا برات یه اسکریپت `generate_portrait.py` هم اضافه کنم که عکس رو به ASCII رنگی مثل پروفایل نمونه تبدیل کنه.

## نکات
- گراف مشارکت از یه API عمومی و رایگان (`github-contributions-api.jogruber.de`) داده‌ی واقعی گیت‌هابت رو می‌خونه؛ نیازی به توکن یا رمز نیست.
- اگه اسم ریپوی اسکریپت‌ها رو عوض کنی یا جابه‌جاشون کنی، مسیرها توی workflow و README رو هم باید هماهنگ کنی.
- رنگ سبز همه‌جا از کد `#39FF14` استفاده شده؛ اگه بخوای عوضش کنی، همین کد رنگ رو توی سه فایل اسکریپت پیدا و جایگزین کن.
