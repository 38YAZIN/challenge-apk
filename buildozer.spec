[app]
title = MyChallenge
package.name = shadowtest
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy

orientation = portrait
fullscreen = 0

# ترك الإصدارات فارغة ليختار السيرفر الأنسب تلقائياً
android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
