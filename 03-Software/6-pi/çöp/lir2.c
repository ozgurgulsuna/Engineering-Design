#include <stdlib.h>
#include <stdio.h>
//usr def functs;
#define INT_MAX 2147483647 //usr def functs;
//////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////
int predict_vector_size(int array[], int length) {
    int count = 0;
    int* zero_indices = calloc(length, sizeof(int));
    for (int i = 0; i < length; i++) {
        if (array[i] == 0) {
            zero_indices[count++] = i;
        }
    }
    if (count == 0) {
        if (length == 0) {
            return 0;
        }
        return length;
    }
    return zero_indices[0];
}
//////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////



int* largest_interior_rectangle(int* grid,int* contour,int n_rows, int n_cols,int n_contour){
    //h_left2right, h_right2left, v_top2bottom, v_bottom2top = adjacencies
    
    
    
    int* h_left2right = horizontal_adjacency_left2right(grid, n_rows, n_cols);
    int* h_right2left = horizontal_adjacency_right2left(grid, n_rows, n_cols);
    int* v_top2bottom = vertical_adjacency_top2bottom(grid, n_rows, n_cols);
    int* v_bottom2top = vertical_adjacency_bottom2top(grid, n_rows, n_cols);
    ////////////////////////////////////////////////////////////////////////////////////////
    //span_map = np.zeros(shape + (2,), "uint32")
    //vazgeçtim (who needs span_map anyway)
	
    int i, x, y, x_correct=0,y_correct=0,w_correct=0,h_correct=0;//
    for (i = 0; i < n_contour; i++){
        //x, y = contour[idx, 0], contour[idx, 1]
        x = contour[2*i];
        y = contour[2*i+1];
	
        ////////////////////////////////////////////////////////////////////////////////////
        //h_vectors = h_vectors_all_directions(h_left2right, h_right2left, x, y)
        //v_vectors = v_vectors_all_directions(v_top2bottom, v_bottom2top, x, y)
        int* h_l2r_t2b = h_vector_top2bottom(h_left2right, x, y, n_rows, n_cols);//0
        int* h_r2l_t2b = h_vector_top2bottom(h_right2left, x, y, n_rows, n_cols);//1
        int* h_l2r_b2t = h_vector_bottom2top(h_left2right, x, y, n_rows, n_cols);//2
        int* h_r2l_b2t = h_vector_bottom2top(h_right2left, x, y, n_rows, n_cols);//3

        int* v_l2r_t2b = v_vector_left2right(v_top2bottom, x, y, n_rows, n_cols);//0
        int* v_r2l_t2b = v_vector_right2left(v_top2bottom, x, y, n_rows, n_cols);//1
        int* v_l2r_b2t = v_vector_left2right(v_bottom2top, x, y, n_rows, n_cols);//2
        int* v_r2l_b2t = v_vector_right2left(v_bottom2top, x, y, n_rows, n_cols);//3
        ////////////////////////////////////////////////////////////////////////////////////
        //span_arrays = spans_all_directions(h_vectors, v_vectors)
        int* span_array_0 = spans(h_l2r_t2b+1, v_l2r_t2b+1, h_l2r_t2b[0]);//0
        int* span_array_1 = spans(h_r2l_t2b+1, v_r2l_t2b+1, h_r2l_t2b[0]);//1
        int* span_array_2 = spans(h_l2r_b2t+1, v_l2r_b2t+1, h_l2r_b2t[0]);//2
        int* span_array_3 = spans(h_r2l_b2t+1, v_r2l_b2t+1, h_r2l_b2t[0]);//3
        ////////////////////////////////////////////////////////////////////////////////////
        //xy_arrays = get_xy_arrays(x, y, span_arrays)
        int* xy_array_0 = get_xy_array(x, y, span_array_0, h_l2r_t2b[0], 0);//0
        int* xy_array_1 = get_xy_array(x, y, span_array_1, h_r2l_t2b[0], 1);//1
        int* xy_array_2 = get_xy_array(x, y, span_array_2, h_l2r_b2t[0], 2);//2
        int* xy_array_3 = get_xy_array(x, y, span_array_3, h_r2l_b2t[0], 3);//3
        ////////////////////////////////////////////////////////////////////////////////////
        //damn output if you can do better, try it then.
        for(i=0;i<h_l2r_t2b[0];i++){
           if(span_array_0[2*i]*span_array_0[2*i+1]>w_correct*h_correct){
                w_correct=span_array_0[2*i];
                h_correct=span_array_0[2*i+1];
                x_correct=xy_array_0[2*i];
                y_correct=xy_array_0[2*i+1];
           }
        }

        for(i=0;i<h_r2l_t2b[0];i++){
            if(span_array_1[2*i]*span_array_1[2*i+1]>w_correct*h_correct){
                w_correct=span_array_1[2*i];
                h_correct=span_array_1[2*i+1];
                x_correct=xy_array_1[2*i];
                y_correct=xy_array_1[2*i+1];
            }
        }

        for(i=0;i<h_l2r_b2t[0];i++){
            if(span_array_2[2*i]*span_array_2[2*i+1]>w_correct*h_correct){
                w_correct=span_array_2[2*i];
                h_correct=span_array_2[2*i+1];
                x_correct=xy_array_2[2*i];
                y_correct=xy_array_2[2*i+1];
            }
        }

        for(i=0;i<h_r2l_b2t[0];i++){
            if(span_array_3[2*i]*span_array_3[2*i+1]>w_correct*h_correct){
                w_correct=span_array_3[2*i];
                h_correct=span_array_3[2*i+1];
                x_correct=xy_array_3[2*i];
                y_correct=xy_array_3[2*i+1];
            }
        y_correct=xy_array_3[2*i+1];
        }


        //free memory
        free(h_l2r_t2b);
        free(h_r2l_t2b);
        free(h_l2r_b2t);
        free(h_r2l_b2t);
        //free(v_l2r_t2b);
        free(v_r2l_t2b);
        //free(v_l2r_b2t);
        free(v_r2l_b2t);
        free(span_array_0);
        free(span_array_1);
        free(span_array_2);
        free(span_array_3);
        free(xy_array_0);
        free(xy_array_1);
        //free(xy_array_2);
        //free(xy_array_3);

    }//

    free(h_left2right);
    free(h_right2left);
    free(v_top2bottom);
    free(v_bottom2top);

    int* output = (int*)malloc(4*sizeof(int));
    output[0]=x_correct;
    output[1]=y_correct;
    output[2]=w_correct;
    output[3]=h_correct;
    return output;
}
