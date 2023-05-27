import cv2 as cv
import multiprocessing
camera1=-1
camera2=-1
for i in range(20):
		vid= cv.VideoCapture(i)
		ret,frame=vid.read()
		if (ret):
			camera1=i
			break
for i in range(20):
	if (camera1==i):
		continue
	vid= cv.VideoCapture(i)
	ret,frame=vid.read()
	if (ret):
		camera2=i
		break
print(camera1, camera2)
vid= cv.VideoCapture(camera1);
#print(multiprocessing.cpu_count())
vid_r= cv.VideoCapture(camera2)
while(1):
	_,frame=vid.read()
	_,frame_r=vid_r.read()

	cv.imshow("live{}".format(camera1),frame)
	cv.imshow("live{}".format(camera2),frame_r)
	pressed = cv.waitKey(1) & 0xFF
	if(pressed == ord("q")):
		cv.destroyAllWindows()
		break

