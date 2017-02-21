from Classes import *
from inventory import *
import sys
import csv
import os
from inventory import *
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
                 customer_choice.name, "pending", 'transaction.csv')
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
    print("\nType: rent to rent an item\nType: return to return an item\nType: start to rerun program\nType: q to quit\n")
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
        rerun()


def start():
    "Initialized program start"

    print('At anytime q will exit program')
    action = input('Are you a customer or CEO \n').strip().lower()
    if action == "customer":
        menu()
    elif action == "CEO":
        CEO()
    elif action == "q":
        print('System closing....')
        sys.exit()
    else:
        print("\nINVALID INPUT\n")
        start()



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

start()
