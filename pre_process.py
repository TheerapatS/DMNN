import math
from copy import deepcopy


def pre_process (input_data_set, a):
    mean_of_column = [0] * len(input_data_set)
    id_class = []
    id_class.append(deepcopy(input_data_set[0]))
    id_class.append(deepcopy(input_data_set[len(input_data_set)-1]))
    for i in range(a,len(input_data_set)):
        mean_temp = 0.0
        n = 0
        for j in input_data_set[i]:
            if type(j) is not str:
                if not math.isnan(j):
                    mean_temp += j
                    n += 1
        if n == 0:
            mean_of_column[i] == 0
        else :
            mean_of_column[i] = mean_temp/n
    data_set = []
    data_set.append(deepcopy(input_data_set[0]))
    index = 1
    for i in range(a,len(input_data_set)):
        data_set.append([])
        for j in input_data_set[i]:
            if type(j) is not str:
                if math.isnan(j):
                    data_set[index].append(mean_of_column[i])
                else:
                    data_set[index].append(j)
            else:
                data_set[index].append(j)
        index += 1
    return data_set,id_class