# Description: This script will train a simple neural network to 
# find the position of the rectangles in the image. The network will
# be trained on a dataset of 1000 images. There will also be a test
# set of 100 images. The network will be trained using Gradient Descent.
# The network will be trained using the following parameters:
#
# 1. Learning Rate: 0.01
# 2. Number of Epochs: 100 (number of times the network will be trained)
# 3. Number of Hidden Layers: 1
# 4. Number of Neurons in Hidden Layer: 10
# 5. Number of Output Neurons: 4 (x1,y1,x2,y2)
# 6. Activation Function: Sigmoid
# 7. Loss Function: Mean Squared Error
# 8. Optimizer: Gradient Descent
# 9. Batch Size: 100 (number of images to be trained at a time)
# 10. Number of Training Images: 1000
# 11. Number of Test Images: 100

# Import the necessary libraries
import numpy as np
import pandas as pd

# Define the sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Define the derivative of the sigmoid function
def sigmoid_derivative(x):
    return x * (1 - x)

# Define the mean squared error function
def mse(y_true, y_pred):
    return np.mean(np.square(y_true - y_pred))

# Define the derivative of the mean squared error function
def mse_derivative(y_true, y_pred):
    return 2 * (y_pred - y_true) / y_true.size

# Read the data from the csv file
data = pd.read_csv('rectangles.csv')

# Print the head of the data
print(data.head())

data = np.array(data)
m, n = data.shape
np.random.shuffle(data)

data_test = data
