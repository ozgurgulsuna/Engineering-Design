import cv2 as cv
import numpy as np
def per_dir(shape,rect_points,rect_points_r):
    # returns required movement 
    pixel2mmx = 1.304
    pixel2mmy = 1.304                           #1px kaç mm ediyor
    base_w = 313                             #bunu değiştir
    base_h = 338                             #bunu değiştir
    # base_x x of upper left corner of target rectangle
    base_x=  162                              #bunu değiştir
    # base_y y of upper left corner of target rectangle
    base_y=  143                              #bunu değiştir
    #### base_ratio===ekranda görünmesi gereken yerin x/y oranı
    # smaller y, larger area 
    if rect_points[1] <= rect_points_r[1]:
        # camera 1 area is larger
        pixel2mmx = 1.304
        pixel2mmy = 1.304                           
        base_w = 313                             
        base_h = 338
        base_x = 162
        base_y = 143
        # find center of rectangle whether at the right of the image or not
        if rect_points[0]+rect_points[2]/2>shape[1]/2:##right
            # upper left corner is correct and known
            print("in x direction ", (base_x-rect_points[0]))*pixel2mmx,"mm")
            print("in y direction ", (rect_points[1]-base_y)*pixel2mmy,"mm")
            x = int(base_x-rect_points[0]*pixel2mmx)
            y = int(rect_points[1]-base_y*pixel2mmy)
        else: ##left
            print("in x direction ", (base_x+base_w-rect_points[2]-rect_points[0])*pixel2mmx,"mm")
            print("in y direction ", (rect_points[1]-base_y)*pixel2mmy,"mm") 
            x = int(base_x+base_w-rect_points[2]-rect_points[0]*pixel2mmx)
            y = int((rect_points[1]-base_y*pixel2mmy
    else:
        # camera 2 area is larger
        pixel2mmx = 1.304
        pixel2mmy = 1.304                           
        base_w = 313                             
        base_h = 338
        base_x = 162
        base_y = 143
        # NOTE: write a note here
        if rect_points_r[0]+rect_points_r[2]/2>shape[1]/2: # right of the image captured from camera 2
            print("in x direction ", -(base_x-rect_points_r[0])*pixel2mmx,"mm")
            print("in y direction ",  (base_y-rect_points_r[1])*pixel2mmy,"mm")
            x = -(int(base_x-rect_points_r[0]*pixel2mmx))
            y = (int(base_y-rect_points_r[1]*pixel2mmy))
        else:
            print("in x direction ", -(base_x+base_w-rect_points_r[2]-rect_points_r[0])*pixel2mmx,"mm")
            print("in y direction ",  (base_y-rect_points_r[1])*pixel2mmy,"mm")
            x = -(int(base_x+base_w-rect_points_r[2]-rect_points_r[0])*pixel2mmx)
            y = int((base_y-rect_points_r[1])*pixel2mmy)

    return x,y




    
