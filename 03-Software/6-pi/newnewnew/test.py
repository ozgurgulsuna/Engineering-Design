# this is the main code for coverage detection algorithm

# import opencv library
import cv2 as cv

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

# define a video capture object
vid = cv.VideoCapture(0)                                                # 0 : webcam, to find other cameras, change the number
vid_r=cv.VideoCapture(2)                                                # 1 : reversed x y axis cam
_, frame = vid.read()
# background image is added to the system, image is determined in advance during calibration

#background_path = "Background.jpeg"
#background_image = cv.imread(background_path)
background_image,background_image_r = background.background(vid,vid_r)  #button=2
background_image = cv.cvtColor(background_image, cv.COLOR_BGR2GRAY)
background_image_r = cv.cvtColor(background_image_r, cv.COLOR_BGR2GRAY)
background_image = perspective_2.perspective_2(background_image)
background_image_r = perspective_2.perspective_2(background_image_r)
time.sleep(1)
i = 1
flag=0
# repeat the same operation steps until the operation is terminated
while(1):
    # to see the video, not essential for operation
    # Capture the video frame by frame
    _, frame = vid.read()
    # Display the resulting frame
    cv.imshow('Live Video', frame)
    
    # determine pressed key, used for test purposes
    pressed = cv.waitKey(1) & 0xFF

    # to stop video stream, press "q"

    if (pressed == ord('x')):
        i=i+1
    # capture an image to process
    while(i==2):
        if (pressed == ord('q')):
            cv.destroyAllWindows()
            flag = 1
            break
        start = time.time()

        # Capture a frame
        ret, image = vid.read()
        _, image_r = vid_r.read()
        # convert image to gray scale
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        image_r = cv.cvtColor(image_r, cv.COLOR_BGR2GRAY)
        image = perspective_2.perspective_2(image)
        image_r = perspective_2.perspective_2(image_r)
        # Display the resulting frame
        #cv.imshow('Image to process', image)

        # compare image with background image
        cont, cont_img = img_compare.img_compare(background_image, image)
        cont_r, cont_img_r = img_compare.img_compare(background_image_r, image_r)
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
        cont_r, cont_img_r = queue2.get()"""
        print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")

        #perspective_img = cv.cvtColor(perspective_img, cv.COLOR_BGR2GRAY)

        #_,thresh=cv.threshold(cont_img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
        #pers_cont, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        # Largest interior rectange detection
        cv.imshow('Image to process', cont_img)
        cv.waitKey(0)
        rect_img, rect_points = rect_detect.rect_detect([cont],cont_img.shape)
        rect_img_r, rect_points_r = rect_detect.rect_detect([cont_r],cont_img_r.shape)
        """
        process3 =multiprocessing.Process(target=rect_detect.rect_detect, args=([cont],cont_img.shape,queue1))
        process4 =multiprocessing.Process(target=rect_detect.rect_detect, args=([cont_r],cont_img_r.shape,queue2))
        process3.start()
        process4.start()
        process3.join()
        process4.join()
        rect_img, rect_points = queue1.get()
        rect_img_r, rect_points_r = queue2.get()"""


        cv.imshow('Detected Largest Interior Rectangle', rect_img)
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
