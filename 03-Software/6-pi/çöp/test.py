import ctypes
import numpy as np
from ctypes import c_int, POINTER
# Load the shared library
lib = ctypes.CDLL('./lir.so')

# Define the argument and return types of the C function


                

lib.horizontal_adjacency_left2right.restype = ctypes.POINTER(c_int)
lib.horizontal_adjacency_left2right.argtypes = [POINTER(c_int), c_int, c_int]
lib.horizontal_adjacency_right2left.restype = ctypes.POINTER(c_int)
lib.horizontal_adjacency_right2left.argtypes = [POINTER(c_int), c_int, c_int]
lib.vertical_adjacency_top2bottom.restype = ctypes.POINTER(c_int)
lib.vertical_adjacency_top2bottom.argtypes = [POINTER(c_int), c_int, c_int]
lib.vertical_adjacency_bottom2top.restype = ctypes.POINTER(c_int)
lib.vertical_adjacency_bottom2top.argtypes = [POINTER(c_int), c_int, c_int]
lib.h_vector_top2bottom.restype = ctypes.POINTER(c_int)
lib.h_vector_top2bottom.argtypes = [POINTER(c_int), c_int, c_int, c_int]
lib.h_vector_bottom2top.restype = ctypes.POINTER(c_int)
lib.h_vector_bottom2top.argtypes = [POINTER(c_int), c_int, c_int, c_int]
lib.v_vector_left2right.restype = ctypes.POINTER(c_int)
lib.v_vector_left2right.argtypes = [POINTER(c_int), c_int, c_int, c_int]
lib.v_vector_right2left.restype = ctypes.POINTER(c_int)
lib.v_vector_right2left.argtypes = [POINTER(c_int), c_int, c_int, c_int]

lib.spans.restype = ctypes.POINTER(c_int)
lib.spans.argtypes = [POINTER(c_int), POINTER(c_int), c_int]
lib.largest_interior_rectangle.restype = ctypes.POINTER(c_int)
lib.largest_interior_rectangle.argtypes = [POINTER(c_int),POINTER(c_int), c_int, c_int, c_int]


grid= np.array([[0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 1, 1, 0, 0, 0],
                 [0, 0, 1, 1, 1, 1, 1, 0, 0],
                 [0, 0, 1, 1, 1, 1, 1, 1, 0],
                 [0, 0, 1, 1, 1, 1, 1, 1, 0],
                 [0, 1, 1, 1, 1, 1, 1, 0, 0],
                 [0, 0, 1, 1, 1, 1, 0, 0, 0],
                 [0, 0, 1, 1, 1, 1, 0, 0, 0],
                 [1, 1, 1, 1, 1, 1, 0, 0, 0],
                 [1, 1, 0, 0, 0, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1]], dtype=np.int32)
# Convert the NumPy array to a C-compatible array
arr = grid.ctypes.data_as(POINTER(c_int))
n_rows = len(grid)
n_cols = len(grid[1])
print("Original array:\n", grid)
# Call the C function to manipulate the array
manipulated_arr = lib.vertical_adjacency_bottom2top(arr, n_rows, n_cols)
# Convert the C-compatible pointer to a NumPy array
anipulated_arr = np.ctypeslib.as_array(manipulated_arr, shape=(n_rows, n_cols))
print("Manipulated array:\n", anipulated_arr)
manipulated_arr = lib.h_vector_top2bottom(manipulated_arr,2,0,n_rows, n_cols)
manipulated_arr = np.ctypeslib.as_array(manipulated_arr, shape=(1, n_cols))

# Print the original and manipulated array

print("Manipulated array:\n", manipulated_arr)
################################################################
grid2= np.array([  [0, 1, 1, 0, 1, 0],
		   [0, 1, 1, 1, 0, 0],
		   [0, 1, 1, 1, 0, 0],
		   [0, 1, 0, 0, 0, 0],
		   [0, 0, 0, 0, 0, 0]],dtype=np.int32)
arr2 = grid2.ctypes.data_as(POINTER(c_int))
n_rows = len(grid2)
n_cols = len(grid2[1])

h_left2right = lib.horizontal_adjacency_left2right(arr2, n_rows, n_cols)
h_right2left = lib.horizontal_adjacency_right2left(arr2, n_rows, n_cols)
v_top2bottom = lib.vertical_adjacency_top2bottom(arr2, n_rows, n_cols)
v_bottom2top = lib.vertical_adjacency_bottom2top(arr2, n_rows, n_cols)
contour=np.array([[1,0],[2,0],[2,1],[3,1],[3,2],[2,2],[1,3],[1,2],[1,1]],dtype=np.int32)
cont=contour.ctypes.data_as(POINTER(c_int))
n_contour=9

x = contour[0][0]
y = contour[0][1]

h_l2r_t2b = lib.h_vector_top2bottom(h_left2right, x, y, n_rows, n_cols)#;//0
h_r2l_t2b = lib.h_vector_top2bottom(h_right2left, x, y, n_rows, n_cols)#;//1
h_l2r_b2t = lib.h_vector_bottom2top(h_left2right, x, y, n_rows, n_cols)#;//2
h_r2l_b2t = lib.h_vector_bottom2top(h_right2left, x, y, n_rows, n_cols)#;//3

v_l2r_t2b = lib.v_vector_left2right(v_top2bottom, x, y, n_rows, n_cols)#;//0
v_r2l_t2b = lib.v_vector_right2left(v_top2bottom, x, y, n_rows, n_cols)#;//1
v_l2r_b2t = lib.v_vector_left2right(v_bottom2top, x, y, n_rows, n_cols)#;//2
v_r2l_b2t = lib.v_vector_right2left(v_bottom2top, x, y, n_rows, n_cols)#;//3

n=3
manipulated_arr = np.ctypeslib.as_array(h_l2r_t2b, shape=(1, n))
print("h_l2r_t2b :\n", manipulated_arr)
manipulated_arr = np.ctypeslib.as_array(h_left2right, shape=(n_rows, n_cols))
print("h_left2right :\n", manipulated_arr)

manipulated_arr = np.ctypeslib.as_array(h_r2l_t2b, shape=(1, n))
print("h_r2l_t2b array:\n", manipulated_arr)
manipulated_arr = np.ctypeslib.as_array(h_right2left, shape=(n_rows, n_cols))
print("h_right2left array:\n", manipulated_arr)

manipulated_arr = np.ctypeslib.as_array(h_l2r_b2t, shape=(1, n))
print("h_l2r_b2t array:\n", manipulated_arr)
manipulated_arr = np.ctypeslib.as_array(h_left2right, shape=(n_rows, n_cols))
print("h_left2right array:\n", manipulated_arr)

manipulated_arr = np.ctypeslib.as_array(h_r2l_b2t, shape=(1, n))
print("h_r2l_b2t array:\n", manipulated_arr)
manipulated_arr = np.ctypeslib.as_array(h_right2left, shape=(n_rows, n_cols))
print("h_right2left array:\n", manipulated_arr)



##############################################################################
n=4
manipulated_arr = np.ctypeslib.as_array(v_l2r_t2b, shape=(1, n))
print("v_l2r_t2b array:\n", manipulated_arr)
manipulated_arr = np.ctypeslib.as_array(v_top2bottom, shape=(n_rows, n_cols))
print("v_top2bottom array:\n", manipulated_arr)

manipulated_arr = np.ctypeslib.as_array(v_r2l_t2b, shape=(1, n))
print("v_r2l_t2b array:\n", manipulated_arr)
manipulated_arr = np.ctypeslib.as_array(v_top2bottom, shape=(n_rows, n_cols))
print("v_top2bottom array:\n", manipulated_arr)

manipulated_arr = np.ctypeslib.as_array(v_l2r_b2t, shape=(1, n))
print("v_l2r_b2t array:\n", manipulated_arr)
manipulated_arr = np.ctypeslib.as_array(v_bottom2top, shape=(n_rows, n_cols))
print("v_bottom2top array:\n", manipulated_arr)

manipulated_arr = np.ctypeslib.as_array(v_r2l_b2t, shape=(1, n))
print("v_r2l_b2t array:\n", manipulated_arr)
manipulated_arr = np.ctypeslib.as_array(v_bottom2top, shape=(n_rows, n_cols))
print("v_bottom2top array:\n", manipulated_arr)
##############################################################################

pt=np.ctypeslib.as_array(h_l2r_t2b, shape=(1, 1))
print(pt)
pt=np.ctypeslib.as_array(h_r2l_t2b, shape=(1, 1))
print(pt)
pt=np.ctypeslib.as_array(h_l2r_b2t, shape=(1, 1))
print(pt)
pt=np.ctypeslib.as_array(h_r2l_b2t, shape=(1, 1))
print(pt)
span_array_0 = lib.spans(h_l2r_t2b, v_l2r_t2b, 2)#;//0
span_array_1 = lib.spans(h_r2l_t2b, v_r2l_t2b, 1)#;//1
span_array_2 = lib.spans(h_l2r_b2t, v_l2r_b2t, 1)#;//2
span_array_3 = lib.spans(h_r2l_b2t, v_r2l_b2t, 1)#;//3

manipulated_arr = np.ctypeslib.as_array(span_array_0, shape=(2, 2))
print("span_array_0 array:\n", manipulated_arr)
manipulated_arr = np.ctypeslib.as_array(span_array_1, shape=(1, 2))
print("span_array_1 array:\n", manipulated_arr)
manipulated_arr = np.ctypeslib.as_array(span_array_2, shape=(1, 2))
print("span_array_2 array:\n", manipulated_arr)
manipulated_arr = np.ctypeslib.as_array(span_array_3, shape=(1, 2))
print("span_array_3 array:\n", manipulated_arr)

rect=lib.largest_interior_rectangle(arr2, cont, n_rows, n_cols,n_contour)
manipulated_arr = np.ctypeslib.as_array(rect, shape=(1, 4))
print("rect array:\n", manipulated_arr)




