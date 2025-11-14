[app]
title = MyApp
package.name = myapp
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3,kivy

orientation = portrait

[buildozer]
log_level = 2

[android]
api = 33
minapi = 21
ndk = 25b
android.build_tools_version = 33.0.2
android.permissions = INTERNET

[android:entrypoint]
main = main.py

[android:meta-data]
