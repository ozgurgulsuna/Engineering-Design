# this is the main code for coverage detection algorithm

# import opencv library
import cv2 as cv
import cv2
# main functions
import per_dir_2
import img_compare
import perspective_2
import rect_detect_2 as rect_detect
import background
# not essential visualization functions
import visualization as vs
import multiprocessing
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
vid = cv.VideoCapture(0) 
vid.set(cv2.CAP_PROP_SHARPNESS,15)
vid.set(cv2.CAP_PROP_BRIGHTNESS,0)
vid.set(cv2.CAP_PROP_SATURATION,37)                                               # 0 : webcam, to find other cameras, change the number
vid_r=cv.VideoCapture(2)                                                # 1 : reversed x y axis cam
vid_r.set(cv2.CAP_PROP_SHARPNESS,15)
vid_r.set(cv2.CAP_PROP_BRIGHTNESS,0)
vid_r.set(cv2.CAP_PROP_SATURATION,37)
_, frame = vid.read()
# background image is added to the system, image is determined in advance during calibration

#background_path = "Background.jpeg"
#background_image = cv.imread(background_path)
background_image,background_image_r = background.background(vid,vid_r)  #button=2
background_image = cv.cvtColor(background_image, cv.COLOR_BGR2GRAY)
background_image_r = cv.cvtColor(background_image_r, cv.COLOR_BGR2GRAY)

# add pole masks before perspective correction####################################################
# fixed pole
cv.rectangle(background_image,[245,0],[270,140],255,-1)
# bottom of movable pole
cv.rectangle(background_image,[270,75],[340,140],255,-1)
# slave pole can also be eliminated

# fixed pole
cv.rectangle(background_image_r,[245,0],[270,140],255,-1)
# bottom of movable pole
cv.rectangle(background_image_r,[270,75],[340,140],255,-1)
# slave pole can also be eliminated

##################################################################################################


background_image = perspective_2.perspective_2(background_image)
background_image_r = perspective_2.perspective_2(background_image_r)
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
        image_r = perspective_2.perspective_2(image_r)
        # Display the resulting frame
        #cv.imshow('Image to process', image)

        # compare image with background image
        try:
                cont, cont_img = img_compare.img_compare(background_image, image)
                cont_r, cont_img_r = img_compare.img_compare(background_image_r, image_r)
        except:
               continue
        cv.imshow("back",background_image)
        cv.imshow("img",image)
        cv.imshow("out",cont_img)
        cv.waitKey(1)
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
        rect_img, rect_points = rect_detect.rect_detect(cont,cont_img.shape)
        #print("Rect2")
        rect_img_r, rect_points_r = rect_detect.rect_detect(cont_r,cont_img_r.shape)
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

        #cv.imshow('Detected Largest Interior Rectangle', rect_img)
        #cv.waitKey(0)
        per_dir_2.per_dir(shape = rect_img.shape, rect_points=rect_points,rect_points_r=rect_points_r)

            
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
