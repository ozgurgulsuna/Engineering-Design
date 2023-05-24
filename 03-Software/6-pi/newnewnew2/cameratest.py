import cv2 as cv
vid= cv.VideoCapture(4)
#vid_r= cv.VideoCapture(2)
while(1):
	_,frame=vid.read()
	#_,frame_r=vid_r.read()

	cv.imshow("live1",frame)
	#cv.imshow("live2",frame_r)
	pressed = cv.waitKey(1) & 0xFF
	if(pressed == ord("q")):
		cv.destroyAllWindows()
		break

