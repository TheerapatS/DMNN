from activation_func import act_func
from copy import deepcopy
import random

def train (data_set, learning_rate, I, X, H, Y, O, g, D, activation_function):
    round = 0
    dWx = deepcopy(X)
    dWy = deepcopy(Y)
    while round<1:
        if round == 0:
            for i in range(len(H)+1):
                if i < len(H):
                    for j in range(len(H[i])):
                        if i == 0:
                            for k in range(len(I)):
                                H[i][j] += I[k]*(X[i][(k*len(H[i]))+j])
                        else :
                            for k in range(len(H[i-1])):
                                H[i][j] += H[i-1][k]*(X[i][(k*len(H[i]))+j])
                        H[i][j] += Y[i][j]
                        x = H[i][j]
                        H[i][j] = act_func(x,activation_function)
                else :
                    for j in range(len(O)):
                        for k in range(len(H[len(H)-1])):
                                O[j] += H[len(H)-1][k]*(X[i][(k*len(O))+j])                     
                        O[j] += Y[i][j]
                        x = O[j]
                        O[j] = act_func(x,activation_function)
                        e = D[j] - O[j]
                        g[i][j] = (e) * (act_func(O[j],activation_function,dif=True))
            for i in range(len(H) , -1, -1):
                if i == len(H):
                    for j in range(len(g[i-1])):
                        for k in range(len(O)):
                            g[i-1][j] += X[i][k+(len(O)*j)] * g[i][k]
                        g[i-1][j] *= act_func(H[i-1][j],activation_function,dif=True)

                    for k in range(len(dWx[i])):
                        if k % len(O) == 0:  
                            dWx[i][k] = (-1)*(learning_rate)*(g[i][k%len(O)])*(H[i-1][int(k/len(O))])
                        else :
                            dWx[i][k] = (-1)*(learning_rate)*(g[i][k%len(O)])*(H[i-1][int((k)/len(O))])
                    for k in range(len(dWy[i])):
                        dWy[i][k] = (-1)*(learning_rate)*(g[i][k%len(O)])

                elif i==0:
                    for k in range(len(dWx[i])):
                        if k % len(H[i]) == 0:  
                            dWx[i][k] = (-1)*(learning_rate)*(g[i][int(k%len(H[i]))])*(I[int(k/len(H[i]))])
                        else :
                            dWx[i][k] = (-1)*(learning_rate)*(g[i][int(k%len(H[i]))])*(I[int((k)/len(H[i]))])
                    for k in range(len(dWy[i])):
                        dWy[i][k] = (-1)*(learning_rate)*(g[i][int(k%len(H[i]))])
                else :
                    for j in range(len(g[i-1])):
                        for k in range(len(H[i])):
                            g[i-1][j] += X[i][k+(len(H[i])*j)] * g[i][k]
                        g[i-1][j] *= act_func(H[i-1][j],activation_function,dif=True)

                    for k in range(len(dWx[i])):
                        if k % len(H[i]) == 0:  
                            dWx[i][k] = (-1)*(learning_rate)*(g[i][int(k%len(H[i]))])*(H[i-1][int(k/len(H[i-1]))])
                        else :
                            dWx[i][k] = (dWy-1)*(learning_rate)*(g[i][int(k%len(H[i]))])*(H[i-1][int((k-(k%len(H[i-1])))/len(H[i-1]))])
                    for k in range(len([i])):
                        dWy[i][k] = (-1)*(learning_rate)*(g[i][int(k%len(H[i]))])
        print (dWy)
        round += 1

def converset_data(data_set):
    c_data_set = []
    for i in range (len(data_set[0])):
        t = []
        for j in range (len(data_set)):
            t.append(data_set[j][i])
        c_data_set.append(t)
    return c_data_set

def cross_validation(class_data_real, part_of_validate, data_size): #data_size = 1080
    print (data_size)
    class_data = deepcopy(class_data_real)
    if part_of_validate == 5:
        one_part = int(data_size / 2)
    elif part_of_validate == 2:
        one_part = int(data_size / 5)
    elif part_of_validate == 1:
        one_part = int(data_size / 10)
    
    data_train = []
    for i in range(10 - part_of_validate):
        data_train.append([])
    data_test = []
    print (one_part)
    print (int(one_part/float(len(class_data))))
    for i in range(10):
        count_one_part = 0
        print (i)
        if i < 9 - part_of_validate:
            class_data_index = 0
            while (count_one_part < one_part):
                print (class_data_index)
                if part_of_validate == 5:
                    one_part = int(data_size / 2)
                elif part_of_validate == 2:
                    one_part = int(data_size / 5)
                elif part_of_validate == 1:
                    one_part = int(data_size / 10)
                one_class_part = 
                for j in range(0,int(one_part/len(class_data))+1):
                    if len(class_data[class_data_index])!= 0:
                        t = random.randint(0,len(class_data[class_data_index])-1)
                        data_train[i].append(class_data[class_data_index][t])
                        class_data[class_data_index].pop(t)
                        count_one_part += 1
                class_data_index += 1
        else:
            for j in range(len(class_data)):
                while len(class_data[j]) != 0:
                    # t = random.randint(0,len(class_data[i]))
                    data_test.append(class_data[j][0])
                    class_data[j].pop(0)
    return data_test,data_train
# def validation ():

def class_tokenize(one_instant,class_data):
    if one_instant[len(one_instant)-1] == 'c-CS-m':
        class_data[0].append(one_instant)
    elif one_instant[len(one_instant)-1] == 'c-SC-m':
        class_data[1].append(one_instant)
    elif one_instant[len(one_instant)-1] == 'c-CS-s':
        class_data[2].append(one_instant)
    elif one_instant[len(one_instant)-1] == 'c-SC-s':
        class_data[3].append(one_instant)
    elif one_instant[len(one_instant)-1] == 't-CS-m':
        class_data[4].append(one_instant)
    elif one_instant[len(one_instant)-1] == 't-SC-m':
        class_data[5].append(one_instant)
    elif one_instant[len(one_instant)-1] == 't-CS-s':
        class_data[6].append(one_instant)
    elif one_instant[len(one_instant)-1] == 't-SC-s':
        class_data[7].append(one_instant)
    return class_data

def class_check(t):
    if t == 'c-CS-m':
        return [1,0,0,0,0,0,0,0]
    elif t == 'c-SC-m':
        return [0,1,0,0,0,0,0,0]
    elif t == 'c-CS-s':
        return [0,0,1,0,0,0,0,0]
    elif t == 'c-SC-s':
        return [0,0,0,1,0,0,0,0]
    elif t == 't-CS-m':
        return [0,0,0,0,1,0,0,0]
    elif t == 't-SC-m':
        return [0,0,0,0,0,1,0,0]
    elif t == 't-CS-s':
        return [0,0,0,0,0,0,1,0]
    elif t == 't-SC-s':
        return [0,0,0,0,0,0,0,1]