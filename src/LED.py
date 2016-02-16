from gpiozero import LED
from time import sleep

led = LED(17)

while True:
    led.on() 
    print 'on\n' 
    sleep(1)
    led.off()
    print 'off\n'
    sleep(1) 