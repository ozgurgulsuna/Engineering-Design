import cv2 as cv
import numpy as np
import time
#from lir_within_contour import largest_interior_rectangle \
#    as lir
import ctypes
from ctypes import c_int, POINTER
# Load the shared library
lib = ctypes.CDLL('./lir.so')
lib.largest_interior_rectangle.restype = (c_int)
lib.largest_interior_rectangle.argtypes = [POINTER(c_int),POINTER(c_int), c_int, c_int, c_int,POINTER(c_int)]


def rect_detect(conts,shape,queue):
    start = time.time()
    # Import your picture
    # Color it in gray

    # Create our mask by selecting the non-zero values of the picture
    # Select the contour
    # if your mask is incurved or if you want better results, 
    # you may want to use cv2.CHAIN_APPROX_NONE instead of cv2.CHAIN_APPROX_SIMPLE, 
    # but the rectangle search will be longer
    recto=[]
    blank=np.zeros(shape,dtype="uint8")
    for x in conts:
        mask = np.zeros(shape, dtype='uint8')
        contour = np.squeeze(x[0][:, 0, :])
        n_contour = len(contour)

        #print(contour)
        cv.drawContours(mask, x, -1, 255, -1)
        grid=mask>0
        #cv.imshow("mask(grid)", (grid*255).astype("uint8"))
        contour = contour.astype("uint32", order="C")
	
        n_rows = len(grid)
        n_cols = len(grid[1])
        #print(contour.ndim)
        #grid=grid.flatten()
        grid=grid.astype(np.int32)
        gr=grid.ctypes.data_as(POINTER(c_int))
        print(grid)
        cont=contour.ctypes.data_as(POINTER(c_int))
        rect=np.array([0,0,0,0],dtype=np.int32)
        rc=rect.ctypes.data_as(POINTER(c_int))
        a=lib.largest_interior_rectangle(gr, cont, n_rows, n_cols,n_contour,rc)



        cv.rectangle(blank,(rect[0],rect[1]),(rect[2]+rect[0],rect[3]+rect[1]),255,-1)
        recto.append([rect])

    #cv.imshow("hey", blank)
    end = time.time()
    print(end - start)
    #cv.waitKey(0)
    #return blank,rect
    queue.put([blank, rect])


