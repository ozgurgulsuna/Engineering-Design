# import required libraries
import cv2 as cv
import cv2
import numpy as np
import os 


# can we parametrize this function?
def perspective_2(img):
    # find the height and width of image
    # width = number of columns, height = number of rows in image array
    rows,cols = img.shape

    # define four points on input image 476,340 1500,340 1918,643 88,643
    pts1 = np.float32([[206,99],[449,98],[137,237],[514,237]])

    # define the corresponding four points on output image
    pts2 = np.float32([[249,190],[403,190],[249,374],[403,374]])

    # get the perspective transform matrix
    M = cv.getPerspectiveTransform(pts1,pts2)
    
    # mask
    #pts=np.array([[205,135],[166,245],[209,246],[217,209],[291,204],[281,248],[345,240],[343,137],[290,129],[285,160],[240,162],[244,134]],np.int32)
    #pts=pts.reshape((-1,1,2))
    #cv.fillPoly(img,[pts],255)
    
    # transform the image using perspective transform matrix
    dst = cv.warpPerspective(img,M,(cols, rows))
    return dst
    
    
def perspective_2_r(img):
    # find the height and width of image
    # width = number of columns, height = number of rows in image array
    rows,cols = img.shape

    # define four points on input image 476,340 1500,340 1918,643 88,643
    pts1 = np.float32([[207,109],[446,106],[138,245],[519,244]])

    # define the corresponding four points on output image
    pts2 = np.float32([[207,211],[427,211],[207,376],[427,376]])

    # get the perspective transform matrix
    M = cv.getPerspectiveTransform(pts1,pts2)
    
    # mask
    #pts=np.array([[274,149],[283,173],[283,259],[342,255],[343,220],[330,160],[308,161],[304,151]],np.int32)
    #pts=pts.reshape((-1,1,2))
    #cv.fillPoly(img,[pts],255)
    
    # transform the image using perspective transform matrix
    dst = cv.warpPerspective(img,M,(cols, rows))
    return dst

##############################################
# get the path/directory
folder_dir = "base" #######directorrrrrry
frames = []
i=1
for fid in os.listdir(folder_dir):
        
    if (fid.endswith(".jpeg")):
        cap=cv2.imread("base/"+fid, cv2.IMREAD_COLOR) #######directorrrrrry
        cv2.imwrite('base/Base{}.jpg'.format(i), perspective_2(cv.cvtColor(cap, cv.COLOR_BGR2GRAY))) #######directorrrrrry
        i=i+1
i=1
folder_dir = "base_r" #######directorrrrrry
frames_r = []
for fid in os.listdir(folder_dir):
        
    if (fid.endswith(".jpeg")):
        cap_r=cv2.imread("base/"+fid, cv2.IMREAD_COLOR) #######directorrrrrry
        cv2.imwrite('base_r/Base_r{}.jpg'.format(i), perspective_2(cv.cvtColor(cap_r, cv.COLOR_BGR2GRAY))) #######directorrrrrry  
        i=i+1
