import cv2 as cv
import numpy as np
import center

def img_compare(first,second):
    first = cv.GaussianBlur(first,(5,5),0)
    second = cv.GaussianBlur(second,(5,5),0)
    #
    #print(np.mean(first))

    mask = cv.inRange(second, 0, np.mean(second))



    #
    #diff=(first-second)
    diff=cv.absdiff(first,second)
    #// inorder to perform the absdiff, the images need to be of equal size
    #// NOTE: I believe this is the reason why you have a big blue box on the edges
    #// as well of the output image. This can be fixed by using two equal images in the first place


    #// after getting the difference, we binarize it

    _,thresh=cv.threshold(diff, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    con_real=[]

    for cont in contours:
        mask = np.zeros(second.shape,np.uint8)
        cv.drawContours(mask,[cont],0,255,-1)
        if cv.contourArea(cont)>(first.shape[0]*first.shape[1]*3/100) and\
        cv.contourArea(cont)<((first.shape[0]-1)*(first.shape[1]-1))\
        and np.mean(second)-100 < cv.mean(second,mask = mask)[0]:
            con_real.append([cont])
    blank=np.ones(first.shape, dtype='uint8')*255
    for cont in con_real:
        cv.drawContours(blank, cont, -1, 0, -1)
    #// this matrix will be used for drawing purposes
    if len(con_real) == 1:
        return con_real, blank
        #queue.put([con_real, blank])
    
    elif len(con_real) == 0: ## area treshold is too big
        con_real=[]
        for cont in contours:
            mask = np.zeros(second.shape,np.uint8)
            cv.drawContours(mask,[cont],0,255,-1)
            if cv.contourArea(cont)>(first.shape[0]*first.shape[1]*1/100) and\
            cv.contourArea(cont)<((first.shape[0]-1)*(first.shape[1]-1))\
            and np.mean(second)-100 < cv.mean(second,mask = mask)[0]:
                con_real.append([cont])
        blank=np.ones(first.shape, dtype='uint8')*255
        cont_real=con_real[0]
        print(cont_real)
        for cont in con_real:
            print(cont)
            cv.drawContours(blank, cont, -1, 0, -1)
            if center.center(cont[0])> center.center(cont_real[0]):
                cont_real=cont
    con_real=[]
    con_real.append([cont_real])


    return con_real, blank
    #queue.put([con_real, blank])
    
    """
    else: ## area treshold is too small(not realy needed)
        pass
    """
    #// For each detected contour, calculate its bounding rectangle and draw it
    #// You can also filter out some noise should you wish by checking if the contour is big
    #// or small enough along with other contour properties.
    #// Ref: https://docs.opencv.org/trunk/dd/d49/tutorial_py_contour_features.html
    #// Ref: https://docs.opencv.org/trunk/d1/d32/tutorial_py_contour_properties.html
