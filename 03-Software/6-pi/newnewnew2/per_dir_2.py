import cv2 as cv
import numpy as np
def per_dir(shape,rect_points,rect_points_r):
    # returns required movement 
    #pixel2mmx = 2.75
    #pixel2mmy = 2.75                           #1px kaç mm ediyor
    #base_w = 451-160                             #bunu değiştir
    #base_h = 480-179                             #bunu değiştir
    # base_x x of upper left corner of target rectangle
    #base_x=  160                              #bunu değiştir
    # base_y y of upper left corner of target rectangle
    #base_y=  179                              #bunu değiştir
    pixel2mmx = 2.3
    pixel2mmy = 2.35                           #1px kaç mm ediyor
    base_x = 231
    base_y = 190
    base_w = 419-base_x                            
    #base_h = 480-base_y

    #R
    pixel2mmx_r = 2.16
    pixel2mmy_r = 2.10                           #1px kaç mm ediyor

    base_x_r = 231
    base_y_r = 190
    base_w_r = 419-base_x_r                          
    #base_h_r = 480-base_y_r
    sheight = 1000                               # shadow height
    
    
    #### base_ratio===ekranda görünmesi gereken yerin x/y oranı
    # smaller y, larger area 
    if rect_points[2]*rect_points[3] >= rect_points_r[2]*rect_points_r[3]:
        # camera 1 area is larger

        # if upper corner goes beyond border:
        if rect_points[1]<shape[0]/47 and rect_points[3]<shape[0]*46/47:
            # lower
            if rect_points[0]+rect_points[2]/2>(shape[1]/2-shape[1]/20):##right
                x = (base_x-rect_points[0])*pixel2mmx
                y = (rect_points[1]+rect_points[3]-base_y-sheight)*pixel2mmy
            
            else:
                x = (base_x+base_w-rect_points[2]-rect_points[0])*pixel2mmx
                y = (rect_points[1]+rect_points[3]-base_y-sheight)*pixel2mmy            
        # find center of rectangle whether at the right of the image or not
        elif rect_points[0]+rect_points[2]/2>(shape[1]/2-shape[1]/20):##right
            # upper left corner is correct and known
            #print("in x direction ", (base_x-rect_points[0])*pixel2mmx,"mm")
            #print("in y direction ", (rect_points[1]-base_y)*pixel2mmy,"mm")
            x = (base_x-rect_points[0])*pixel2mmx
            y = (rect_points[1]-base_y)*pixel2mmy
        else: ##left
            #print("in x direction ", (base_x+base_w-rect_points[2]-rect_points[0])*pixel2mmx,"mm")
            #print("in y direction ", (rect_points[1]-base_y)*pixel2mmy,"mm") 
            x = (base_x+base_w-rect_points[2]-rect_points[0])*pixel2mmx
            y = (rect_points[1]-base_y)*pixel2mmy
    else:
        # camera 2 area is larger
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
                x = -(base_x-rect_points[0])*pixel2mmx
                y = -(rect_points[1]+rect_points[3]-base_y-sheight)*pixel2mmy
            
            else:
                x = -(base_x+base_w-rect_points[2]-rect_points[0])*pixel2mmx
                y = -(rect_points[1]+rect_points[3]-base_y-sheight)*pixel2mmy       
        
        
        elif rect_points_r[0]+rect_points_r[2]/2>shape[1]/2: # right of the image captured from camera 2
            #print("in x direction ", -(base_x-rect_points_r[0])*pixel2mmx,"mm")
            #print("in y direction ",  (base_y-rect_points_r[1])*pixel2mmy,"mm")
            x = -(base_x-rect_points_r[0])*pixel2mmx
            y = (base_y-rect_points_r[1])*pixel2mmy
        else:
            #print("in x direction ", -(base_x+base_w-rect_points_r[2]-rect_points_r[0])*pixel2mmx,"mm")
            #print("in y direction ",  (base_y-rect_points_r[1])*pixel2mmy,"mm")
            x = -(base_x+base_w-rect_points_r[2]-rect_points_r[0])*pixel2mmx
            y = (base_y-rect_points_r[1])*pixel2mmy
    print("in x direction ",int(x),"mm")
    print("in y direction ",int(y),"mm")
    return int(7*x/8),int(7*y/8)                # scale output 




    
