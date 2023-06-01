import os 
import numpy as np

import cv2 as cv

def background():
    ##############################################
    # get the path/directory
    folder_dir = "back" #######directorrrrrry
    frames = []
    for fid in os.listdir(folder_dir):
        
        if (fid.endswith(".jpeg")):
            cap=cv.imread("back/"+fid, cv.IMREAD_COLOR) #######directorrrrrry
            frames.append(cap)

    folder_dir = "back_r" #######directorrrrrry
    frames_r = []
    for fid in os.listdir(folder_dir):
        
        if (fid.endswith(".jpeg")):
            cap_r=cv.imread("back/"+fid, cv.IMREAD_COLOR) #######directorrrrrry
            frames_r.append(cap_r)
    # Calculate the median along the time axis
    medianFrame = np.median(frames, axis=0).astype(dtype=np.uint8)
    medianFrame_r = np.median(frames_r, axis=0).astype(dtype=np.uint8)
    cv.destroyAllWindows()
    return medianFrame, medianFrame_r  

