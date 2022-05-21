import csv
import matplotlib as matplot

def get_data_from_pricing_file(pricing_file):
    return_list = []
    
    file = open(pricing_file)
    csvreader = csv.reader(file)
    for row in csvreader:
        return_list.append(row)
    return return_list

