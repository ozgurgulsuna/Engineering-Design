import os 
import numpy as np

import cv2

def background(cap,cap_r):
    i=1
    while(True):
        _ , back = cap.read()
        _ , back_r = cap_r.read()
        cv2.imshow('Live Video', cv2.resize(back,(int(back.shape[1]),int(back.shape[0])),interpolation=cv2.INTER_AREA))
        pressed = cv2.waitKey(1) & 0xFF
        if (pressed == ord('2')):
            cv2.imwrite('back/Back{}.jpeg'.format(i), back) #######directorrrrrry
            cv2.imwrite('back_r/Back{}.jpeg'.format(i), back_r) #######directorrrrrry            
            i=i+1
        if (i == 9):
            break

        
    # cap = cv2.VideoCapture(0)

    ##############################################
    # get the path/directory
    folder_dir = "back" #######directorrrrrry
    frames = []
    for fid in os.listdir(folder_dir):
        
        if (fid.endswith(".jpeg")):
            cap=cv2.imread("back/"+fid, cv2.IMREAD_COLOR) #######directorrrrrry
            frames.append(cap)

    folder_dir = "back_r" #######directorrrrrry
    frames_r = []
    for fid in os.listdir(folder_dir):
        
        if (fid.endswith(".jpeg")):
            cap_r=cv2.imread("back/"+fid, cv2.IMREAD_COLOR) #######directorrrrrry
            frames_r.append(cap_r)
    # Calculate the median along the time axis
    medianFrame = np.median(frames, axis=0).astype(dtype=np.uint8)
    medianFrame_r = np.median(frames_r, axis=0).astype(dtype=np.uint8)
    cv2.destroyAllWindows()
    return medianFrame, medianFrame_r  

