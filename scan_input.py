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
        input_str = input("How many part of traning set 1:1(1), 4:1(2), 9:1(3) :: ")
    if input_str == '1':
        part_of_validate = 5
    elif input_str == '2':
        part_of_validate = 2
    elif input_str == '3':
        part_of_validate = 1
    else:
        part_of_validate = 0
    # part_of_train = int (input_str.strip('\n')) - int('0')
    # part_of_validate = 10 - part_of_train

    activation_function = -1
    while activation_function == -1:
        input_str = input("Activation function [Sigmoid(1), tanh(2), ReLU(3), LeakyReLU(4)] :: ")   # Sigmoid = 0 , tanh = 1 , ReLU = 2 , LeakyReLU = 3
        if input_str == '1':
            activation_function = 0
        elif input_str == '2':
            activation_function = 1
        elif input_str == '3':
            activation_function = 2
        elif input_str == '4':
            activation_function = 3
        
    return number_of_hidden, number_of_node_hidden, part_of_validate, activation_function