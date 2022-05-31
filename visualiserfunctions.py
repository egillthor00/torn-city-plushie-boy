import csv
import matplotlib.pyplot as plt

def get_data_from_pricing_file(pricing_file):
    return_list = []
    
    file = open(pricing_file)
    csvreader = csv.reader(file)
    for row in csvreader:
        return_list.append(row)
    return return_list

def get_query_plushie(data, answer):
    X_list = []
    Y_list = []
    for i in data:
        if len(Y_list) == 0:
            X_list.append(i[0])
            Y_list.append(i[answer+1])
        if i[answer+1] != Y_list[-1]:
            X_list.append(i[0])
            Y_list.append(i[answer+1])
        if len(Y_list) == 100:
            return X_list, Y_list

