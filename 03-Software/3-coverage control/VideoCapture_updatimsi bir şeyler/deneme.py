import cv2
import background
import img_compare
import rect_detect
import numpy as np
img1=cv2.imread('Shadow2.jpeg', cv2.IMREAD_COLOR)
img2=cv2.imread('Third.jpeg', cv2.IMREAD_COLOR)
img1=cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2=cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
cont, cont_img = img_compare.img_compare(img1, img2)


img,rect=rect_detect.rect_detect(cont,cont_img.shape)
img=cv2.cvtColor(img, cv2.COLOR_GRAY2BGRA)
cv2.circle(img,(((rect[2])/2).astype(np.uint32)+rect[0],rect[1]), 5, (0,0,255), -1)
print(type(((rect[2])/2).astype(np.uint32)))
print(type(img.shape[1]))
cv2.imshow("hey",img)
cv2.waitKey(0)