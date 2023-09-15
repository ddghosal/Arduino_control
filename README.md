# Arduino_control

This section helps to make an Arduino leonardo board communicate between a Digital Micromirror device (DMD) and a Thorlab scmos camera.

Basically the code is for: when the DMD sends high signal to the Arduino, it will trigger the camera to capture image automatically. Now here is two ways to do that:

  i) with Arduino IDE env. (the .ino file)
  
  ii) without the IDE i.e.using solely python script (using either pyfirmata or pyserial module)
  
  Please note that: 'pyfirmata' works fine on macOs and Linux, while it might have a glitch with Windows. If you find the same- use 'pymata4' module instead.
