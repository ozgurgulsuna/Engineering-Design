# import required libraries
import cv2 as cv
import numpy as np


# can we parametrize this function?
def perspective_2(img):
    # find the height and width of image
    # width = number of columns, height = number of rows in image array
    rows,cols = img.shape

    # define four points on input image 476,340 1500,340 1918,643 88,643
    pts1 = np.float32([[238,140],[457,141],[20,480],[628,480]])

    # define the corresponding four points on output image
    pts2 = np.float32([[267,270],[429,262],[243,480],[421,480]])

    # get the perspective transform matrix
    M = cv.getPerspectiveTransform(pts1,pts2)

    # transform the image using perspective transform matrix
    dst = cv.warpPerspective(img,M,(cols, rows))
    return dst
