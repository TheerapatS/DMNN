from copy import deepcopy

def zerolistmaker (n):
    return [0] * n

def mk_neural_structure (number_of_hidden, number_of_node_hidden, number_of_input, number_of_output):
    I = zerolistmaker(number_of_input)
    O = zerolistmaker(number_of_output)
    H = []
    Y = []
    g = []
    temp = zerolistmaker(number_of_node_hidden)
    for i in range(number_of_hidden):
        H.append(deepcopy(temp))
        Y.append(deepcopy(temp))
        g.append(deepcopy(temp))
    Y.append(deepcopy(temp))
    g.append(deepcopy(temp))
    X = []
    
    for i in range(number_of_hidden + 1):
        if i == 0:
            temp = zerolistmaker(len(H[i]) * number_of_input)
        elif i == number_of_hidden:
            temp = zerolistmaker(len(H[i-1]) * number_of_output)
        else:
            temp = zerolistmaker(len(H[i]) * len(H[i-1]))
        X.append(deepcopy(temp))
    return I,X,H,Y,O,g