import cv2 as cv
import multiprocessing


vid = cv.VideoCapture("/dev/v4l/by-path/platform-3f980000.usb-usb-0:1.2:1.0-video-index0") 
#print(multiprocessing.cpu_count())
vid_r=cv.VideoCapture("/dev/v4l/by-path/platform-3f980000.usb-usb-0:1.3:1.0-video-index0")    

i = 0

while(1):
	_,frame=vid.read()
	_,frame_r=vid_r.read()

	cv.imshow("live",frame)
	cv.imshow("live_r",frame_r)
	pressed = cv.waitKey(1) & 0xFF
	if(pressed == ord("q")):
		cv.destroyAllWindows()
		break
	if(pressed == ord("1")):
		cv.imwrite("perspective/image_{}.jpeg".format(i),frame)
		cv.imwrite("perspective/image_r{}.jpeg".format(i),frame_r)
		i = i + 1

