from Classes import *
from inventory import *
import sys
import csv
import os
from inventory import *
from Classes import *
import datetime
import time
from file_manipulation import *


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
            print(customer_choice.deposit_value, customer_choice.price)
            print("You must place a deposit of $", customer_choice.deposit_value,\
                "along with a fee of $", customer_choice.price,\
                "every hour the item is rented. Deposits are refunded upon return.\n")
            print("Confirm you purchase for\n", str(customer_choice))
            confirmation = input('y/n\n').strip().lower()
            if confirmation == "y":
                renovate_inventory(customer_choice.name, \
                int(customer_choice.quantity)- 1, 'inventory.csv')
                renovate_transaction(datetime.datetime.now(),\
                 customer_choice.name, "pending", 'transaction.csv')
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


def restart():
    print("\nType: rent to rent an item\nType: return to return an item\nType: start to restart program\nType: q to quit\n")
    choice = input().strip().lower()
    if choice == "rent":
        rent()
    elif choice == "return":
        return_item()
    elif choice == "start":
        start()
    elif choice == "q":
        print('System closing....')
    else:
        print("invalid input")
        restart()



