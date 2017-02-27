from Classes import *
import csv
from file_manipulation import *

def view_inv(inventory_list):
    inventory_string = ''
    for item in inventory_list:
        inventory_string += ('\nRental: ' + str(item[0])+ '\nQuantity: '+  str(item[1])+
                              '\nDeposit: '+"$"+ str(item[2])+"\nPrice Per Week: "+ "$" + str(item[3])+
                                             '\nReplacement Value: '+ "$" + str(int(item[4]))+ "\n")
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
        writer.writerow([i.name, i.quantity, i.deposit, i.price, i.replacement_value])
    file.close()
    with open(f) as file:
        inv = file.read()
        return inv




def return_deposits(item, f):
    deposit = data_from_file(f)
    if len(deposit) == 0:
        print("Wait it looks like there are 0 rentals to be returned..")
    else:
        new_deposit = []
        for i in deposit:
            new_deposit.append(i[0])
        new_deposit.pop(new_deposit.index(item))
        open(f, 'w').close()
        with open(f, 'w') as file:
            writer = csv.writer(file)
            for i in new_deposit:
                writer.writerow([i])
def show_transaction(transactions):
    trans_string = ""
    for transaction in transactions:
        trans_string += ("\nDatetime: " + str(transaction[0]) + "\nRental:" + str(transaction[1]) +
                                         "\nstatus " + str(transaction[2]) + "\n")
    return trans_string





