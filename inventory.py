from Classes import *
import csv
from file_manipulation import *

def view_inv(inventory_list):
    inventory_string = ''
    for item in inventory_list:
        inventory_string += ('\nRental: ' + str(item[0])+ '\nQuantity: '+  str(item[1])+\
                              '\nDeposit: '+"$"+ str(item[2])+"\nPrice Per Week: "+ "$" + str(item[3])+\
                                             '\nReplacement Value: '+ "$" + str(item[4])+ "\n")
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



def view_revenue(f1, f2):
    revenue_list = []
    tax_list = []
    deposits_list = []
    rev = data_from_file(f1)
    if len(rev) > 0:
        for i in rev:
            revenue_list.append(int(i[0]))
            tax_list.append(float(i[1]))
            total = sum(revenue_list)
            tax = sum(tax_list)
            final_total = total + tax
    else:
        tax = 0
        total = 0
        final_total = 0
    deposits = data_from_file(f2)
    for deposit in deposits:
        deposits_list.append(int(deposit[0]))
    deposit_total = sum(deposits_list)
    return "All current pending deposits: " + "$", deposit_total, "total w/o tax: $",\
        total, "sales tax: $", tax, "total: $", final_total

def return_deposits(item, filename):
    deposit = data_from_file(filename)
    if len(deposit) == 0:
        print("There are not items to be returned did you mean to rent? ")
    else:
        new_deposit = []
        for i in deposit:
            new_deposit.append(i[0])
        new_deposit.pop(new_deposit.index(item))
        open(filename, 'w').close()
        with open(filename, 'w') as file:
            writer = csv.writer(file)
            for i in new_deposit:
                writer.writerow([i])






