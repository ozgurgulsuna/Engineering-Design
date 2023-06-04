import cv2 as cv
import numpy as np
import center


def img_compare(first,second):
    
    # to save images, define variable
    i = 6
    
    
    first = cv.GaussianBlur(first,(5,5),0)
    second = cv.GaussianBlur(second,(5,5),0)
    
    
    #print(np.mean(first))
    
    #cv.rectangle(first,[230,0],[300,400],255,-1)
    #cv.imshow("bg",first) 
    
    #cv.waitKey(0) 

  
    diff=cv.absdiff(first,second)

    a,thresh_b=cv.threshold(diff, 50, 255,cv.THRESH_OTSU +  cv.THRESH_BINARY  )
    """
    cv.imwrite("images/thresh_b_{}.jpeg".format(i),thresh_b)
    cv.imshow("tresh_b",thresh_b)
    cv.waitKey(0)

    cv.imwrite("images/diff_{}.jpeg".format(i),diff)
    cv.imshow("difference of first and second",diff)
    cv.waitKey(0)
    """
    #// inorder to perform the absdiff, the images need to be of equal size
    #// NOTE: I believe this is the reason why you have a big blue box on the edges
    #// as well of the output image. This can be fixed by using two equal images in the first place


    #// after getting the difference, we binarize it

    _,thresh=cv.threshold(diff, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    con_real=[]
    hey=np.ones(first.shape, dtype='uint8')*255
    cv.drawContours(hey,contours,-1,0,-1)
    """
    cv.imwrite("images/diff2_{}.jpeg".format(i),hey)
    cv.imshow("threshold applied to difference",hey)
    cv.waitKey(0)
    """
    for cont in contours:
        #cont=cv.convexHull(cont)
        #epsilon = 4
        #cont=cv.approxPolyDP(cont,epsilon,True)
        mask = np.zeros(second.shape,np.uint8)
        cv.drawContours(mask,[cont],0,255,-1)
        if cv.contourArea(cont)>(first.shape[0]*first.shape[1]*18/100) and\
        cv.contourArea(cont)<((first.shape[0]-1)*(first.shape[1]-1))\
        and np.mean(second)+10 > cv.mean(second,mask = mask)[0]:
            con_real.append([cont])
            #print("hey")
    blank=np.ones(first.shape, dtype='uint8')*255
    for cont in con_real:
        cv.drawContours(blank, cont, -1, 0, -1)
    #// this matrix will be used for drawing purposes

    if len(con_real) == 1:
    

        return con_real, blank

    
    elif len(con_real) == 0: ## area treshold is too big
        con_real=[]
        for cont in contours:
            #epsilon = 4
            #cont=cv.approxPolyDP(cont,epsilon,True)
            mask = np.zeros(second.shape,np.uint8)
            cv.drawContours(mask,[cont],0,255,-1)
            if cv.contourArea(cont)>(first.shape[0]*first.shape[1]*8/100) and\
            cv.contourArea(cont) < ((first.shape[0]-1)*(first.shape[1]-1))\
            and np.mean(second)+10 > cv.mean(second,mask = mask)[0]:
                con_real.append([cont])
        blank=np.ones(first.shape, dtype='uint8')*255
        cont_real=con_real[0]
        for cont in con_real:
            cv.drawContours(blank, cont, -1, 0, -1)

            x = center.center(cont[0])
            y = center.center(cont_real[0])            
            if center.center(cont[0])> center.center(cont_real[0]):
                cont_real=cont
        con_real=[]
        con_real.append(cont_real)
        return con_real, blank

    else:
        cont_real=con_real[0]
        
        for cont in con_real:
            blank=np.ones(first.shape, dtype='uint8')*255
            cv.drawContours(blank, cont, -1, 0, -1)

            if center.center(cont[0]) > center.center(cont_real[0]):
                cont_real=cont

        con_real=[]
        con_real.append(cont_real)
        return con_real, blank

        
    #else: ## area treshold is too small(not realy needed)
    #    pass
    #// For each detected contour, calculate its bounding rectangle and draw it
    #// You can also filter out some noise should you wish by checking if the contour is big
    #// or small enough along with other contour properties.
    #// Ref: https://docs.opencv.org/trunk/dd/d49/tutorial_py_contour_features.html
    #// Ref: https://docs.opencv.org/trunk/d1/d32/tutorial_py_contour_properties.html
