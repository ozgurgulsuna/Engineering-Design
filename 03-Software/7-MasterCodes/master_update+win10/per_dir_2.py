import cv2 as cv
import numpy as np
def per_dir(shape,rect_points,rect_points_r, cont, cont_r):
    cont=cont[0]
    cont_r=cont_r[0]
    base = np.zeros(shape,dtype="uint8")
    base_r = np.zeros(shape,dtype="uint8")
    # returns required movement 
    #pixel2mmx = 2.75
    #pixel2mmy = 2.75                           #1px kaç mm ediyor
    #base_w = 451-160                             #bunu değiştir
    #base_h = 480-179                             #bunu değiştir
    # base_x x of upper left corner of target rectangle
    #base_x=  160                              #bunu değiştir
    # base_y y of upper left corner of target rectangle
    #base_y=  179                              #bunu değiştir
    pixel2mmx = 2.017543
    pixel2mmy = 2.017543                           #1px kaç mm ediyor
    base_x = 206
    base_y = 241
    base_w = 228                            
    #base_h = 480-base_y

    #R
    pixel2mmx_r = 2.0354
    pixel2mmy_r = 2.0354                           #1px kaç mm ediyor

    base_x_r = 208
    base_y_r = 241
    base_w_r = 226                          
    #base_h_r = 480-base_y_r
    sheight = 1000                               # shadow height
    
    
    #### base_ratio===ekranda görünmesi gereken yerin x/y oranı
    # smaller y, larger area
    contour_image = np.zeros(shape,dtype="uint8")
    contour_image_r = np.zeros(shape,dtype="uint8")
    cv.rectangle(base,(base_x,base_y),(base_x+base_w,639),255,-1)
    cv.rectangle(base_r,(base_x_r,base_y_r),(base_x_r+base_w_r,639),255,-1)
    
    cv.drawContours(contour_image, cont, -1, (255), thickness=cv.FILLED)
    cv.drawContours(contour_image_r, cont_r, -1, (255), thickness=cv.FILLED)
    intersection = cv.bitwise_and(contour_image, base)
    intersection_r = cv.bitwise_and(contour_image_r, base_r)
    intersection_area = cv.countNonZero(intersection) 
    white_area = cv.countNonZero(base)
    intersection_area_r = cv.countNonZero(intersection_r)
    white_area_r = cv.countNonZero(base_r)
    percentage_intersection = (intersection_area / white_area) * 100
    percentage_intersection_r = (intersection_area_r / white_area_r) * 100
    

    if rect_points[2]*rect_points[3] ==0 and rect_points_r[2]*rect_points_r[3]==0:
        return 0,0
    if percentage_intersection > 90 and percentage_intersection_r > 90:
        return -99999,-99999




    if rect_points[2]*rect_points[3] >= rect_points_r[2]*rect_points_r[3]:          ##############################değişti
        # camera 1 area is larger
        print("camera1")

        # if upper corner goes beyond border:
        if rect_points[1]<shape[0]/47 and rect_points[3]<shape[0]*46/47:
            # lower
            if rect_points[0]+rect_points[2]/2>(shape[1]/2-shape[1]/20):##right
                print("lower left corner")
                x = (base_x-rect_points[0])*pixel2mmx
                y = (rect_points[1]+rect_points[3]-base_y)*pixel2mmy-sheight
            
            else:
                print("lower right corner")
                x = (base_x+base_w-rect_points[2]-rect_points[0])*pixel2mmx
                y = (rect_points[1]+rect_points[3]-base_y)*pixel2mmy-sheight            
        # find center of rectangle whether at the right of the image or not
        elif rect_points[0]+rect_points[2]/2>(shape[1]/2-shape[1]/20):##right
            print("upper left corner")
            # upper left corner is correct and known
            #print("in x direction ", (base_x-rect_points[0])*pixel2mmx,"mm")
            #print("in y direction ", (rect_points[1]-base_y)*pixel2mmy,"mm")
            x = (base_x-rect_points[0])*pixel2mmx
            y = (rect_points[1]-base_y)*pixel2mmy
        else: ##left
            print("upper right corner")
            #print("in x direction ", (base_x+base_w-rect_points[2]-rect_points[0])*pixel2mmx,"mm")
            #print("in y direction ", (rect_points[1]-base_y)*pixel2mmy,"mm") 
            x = (base_x+base_w-rect_points[2]-rect_points[0])*pixel2mmx
            y = (rect_points[1]-base_y)*pixel2mmy
    else:
        # camera 2 area is larger
        print("camera2")
        # NOTE: write a note here
        pixel2mmx = pixel2mmx_r
        pixel2mmy = pixel2mmy_r                           #1px kaç mm ediyor

        base_x = base_x_r
        base_y = base_y_r
        base_w = base_w_r                             
        #base_h = base_h_r
        
        # if upper corner goes beyond border:
        if rect_points[1]<shape[0]/47 and rect_points[3]<shape[0]*46/47:
            if rect_points[0]+rect_points[2]/2>(shape[1]/2-shape[1]/20):##right
                print("lower left corner")
                x = -(base_x-rect_points[0])*pixel2mmx
                y = -(rect_points[1]+rect_points[3]-base_y)*pixel2mmy-sheight
            
            else:
                print("lower right corner")
                x = -(base_x+base_w-rect_points[2]-rect_points[0])*pixel2mmx
                y = -(rect_points[1]+rect_points[3]-base_y)*pixel2mmy-sheight       
        
        
        elif rect_points_r[0]+rect_points_r[2]/2>shape[1]/2: # right of the image captured from camera 2
            print("upper left corner")
            #print("in x direction ", -(base_x-rect_points_r[0])*pixel2mmx,"mm")
            #print("in y direction ",  (base_y-rect_points_r[1])*pixel2mmy,"mm")
            x = -(base_x-rect_points_r[0])*pixel2mmx
            y = (base_y-rect_points_r[1])*pixel2mmy
        else:
            print("upper right corner")
            #print("in x direction ", -(base_x+base_w-rect_points_r[2]-rect_points_r[0])*pixel2mmx,"mm")
            #print("in y direction ",  (base_y-rect_points_r[1])*pixel2mmy,"mm")
            x = -(base_x+base_w-rect_points_r[2]-rect_points_r[0])*pixel2mmx
            y = (base_y-rect_points_r[1])*pixel2mmy
    print("in x direction ",int(x),"mm")
    print("in y direction ",int(y),"mm")
    #return int(7*x/8),int(7*y/8)                # scale output 
    return int(x),int(y)                # scale output 




    
