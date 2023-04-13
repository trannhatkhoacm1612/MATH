import numpy as np

def backward_propagation(A, X, Y):
    m = X.shape[1]
    
    dZ = A - Y
    dW = 1/m * np.matmul(dZ, X.T)
    db = 1/m * np.sum(dZ, axis = 1, keepdims = True)
    
    grads = {"dW": dW,
             "db": db}
    
    return grads

def update_parameters(parameters, grads, learning_rate = 2):
    
    W = parameters["W"]
    b = parameters["b"]
    
    dW = grads["dW"]
    db = grads["db"]
    
    W = W - learning_rate * dW
    b = b - learning_rate * db
    
    parameters = {"W": W,
                  "b": b}
    
    return parameters

def train_nn(parameters, A, X, Y):
    grads = backward_propagation(A, X, Y)
    
    parameters = update_parameters(parameters, grads)
    
    return parameters
