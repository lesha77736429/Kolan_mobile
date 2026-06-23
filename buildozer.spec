[app]
title = Kolan Mobile
package.name = kolan
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Указываем самые свежие версии библиотек напрямую из репозиториев
requirements = python3,kivy==2.3.0,https://github.com/kivymd/KivyMD/archive/master.zip,pillow

orientation = portrait
fullscreen = 1
android.archs = armeabi-v7a, arm64-v8a
android.allow_backup = True
android.api = 33

[buildozer]
log_level = 2
warn_on_root = 1
