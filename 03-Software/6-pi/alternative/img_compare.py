import cv2 as cv
import numpy as np
import center

def img_compare(first,second):
    first = cv.GaussianBlur(first,(5,5),0)
    second = cv.GaussianBlur(second,(5,5),0)
    #
    #print(np.mean(first))
    #cv.rectangle(first,[230,0],[300,400],255,-1)
    #cv.imshow("bg",first)
    cv.waitKey(0) 
    #mask = cv.inRange(second, 0, np.mean(second)*.9)
    #cv.imshow("mask",mask)
    #cv.waitKey(0)
    _,thresh_b=cv.threshold(first, 40, 255,cv.THRESH_BINARY)
    _,thresh_i=cv.threshold(second, 175, 255,cv.THRESH_OTSU  )
    thresh_whoknows=cv.adaptiveThreshold(first,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,15,2)
    thresh_b_u=cv.bitwise_or(cv.bitwise_not(thresh_whoknows),thresh_b)
    cv.imshow("thresh_b_u",thresh_b_u) 

    #print(thresh_whoknows)
    cv.imshow("thresh_whoknows",thresh_whoknows)
    cv.imshow("tresh_b",thresh_b)
    cv.waitKey(0)
    cv.imshow("tresh_i",thresh_i)
    cv.waitKey(0)
    #
    #diff=(first-second)
    diff=cv.absdiff(thresh_b_u,second)
    cv.imshow("die",diff)
    cv.waitKey(0)
    #cv.imshow("diff",diff)
    #// inorder to perform the absdiff, the images need to be of equal size
    #// NOTE: I believe this is the reason why you have a big blue box on the edges
    #// as well of the output image. This can be fixed by using two equal images in the first place


    #// after getting the difference, we binarize it

    _,thresh=cv.threshold(diff, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    #print(thresh)
    contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    #print(len(contours))
    con_real=[]
    cv.imshow("why",thresh)
    hey=np.ones(first.shape, dtype='uint8')*255
    cv.drawContours(hey,contours,-1,0,-1)
    
    #cv.drawContours(hey,contours[1],-1,0,-1)
    #cv.drawContours(hey,contours[2],-1,0,-1)
    cv.imshow("hey",hey)
    cv.waitKey(0)
    for cont in contours:
        mask = np.zeros(second.shape,np.uint8)
        cv.drawContours(mask,[cont],0,255,-1)
        #cv.imshow("pain",mask)
        #cv.waitKey(0)
        if cv.contourArea(cont)>(first.shape[0]*first.shape[1]*15/100) and\
        cv.contourArea(cont)<((first.shape[0]-1)*(first.shape[1]-1))\
        and np.mean(second)*1.3 > cv.mean(second,mask = mask)[0]:
            con_real.append([cont])
            #print("hey")
    blank=np.ones(first.shape, dtype='uint8')*255
    for cont in con_real:
        cv.drawContours(blank, cont, -1, 0, -1)
    #// this matrix will be used for drawing purposes
    #print(con_real)
    if len(con_real) == 1:
    
        #print(con_real)
        #cv.imshow("blank13213eds",blank)
        #cv.waitKey(0)
        print("1")
        return con_real, blank
        #queue.put([con_real, blank])
    
    elif len(con_real) == 0: ## area treshold is too big
        con_real=[]
        for cont in contours:
            mask = np.zeros(second.shape,np.uint8)
            cv.drawContours(mask,[cont],0,255,-1)
            if cv.contourArea(cont)>(first.shape[0]*first.shape[1]*1/200) and\
            cv.contourArea(cont) < ((first.shape[0]-1)*(first.shape[1]-1))\
            and np.mean(second)+10 > cv.mean(second,mask = mask)[0]:
                con_real.append([cont])
        blank=np.ones(first.shape, dtype='uint8')*255
        cont_real=con_real[0]
        for cont in con_real:
            
            #print("cont:", cont)
            x = center.center(cont[0])
            y = center.center(cont_real[0])            
            if center.center(cont[0])> center.center(cont_real[0]):
                cont_real=cont
        con_real=[]
        cv.drawContours(blank, cont_real, -1, 0, -1)
        con_real.append(cont_real)
        print("2")
        return con_real, blank
        #queue.put([con_real, blank])
    
    else:
        cont_real=con_real[0]
        blank=np.ones(first.shape, dtype='uint8')*255
        for cont in con_real:
            #cv.imshow("img",blank)
            #cv.waitKey(0)
            if center.center(cont[0]) > center.center(cont_real[0]):
                cont_real=cont
                #print("dead")
        con_real=[]
        con_real.append(cont_real)
        cv.drawContours(blank, cont_real, -1, 0, -1)
        print("3")
        return con_real, blank
        #queue.put([con_real, blank])
        
    #else: ## area treshold is too small(not realy needed)
    #    pass
    #// For each detected contour, calculate its bounding rectangle and draw it
    #// You can also filter out some noise should you wish by checking if the contour is big
    #// or small enough along with other contour properties.
    #// Ref: https://docs.opencv.org/trunk/dd/d49/tutorial_py_contour_features.html
    #// Ref: https://docs.opencv.org/trunk/d1/d32/tutorial_py_contour_properties.html
