import sys
from inventory import *
import time
from file_manipulation import *
# from prac import *

# location of password existence check file
# EC = '/home/basecamp/Desktop/Rental-Agency/existence_check.txt'
# PWD = '/home/basecamp/Desktop/Rental-Agency/pswd.txt'  # Location of password file
#
# pswd_exist = open(EC).read()  # Checking to see if the password exists
# if pswd_exist == 'YES':
#     pass
# else:
#     pick_password()  # If it doesn't, user will pick a password

# Checking for password


def main():
    "Initialized program main"

    print("Guz's Medical Equipment Rental Agency")
    time.sleep(1)
    sign_in = input('Choose Your position: Customer or CEO \n').strip().lower()
    if sign_in == "customer":
        menu()
    elif sign_in == "ceo":
        CEO()
    elif sign_in == "q":
        print('System closing....')
        sys.exit()
    else:
        print("\nINVALID INPUT\n")
        main()



def menu():
    print("Hello how you doing!??")
    time.sleep(1)
    print("Welcome to Guz's Medical Equipment Rental Agency. ")
    time.sleep(1)
    print("How can I help you today?")
    choice = input("are you renting or returning an item?\n").strip().lower()
    if choice == "rent":
        check_if_files_exist()
        rent()
    elif choice == "return":
        return_item()
    elif choice == "q":
        print("System closing...")
        sys.exit()
    else:
        print("\nINVALID INPUT\n")
        print('did you mean rent or return? ')
        menu()


def rent():
    show = data_from_file('inventory.csv')
    print(view_inv(show))
    item = input("What will you be renting? Product name: ").strip().capitalize()
    if item == "Q":
        print('System closing...')
        sys.exit()
    else:
        customer_choice = choose_item(data_from_file('inventory.csv'), item)
        if customer_choice == None:
            print("\nInvalid choice " + item + " is not in inventory\n")
            rent()
        else:
            print(customer_choice.deposit, customer_choice.price)
            print("You must place a deposit of $", customer_choice.deposit,\
                "along with a fee of $", customer_choice.price,\
                "every hour the item is rented. Deposits are refunded upon return.\n")
            print("Confirm you purchase for\n", str(customer_choice))
            confirmation = input('y/n\n').strip().lower()
            if confirmation == "y":
                renovate_inventory(customer_choice.name, \
                int(customer_choice.quantity)- 1, 'inventory.csv')
                renovate_transaction(datetime.datetime.now(),\
                 customer_choice.name, "awaiting", 'transaction.csv')
                update_deposits(customer_choice.deposit, 'deposit.csv')
                rerun()
            elif confirmation == "n":
                rerun()
            elif confirmation == "q":
                print("System closing...")
                sys.exit()
            else:
                print('invalid entry')
                rerun()


def rerun():
    print("\nType: rent to rent an item\nType: return to return an item\nType: main to rerun program\nType: q to quit\n")
    choice = input().strip().lower()
    if choice == "rent":
        rent()
    elif choice == "return":
        return_item()
    elif choice == "main":
        main()
    elif choice == "q":
        print('System closing....')
    else:
        print("invalid input")
        rerun()

def CEO():
    "Inputs for all CEO actions"

    choice = input(
        'Type: i to view inventory\nType: t to view transaction history\nType: r to view revenue\nType: Replace to add a replacement item to inventory.\nType: s to restart\n').strip().lower()
    if choice == "i":
        inv = data_from_file('inventory.csv')
        print(view_inv(inv))
        CEO()
    elif choice == "t":
        sales = data_from_file('transaction.csv')
        print(show_transaction(sales))
        CEO()
    elif choice == "r":
        sales = data_from_file('revenue.csv')
        print("\n")
        p_rev = view_revenue('revenue.csv', 'deposit.csv')
        print(p_rev[0], p_rev[1], "\n" + p_rev[2], p_rev[3], "\n" + p_rev[4], p_rev[5], "\n" + p_rev[6], "\n" + p_rev[7], "\n" + p_rev[8], "\n" + p_rev[9], "\n" + p_rev[10], "\n" + p_rev[11])
        print("\n")
        CEO()
    elif choice == 'rq':
        name = input("Product being replaced: ").strip().capitalize()
        quantity = input("How many? ").strip()
        if quantity.isdigit() != True:
            print("invalid input")
            CEO()
        if name == "q" or quantity == "q":
            print('System closing...')
            sys.exit()
        inv = data_from_file("inventory.csv")
        item = choose_item(inv, name)
        if item == None:
            print('invaid input')
            CEO()
        renovate_inventory(name, int(item.quantity) + int(quantity), 'inventory.csv')
        print("\nInventory has been updated\n")
        CEO()
    elif choice == "s":
        main()
    elif choice == "q":
        print('System closing....')
        sys.exit()















def return_item():
    "contains inputs to determine how to calculate revenue on returned items"
    inv = data_from_file('inventory.csv')
    for item in inv:
        print("\n"+item[0])
    item = input("\nWhat item are you returning\n").strip().capitalize()
    if item == 'Q':
        print("System closing....")
        sys.exit()
    else:
        returning_item = choose_item(data_from_file('inventory.csv'), item)
        if returning_item == None:
            print("Invalid Input " + item + " is not in inventory to be returned")
            return_item()
        else:
            hours = input("How many hours was the product rented? ").strip().lower()
            if hours == "q":
                print('System closing....')
                sys.exit()
            elif hours.isdigit():
                item_status = input("Is the product broken or damaged y/n? ").strip().lower()
                if item_status == "y":
                    print("Your deposit will not be returned you owe the following:"+ \
                            str(returning_item.replacement_value) +\
                            " dollars for replacement of the item. and "\
                            + "$" + str(int(returning_item.price) * int(hours)) + " for rent.")
                    rent_amount = int(returning_item.price) * int(hours)
                    sales_tax = rent_amount * 0.07
                    update_revenue(rent_amount, sales_tax, 'revenue.csv')
                    renovate_transaction(datetime.datetime.now(), returning_item.name, \
                    "compensated", 'transaction.csv')
                    rerun()
                elif item_status == 'n':
                    print("Your deposit will be returned you owe the following: $"+ \
                    str(int(returning_item.price) * int(hours)) + " for rent.")
                    return_deposits(returning_item.deposit, 'deposit.csv')
                    renovate_inventory(returning_item.name, int(returning_item.quantity)+1, 'inventory.csv')
                    rent_amount = int(returning_item.price) * int(hours)
                    sales_tax = rent_amount * 0.07
                    update_revenue(rent_amount, sales_tax, 'revenue.csv')
                    renovate_transaction(datetime.datetime.now(), returning_item.name, \
                    "returned", 'transaction.csv')
                    rerun()
                elif item_status == "q":
                    print('System closing....')
                else:
                    print('\nInvalid Input\n')
                    return_item()

            else:
                print('invalid input')
                print('hours must be a number')
                return_item()

if __name__ == '__main__':
    main()