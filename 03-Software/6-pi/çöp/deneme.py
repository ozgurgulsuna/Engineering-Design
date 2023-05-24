import cv2
import img_compare
import numpy as np
import rect_detect_2
while(True):
	img1=cv2.imread('Shadow2.jpeg', cv2.IMREAD_COLOR)
	img2=cv2.imread('Third.jpeg', cv2.IMREAD_COLOR)
	img1=cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
	img2=cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
	img1=cv2.resize(img1,(int(img1.shape[1]),int(img1.shape[0])),interpolation=cv2.INTER_AREA)
	img2=cv2.resize(img2,(int(img1.shape[1]),int(img1.shape[0])),interpolation=cv2.INTER_AREA)
	cont, cont_img = img_compare.img_compare(img1, img2)
	#print(np.squeeze(cont[0][0]))

	img,rect=rect_detect_2.rect_detect(cont,cont_img.shape)

	#img=cv2.cvtColor(img, cv2.COLOR_GRAY2BGRA)
	#cv2.circle(img,(((rect[2])/2).astype(np.uint32)+rect[0],rect[1]), 5, (0,0,255), -1)
	#cv2.imshow("hey",img)
	cv2.imwrite("hey.png",img)
	#cv2.waitKey(0)
