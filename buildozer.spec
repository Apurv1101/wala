[app]

title = Face Recognition App
package.name = faceapp
package.domain = org.kivy
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp3
version = 1.0
requirements = python3,kivy,opencv-contrib-python,requests,pillow
orientation = portrait
fullscreen = 1

android.permissions = CAMERA,INTERNET,RECORD_AUDIO,WAKE_LOCK,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

android.minapi = 21
android.ndk = 25b
android.api = 33
android.sdk = 33
android.ndk_path = 
android.sdk_path = 

android.archs = armeabi-v7a, arm64-v8a

android.gradle_dependencies = 
android.gradle_plugins = 

android.enable_androidx = 1
android.useandroidx = 1

# Prevent crashes on camera/audio by explicitly handling permissions
android.manifest.placeholders = android.permission.CAMERA

# Audio, OpenCV & camera fix
android.meta_data = com.google.firebase.messaging.default_notification_icon=@mipmap/ic_launcher

# Fix for OpenCV modules
android.add_libs_armeabi_v7a = libs/opencv_java4.so
android.add_libs_arm64_v8a = libs/opencv_java4.so

# Use this if you manually bundle OpenCV Java libraries
# android.add_src = path_to_opencv_sdk/java

# Include MP3
presplash.filename = %(source.dir)s/splash.png

# Optional: icon
icon.filename = %(source.dir)s/icon.png

[buildozer]
log_level = 2
warn_on_root = 1
