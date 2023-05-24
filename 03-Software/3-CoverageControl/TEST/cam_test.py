from time import sleep
from picamera import PiCamera

camera = PiCamera(resolution=(1980, 720), framerate=30)
camera.led = False
# Set ISO to the desired value
camera.iso = 1000
camera.rotation = 180
# Wait for the automatic gain control to settle
sleep(2)
# Now fix the values
camera.shutter_speed = camera.exposure_speed
camera.exposure_mode = 'off'
g = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = g
# Finally, take several photos with the fixed settings
camera.capture_sequence(['image%02d.jpg' % i for i in range(1)])
