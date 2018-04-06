import math

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