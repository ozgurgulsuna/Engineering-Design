# import the opencv library
import cv2

def rescaleFrame(frame, scale = 0.75):
    #images,videos and live video
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width, height)

    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)


# define a video capture object

# 0 : webcam, to find other cameras, change the number
vid = cv2.VideoCapture(0)

# IP Webcam app (Play Store)
# vid = cv2.VideoCapture('http://192.168.0.20:8080/video')


while(True):
	
    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    #to find a working channel, added
    # print('Is camera is available? ',ret)

    # for ip based camera, scale is needed to obtain videos that fits to the screen
    # frame = rescaleFrame(frame, 0.6)

    # Display the resulting frame
    cv2.imshow('Live Video', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('l'):
        # send this frame to the image processing algorithm
        cv2.imshow('Captured Image', frame)
    # to quit    
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
