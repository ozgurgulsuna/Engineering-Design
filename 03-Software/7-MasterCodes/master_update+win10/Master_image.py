import serial
import numpy as np
import time
import cv2 as cv
import threading


import background
import perspective_2
import img_compare
import per_dir_2
import rect_detect_2 as rect_detect


# Define commands
move_initialize_command = 'i'
move_command = 'm'
shutdown_command = 's'
error_command = 'e'
begin_command = 'b'
zero_command = 'z'
interpolation_interval = 5

def main():
    # Hello
    print("Hello World!")
    """
    # Establish connection with the serial ports
    ser_right = serial.Serial('/dev/serial/by-id/usb-STMicroelectronics_STM32_Virtual_ComPort_338C36623034-if00')   # open serial port
    print(ser_right.name)               # check which port was really used
    
    ser_middle = serial.Serial('/dev/serial/by-id/usb-STMicroelectronics_STM32_Virtual_ComPort_388D38403238-if00') # open serial port
    print(ser_middle.name)              # check which port was really used
    
    ser_left = serial.Serial('/dev/serial/by-id/usb-STMicroelectronics_STM32_Virtual_ComPort_386739803237-if00')   # open serial port
    print(ser_left.name)                # check which port was really used
    
    
    # Send zero command
    send_zero_command = input("Send zero command ('y' if 'yes')?: ")
    
    if send_zero_command == 'y':
        sent_message = zero_command.encode('utf-8')
        print(sent_message)
        print('')
        ser_right.write(sent_message)
        ser_left.write(sent_message)
    
    # Start initializing the system by moving it manually
    right_pole_initialize = input("Start initializing right pole ('y' if 'yes')?: ")

    while right_pole_initialize == 'y':
        
        move_inner = int(input("Enter the displacement for the inner motor (in mm): "))
        move_middle = int(input("Enter the displacement for the middle motor (in mm): "))
        move_outer = int(input("Enter the displacement for the outer motor (in mm): "))
        
        sent_message = move_initialize_command.encode('utf-8') + move_inner.to_bytes(2, 'big', signed = True) \
            + move_middle.to_bytes(2, 'big', signed = True) + move_outer.to_bytes(2, 'big', signed = True)
        
        print(sent_message)
        print('')
        ser_right.write(sent_message)

        # 'y' if initialization should be continued
        right_pole_initialize = input("Continue initializing?: ")
    
    # Send command to set the motor position related values to 0
    sent_message = begin_command.encode('utf-8')
    print(sent_message)
    print('')
    ser_right.write(sent_message)
    
    
    
    # Start initializing the system by moving it manually
    left_pole_initialize = input("Start initializing left pole ('y' if 'yes'): ")

    while left_pole_initialize == 'y':
        
        move_inner = int(input("Enter the displacement for the inner motor (in mm): "))
        move_middle = int(input("Enter the displacement for the middle motor (in mm): "))
        move_outer = int(input("Enter the displacement for the outer motor (in mm): "))
        
        sent_message = move_initialize_command.encode('utf-8') + move_inner.to_bytes(2, 'big', signed = True) \
            + move_middle.to_bytes(2, 'big', signed = True) + move_outer.to_bytes(2, 'big', signed = True)
        
        print(sent_message)
        print('')
        ser_left.write(sent_message)

        # 'y' if initialization should be continued
        left_pole_initialize = input("Continue initializing?: ")
    
    # Send command to set the motor positio related values to 0
    sent_message = begin_command.encode('utf-8')
    print(sent_message)
    print('')
    ser_left.write(sent_message)
    
    """
    
    # Initialize cameras, take background pictures, etc.
    initialize_camera()
    
    
    
    #background_image, background_image_r = take_background()
    background_image,background_image_r = background.background()
    
    
    
    
    background_image, background_image_r = process_background(background_image, background_image_r)

    # Start camera threads
    time.sleep(1)
    i = 1
    flag=0
    # repeat the same operation steps until the operation is terminated
    threading.Thread(target=camera_thread).start()
    threading.Thread(target=camera_thread_r).start()
    time.sleep(1)
    
    
    
    global x_t
    global y_t
    
    x_t=0
    y_t=0
    
    
    while True:
        
        move_x, move_y = get_xy(background_image, background_image_r)
        
        """
        move_x = int(input("Displacement in X axis (in mm): "))
        move_y = int(input("Displacement in Y axis (in mm): "))
        
        sent_message_middle = move_command.encode('utf-8') + move_x.to_bytes(2, 'big', signed = True) + move_y.to_bytes(2, 'big', signed = True)
        ser_middle.write(sent_message_middle)
        
        
        # Send move command w/ interpolation
        # send move y in the first step of interpolation
        first_step =int(abs(move_x) % interpolation_interval)
        if first_step !=0  :
            if move_x < 0:
                first_step = -first_step
            sent_message_right = move_command.encode('utf-8') + first_step.to_bytes(2, 'big', signed = True) + move_y.to_bytes(2, 'big', signed = True)
            ser_right.write(sent_message_right)

            move_x_neg = -first_step
            sent_message_left = move_command.encode('utf-8') + move_x_neg.to_bytes(2, 'big', signed = True) + move_y.to_bytes(2, 'big', signed = True)
            ser_left.write(sent_message_left)

            # Wait for acknowledge
            received_message = ser_right.readline().decode('utf-8')
            print(received_message)
        
            # If not acknowledged, shutdown
            if received_message != 'a':
                pass
                # sent_message = shutdown_command.encode('utf-8')
                # ser_right.write(sent_message)
                # ser_middle.write(sent_message)
                # ser_left.write(sent_message)

            # Wait for acknowledge
            received_message = ser_left.readline().decode('utf-8')
            print(received_message)
            
            # If not acknowledged, shutdown
            if received_message != 'a':
                pass
                # sent_message = shutdown_command.encode('utf-8')
                # ser_right.write(sent_message)
                # ser_middle.write(sent_message)
                # ser_left.write(sent_message)

            move_y = 0

        for step in range(int(abs(move_x)/interpolation_interval)):
            if move_x < 0:
                interval = -interpolation_interval
            else:
                interval = interpolation_interval

            sent_message_right = move_command.encode('utf-8') + interval.to_bytes(2, 'big', signed = True) + move_y.to_bytes(2, 'big', signed = True)
            ser_right.write(sent_message_right)

            move_x_neg = -interval
            sent_message_left = move_command.encode('utf-8') + move_x_neg.to_bytes(2, 'big', signed = True) + move_y.to_bytes(2, 'big', signed = True)
            ser_left.write(sent_message_left)

            # Wait for acknowledge
            received_message = ser_right.readline().decode('utf-8')
            print(received_message)
            
            # If not acknowledged, shutdown
            if received_message != 'a':
                pass
                # sent_message = shutdown_command.encode('utf-8')
                # ser_right.write(sent_message)
                # ser_middle.write(sent_message)
                # ser_left.write(sent_message)

            # Wait for acknowledge
            received_message = ser_left.readline().decode('utf-8')
            print(received_message)
            
            # If not acknowledged, shutdown
            if received_message != 'a':
                pass
                # sent_message = shutdown_command.encode('utf-8')
                # ser_right.write(sent_message)
                # ser_middle.write(sent_message)
                # ser_left.write(sent_message)

            if step == 0 :
                move_y = 0

        

        
        
        # Wait for acknowledge
        received_message = ser_middle.readline().decode('utf-8')
        print(received_message)
        
        # If not acknowledged, shutdown
        if received_message != 'a':
            pass
            # sent_message = shutdown_command.encode('utf-8')
            # ser_right.write(sent_message)
            # ser_middle.write(sent_message)
            # ser_left.write(sent_message)
        
        """
    """    

    # ser_right.close()             # close port
    # ser_middle.close()             # close port
    # ser_left.close()             # close port
    """

# This function will include the whole python code for running image processing to extract move_x & move_y
def get_xy(background_image, background_image_r):
    
    global x_t
    global y_t

    start = time.time()
    # frame = cam_result_1
    # Display the resulting frame
    # cv.imshow('Live Video', frame)
    
    # Capture a frame
    image = cam_result_1
    image_r = cam_result_2
    # convert image to gray scale
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    image_r = cv.cvtColor(image_r, cv.COLOR_BGR2GRAY)
    image = perspective_2.perspective_2(image)
    image_r = perspective_2.perspective_2(image_r)
    # Display the resulting frame
    # cv.imshow('Image to process', image)

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
           return get_xy(background_image, background_image_r)
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
    
    #print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")

    #perspective_img = cv.cvtColor(perspective_img, cv.COLOR_BGR2GRAY)

    #_,thresh=cv.threshold(cont_img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    #pers_cont, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

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

    cv.imshow('Detected Largest Interior Rectangle', rect_img)
    cv.imshow('Detected Largest Interior Rectangle r', rect_img_r)
    #cv.waitKey(0)
    delta_x, delta_y = per_dir_2.per_dir(shape = rect_img.shape, rect_points=rect_points,rect_points_r=rect_points_r)
    
    
    """
    # limitations
    x_limit_ref = 250
    if(x_t+delta_x < x_limit_ref and x_t+delta_x > -x_limit_ref):
        x_t=x_t+delta_x
    else:
        delta_x = (x_t+delta_x >= x_limit_ref) ? (x_limit_ref-x_t) : (-x_limit_ref-x_t)
        x_t = (x_t+delta_x >= x_limit_ref) ? (x_limit_ref) : (-x_limit_ref)
        
    # y fix #################################################################################################################################################################
    y_limit_ref = 350
    
    if(y_t+delta_y < y_limit_ref and y_t+delta_y > -y_limit_ref):
        y_t=y_t+delta_y
    else:
        delta_y = (y_t+delta_y >= y_limit_ref) ? (y_limit_ref-y_t) : (-y_limit_ref-y_t)
        y_t = (y_t+delta_y >= y_limit_ref) ? (y_limit_ref) : (-y_limit_ref)
        
    """
    
    end = time.time()
    print("operation time:", (end - start), "   "   "seconds")

    return delta_x, delta_y
    

def take_background(ser_right, ser_middle, ser_left, cap,cap_r):
    
    # Take eight background pictures
    for i in range(8):
        # Move the canopy as much as you like
        continue_moving = 'y'
        while continue_moving == 'y':
            move_x = int(input("Displacement in X axis (in mm): "))
            # move_y = int(input("Displacement in Y axis (in mm): "))
        
            # Send move command
            sent_message = move_command.encode('utf-8') + move_x.to_bytes(2, 'big', signed = True) # + move_y.to_bytes(2, 'big', signed = True)
            ser_right.write(sent_message)
            # ser_middle.write(sent_message)
            ser_left.write(sent_message)

            continue_moving = input("Continue taking background ('y' if yes)?")
        
        ### TAKE THE PHOTO HERE ###
        _ , back = cap.read()
        _ , back_r = cap_r.read()
        cv.imshow('Background{}'.format(i), cv.resize(back,(int(back.shape[1]),int(back.shape[0])),interpolation=cv.INTER_AREA))
        cv.imshow('Live Video_r{}'.format(i), cv.resize(back_r,(int(back.shape[1]),int(back.shape[0])),interpolation=cv.INTER_AREA))
        cv.imwrite('back/Back{}.jpeg'.format(i), back) #######directorrrrrry
        cv.imwrite('back_r/Back{}.jpeg'.format(i), back_r) #######directorrrrrry 
        cv.waitKey(0)
        
    background_image,background_image_r = background.background()
    return background_image, background_image_r

def initialize_camera():
    global vid
    global vid_r
    global frame
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

def process_background(background_image, background_image_r):
    background_image = cv.cvtColor(background_image, cv.COLOR_BGR2GRAY)
    background_image_r = cv.cvtColor(background_image_r, cv.COLOR_BGR2GRAY)
    
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

    background_image = perspective_2.perspective_2(background_image)
    background_image_r = perspective_2.perspective_2(background_image_r)
    
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

    return background_image, background_image_r
    

# Some weird mehmetcan fixes
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


if __name__ == "__main__":
    main()
