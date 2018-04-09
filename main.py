import pandas
from scan_input import recieve_data
from make_structure import mk_neural_structure
from pre_process import pre_process
from n_network import train
# def neural_network(data_set, ):

if __name__ == "__main__":
    input_data_set = []
    df = pandas.read_excel('Data_Cortex_Nuclear.xls')

    columns = df.columns
    for i in columns:
        input_data_set.append (df[i].values)

    data_set,id_class = pre_process(input_data_set, 1, 4)  # pre process
    # for i in data_set:
    #     print (i[0])
    
    # number_of_hidden, number_of_node_hidden, part_of_train, part_of_validate, activation_function = recieve_data()  #init data
    number_of_input = len(data_set)
    number_of_output = 2

    # __, X, H, Y, O = mk_neural_structure ( number_of_hidden, number_of_node_hidden, number_of_input, number_of_output)
    # print (I)
    # print (X)
    # print (H)
    # print (Y)
    # print (O)
    # test
    I = [1, 0, 1, 1]
    X = [[0.3,0.2,0.1,0.2,0.2,0.1,0.1,0.3],[0.1,0.2,0.1,0.2]]
    H = [[0,0]]
    Y = [[0.2,0.4],[0.1,0.2]]
    O = [0,0]
    activation_function = 0
    learning_rate = 0.1
    train(data_set, learning_rate, I, X, H, Y, O,activation_function)

    
        




    