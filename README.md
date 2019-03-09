# MPU6050_teapot_demo
Pyrhon server-client working demo for MPU-6050 gyro to control the teapot.


```
sudo apt-get install python-webpy python-opengl
(pip install pyopengl) apt-get python-opengl is better
python server.py
python client.py
```

http://blog.bitify.co.uk/2013/11/3d-opengl-visualisation-of-data-from.html

https://www.okahiro.info/gd/2016/10/05/post-1971/


```
check if you have required drivers/libraries

$ pip list |grep GL
PyOpenGL (3.1.0)

$ apt list python-opengl
python-opengl/stable,now 3.1.0+dfsg-1 all [installed]
```

```
OpenGL "fake KMS" is better than "Legacy" but still at low FPS.

Raspberry Pi 3B, kernel 4.14.98 tested on 2019-3-10

$ uname -a
Linux rpi000 4.14.98-v7+ #1200 SMP Tue Feb 12 20:27:48 GMT 2019 armv7l GNU/Linux

$ glxgears

If OpenGL is disabled as raspi-config/Advanced Options/GL Driver = G3 Legacy:
205 frames in 5.0 seconds = 40.877 FPS
The gears are in strange colors, and in lower FPS.

If OpenGL is enabled as raspi-config/Advanced Options/GL Driver = G2 GL (Fake KMS):
300 frames in 5.0 seconds = 59.995 FPS
The gears are being rendering correctly in red, green, and blue.

If you selected the GL Driver as G1 GL (Full KMS), there is no difference in the teapot demo and glxgears rendering. But you cannot use RealVNC anymore.

$ sudo raspi-config
Advanced Options
GL Driver

($ glxinfo | head)
```
