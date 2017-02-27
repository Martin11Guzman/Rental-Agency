import sys
from inventory import *
import time
from file_manipulation import *


def main():
    "Initialized program main"
    sign_in = input('Choose Your position: Customer or CEO \n').strip().lower()
    if sign_in == "customer":
        menu()
    elif sign_in == "ceo":
        CEO()
    elif sign_in == "q":
        print("<<<<<<<<<Thank you for choosing Guz's>>>>>>>>>")
        sys.exit()
    else:
        print("\nIncorrect input\n")
        main()



def menu():
    print("<<<<< WELCOME TO GUZ'S MEDICAL EQUIPMENT RENTAL AGENCY © >>>>>>>>>>> ")
    time.sleep(1)
    print("How may we help you?")
    time.sleep(1)
    print("Rental options:")
    time.sleep(1)
    print("choose rent to Rent a rental\n               Or \nChoose return to Return a rental")

    print("\n")
    choice = input("Please type in your Rental option my fellow client.\n").strip().lower()
    if choice == "rent":
        check_if_files_exist()
        time.sleep(2)
        rent()
    elif choice == "return":
        return_item()
    elif choice == "q":
        print("<<<<<<<<<Thank you for choosing Guz's>>>>>>>>>")
        sys.exit()
    else:
        print("\nIncorrect input\n")
        print('PLEASE TYPE IN OPTION CORRECTLY:  rent or return? ')
        time.sleep(1)
        menu()


def rent():
    show = data_from_file('inventory.csv')
    print(view_inv(show))
    item = input("Please choose any of the medical equipment above to rent. ").strip().capitalize()
    if item == "q":
        print("<<<<<<<<Thank you for choosing Guz's>>>>>>>>>")
        sys.exit()
    else:
        customer_choice = choose_item(data_from_file('inventory.csv'), item)
        if customer_choice == None:
            print("\nInvalid choice " + item + " is not in inventory\n")
            rent()
        else:
            print("<<<<<<<<  PROCESSING PURCHASE >>>>>>>>>")
            time.sleep(1)
            print("<<<<<<<<  CLIENT RECEIPT >>>>>>>")

            print("Deposit fee: $",customer_choice.deposit,
                  "\n"
                "Amount of weeks rented item with flat rental fee: $",customer_choice.price,
                  "\n"
                "All Deposits will be reimbursed after return")

            print("Do you accept your purchase\n", str(customer_choice))
            decision = input('Yes or NO\n').strip().lower()
            if decision == "yes":
                renovate_inventory(customer_choice.name,
                int(customer_choice.quantity)- 1, 'inventory.csv')
                renovate_transaction(datetime.datetime.now(),
                customer_choice.name, "awaiting", 'transaction.csv')
                update_deposits(customer_choice.deposit, 'deposit.csv')
                print("<<<<<<<<<<<<<<<<<<Thanks for purchasing a rental  At Guz's!!>>>>>>>>>>>")
                time.sleep(1)
                rerun()
            elif decision == "no":
                rerun()
            elif decision == "q":
                print("Rental agency closing...")
                sys.exit()
            else:
                print('invalid entry')
                rerun()


def rerun():
    print("\nChoose option: rent to rent an item\nChoose option:return to return an item\nChoose option: restart to rerun program\nChoose option: q to quit\n")
    choice = input().strip().lower()
    if choice == "rent":
        rent()
    elif choice == "return":
        return_item()
    elif choice == "restart":
        main()
    elif choice == "q":
        print("<<<<<<<<<Thank you for choosing Guz's>>>>>>>>>")
    else:
        print("invalid input")
        rerun()

def CEO():
    "Inputs for all CEO actions"
    print(" Hey their Mr.'Ceo' ")

    choice = input(
        'Choose option:<view inventory> - to view inventory\nChoose option:<transaction history? - to display transactions\nChoose option:<update> - to add an item to inventory.\nChoose option:<restart> - to restart\n').strip().lower()
    if choice == "view inventory":
        inv = data_from_file('inventory.csv')
        print(view_inv(inv))
        CEO()
    elif choice == "transaction history":
        sales = data_from_file('transaction.csv')
        print(show_transaction(sales))
        CEO()
    elif choice == 'update':
        name = input("Rentals being added: ").strip().capitalize()
        quantity = input("How many? ").strip()
        if quantity.isdigit() != True:
            print("invalid input")
            CEO()
        if name == "q" or quantity == "q":
            print("<<<<<<<<<Thank you for choosing Guz's>>>>>>>>>")
            sys.exit()
        inv = data_from_file("inventory.csv")
        item = choose_item(inv, name)
        if item == None:
            print('invaid input')
            CEO()
        renovate_inventory(name, int(item.quantity) + int(quantity), 'inventory.csv')
        print("\nYour inventory has been renovated!\n")
        CEO()
    elif choice == "restart":
        main()
    elif choice == "q":
        print("<<<<<<<<<Thank you for choosing Guz's>>>>>>>>>")
        sys.exit()






def return_item():
    "contains inputs to determine how to calculate revenue on returned items"
    inv = data_from_file('inventory.csv')
    for item in inv:
        print("\n"+item[0])
    item = input("\nWhat rental are you returning \n").strip().capitalize()
    if item == 'q':
        print("<<<<<<<<<Thank you for choosing Guz's>>>>>>>>>")
        sys.exit()
    else:
        returning_item = choose_item(data_from_file('inventory.csv'), item)
        if returning_item == None:
            print("Invalid Input " + item + " is not in inventory to be returned")
            return_item()
        else:
            weeks = input("For how many weeks did you rent the rental item? ").strip().lower()
            if weeks == "q":
                print("<<<<<<<<<Thank you for choosing Guz's>>>>>>>>>")
                sys.exit()
            elif weeks.isdigit():
                item_status = input(" is there any issues with your expensive rental? yes/no ").strip().lower()
                if item_status == "yes":
                    print("Your deposit will not be returned due to your irresponsibility.  you owe the following:"+
                            str(int(returning_item.replacement_value)) +
                            " dollars for replacement of the item. and "
                            + "$" + str(int(returning_item.price) * int(weeks)) + " for rent.")
                    rent_amount = int(returning_item.price) * int(weeks)
                    sales_tax = rent_amount * 0.07
                    update_revenue(rent_amount, sales_tax, 'revenue.csv')
                    renovate_transaction(datetime.datetime.now(), returning_item.name,
                    "Reimburse", 'transaction.csv')
                    rerun()
                elif item_status == 'no':
                    print("This is what you owe my fellow client: $"+ \
                    str(int(returning_item.price) * int(weeks)) + " for the rental fee.")
                    return_deposits(returning_item.deposit, 'deposit.csv')
                    renovate_inventory(returning_item.name, int(returning_item.quantity)+1, 'inventory.csv')
                    rent_amount = int(returning_item.price) * int(weeks)
                    sales_tax = rent_amount * 0.07
                    update_revenue(rent_amount, sales_tax, 'revenue.csv')
                    renovate_transaction(datetime.datetime.now(), returning_item.name,
                    "returned", 'transaction.csv')
                    rerun()
                elif item_status == "q":
                    print("<<<<<<<<<Thank you for choosing Guz's>>>>>>>>>")
                else:
                    print('\nIncorrect Input\n')
                    return_item()

            else:
                print('invalid input')
                return_item()

if __name__ == '__main__':
    main()

