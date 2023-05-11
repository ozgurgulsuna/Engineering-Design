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