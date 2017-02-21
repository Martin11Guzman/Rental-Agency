from Classes import *
import csv
from file_manipulation import *

def view_inv(inventory_list):
    inventory_string = ''
    for item in inventory_list:
        inventory_string += ('\nRental: ' + str(item[0])+ '\nreplacement value: '+ "$" + str(item[1])+\
                              '\ndeposit: '+"$"+ str(item[2])+"\nprice per week: "+ "$" + str(item[3])+\
                                             '\ncurrent stock: '+ str(item[4])+ "\n")
        return inventory_string

def renovate_inventory(name, quantity, f):
    stock = []
    inv = data_from_file(f)
    for i in inv:
        stock.append(Rental(i[0], i[1], i[2], i[3], i[4]))
    for i in stock:
        if i.name == name:
            i.quantity = quantity
    file = open(f, 'w')
    writer = csv.writer(file, delimiter=',')
    for i in stock:
        writer.writerow([i.name, i.replacement_value, i.deposit, i.price, i.quantity])
    file.close()
    with open(f) as file:
        inv = file.read()
        return inv

def renovate_transaction(f, date, item, status ):
    return write_row(f, [[date, item, status]])






