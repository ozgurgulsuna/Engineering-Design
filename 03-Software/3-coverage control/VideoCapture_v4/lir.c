#include <stdlib.h>
#include <stdio.h>
//usr def functs;
#define INT_MAX 2147483647 //usr def functs;

int * horizontal_adjacency_left2right(int* grid,int n_rows, int n_cols) {
    int i, j, span;
    int* result = calloc(n_rows * n_cols, sizeof(int));
    for (i = 0; i < n_rows; i++) {
        span = 0;
        for (j = n_cols-1; j >-1 ; j--){
            if(grid[i * n_cols + j]){
                span++;
            }
            else{
               span = 0;
            }
            result[i * n_cols + j]=span;
        }
    }
    return result;
}
//////////////////////////////////////////////////////////////////////////////////////
int * horizontal_adjacency_right2left(int* grid,int n_rows, int n_cols) {
    int i, j, span;
    int* result = calloc(n_rows * n_cols, sizeof(int));
    for (i = 0; i < n_rows; i++) {
        span = 0;
        for (j = 0; j<n_cols ; j++){
            if(grid[i * n_cols + j]){
                span++;
            }
            else{
               span = 0;
            }
            result[i * n_cols + j]=span;
        }
    }
    return result;
}
//////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////
int * vertical_adjacency_top2bottom(int* grid,int n_rows, int n_cols) {
    int i, j, span;
    int* result = calloc(n_rows * n_cols, sizeof(int));
    for (i = 0; i < n_cols; i++) {
        span = 0;
        for (j = n_rows-1; j >-1 ; j--){
            if(grid[j * n_cols + i]){
                span++;
            }
            else{
               span = 0;
            }
            result[j * n_cols + i]=span;
        }
    }
        return result;
}
//////////////////////////////////////////////////////////////////////////////////////
int * vertical_adjacency_bottom2top(int* grid,int n_rows, int n_cols) {
    int i, j, span;
    int* result = calloc(n_rows * n_cols, sizeof(int));
    for (i = 0; i < n_cols; i++) {
        span = 0;
        for (j = 0; j<n_rows ; j++){
            if(grid[j * n_cols + i]){
                span++;
            }
            else{
               span = 0;
            }
            result[j * n_cols + i]=span;
        }
    }
        return result;
}
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

int * h_vector_top2bottom(int*h_adjacency, int x, int y, int n_rows, int n_cols){
    int* subArray=calloc(n_rows-y, sizeof(int));
    for (int i = y; i < (n_rows); i++)
    {
        subArray[i-y] = *(h_adjacency + i * n_cols + x);
    }
    int vector_size = predict_vector_size(subArray,n_rows-y);
    int* h_vector = calloc(vector_size, sizeof(int));
    int * hell = calloc(vector_size, sizeof(int));
    int h = INT_MAX;
    for (int p = 0; p < vector_size; p++)
    {
        h = subArray[p]< h ? subArray[p] : h;
        h_vector[p] = h;
    }

    int size = sizeof(h_vector) / sizeof(sizeof(int));
    int *new_arr = malloc(size * sizeof(int));
    int unique_count = 1;
    new_arr[0]=0 ;
    for (int i = 0; i < vector_size; i++) {
        if (i == 0 || h_vector[i] != h_vector[i - 1]) {
            new_arr[unique_count] = h_vector[i];
            unique_count = unique_count + 1;
        }
    }
    new_arr[0]=unique_count;
    hell = new_arr;
    free(new_arr);
    free(h_vector);
    free(subArray);
    return hell;
}

//////////////////////////////////////////////////////////////////////////////////////
int * h_vector_bottom2top(int*h_adjacency, int x, int y, int n_rows, int n_cols){
    int* subArray=calloc(n_rows-y, sizeof(int));
    for (int i = y; i >= 0; i--)
    {
        subArray[y-i] = *(h_adjacency + i * n_cols + x);
    }
    int vector_size = predict_vector_size(subArray,n_rows-y);
    int* h_vector = calloc(vector_size, sizeof(int));
    int * hell = calloc(vector_size, sizeof(int));
    int h = INT_MAX;
    for (int p = 0; p < vector_size; p++)
    {
        h = subArray[p]< h ? subArray[p] : h;
        h_vector[p] = h;
    }

    int size = sizeof(h_vector) / sizeof(sizeof(int));
    int *new_arr = malloc(size * sizeof(int));
    int unique_count = 1;
    new_arr[0]=0 ;
    for (int i = 0; i < vector_size; i++) {
        if (i == 0 || h_vector[i] != h_vector[i - 1]) {
            new_arr[unique_count] = h_vector[i];
            unique_count = unique_count + 1;
        }
    }
    new_arr[0]=unique_count-1;
    free(new_arr);
    free(h_vector);
    free(subArray);
    hell = new_arr;
    return hell;
}

//////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////
int * v_vector_left2right(int*h_adjacency, int x, int y, int n_rows, int n_cols){
    int* subArray=calloc(n_cols-x, sizeof(int));
    for (int i = x; i < (n_cols); i++)
    {
        subArray[i-x] = *(h_adjacency + n_cols*y + i);
    }
    int vector_size = predict_vector_size(subArray,n_cols-x);
    int* v_vector = calloc(vector_size, sizeof(int));
    int * hell = calloc(vector_size, sizeof(int));
    int v = INT_MAX;
    for (int p = 0; p < vector_size; p++)
    {
        v = subArray[p]< v ? subArray[p] : v;
        v_vector[p] = v;
    }

    int *new_arr = calloc(vector_size, sizeof(int));
    int unique_count = 1;
    new_arr[0]=0 ;
    for (int i = 0; i < vector_size; i++) {
        if (i == 0 || v_vector[i] != v_vector[i - 1]) {
            new_arr[unique_count] = v_vector[i];
            unique_count = unique_count + 1;
        }
    }
    new_arr[0]=unique_count-1;
    free(new_arr);
    free(v_vector);
    free(subArray);
    hell = new_arr;
    return hell;
}


//////////////////////////////////////////////////////////////////////////////////////

int * v_vector_right2left(int*h_adjacency, int x, int y, int n_rows, int n_cols){
    int* subArray=calloc(n_cols-x, sizeof(int));
    for (int i = x; i >= 0; i--)
    {
        subArray[i-x] = *(h_adjacency + n_cols*y + i);
    }
    int vector_size = predict_vector_size(subArray,n_cols-x);
    int* v_vector = calloc(vector_size, sizeof(int));
    int * hell = calloc(vector_size, sizeof(int));
    int v = INT_MAX;
    for (int p = 0; p < vector_size; p++)
    {
        v = subArray[p]< v ? subArray[p] : v;
        v_vector[p] = v;
    }

    int *new_arr = calloc(vector_size, sizeof(int));
    int unique_count = 1;
    new_arr[0]=0 ;
    for (int i = 0; i < vector_size; i++) {
        if (i == 0 || v_vector[i] != v_vector[i - 1]) {
            new_arr[unique_count] = v_vector[i];
            unique_count = unique_count + 1;
        }
    }
    new_arr[0]=unique_count-1;
    free(new_arr);
    free(v_vector);
    free(subArray);
    hell = new_arr;
    return hell;
}

//////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////

int* spans(int* h_vector, int * v_vector, int length){
    int * array = calloc(length*2,sizeof(int));
    int i;
    // for loop to fill array
    for (i = 0; i < length; i++){
        array[2*i] = h_vector[i];
        array[2*i+1] = v_vector[length-1-i];
    }
    return array;
    // returns 1d array of span matrix, dont forget to free memory!!!!!!!!!!!!!!!!!!!!
}

//////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////
int* get_xy_array(int x, int y, int* span, int size_xy, int mode){
    int* array = calloc(2 * size_xy, sizeof(int));
    for(int i = 0; i < size_xy; i++){
    array[2*i]=x;
    array[2*i+1]=y;
    }
    if(mode == 1){
        for(int i = 0; i < size_xy; i++){
            array[2*i]=array[2*i]-span[2*i]+1;
        }
    }
    if(mode == 2){
        for(int i = 0; i < size_xy; i++){
            array[2*i+1]=array[2*i+1]-span[2*i+1]+1;
        }
    }
    if(mode == 3){
        for(int i = 0; i < size_xy; i++){
            array[2*i]=array[2*i]-span[2*i]+1;
            array[2*i+1]=array[2*i+1]-span[2*i+1]+1;
        }
    }
    return array;
}


//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////


// contour taken in as contour=np.squeeze(contour[0][0]) then contour=contour.astype(np.int.32)
int* largest_interior_rectangle(int* grid,int* contour,int n_rows, int n_cols,int n_contour){
    //h_left2right, h_right2left, v_top2bottom, v_bottom2top = adjacencies
    int* h_left2right = horizontal_adjacency_left2right(grid, n_rows, n_cols);
    int* h_right2left = horizontal_adjacency_right2left(grid, n_rows, n_cols);
    int* v_top2bottom = vertical_adjacency_top2bottom(grid, n_rows, n_cols);
    int* v_bottom2top = vertical_adjacency_bottom2top(grid, n_rows, n_cols);
    ////////////////////////////////////////////////////////////////////////////////////////
    //span_map = np.zeros(shape + (2,), "uint32")
    //vazgeçtim (who needs span_map anyway)


    int i, x, y, x_correct,y_correct,w_correct=0,h_correct=0;
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

        int* v_l2r_t2b = v_vector_top2bottom(v_top2bottom, x, y, n_rows, n_cols);//0
        int* v_r2l_t2b = v_vector_top2bottom(v_bottom2top, x, y, n_rows, n_cols);//1
        int* v_l2r_b2t = v_vector_bottom2top(v_top2bottom, x, y, n_rows, n_cols);//2
        int* v_r2l_b2t = v_vector_bottom2top(v_bottom2top, x, y, n_rows, n_cols);//3
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
           if(span_array_0[2*i]*span_array_0[2*i+1]<w_correct*h_correct){
                w_correct=span_array_0[2*i];
                h_correct=span_array_0[2*i+1];
                x_correct=xy_array_0[2*i];
                y_correct=xy_array_0[2*i+1];
           }
        }

        for(i=0;i<h_r2l_t2b[0];i++){
            if(span_array_1[2*i]*span_array_1[2*i+1]<w_correct*h_correct){
                w_correct=span_array_1[2*i];
                h_correct=span_array_1[2*i+1];
                x_correct=xy_array_1[2*i];
                y_correct=xy_array_1[2*i+1];
            }
        }

        for(i=0;i<h_l2r_b2t[0];i++){
            if(span_array_2[2*i]*span_array_2[2*i+1]<w_correct*h_correct){
                w_correct=span_array_2[2*i];
                h_correct=span_array_2[2*i+1];
                x_correct=xy_array_2[2*i];
                y_correct=xy_array_2[2*i+1];
            }
        }

        for(i=0;i<h_r2l_b2t[0];i++){
            if(span_array_3[2*i]*span_array_3[2*i+1]<w_correct*h_correct){
                w_correct=span_array_3[2*i];
                h_correct=span_array_3[2*i+1];
                x_correct=xy_array_3[2*i];
                y_correct=xy_array_3[2*i+1];
            }
        }


        //free memory
        free(h_l2r_t2b);
        free(h_r2l_t2b);
        free(h_l2r_b2t);
        free(h_r2l_b2t);
        free(v_l2r_t2b);
        free(v_r2l_t2b);
        free(v_l2r_b2t);
        free(v_r2l_b2t);
        free(span_array_0);
        free(span_array_1);
        free(span_array_2);
        free(span_array_3);
        free(xy_array_0);
        free(xy_array_1);
        free(xy_array_2);
        free(xy_array_3);

    }
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