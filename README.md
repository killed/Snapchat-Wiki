# Snapchat Wiki

[Contact Me](https://t.me/lololololidk)

[Wiki](https://github.com/killed/Snapchat-Wiki/wiki)

# Android

* Check if your device is flagged/detected with [this](https://github.com/killed/Snapchat-Wiki/releases/tag/v13.12.0.37) apk (`v13.12.0.37`)

<img src="https://i.imgur.com/h1HJuIm.png" height="300"> <img src="https://i.imgur.com/QPS3goP.png" height="300">

* [Native detection](https://github.com/killed/Snapchat-Wiki/blob/master/Android/DETECTION.md)

* Version `12.33*` and below don't use any sensor data

* Versions -

`13.13.0.36` `13.12.0.37` `13.11.0.42` `13.10.0.40` `13.9.0.42` `13.8.0.44` `13.7.0.42` `13.6.0.39` `13.5.0.41` `13.4.0.45` `13.3.0.42` `13.2.0.41` `13.1.0.43` `13.0.0.50` `12.93.0.43` `12.92.0.48 ` `12.91.0.50` `12.90.0.46` `12.89.0.40` `12.88.0.43` `12.87.0.44` `12.86.0.44` `12.85.0.45` `12.84.0.40` `12.83.0.37` `12.82.0.51` `12.81.0.44` `12.80.1.0` `12.79.0.37` `12.78.0.43` `12.77.0.37` `12.76.0.38` `12.75.0.42` `12.74.0.40` `12.73.0.40` `12.72.0.37` `12.71.0.30` `12.70.0.34` `12.69.0.23` `12.68.0.25` `12.67.1.0` `12.65.0.38` `12.64.0.42` `12.63.0.55` `12.62.1.53` `12.61.0.49` `12.60.0.58` `12.58.0.62` `12.57.0.55` `12.56.0.57` `12.55.0.49` `12.54.0.67` `12.53.0.46` `12.52.0.60` `12.51.0.62` `12.50.1.0` `12.49.0.67` `12.48.1.0` `12.47.0.49` `12.46.0.51` `12.45.0.55` `12.44.0.59` `12.43.0.56` `12.42.0.60` `12.41.0.54` `12.40.0.43` `12.39.0.48` `12.38.0.45` `12.37.0.43` `12.36.0.53` `12.35.0.45` `12.34.0.36` `12.33.1.19` `12.32.0.35` `12.31.0.36` `12.30.0.27` `12.29.1.14` `12.28.0.22` `12.27.0.8` `12.26.0.20` `12.25.0.35` `12.24.0.34` `12.23.0.38` `12.22.0.32` `12.21.0.34` `12.20.0.33` `12.19.0.32` `12.18.0.33` `12.17.0.17` `12.16.0.28` `12.15.0.30` `12.14.0.29` `12.13.0.33` `12.12.0.28` `12.11.0.25` `12.10.0.31` `12.09.0.24` `12.08.0.29` `12.07.0.34` `12.06.0.34` `12.05.0.37` `12.04.0.31` `12.03.0.22` `12.02.1.33` `12.01.0.33` `12.00.0.31` `11.96.0.31` `11.95.0.39` `11.94.0.33` `11.93.1.38` `11.92.0.33` `11.91.1.39` `11.90.1.31` `11.89.0.31` `11.88.0.29` `11.87.1.38` `11.86.0.37` `11.85.1.32` `11.80.0.32` `11.79.0.34` `11.78.1.39` `11.77.0.27` `11.76.1.34` `11.75.0.33`

## Frida

* Use [StrongRFrida](https://github.com/killed/StrongRMagiskFrida) to bypass frida detection

* To unpin ssl use [Mitmproxy](https://mitmproxy.org/) and this [script](https://github.com/killed/Snapchat-Wiki/blob/master/Android/unpinSsl.js)

* Automatically unpin ssl with the Magisk module [here](https://github.com/killed/Magisk-Snapchat-SSL-Unpin)

* Hook the native signing (v11 & v12) `x-snapchat-att` [here](https://github.com/killed/Snapchat-Wiki/blob/master/Android/hookSigning.js) (versions supported above)

* `x-snapchat-att` signing bridge [here](https://github.com/killed/Snapchat-Wiki/blob/master/Android/signingBridge.js) - open snapchat try login once then attach with the script (versions supported above) (`port will be 1234`)

### Signing Bridge

* POST `IP:1234/sign`

Request
```json
{
    "endpoint": "/snap.security.ArgosService/GetTokens"
}
```

Response
```json
{
    "User-Agent": "Snapchat/13.12.0.37 (Pixel 6 Pro; Android 12#8353555#32; gzip) V/MUSHROOM grpc-c++/1.48.0 grpc-c/26.0.0 (android; cronet_http)",
    "X-Snapchat-ATT": "CgkYARVL+k+6CAo........................................................................................................................................................................................................................................................................................................................................................................................."
}
```

# Disclaimer
This project is in no way affiliated with, authorized, maintained, sponsored or endorsed by [Snapchat](https://www.snapchat.com) or any of its affiliates or subsidiaries. This is an independent project that utilizes [Snapchat's](https://www.snapchat.com) private API. Use at your own risk.
