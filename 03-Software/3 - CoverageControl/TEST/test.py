import cv2
import math


def rescaleFrame(frame, scale = 0.75):
    #images,videos and live video
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width, height)

    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)


# define a video capture object

# 0 : webcam, to find other cameras, change the number
cap = cv2.VideoCapture(0)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

#codec = cv2.VideoWriter_fourcc(	'M', 'J', 'P', 'G'	)
#cap.set(6, codec)
#cap.set(5, 30)
#cap.set(3, 1920)
#cap.set(4, 1080)

# IP Webcam app (Play Store)
#vid = cv2.VideoCapture('http://144.122.227.69:8080/video')


# first, second and base images to compare, in case no pictures is taken for comparison

i = 0               # only for saving images

while(True):
    # Capture the video frame by frame
    ret, frame = cap.read()
    frame = cv2.rotate(frame, cv2.ROTATE_180)

    # to find a working channel, added
    # print('Is camera is available? ',ret)

    # for ip based camera, scale is needed to obtain videos that fits to the screen
    # frame = rescaleFrame(frame, 0.6)

    # Display the resulting frame
    cv2.imshow('Live Video', frame)
    pressed = cv2.waitKey(1) & 0xFF
    if pressed == ord('q'): 
        break
    elif pressed == ord('z'):
        __, cal = cap.read()
        cal= cv2.rotate(cal, cv2.ROTATE_180)
        cv2.imwrite('/home/pi/Desktop/madness/Cali/calibration{}.jpeg'.format(i), cal)
        i = i + 1
cap.release()
cv2.destroyAllWindows()
