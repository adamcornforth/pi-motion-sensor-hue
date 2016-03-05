Raspberry Pi PIR/Hue project 
-----

Mini project for the Raspberry Pi that turns some Philips Hue lights on when motion is detected via a connected PIR (Passive Infrared).

## GPIO

The data wire from the PIR is connected to the Pi's GPIO port number 18. 

The Pi also triggers GPIO port number 17 if motion has been detected. In my project I have an LED wired up to this GPIO port.

## Grunt 

Use `grunt watch` in the project root to automatically upload all the files in `src/` to a Pi that exists at `pi@pi` on the same network every time a file in `src/` changes. The watch task will also run the Python script after uploading the files. 

Note that you may need to create the `home/pi/apps/hue` directory on your PI to allow the Grunt task to work. 

## Image Capture 

The script also captures an image via the Pi's camera module every time motion is detected and the detected motion causes the Hue lights to turn on. These are saved in the `/home/pi/apps/hue/images` directory.  
