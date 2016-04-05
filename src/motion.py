from Camera import Camera
from Pir import Pir
from Hue import Hue
from Uploader import Uploader
from time import sleep
import time

hue = Hue()
camera = Camera()
pir = Pir()
uploader = Uploader()

motion = False

hue.lights_off()

while (True):
    motion = pir.detectMotion()
 
    if motion:
        # if motion causes light to trigger
        if(hue.report_motion()):
            # capture picture
            lastCapture = time.time()
            sleep(0.5)
            filename = camera.saveImage(camera.cameraSettings, camera.saveWidth, camera.saveHeight, camera.saveQuality, camera.diskSpaceToReserve)
            uploader.upload(filename)

    else:
        hue.report_no_motion()
