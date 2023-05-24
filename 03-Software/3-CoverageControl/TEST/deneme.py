import picamera
from time import sleep

camera = picamera.PiCamera()
camera.resolution = (1980, 1800)
camera.framerate = 15
camera.rotation = 180
camera.start_preview()
sleep(1)
camera.capture('/home/sundance/Desktop/max2.jpg')
sleep(50)
camera.stop_preview()
