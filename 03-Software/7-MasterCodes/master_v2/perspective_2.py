# import required libraries
import cv2 as cv
import numpy as np


# can we parametrize this function?
def perspective_2(img):
    # find the height and width of image
    # width = number of columns, height = number of rows in image array
    rows,cols = img.shape

    # define four points on input image 476,340 1500,340 1918,643 88,643
    pts1 = np.float32([[170,58],[418,57],[2,389],[598,390]])

    # define the corresponding four points on output image
    pts2 = np.float32([[161,152],[423,151],[170,475],[450,478]])

    # get the perspective transform matrix
    M = cv.getPerspectiveTransform(pts1,pts2)

    # transform the image using perspective transform matrix
    dst = cv.warpPerspective(img,M,(cols, rows))
    return dst
