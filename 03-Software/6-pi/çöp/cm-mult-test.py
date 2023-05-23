import cv2 as cv

vid = cv.VideoCapture(1)          
vid_r= cv.VideoCapture(3)                                      # 0 : webcam, to find other cameras, change the number
while(1):
    # to see the video, not essential for operation
    # Capture the video frame by frame
    _, frame = vid.read()
    _, frame_r = vid_r.read()
    # Display the resulting frame
    cv.imshow('Live Video', frame)
    cv.imshow('Live Video_r', frame_r)
    # determine pressed key, used for test purposes
    pressed = cv.waitKey(1) & 0xFF

    # to stop video stream, press "q"
    if (pressed == ord('q')):
        cv.destroyAllWindows()
        break


