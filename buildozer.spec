[app]
title = Kolan Mobile
package.name = kolan
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Оставляем стабильные версии библиотек
requirements = python3,kivy==2.3.0,https://github.com/kivymd/KivyMD/archive/master.zip,pillow

orientation = portrait
fullscreen = 1
android.archs = armeabi-v7a, arm64-v8a
android.allow_backup = True

# ЖЕСТКО ФИКСИРУЕМ ВЕРСИИ ДЛЯ GOOGLE (это решит проблему с NDK 27)
android.api = 34
android.minapi = 24
android.ndk = 26b
android.ndk_api = 24

[buildozer]
log_level = 2
warn_on_root = 1
