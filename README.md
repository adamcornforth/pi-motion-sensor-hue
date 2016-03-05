Raspberry Pi PIR/Hue project 
-----

Mini project for the Raspberry Pi that turns some Philips Hue lights on when motion is detected via a connected PIR (Passive Infrared).

## GPIO

The data wire from the PIR is connected to the Pi's GPIO port number 18. 

The Pi also triggers GPIO port number 17 if motion has been detected. In my project I have an LED wired up to this GPIO port. 
