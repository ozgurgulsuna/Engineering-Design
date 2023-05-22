import cv2 as cv
import numpy as np
def per_dir(shape,rect_points,rect_points_r):
    pixel2mm = 3.7                           #1px kaç mm ediyor
    base_w = 200                             #bunu değiştir
    base_h = 200                             #bunu değiştir
    base_x=  10                              #bunu değiştir
    base_y=  10                              #bunu değiştir
    #### base_ratio===ekranda görünmesi gereken yerin x/y oranı
    if rect_points[2]*rect_points[3] >= rect_points_r[2]*rect_points_r[3]:
        if rect_points[2]>shape[1]:
            print("in x direction ", (base_x-rect_points[0])*pixel2mm,"mm")
            print("in y direction ", (base_y-rect_points[1])*pixel2mm,"mm")
        else:
            print("in x direction ", (base_x+base_w-rect_points[2]-rect_points[0])*pixel2mm,"mm")
            print("in y direction ", (base_y-rect_points[1])*pixel2mm,"mm") 
    else:
        if rect_points_r[2]>shape[1]:
            print("in x direction ", -(base_x-rect_points_r[0])*pixel2mm,"mm")
            print("in y direction ", -(base_y-rect_points_r[1])*pixel2mm,"mm")
        else:
            print("in x direction ", -(base_x+base_w-rect_points_r[2]-rect_points_r[0])*pixel2mm,"mm")
            print("in y direction ", -(base_y-rect_points_r[1])*pixel2mm,"mm")





    
