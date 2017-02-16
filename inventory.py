from Classes import *
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

def write_row(f, attributes):
    with open(f, 'a', newline='') as file:
        writer = csv.writer(file)
        for row in attributes:
            writer.writerow(row)
    with open(f) as file:
        data = file.read()
        return data



def view_inv(inventory_list):
    inventory_string = ''
    for item in inventory_list:
        inventory_string += ('\nRental: ' + str(item[0])+ '\nreplacement value: '+ "$" + str(item[1])+\
                              '\ndeposit: '+"$"+ str(item[2])+"\nprice per week: "+ "$" + str(item[3])+\
                                             '\ncurrent stock: '+ str(item[4])+ "\n")
        return inventory_string








def choose_item(inventory_list, name):
    for i in inventory_list:
        customer_item = Rental(i[0], i[1], i[2], i[3], i[4])
        if customer_item.name == name:
            return customer_item
        else:
            customer_item = None
        return customer_item














def rent():
    show = data_from_file('inventory.csv')
    print(view_inv(show))
    item = input("What will you be renting? Product name: ").strip().capitalize()
    if item == "Q":
        print('System closing...')
        sys.exit()
    else:
        customer_choice = get_item_by_name(data_from_file('inventory.csv'), item)
        if customer_choice == None:
            print("\nInvalid choice " + item + " is not in inventory\n")
            rent()
        else:
            print(customer_choice.deposit_value, customer_choice.price)
            print("You must place a deposit of $", customer_choice.deposit_value, "along with a fee of $",
                  customer_choice.price, "every hour the item is rented. Deposits are refunded upon return.\n")
            print("Confirm you purchase for\n", str(customer_choice))
            confirmation = input('y/n\n').strip().lower()
            if confirmation == "y":
                update_inventory(customer_choice.name, int(customer_choice.quantity) - 1, 'inventory.csv')
                update_transaction(datetime.datetime.now(), customer_choice.name, "pending", 'transaction.csv')
                update_deposits(customer_choice.deposit_value, 'deposit.csv')
                restart()
            elif confirmation == "n":
                restart()
            elif confirmation == "q":
                print("System closing...")
                sys.exit()
            else:
                print('invalid entry')


restart()