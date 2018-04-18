import pandas
from scan_input import recieve_data
from make_structure import mk_neural_structure
from pre_process import pre_process
from n_network import *
# def neural_network(data_set, ):

if __name__ == "__main__":
    input_data_set = []
    df = pandas.read_excel('Data_Cortex_Nuclear.xls')

    columns = df.columns
    for i in columns:
        input_data_set.append(df[i].values)

    data_set,id_class = pre_process(input_data_set, 1)  # pre process
    # for i in data_set:
    #     print (i[0])
    
    number_of_hidden, number_of_node_hidden, part_of_validate, activation_function = recieve_data()  #init data
    number_of_input = len(data_set) - 5
    number_of_output = 8

    I, X, H, Y, O, g = mk_neural_structure ( number_of_hidden, number_of_node_hidden, number_of_input, number_of_output)
    
    # test
    # I = [1, 0, 1, 1]
    # X = [[0.3,0.2,0.1,0.2,0.2,0.1,0.1,0.3],[0.1,0.2,0.1,0.2]]
    # g = [[0,0],[0,0]]
    # H = [[0,0]]
    # Y = [[0.2,0.4],[0.1,0.2]]
    # O = [0,0]
    
    # dW = deepcopy(X)
    # print (dW)
    # activation_function = 0
    learning_rate = 0.01
    train(data_set, learning_rate, I, X, H, Y, O, g, activation_function,part_of_validate)
    # c_data_set = converset_data(data_set)
    # class_data = [[],[],[],[],[],[],[],[]]
    # for i in c_data_set:
    #     class_data = class_tokenize(i,class_data)
    # for i in class_data:
    #     print (len(i))

    # a,b = cross_validation(class_data,part_of_validate,len(c_data_set))
    # for i in a:
    #     print (len(i))
    # # print (a[0])
    
    # print (len(b))
    
        




    