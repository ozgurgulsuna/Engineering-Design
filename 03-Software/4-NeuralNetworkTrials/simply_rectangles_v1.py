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

# Define the parameters
learning_rate = 0.01
epochs = 100
n_hidden = 10
n_output = 4
n_input = 2500
# batch_size = 100
# n_train = 1000
# n_test = 100

# Defin the main function
def main():

    # Load the data
    data = pd.read_csv('data.csv')

    # Initialize the weights and biases
    parameters = initialize_parameters(n_input, n_hidden, n_output)

    # Train the network using Gradient Descent
    for i in range(epochs):
        # Forward propagate
        A2, cache = forward_propagate(data, parameters)

        # Back propagate
        grads = back_propagate(parameters, cache, data, data)

        # Update the weights and biases
        parameters = update_parameters(parameters, grads, learning_rate)

        # Calculate the loss
        loss = mse(data, A2)
        print("Loss after epoch %i: %f" %(i, loss))
        print(parameters)

    # Test the network
    #A2, cache = forward_propagate(data_test, parameters)
    #loss = mse(data_test, A2)
    #print("Loss after testing: %f" %(loss))


# Define a function to initialize weights and biases
def initialize_parameters(n_x, n_h, n_y):
    np.random.seed(1)
    W1 = np.random.randn(n_h, n_x) * 0.01
    b1 = np.zeros((n_h, 1))
    W2 = np.random.randn(n_y, n_h) * 0.01
    b2 = np.zeros((n_y, 1))
    parameters = {"W1": W1,
                  "b1": b1,
                  "W2": W2,
                  "b2": b2}
    return parameters

# Define a function to forward propagate
def forward_propagate(X, parameters):
    # Retrieve each parameter from the dictionary "parameters"
    W1 = parameters['W1']
    b1 = parameters['b1']
    W2 = parameters['W2']
    b2 = parameters['b2']

    # Implement Forward Propagation to calculate A2 (probabilities)
    Z1 = np.dot(W1, X) + b1
    A1 = sigmoid(Z1)
    Z2 = np.dot(W2, A1) + b2
    A2 = softmax(Z2)
    cache = {"Z1": Z1,
             "A1": A1,
             "Z2": Z2,
             "A2": A2}
    return A2, cache

# Define a function to back propagate
def back_propagate(parameters, cache, X, Y):
    m = X.shape[1]

    # First, retrieve W1 and W2 from the dictionary "parameters".
    W1 = parameters['W1']
    W2 = parameters['W2']

    # Retrieve also A1 and A2 from dictionary "cache".
    A1 = cache['A1']
    A2 = cache['A2']

    # Backward propagation: calculate dW1, db1, dW2, db2.
    dZ2 = A2 - Y
    dW2 = (1 / m) * np.dot(dZ2, A1.T)
    db2 = (1 / m) * np.sum(dZ2, axis=1, keepdims=True)
    dZ1 = np.dot(W2.T, dZ2) * sigmoid_derivative(A1)
    dW1 = (1 / m) * np.dot(dZ1, X.T)
    db1 = (1 / m) * np.sum(dZ1, axis=1, keepdims=True)

    grads = {"dW1": dW1,
             "db1": db1,
             "dW2": dW2,
             "db2": db2}
    return grads

# Define a function to update the weights and biases
def update_parameters(parameters, grads, learning_rate=1.2):
    # Retrieve each parameter from the dictionary "parameters"
    W1 = parameters['W1']
    b1 = parameters['b1']
    W2 = parameters['W2']
    b2 = parameters['b2']

    # Retrieve each gradient from the dictionary "grads"
    dW1 = grads['dW1']
    db1 = grads['db1']
    dW2 = grads['dW2']
    db2 = grads['db2']

    # Update rule for each parameter
    W1 = W1 - learning_rate * dW1
    b1 = b1 - learning_rate * db1
    W2 = W2 - learning_rate * dW2
    b2 = b2 - learning_rate * db2

    parameters = {"W1": W1,
                  "b1": b1,
                  "W2": W2,
                  "b2": b2}
    return parameters

# Define the softmax function
def softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis=0)

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

