
from Camera import Camera
from Pir import Pir
from Hue import Hue
import time

hue = Hue()
camera = Camera()
pir = Pir()

motion = False

hue.lights_off()

while (True):
    motion = pir.detectMotion()
 
    if motion:
        # if motion causes light to trigger
        if(hue.report_motion()):
            # capture picture
            lastCapture = time.time()
            camera.saveImage(camera.cameraSettings, camera.saveWidth, camera.saveHeight, camera.saveQuality, camera.diskSpaceToReserve)

    else:
        hue.report_no_motion()
