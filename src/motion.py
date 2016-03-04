
from MotionDetector import MotionDetector
from Hue import Hue
import time

hue = Hue()
motion = MotionDetector()

takePicture = False

hue.lights_off()

while (True):


    takePicture = motion.detectMotion()
 
    if takePicture:
        # if motion causes light to trigger
        if(hue.report_motion()):
            motion.setThresholds(10, 200)
            # capture picture
            lastCapture = time.time()
            motion.saveImage(motion.cameraSettings, motion.saveWidth, motion.saveHeight, motion.saveQuality, motion.diskSpaceToReserve)
    else:
        if(hue.report_no_motion()):
            motion.setThresholds(10, 20)

    # Swap comparison buffers
    motion.image1 = motion.image2
    motion.buffer1 = motion.buffer2