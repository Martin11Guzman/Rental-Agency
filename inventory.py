from Classes import *
import csv
from file_manipulation import *

"""
This file has functions that contain obj's from Rental class, Transaction class.
each function either displays or writes data to files

"""

def view_inv(inventory_list):
    """list -> None
       empty string that adds Rental attributes
    """
    inventory_string = ''
    for item in inventory_list:
        inventory_string += ('\nRental: ' + str(item[0])+ '\nQuantity: '+  str(item[1])+
                              '\nDeposit: '+"$"+ str(item[2])+"\nPrice Per Week: "+ "$" + str(item[3])+
                                             '\nReplacement Value: '+ "$" + str(int(item[4]))+ "\n")
    return inventory_string

def renovate_inventory(name, quantity, f):
    """str, int -> None"""
    stock = []
    inv = data_from_file(f)
    # iterates over data_from_file obj by index
    for i in inv:
        stock.append(Rental(i[0], i[1], i[2], i[3], i[4]))
    # iterates over stock list by name and quantity and writes to f object
    for i in stock:
        if i.name == name:
            i.quantity = quantity
    file = open(f, 'w')
    writer = csv.writer(file, delimiter=',')
    for i in stock:
        # csv built in writes list of rental attributes
        writer.writerow([i.name, i.quantity, i.deposit, i.price, i.replacement_value])
    file.close()
    with open(f) as file:
        inv = file.read()
        return inv



def choose_item(inventory_list, name):
    """list of lists, str -> Rental"""
    customer_item = ''
    # empty list that iterates over Rental list Index
    for i in inventory_list:
        customer_item = Rental(i[0], i[1], i[2], i[3], i[4])
        # item is chosen by name
        if customer_item.name == name:
            return customer_item
        else:
            customer_item = None
    return customer_item

def return_deposits(item, f):
    """str -> None"""
    deposit = data_from_file(f)
    # deposit takes f object to get data from file
    if len(deposit) == 0:
        print("Wait it looks like there are 0 rentals to be returned..")
    else:
        new_deposit = []
        # empty list appends iterates from deposit
        for i in deposit:
            new_deposit.append(i[0])
        # Takes out new_deposit from list
        new_deposit.pop(new_deposit.index(item))
        open(f, 'w').close()
        with open(f, 'w') as file:
            writer = csv.writer(file)
            for i in new_deposit:
                writer.writerow([i])





