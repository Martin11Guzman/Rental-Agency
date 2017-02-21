import inventory
from Classes import *
from inventory import *
import csv

def check_if_files_exist():
    datafile="/home/basecamp/Desktop/Rental-Agency/inventory.csv"
    try:
        make_data_files(datafile)
        make_data_files('revenue.csv')
        make_data_files('deposit.csv')
        make_data_files('transaction.csv')
        write_row("inventory.csv", inv_items())


        print("Testing your dns servers, please wait...")
    except IOError as e:
       print("Error: %s not found." % datafile)

def make_data_files(f):
    with open(f, 'w') as files:
        return files.close()

def data_from_file(f):
    with open(f, newline='') as data:
        invent = csv.reader(data, delimiter=',', quotechar='|')
        return list(invent)
    # with open(f, 'rb') as data:
    #     invent = pickle.load(f)

def write_row(f, attributes):
    with open(f, 'a', newline='') as file:
        writer = csv.writer(file)
        for row in attributes:
            writer.writerow(row)
    with open(f) as file:
        data = file.read()
        return data



def choose_item(inventory_list, name):
    for i in inventory_list:
        customer_item = Rental(i[0], i[1], i[2], i[3], i[4])
        if customer_item.name == name:
            return customer_item
        else:
            customer_item = None
        return customer_item

def update_deposits(deposit, f):
    return write_row(f, [[deposit]])

def update_revenue(rent, sales_tax, f):
    return write_row(f, [[rent, sales_tax]])

def update_transaction(date, item, status, f):
    return write_row(f, [[date, item, status]])


