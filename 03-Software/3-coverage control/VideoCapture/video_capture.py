# import the opencv library
import cv2
import img_compare
import rect_detect

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
vid = cv2.VideoCapture('http://192.168.43.1:8080/video')

# first image to compare, in case no pictures is taken for comparison
ret, first = vid.read()
first = cv2.cvtColor(first, cv2.COLOR_BGR2GRAY)
first = rescaleFrame(first, 0.6)

while(True):
    # Capture the video frame by frame
    ret, frame = vid.read()

    # to find a working channel, added
    # print('Is camera is available? ',ret)

    # for ip based camera, scale is needed to obtain videos that fits to the screen
    frame = rescaleFrame(frame, 0.6)

    # Display the resulting frame
    cv2.imshow('Live Video', frame)

    pressed = cv2.waitKey(1) & 0xFF
    # pressed button
    if ((pressed == ord('f')) or (pressed == ord('s')) or (pressed == ord('q')) or (pressed == ord('d'))):
        # capture first image for comparison
        # waits 1 msec
        if pressed == ord('f'):
            ret, first = vid.read()
            first = cv2.cvtColor(first, cv2.COLOR_BGR2GRAY)
            first = rescaleFrame(first, 0.6)

            # Display the resulting frame
            cv2.imshow('First', first)
    
        # capture second image
        elif pressed == ord('s'):
            # send this frame to the image processing algorithm
            ret, second = vid.read()
            second = rescaleFrame(second, 0.6)

            # Display the resulting frame
            cv2.imshow('Second', second)
            second = cv2.cvtColor(second, cv2.COLOR_BGR2GRAY)

            cmp = img_compare.img_compare(first, second)
            rect_detect.rect_detect(cmp)
            
        # to quit, use key 'q'
        elif pressed == ord('q'):
            break

        # to destroy windows, use key 'd'
        elif pressed == ord('d'):
            cv2.destroyAllWindows()

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
