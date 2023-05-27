import cv2 as cv
from background import background
import img_compare
import perspective_2

img1 = background()
img1 =perspective_2.perspective_2(cv.cvtColor(img1, cv.COLOR_BGR2GRAY))
cv.imshow("img1",img1)
img2=perspective_2.perspective_2(cv.cvtColor(cv.imread("Back3.jpeg"),cv.COLOR_BGR2GRAY))
#img2=perspective_2.perspective_2(cv.cvtColor(cv.imread("t1.jpeg"),cv.COLOR_BGR2GRAY))
cv.imshow("img2", img2)
_,comp=img_compare.img_compare(img1,img2)
cv.imshow("comp",comp)
cv.waitKey(0)

