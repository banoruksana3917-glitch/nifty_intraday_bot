[app]
title = MyApp
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy

[buildozer]
log_level = 2

[android]
api = 33
minapi = 21
android.sdk_path = /home/runner/.buildozer/android/platform/android-sdk
android.build_tools_version = 33.0.2
android.allow_backup = False
