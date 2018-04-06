import pandas
import math
from copy import deepcopy

def zerolistmaker (n):
    return [0] * n

def pre_process (input_data_set, a, b):
    mean_of_column = [0] * len(input_data_set)
    for i in range(1,78):
        mean_temp = 0.0
        n = 0
        for j in input_data_set[i]:
            if not math.isnan(j):
                mean_temp += j
                n += 1
        mean_of_column[i] = mean_temp/n
    data_set = []
    index = 0
    for i in range(a,len(input_data_set)-b):
        data_set.append([])
        for j in input_data_set[i]:
            if j == 'Control' or j == 'Memantine' or j == 'C/S':
                data_set[index].append(0)
            elif j == 'Ts65Dn' or j == 'Saline' or j == 'S/C':
                data_set[index].append(1)
            elif math.isnan(j):
                data_set[index].append(mean_of_column[i])
            else:
                data_set[index].append(j)
        index += 1
    return data_set


# def neural_network(data_set, ):

def recieve_data ():
    input_str = ''
    while len(input_str) != 1:
        input_str = input("Number of hidden layer [0 - 9] :: ")
    number_of_hidden = int (input_str.strip('\n')) - int('0')

    input_str = ''
    while len(input_str) != 1:
        input_str = input("Number of node in hidden layer [0 - 9] :: ")
    number_of_node_hidden = int (input_str.strip('\n')) - int('0')

    input_str = ''
    while len(input_str) != 1:
        input_str = input("How many part of traning set in 10 parts [0 - 9] :: ")
    part_of_train = int (input_str.strip('\n')) - int('0')
    part_of_validate = 10 - part_of_train

    activation_function = -1
    while activation_function == -1:
        input_str = input("Activation function [Sigmoid, tanh, ReLU, LeakyReLU] :: ")   # Sigmoid = 0 , tanh = 1 , ReLU = 2 , LeakyReLu = 3
        if input_str == 'Sigmoid':
            activation_function = 0
        elif input_str == 'tanh':
            activation_function = 1
        elif input_str == 'ReLU':
            activation_function = 2
        elif input_str == 'LeakyReLU':
            activation_function = 3
        
    return number_of_hidden, number_of_node_hidden, part_of_train, part_of_validate, activation_function
def mk_neural_structure (number_of_hidden, number_of_node_hidden, number_of_input, number_of_output):
    I = zerolistmaker(number_of_input)
    O = zerolistmaker(number_of_output)
    H = []
    Y = []
    temp = zerolistmaker(number_of_node_hidden)
    for i in range(number_of_hidden):
        H.append(deepcopy(temp))
        Y.append(deepcopy(temp))
    X = []
    for i in range(number_of_hidden + 2):
        if i == 0:
            temp = zerolistmaker(len(h[i]) * number_of_input)
        elif i == number_of_hidden:
            temp = zerolistmaker(len(h[i-1]) * number_of_output)
        else:
            temp = zerolistmaker(len(h[i]) * len(h[i-1]))
        X.append(temp)
    return I,X,H,Y,O
    

if __name__ == "__main__":
    input_data_set = []
    df = pandas.read_excel('Data_Cortex_Nuclear.xls')
    columns = df.columns
    for i in columns:
        input_data_set.append (df[i].values)

    data_set = pre_process(input_data_set, 1, 4)  # pre process

    number_of_hidden, number_of_node_hidden, part_of_train, part_of_validate, activation_function = recieve_data()  #init data
    number_of_input = len(data_set)
    number_of_output = 2

    I, X, H, Y, O = mk_neural_structure ( number_of_hidden, number_of_node_hidden, number_of_input, number_of_output)
    
    

    
        




    