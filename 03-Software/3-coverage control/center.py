##center coordinates of a shape

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
  
#find contour, will change this
img = cv.imread('shapes.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, threshold = cv.threshold(gray, 127, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
contours, _ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

###########################################
#m10/m00=x,m01/m00=y,
contour_lists=[]
t=0
for i in contours:
    if t==0:
        t=1
        continue
    M = cv.moments(i)
    if M['m00'] != 0:
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
    tlist=(i,cx,cy)
    contour_lists.append(tlist)
    t=t+1

blank = np.zeros(img.shape, dtype='uint8')#playfield
for i in range(len(contours)-1):
    cv.drawContours(blank, contour_lists[i], 0, (0, 0, 255), 5)
    cv.circle(blank, (contour_lists[i][1],contour_lists[i][2]), 7, (0, 0, 255), -1)


cv.imshow("test", blank)


print(img.shape)
print(len(contours))
cv.imshow("image", img)
cv.waitKey(0)
