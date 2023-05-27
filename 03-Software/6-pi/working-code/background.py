import os 
import numpy as np

import cv2

def background():
    i=1


    ##############################################
    # get the path/directory
    folder_dir = "back" #######directorrrrrry
    frames = []
    for fid in os.listdir(folder_dir):
        
        if (fid.endswith(".jpeg")):
            cap=cv2.imread("back/"+fid, cv2.IMREAD_COLOR) #######directorrrrrry
            frames.append(cap)
    # Calculate the median along the time axis
    medianFrame = np.median(frames, axis=0).astype(dtype=np.uint8)
    cv2.destroyAllWindows()
    return medianFrame

