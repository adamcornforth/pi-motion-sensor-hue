
from Camera import Camera
from Pir import Pir
from Hue import Hue
from Uploader import Uploader
import time

hue = Hue()
camera = Camera()
pir = Pir()
uploader = Uploader()

motion = False

hue.lights_off()

while (True):
    # motion = pir.detectMotion()
    motion = camera.detectMotion()
    
    if motion:
        # if motion causes light to trigger
        if(hue.report_motion()):
            # capture picture
            lastCapture = time.time()
            filename = camera.saveImage(camera.cameraSettings, camera.saveWidth, camera.saveHeight, camera.saveQuality, camera.diskSpaceToReserve)
            uploader.upload(filename)

    else:
        hue.report_no_motion()
