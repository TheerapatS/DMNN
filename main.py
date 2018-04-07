import pandas
from scan_input import recieve_data
from make_structure import mk_neural_structure
from pre_process import pre_process

# def neural_network(data_set, ):

if __name__ == "__main__":
    input_data_set = []
    df = pandas.read_excel('Data_Cortex_Nuclear.xls')

    columns = df.columns
    for i in columns:
        input_data_set.append (df[i].values)

    data_set,id_class = pre_process(input_data_set, 1, 4)  # pre process
    for i in data_set:
        print (i[0])
    
    number_of_hidden, number_of_node_hidden, part_of_train, part_of_validate, activation_function = recieve_data()  #init data
    number_of_input = len(data_set)
    number_of_output = 2

    I, X, H, Y, O = mk_neural_structure ( number_of_hidden, number_of_node_hidden, number_of_input, number_of_output)
    
    

    
        




    