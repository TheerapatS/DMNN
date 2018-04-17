import math
import numpy as np


def act_func (x,activation_function,dif=False):
    if activation_function == 0:
        if dif:
            return dif_sigmoid(x)
        else :
            return sigmoid(x)
    elif activation_function == 1:
        if dif:
            return dif_tanh(x)
        else :
            return tanh(x)
    elif activation_function == 2:
        if dif:
            return dif_ReLU(x)
        else :
            return ReLU(x)
    elif activation_function == 3:
        if dif:
            return dif_Leaky_ReLU(x)
        else :
            return Leaky_ReLU(x)

def sigmoid(x):
    return (1/(1+(math.exp((-1)*(x)))))

def tanh(x):
    return (math.exp(x) - math.exp((-1)*(x)))/(math.exp(x) + math.exp((-1)*(x)))

def ReLU(x):
    if x < 0:
        return 0
    else :
        return x

def Leaky_ReLU():
    if x < 0:
        return 0.01 * x
    else :
        return x

def dif_sigmoid(n):
    return (n) * (1 - n)

def dif_tanh(n):
    return 1 - ((n)*(n))

def dif_ReLU(n):
    if n == 0:
        return 0
    else :
        return 1

def dif_Leaky_ReLU(n):
    if n < 0:
        return 0.01
    else :
        return 1