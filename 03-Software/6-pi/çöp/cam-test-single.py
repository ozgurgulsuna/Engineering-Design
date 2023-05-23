import cv2 as cv

vid = cv.VideoCapture(3)          
while(1):
    # to see the video, not essential for operation
    # Capture the video frame by frame
    _, frame = vid.read()
    # Display the resulting frame
    cv.imshow('Live Video', frame)
    # determine pressed key, used for test purposes
    pressed = cv.waitKey(1) & 0xFF

    # to stop video stream, press "q"
    if (pressed == ord('q')):
        cv.destroyAllWindows()
        break


