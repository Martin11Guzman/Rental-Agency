import sys
from inventory import *
import time
from file_manipulation import *

"""

Presentation of program contains main(), menu(), rent(), return(), ceo(), rerun()
Each function takes in user input that either calculates or writes data into files


"""

week_format = datetime.datetime.now().strftime("%Y-%m-%d --- Rental should be returned a week from day rented or flat rental rate is applied each week not returned")


def main():
    """Starts the program..called in if __name__ == '__main__': """
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
    """Displays the options a user can make.. navigates the user through sections by calling other functions regarding their output """
    print("<<<<< WELCOME TO GUZ'S MEDICAL EQUIPMENT RENTAL AGENCY © >>>>>>>>>>> ")
    time.sleep(1)
    print("How may we help you?")
    time.sleep(1)
    print("Rental options:")
    time.sleep(1)
    print("choose Rent to rent a rental\n               Or \nChoose Return to return a rental")

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
    """Function that reads inventory file and asks user what they would like to rent"""
    show = data_from_file('inventory.csv')
    print(view_inv(show))
    item = input("Please choose any of the medical equipment above to rent. ").strip().capitalize()
    if item == "q":
        print("<<<<<<<<Thank you for choosing Guz's>>>>>>>>>")
        sys.exit()
    else:
        # if statement calls choose_item that then calls data_from_file and user output searches for item name from inventory_list
        customer_choice = choose_item(data_from_file('inventory.csv'), item)
        # Rental objects are assign to customer_choice where customer choice looks over inventory,csv for Rental name
        if customer_choice == None:
            print("\nInvalid choice " + item + " is not in inventory\n")
            rent()
        else:
            print("<<<<<<<<  PROCESSING PURCHASE >>>>>>>>>")
            time.sleep(.5)
            print("<<<<<<<<  Customer Rental Agreement >>>>>>>")
            time.sleep(1)
            print("Do you accept Guz's Rental Agreement?\n",str(customer_choice))


            print("Deposit fee: $",customer_choice.deposit,
                  "\n"
                "Flat rental fee is applied by weeks rented: $",customer_choice.price,
                  "\n"
                "Deposit will be reimbursed to customer after rental is returned")
            decision = input('Sign Yes: to agree or Sign No: to disagree\n').strip().lower()
            if decision == "yes":
                # inventory is updated, locates by name obj then changes customer_choice quanty by subtracting 1
                renovate_inventory(customer_choice.name,
                int(customer_choice.quantity)- 1, 'inventory.csv')
                # transaction file is updated by built in function datetime where a date is assigned to a rental that has been rented
                renovate_transaction(week_format,
                customer_choice.name, "awaiting", 'transaction.csv')
                # deposit file is updated by taking customer_choice object and getting out the deposit value that gets updated
                update_deposits(customer_choice.deposit, 'deposit.csv')
                print("<<<<<<<<<<<<<<<<<<Thanks for purchasing a rental  At Guz's!!>>>>>>>>>>>")
                time.sleep(1)
                rerun()
            elif decision == "no":
                print("Rental has been restocked back in the Inventory")
                time.sleep(1)
                rerun()
            elif decision == "q":
                print("Rental agency closing...")
                sys.exit()
            else:
                print('invalid entry')
                rerun()


def rerun():
    """ function reenitializes the program for a recursive mode"""
    print("\nChoose option: rent to rent an item\nChoose option:return to return an item\nChoose option: Login to Login in as a Customer or CEO\nChoose option: q to quit\n")
    choice = input().strip().lower()
    if choice == "rent":
        rent()
    elif choice == "return":
        return_item()
    elif choice == "login":
        main()
    elif choice == "q":
        print("<<<<<<<<<Thank you for choosing Guz's>>>>>>>>>")
    else:
        print("invalid input")
        rerun()

def CEO():
    "Inputs for all CEO options that decide whether to view_inventory, update_inventory, or view transaction_history"
    print(" <<<<<<<<<<<<<<<<<<<< Welcome Mr.'Ceo'>>>>>>>>>>>>>>>> ")
    time.sleep(1.6)
    choice = input(
        'Choose option:<view inventory>\nto view inventory\n\nChoose option:<transaction history>\nto display transactions\n\nChoose option:<update>\nto add an item to inventory.\n\nChoose option:<restart>\nto restart\n\n').strip().lower()
    if choice == "view inventory":
        # obj inv takes in f to display inventory.csv
        inv = data_from_file('inventory.csv')
        print(view_inv(inv))
        CEO()
    elif choice == "transaction history":
        # obj sales gets data from file displays the transaction sales
        sales = data_from_file('transaction.csv')
        print(show_transaction(sales))
    elif choice == 'update':
        name = input("Name of rental you want to add: ").strip().capitalize()
        quantity = input("quantity of rentals added? ").strip()
        if quantity.isdigit() != True:
            print("invalid input")
        if name == "q" or quantity == "q":
            print("<<<<<<<<<Thank you for choosing Guz's>>>>>>>>>")
            sys.exit()
        inv = data_from_file("inventory.csv")
        # obj item calls choose_item that reads data from inv and gets name of rental to update inventory and add quantity
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
        print(item[0])
    # for loop iterates over item in inv than prints item by its index
    item = input("\nWhat rental are you returning \n").strip().capitalize()
    if item == 'q':
        print("<<<<<<<<<Thank you for choosing Guz's>>>>>>>>>")
        sys.exit()
    else:
        # returning_item obj reads data from inventory.csv to check if rental name is in inventory to return
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
                item_status = input("is there any issues with your expensive rental? yes/no ").strip().lower()
                print("\n")
                if item_status == "yes":
                    time.sleep(1.3)
                    print(returning_item.name + " are damaged time to pay the consequences!")
                    time.sleep(1)
                    print("Your deposit will not be returned due to your irresponsibility:( you owe the following:$"+
                            str(int(returning_item.replacement_value)) +
                            " dollars for replacement of the item. and "
                            + "$" + str(int(returning_item.price) * int(weeks)) + " for rent.")
                    revenue = int(returning_item.price) * int(weeks)
                    
                    tax = revenue * 0.07
                    renovate_transaction(week_format, returning_item.name,
                    "Rental Reimbursed", 'transaction.csv')
                    rerun()
                elif item_status == 'no':
                    # return_deposit obj gets price of rental and multiplies the fee by weeks rented
                    print("This is what you owe my fellow client: $"+
                    str(int(returning_item.price) * int(weeks)) + " for the rental fee.")
                    return_deposits(returning_item.deposit, 'deposit.csv')
                    # if not demaged returning_item obj gets name and quantity and adds rental back to inventory

                    renovate_inventory(returning_item.name, int(returning_item.quantity)+1, 'inventory.csv')
                    revenue = int(returning_item.price) * int(weeks)
                    tax = revenue * 0.07
                    renovate_transaction(week_format, returning_item.name,
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
