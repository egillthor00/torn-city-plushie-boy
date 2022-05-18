import csv
import datetime as dt

def openfile(file_name):
    file = open(file_name, 'a+', newline='')
    return file

def write_data(file, data, counter = 0):
    sum = 0
    write_list = []
    writer = csv.writer(file)
    if counter != 0:
        write_list.append(str(counter))
    timestamp = dt.datetime.now().time()
    write_list.append(timestamp)
    for i in data["plushies"]:
        for val in i.values():
            cost = val[0].get("cost")
            sum += cost
            write_list.append(cost)
            break
    write_list.append(sum)
    writer.writerow(write_list)
    return

