import cv2 as cv
import numpy as np
import center
def per_dir(img_base,contb,img_track,contt,shape):
    base_center=center.center(contb,shape)
    track_center=center.center(contt,shape)
    if (base_center[1]-track_center[1])>15:
        print("right by "+ (base_center[1]-track_center[1])/shape[1]*100+"%")
    elif(base_center[1]-track_center[1])<-15:
        print("left by "+ (track_center[1]-base_center[1])/shape[1]*100+"%")
    elif (base_center[2]-track_center[2])>15:
        print("down by "+ (base_center[2]-track_center[2])/shape[0]*100+"%")
    elif (base_center[2]-track_center[2])<-15:
        print("up by "+ (track_center[2]-base_center[2])/shape[0]*100+"%")
    else:
        if sum([sum(i) for i in img_base])-sum([sum(i) for i in img_track])\
            >sum([sum(i) for i in img_base])*0.05:
            print("forward")
            percentage=(sum([sum(i) for i in img_base])-sum([sum(i) for i in img_track]))*100/sum([sum(i) for i in img_base])
        elif sum([sum(i) for i in img_base])-sum([sum(i) for i in img_track])\
            <-sum([sum(i) for i in img_base])*0.05:
            print("backward")
            percentage=(sum([sum(i) for i in img_track])-sum([sum(i) for i in img_base]))*100/sum([sum(i) for i in img_base])
        else:
            print("A OK!")
            return 1
        print(percentage)
    return 0        