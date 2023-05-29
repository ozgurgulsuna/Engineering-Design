import cv2 as cv

vid = cv.VideoCapture(1)          
vid2= cv.VideoCapture(2)
while(1):
    # to see the video, not essential for operation
    # Capture the video frame by frame
    _, frame = vid.read()
    _, frame2 = vid2.read()
    # Display the resulting frame
    cv.imshow('Live Video', frame)
    cv.imshow('Live Video2', frame2)
    # determine pressed key, used for test purposes
    pressed = cv.waitKey(1) & 0xFF

    # to stop video stream, press "q"
    if (pressed == ord('q')):
        cv.imwrite('cam-test.jpg', frame)
        cv.imwrite('cam-test2.jpg', frame2)
        cv.destroyAllWindows()
        break


