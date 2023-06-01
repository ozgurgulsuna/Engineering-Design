##center coordinates of a shape
import cv2 as cv
def center(contours):
    M = cv.moments(contours)
    if M['m00'] != 0:
        cy = int(M['m01']/M['m00'])
        return cy
    else:
        return 0

