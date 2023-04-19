from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (2592,1944)
camera.framerate = 15
camera.rotation = 180
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/madness/max2.jpg')
camera.stop_preview()
