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
        input_str = input("Activation function [Sigmoid, tanh, ReLU, LeakyReLU] :: ")   # Sigmoid = 0 , tanh = 1 , ReLU = 2 , LeakyReLU = 3
        if input_str == 'Sigmoid':
            activation_function = 0
        elif input_str == 'tanh':
            activation_function = 1
        elif input_str == 'ReLU':
            activation_function = 2
        elif input_str == 'LeakyReLU':
            activation_function = 3
        
    return number_of_hidden, number_of_node_hidden, part_of_train, part_of_validate, activation_function