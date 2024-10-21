# Snapchat detection on Android

Information was gathered from version `13.12.0.37`

## [\__system_property_get](https://android.googlesource.com/platform/bionic/+/466dbe4/libc/include/sys/system_properties.h)

* `persist.nox.gps.status`
* `ARGH`
* `init.svc.genyd`
* `ro.genymotion.version`
* `ro.build.user`
* `ro.build.description`
* `androVM.inited`
* `init.svc.vbox64-setup`

`ro.build.user` & `ro.build.description` are both checked to see if the value is `genymotion`

`service.adb.root` is checked to see if the value is `1`

## [Sockets](https://developer.android.com/reference/java/net/Socket#bind(java.net.SocketAddress))

Attempts to bind to the following

* `minitouch`
* `STFService`
* `stfagent`
* `stfservice`

## [Open](https://man7.org/linux/man-pages/man2/open.2.html)

Attempts to open the following

* `/data/user_de/0/de.robv.android.xposed.installer/conf/modules.list`
* `/data/user/0/de.robv.android.xposed.installer/conf/modules.list`
* `/data/data/de.robv.android.xposed.installer/conf/modules.list`

If this succeeds it'll check if they contain the following

  * `snapprefs`
  * `snaptools`
  * `interceptmod`
  * `snapintercept`

## [Read](https://man7.org/linux/man-pages/man2/read.2.html)

* `/proc/bus/input/devices` checks for `BlueStacks`, `nox_gpio` & `VirtualBox`
* `/dev/__properties__/u:object_r:default_prop:s0` checks for `init.svc.magisk`
* `/proc/self/mounts` checks for `magisk` & `/sbin/.core`
* `/proc/bus/pci/devices` checks for `bstinput`
* `/proc/self/status` checks for `TracerPid: 0`
* `/proc/mounts` checks for `supersu`

## [Fstatat64](https://man7.org/linux/man-pages/man2/fstatat64.2.html)

### Xposed Modules
  * `/data/data/com.ljmu.andre.snaptools`
  * `/data/user/0/com.ljmu.andre.snaptools`
  * `/data/user_de/0/com.ljmu.andre.snaptools`
  * `/data/data/local.interceptmod`
  * `/data/user/0/local.interceptmod`
  * `/data/user_de/0/local.interceptmod`
  * `/data/data/local.snapintercept`
  * `/data/user/0/local.snapintercept`
  * `/data/user_de/0/local.snapintercept`
  * `/data/data/com.marz.snapprefs`
  * `/data/user/0/com.marz.snapprefs`
  * `/data/user_de/0/com.marz.snapprefs`

### Xposed
  * `/xposed.prop`
  * `/system/bin/app_process.orig`
  * `/system/lib/libxposed_art.so`
  * `/system/lib64/libxposed_art.so`
  * `/system/bin/app_process32_xposed`
  * `/system/bin/app_process64_xposed`
  * `/data/data/de.robv.android.xposed.installer`
  * `/data/user/0/de.robv.android.xposed.installer`
  * `/data/user_de/0/de.robv.android.xposed.installer`

### Magisk
  * `/data/data/com.topjohnwu.magisk`
  * `/data/user/0/com.topjohnwu.magisk`
  * `/data/user_de/0/com.topjohnwu.magisk`
  * `/sbin/magisk`
  * `/sbin/magiskhide`
  * `/init.magisk.rc`
  * `/dev/magisk/bin/busybox`
  * `/system/addon.d/99-magisk.sh`
  * `/data/user/0/magisk.db`
  * `/data/user_de/0/magisk.db`
  * `/root/magisk`
  * `/magisk`
  * `/sbin_orig`
  * `/data/magisk`
  * `/sbin/.core`

### Superuser
  * `/system/app/Superuser.apk`
  * `/system/app/Superuser/Superuser.apk`
  * `/init.supersu.rc`
  * `/system/.supersu`
  * `/data/.supersu`
  * `/dev/block/supersu/su`
  * `/sbin/daemonsu`
  * `/dev/__properties__/u:object_r:supersu_prop:s0`
  * `/data/data/eu.chainfire.supersu`
  * `/data/user/0/eu.chainfire.supersu`
  * `/data/user_de/0/eu.chainfire.supersu`
  * `/data/data/eu.chainfire.suhide`
  * `/data/user/0/eu.chainfire.suhide`
  * `/data/user_de/0/eu.chainfire.suhide`
  * `/sbin/su`
  * `/system/bin/su`
  * `/system/xbin/su`
  * `/system/xbin/nu`
  * `/data/local/xbin/su`
  * `/data/local/bin/su`
  * `/system/sd/xbin/su`
  * `/system/bin/failsafe/su`
  * `/data/local/su`
  * `/su/bin/su`
  * `/su`
  * `/nu`

### TitaniumBackup
  * `/data/data/com.keramidas.TitaniumBackup`
  * `/data/user/0/com.keramidas.TitaniumBackup`
  * `/data/user_de/0/com.keramidas.TitaniumBackup`

### NoxPlayer
  * `/fstab.nox`
  * `/system/bin/noxd`
  * `/ueventd.nox.rc`
  * `/system/bin/noxscreen`
  * `/etc/init.nox.sh`

### Genymotion
  * `/dev/socket/genyd`
  * `/dev/socket/baseband_genyd`
  * `/data/data/com.genymotion.superuser`
  * `/data/user/0/com.genymotion.superuser`
  * `/data/user_de/0/com.genymotion.superuser`
  * `/system/genymotion`

### YouWave
  * `/data/youwave_id`

### BlueStacks
  * `/boot/bstmods`
  * `/dev/socket/bstfolderd`
  * `/mnt/prebundledapps`

### VirtualBox
  * `/dev/vboxuser`
  * `/sys/module/vboxguest`
  * `/sys/bus/pci/drivers/vboxguest`
  * `/system/bin/androVM-prop`

### Apps
  * `/data/data/com.chelpus.lackypatch`
  * `/data/app-lib/net.snclab.RootKeepSurvival-1`
  * `/data/app-lib/org.projectvoodoo.otarootkeeper-1`
  * `/data/data/com.ramdroid.appquarantinepro`
  * `/data/data/com.noshufou.android.su.elite`
  * `/data/app-lib/sa.root.toolkit-1`
  * `/data/app-lib/com.troy1103.hideyourroot-1`
  * `/data/app-lib/com.formyhm.hideroot-1`

