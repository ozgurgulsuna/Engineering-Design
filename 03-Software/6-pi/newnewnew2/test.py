# this is the main code for coverage detection algorithm

# import opencv library
import cv2 as cv
# main functions
import per_dir_2
import img_compare
import perspective_2
import rect_detect_2 as rect_detect
import background
import numpy as np
# necessary to add delays to the system
import time
import threading

def camera_thread():
        global cam_result_1
        while(1):
                _, cam_result_1 = vid.read()
                cv.imshow('Live Video', frame)
                cv.waitKey(1)
def camera_thread_r():
        global cam_result_2
        while(1):
                _, cam_result_2 = vid_r.read()


# define a video capture object
vid = cv.VideoCapture("/dev/v4l/by-path/platform-3f980000.usb-usb-0:1.1.2:1.0-video-index0") 
vid.set(cv.CAP_PROP_SHARPNESS,15)#0 15 2 ##min max default
vid.set(cv.CAP_PROP_BRIGHTNESS,0)#-64 64 0
vid.set(cv.CAP_PROP_SATURATION,37)#0 100 37
vid.set(cv.CAP_PROP_CONTRAST,33)#0 100   33                                     # 0 : webcam, to find other cameras, change the number                                              # 0 : webcam, to find other cameras, change the number
vid_r=cv.VideoCapture("/dev/v4l/by-path/platform-3f980000.usb-usb-0:1.3:1.0-video-index0")                                                # 1 : reversed x y axis cam
vid_r.set(cv.CAP_PROP_SHARPNESS,15)
vid_r.set(cv.CAP_PROP_BRIGHTNESS,0)
vid_r.set(cv.CAP_PROP_SATURATION,37) 
vid_r.set(cv.CAP_PROP_CONTRAST,33) 
_, frame = vid.read()
# background image is added to the system, image is determined in advance during calibration

#background_path = "Background.jpeg"
#background_image = cv.imread(background_path)
background_image,background_image_r = background.background(vid,vid_r)  #button=2
background_image = cv.cvtColor(background_image, cv.COLOR_BGR2GRAY)
background_image_r = cv.cvtColor(background_image_r, cv.COLOR_BGR2GRAY)

# add pole masks before perspective correction####################################################
# fixed pole
#cv.rectangle(background_image,[245,0],[270,140],255,-1)
# bottom of movable pole
#cv.rectangle(background_image,[270,75],[340,140],255,-1)
# slave pole can also be eliminated

# fixed pole
#cv.rectangle(background_image_r,[245,0],[270,140],255,-1)
# bottom of movable pole
#cv.rectangle(background_image_r,[270,75],[340,140],255,-1)
# slave pole can also be eliminated
"""
##################################################################################################
##normal
pts=np.array([[205,135],[166,245],[209,246],[217,209],[291,204],[281,248],[345,240],[343,137],[290,129],[285,160],[240,162],[244,134]],np.int32)
pts=pts.reshape((-1,1,2))
cv.fillPoly(background_image,[pts],255)
pts=np.array([[282,0],[284,179],[275,201],[299,220],[322,196],[311,152],[302,3]],np.int32)
pts=pts.reshape((-1,1,2))
cv.fillPoly(background_image,[pts],255)

##revers
pts=np.array([[223,154],[187,251],[215,253],[247,153]],np.int32)
pts=pts.reshape((-1,1,2))
cv.fillPoly(background_image_r,[pts],255)

pts=np.array([[302,153],[296,248],[353,250],[347,150]],np.int32)
pts=pts.reshape((-1,1,2))
cv.fillPoly(background_image_r,[pts],255)

pts=np.array([[322,177],[312,0],[301,0],[312,175]],np.int32)
pts=pts.reshape((-1,1,2))
cv.fillPoly(background_image_r,[pts],255)
"""



# background masks before perspective
# back
pts=np.array([[208, 137],[236,137],[205,245],[168,244]],np.int32)
pts=pts.reshape((-1,1,2))
cv.fillPoly(background_image,[pts],255)

pts=np.array([[289,139],[339,139],[344,243],[281,241]],np.int32)
pts=pts.reshape((-1,1,2))
cv.fillPoly(background_image,[pts],255)

pts=np.array([[285,1],[299,1],[308,145],[291,149]],np.int32)
pts=pts.reshape((-1,1,2))
cv.fillPoly(background_image,[pts],255)

# back_r
pts=np.array([[222,149],[250,148],[221,255],[186,256]],np.int32)
pts=pts.reshape((-1,1,2))
cv.fillPoly(background_image_r,[pts],255)

pts=np.array([[300,148],[352,148],[358,252],[294,251]],np.int32)
pts=pts.reshape((-1,1,2))
cv.fillPoly(background_image_r,[pts],255)

pts=np.array([[297,1],[303,170],[320,149],[311,1]],np.int32)
pts=pts.reshape((-1,1,2))
cv.fillPoly(background_image_r,[pts],255)


#background_image=255*np.ones(background_image.shape,np.uint8)
#background_image_r=255*np.ones(background_image.shape,np.uint8)

background_image = perspective_2.perspective_2(background_image)
background_image_r = perspective_2.perspective_2_r(background_image_r)



# background masks after perspective
# to destroy triangles comes from perspective
# back triangle
pts=np.array([[183,405],[230,480],[183,480]],np.int32)
pts=pts.reshape((-1,1,2))
cv.fillPoly(background_image,[pts],255)

pts=np.array([[456,399],[411,480],[456,480]],np.int32)
pts=pts.reshape((-1,1,2))
cv.fillPoly(background_image,[pts],255)

# back_r triangle
pts=np.array([[187,419],[230,480],[187,480]],np.int32)
pts=pts.reshape((-1,1,2))
cv.fillPoly(background_image_r,[pts],255)

pts=np.array([[450,404],[402,480],[450,480]],np.int32)
pts=pts.reshape((-1,1,2))
cv.fillPoly(background_image_r,[pts],255)



time.sleep(1)
i = 1
flag=0
# repeat the same operation steps until the operation is terminated
threading.Thread(target=camera_thread).start()
threading.Thread(target=camera_thread_r).start()
time.sleep(1)
while(1):
    # to see the video, not essential for operation
    # Capture the video frame by frame
    frame = cam_result_1
    # Display the resulting frame
    
    
    # determine pressed key, used for test purposes
    pressed = cv.waitKey(1) & 0xFF

    # to stop video stream, press "q"

    if (pressed == ord('x')):
        i=i+1
        cv.destroyAllWindows()
    # capture an image to process
    while(i==2):

        
        if (pressed == ord('q')):
            cv.destroyAllWindows()
            flag = 1
            i=i+1
            break
        start = time.time()
        frame = cam_result_1
        
        # Display the resulting frame
        #cv.imshow('Live Video', frame)
        
        # Capture a frame
        image = cam_result_1
        image_r = cam_result_2
        # convert image to gray scale
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        image_r = cv.cvtColor(image_r, cv.COLOR_BGR2GRAY)
        image = perspective_2.perspective_2(image)
        image_r = perspective_2.perspective_2_r(image_r)
        #CLAHE (constant limited adaptive Histogram Equalization)
        #clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        #image = clahe.apply(image)
        #image_r = clahe.apply(image_r)
        
        # Display the resulting frame
        #cv.imshow('Image to process', image)

        # compare image with background image
        
        t=0
        try:
                cont, cont_img = img_compare.img_compare(background_image, image)
        except:
                t=t+1
                pass
        try:
                cont_r, cont_img_r = img_compare.img_compare(background_image_r, image_r)
        except:
                t=t+1
                pass
        if t==2:
                continue
        try:
                cv.imshow("back",background_image)
                cv.imshow("img",image)
                cv.imshow("out",cont_img)
                cv.waitKey(1)
        except:
                pass
        try:
                cv.imshow("back_r",background_image_r)
                cv.imshow("img_r",image_r)
                cv.imshow("out_r",cont_img_r)
                cv.waitKey(1)
        except: 
                pass
        #print("cont: ",cont)
        """
        queue1 = multiprocessing.Queue()
        queue2 = multiprocessing.Queue()
        process1 =multiprocessing.Process(target=img_compare.img_compare, args=(background_image, image,queue1))
        process2 =multiprocessing.Process(target=img_compare.img_compare, args=(background_image_r, image_r,queue2))

        process1.start()
        process2.start()
        process1.join()
        process2.join()
        cont, cont_img = queue1.get()
        cont_r, cont_img_r = queue2.get()
        """
        #print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")

        #perspective_img = cv.cvtColor(perspective_img, cv.COLOR_BGR2GRAY)

        #_,thresh=cv.threshold(cont_img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
        #pers_cont, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        # Largest interior rectange detection
        #cv.imshow('Image to process', cont_img)
        #cv.waitKey(0)
        #print("Rect1")
        try:
                rect_img, rect_points = rect_detect.rect_detect(cont,cont_img.shape)
        except:
                rect_img = np.zeros(background_image.shape,np.uint8)
                rect_points = np.array([639,479,0,0],dtype=np.int32)
        #print("Rect2")
        try:
                rect_img_r, rect_points_r = rect_detect.rect_detect(cont_r,cont_img_r.shape)
        except:
                rect_img_r = np.zeros(background_image.shape,np.uint8)
                rect_points_r = np.array([639,479,0,0],dtype=np.int32)
        """
        process3 =multiprocessing.Process(target=rect_detect.rect_detect, args=(cont,cont_img.shape,queue1))
        process4 =multiprocessing.Process(target=rect_detect.rect_detect, args=(cont_r,cont_img_r.shape,queue2))
        process3.start()
        process4.start()
        process3.join()
        process4.join()
        rect_img, rect_points = queue1.get()
        rect_img_r, rect_points_r = queue2.get()
        """

        cv.imshow('Detected Largest Interior Rectangle', rect_img)
        cv.imshow('Detected Largest Interior Rectangle r', rect_img_r)
        #cv.waitKey(0)
        x, y = per_dir_2.per_dir(shape = rect_img.shape, rect_points=rect_points,rect_points_r=rect_points_r)
        #x_t=x+x_t
            
        end = time.time()
        print("operation time:", (end - start), "   "   "seconds")

    """
    # Delay for proper operation, may not be used at all
    time.sleep(0.5)         # wait in seconds
    """
    
    if flag == 1:
        break


# After the loop release the cap object
vid.release()
# Destroy all the windows
cv.destroyAllWindows()
