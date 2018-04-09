from activation_func import *


def train (data_set, learning_rate, I, X, H, Y, O,activation_function):
    round = 0
    while round<=5:
        if round == 0:
            for i in range(len(H)+1):
                if i < len(H):
                    for j in range(len(H[i])):
                        if i == 0:
                            for k in range(len(I)):
                                H[i][j] += I[k]*(X[i][(k*len(H[i]))+j])
                                print (I[k],(X[i][(k*len(H[i]))+j]))
         
                        else :
                            for k in range(len(H[i-1])):
                                H[i][j] += H[i-1][k]*(X[i][(k*len(H[i]))+j])

                        H[i][j] += Y[i][j]
                        print (H[i][j])
                        H[i][j] = sigmoid(H[i][j])
                else :
                    for j in range(len(O)):
                        for k in range(len(H[len(H)-1])):
                                O[j] += H[len(H)-1][k]*(X[i][(k*len(O))+j])                        
                        O[j] += Y[i][j]
                        # print (O[j])
                        O[j] = sigmoid(O[j])
        print (H[0][0])
        print (O)
        round += 1
# def validation ():
