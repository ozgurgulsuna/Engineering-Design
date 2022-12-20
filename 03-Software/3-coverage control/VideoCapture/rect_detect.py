import cv2 as cv
import numpy as np
import time
import largestinteriorrectangle as lir

def rect_detect(conts,shape):
    print(conts)
    start = time.time()
    # Import your picture
    # Color it in gray
    mask = np.ones(shape, dtype='uint8')*255
    blank=np.zeros(mask.shape,dtype="uint8")

    for x in range(len(conts)):
        cv.drawContours(mask, conts[x], -1, 0, -1)
        cv.imshow("bca", mask)
        # Create our mask by selecting the non-zero values of the picture
        # Select the contour
        # if your mask is incurved or if you want better results, 
        # you may want to use cv2.CHAIN_APPROX_NONE instead of cv2.CHAIN_APPROX_SIMPLE, 
        # but the rectangle search will be longer
        contour = conts[x][0][:, 0, :]
        print(conts)
        print(contour)
        grid=255-mask>0
        cv.imshow("mask", mask)
        rect=lir.lir(grid,contour)
        print(rect)
        cv.rectangle(blank,[rect[0],rect[1]],[rect[2]+rect[0],rect[3]+rect[1]],255,-1)

    cv.imshow("hey", blank)
    end = time.time()
    print(end - start)
    cv.waitKey(0)

    