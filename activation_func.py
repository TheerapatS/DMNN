import math
import numpy as np


def select_func (activation_function,dif):
    if activation_function == 0:
        if dif:
            return dif_sigmoid()
        else :
            return sigmoid()
    elif activation_function == 1:
        if dif:
            return dif_tanh()
        else :
            return tanh()
    elif activation_function == 2:
        if dif:
            return dif_ReLU()
        else :
            return ReLU()
    elif activation_function == 3:
        if dif:
            return dif_Leaky_ReLU()
        else :
            return Leaky_ReLU()

def sigmoid():

def tanh():

def ReLU():

def Leaky_ReLU():

def dif_sigmoid():

def dif_tanh():

def dif_ReLU():

def dif_Leaky_ReLU():