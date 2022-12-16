import cv2 as cv
import numpy as np
first = cv.imread("first.jpeg", 0)
second = cv.imread("second.jpeg", 0)
first = cv.GaussianBlur(first,(5,5),0)
second = cv.GaussianBlur(second,(5,5),0)
#// inorder to perform the absdiff, the images need to be of equal size
#// NOTE: I believe this is the reason why you have a big blue box on the edges
#// as well of the output image. This can be fixed by using two equal images in the first place
diff=cv.absdiff(first,second)

#// after getting the difference, we binarize it

_,thresh=cv.threshold(diff, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
con_real=[]
for cont in contours:
    if cv.contourArea(cont)>8000:
        con_real.append(cont)
blank=np.zeros(first.shape, dtype='uint8')
cv.drawContours(blank, con_real, -1, (255,255,255), 1)
cv.imshow('Contours Drawn', blank)
#// this matrix will be used for drawing purposes
out=cv.cvtColor(second, cv.COLOR_GRAY2BGR)


#// For each detected contour, calculate its bounding rectangle and draw it
#// You can also filter out some noise should you wish by checking if the contour is big
#// or small enough along with other contour properties.
#// Ref: https://docs.opencv.org/trunk/dd/d49/tutorial_py_contour_features.html
#// Ref: https://docs.opencv.org/trunk/d1/d32/tutorial_py_contour_properties.html
for cont in con_real:
    box = cv.boundingRect(cont)
    cv.rectangle(out, box,(255, 0, 0))


cv.imshow("FIRST", first)
cv.imshow("SECOND", second)
cv.imshow("ABS-DIFF", diff)
cv.imshow("THRESH", thresh)
cv.imshow("OUTPUT", out)

cv.waitKey(0)
cv.imwrite("out.png",blank)
