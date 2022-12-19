import cv2 as cv
import numpy as np
import time
import largestinteriorrectangle as lir

def rect_detect(img):
    start = time.time()
    # Import your picture
    # Color it in gray
    mask = 255-img
    # Create our mask by selecting the non-zero values of the picture
    _, tresh = cv.threshold(mask,0,255,cv.THRESH_BINARY)
    # Select the contour
    contours,_ = cv.findContours(tresh, cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)
    # if your mask is incurved or if you want better results, 
    # you may want to use cv2.CHAIN_APPROX_NONE instead of cv2.CHAIN_APPROX_SIMPLE, 
    # but the rectangle search will be longer
    cv.drawContours(img, contours,0, (0, 0, 255), 1)
    try:
        contour = contours[0][:, 0, :]

        grid=mask>0
        rect=lir.lir(grid,contour)
        blank=np.zeros(mask.shape,dtype="uint8")
        print(contour.shape)
        print(rect)
        cv.rectangle(blank,[rect[0],rect[1]],[rect[2]+rect[0],rect[3]+rect[1]],255,-1)
        cv.imshow("hey", blank)

    except:
        pass
    
    end = time.time()
    print(end - start)
    cv.waitKey(0)
