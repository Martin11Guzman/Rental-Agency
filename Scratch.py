# from datetime import date, datetime
# import pickle
# from Classes import *
# import os
# """
#                                  # SCRATCH FILE
#                                  IGNORE all code within this file..
#                                  This file was for notes,examples,trial and error testing, and scratch work.
#
# """
#
#
# def menu():
#     "Determines all customer actions and takes inputs to complete them"
#     print("Welcome to Guz's Medical Equipment Rental Agency!")
#     choice = input("rent or return\n").strip().lower()
#     if choice == "rent":
#
# """ ...Inventory..............."""
#
#
# def update_inventory(name, quantity, f):
#     Item_obj_l = []
#     inv = data_from_file(f)
#     for i in inv:
#         Item_obj_l.append(Rental(i[0], i[1], i[2], i[3], i[4]))
#     for i in Item_obj_l:
#         if i.name == name:
#             i.quantity = quantity
#     file = open(f, 'w')
#     writer = csv.writer(file, delimiter=',')
#     for i in Item_obj_l:
#         writer.writerow([i.name, i.replacement_value, i.deposit_value, i.deposit_value, i.price, i.quantity])
#     file.close()
#     with open(f) as file:
#         inv = file.read()
#         return inv
#
# def write_row(f, values_to_write):
#     with open(f, 'a', newline='') as file:
#         writer = csv.writer(file)
#         for row in values_to_write:
#             writer.writerow(row)
#     with open(f) as file:
#         data = file.read()
#         return data
#
#
# def choose_item(inventory_items, name):
#     customer_item = ''
#     for i in inventory_items:
#         customer_item = Rental(i[0], i[1], i[2], i[3], i[4],)
#     if customer_item.name == name:
#         return customer_item
#     else:
#         customer_item = None
#         return customer_item
#
# def view_trans(trans_list):
#     trans_string = ""
#     for transaction in trans_list:
#         trans_string += ("\nDatetime: " + str(transaction[0]) + "\nItem:" + str(transaction[1]) + "\nstatus " + str(transaction[2]) + "\n")
#         return trans_string
#
# def view_inv(inventory_list):
#     inventory_string = ''
#     for item in inventory_list:
#         inventory_string += ('\nProduct: ' + str(item[0]) + '\nreplacement value: ' + "$" + str(item[1]) + '\ndeposit: '+"$"+ str(item[2])+ "\nflat rate of: "+ "$" + str(item[3])+ '\ncurrent stock: '+ str(item[4])+ "\n")
#     return inventory_string
#
#
#
#
# def update_transaction(date, item, status, filename):
#     return write_row(filename, [[date, item, status]])
#
#
# def update_revenue(rent, sales_tax, filename):
#     return write_row(filename, [[rent, sales_tax]])
#
#
#
# def update_deposits(deposit, filename):
#
#     return write_row(filename, [[deposit]])
#
#
# def return_deposits(item, filename):
#     deposit = data_from_file(filename)
#     if len(deposit) == 0:
#         print("There are not items to be returned did you mean to rent? ")
#     else:
#         new_deposit = []
#         for i in deposit:
#             new_deposit.append(i[0])
#         new_deposit.pop(new_deposit.index(item))
#         open(filename, 'w').close()
#         with open(filename, 'w') as file:
#             writer = csv.writer(file)
#             for i in new_deposit:
#                 writer.writerow([i])
#
#
# def view_revenue(file1, file2):
#     revenue_list = []
#     tax_list = []
#     deposits_list = []
#     rev = data_from_file(file1)
#     if len(rev) > 0:
#         for i in rev:
#             revenue_list.append(int(i[0]))
#             tax_list.append(float(i[1]))
#             total = sum(revenue_list)
#             tax = sum(tax_list)
#             final_total = total + tax
#     else:
#         tax = 0
#         total = 0
#         final_total = 0
#     deposits = data_from_file(file2)
#     for deposit in deposits:
#         deposits_list.append(int(deposit[0]))
#     deposit_total = sum(deposits_list)
#     return "All current pending deposits: " + "$", deposit_total, "total w/o tax: $", total, "sales tax: $", tax, "total: $", final_total
# # load(repr(inventory_items))
#
#
#
#
#
#
#
# """" CORE """
# import datetime
# from Classes import *
# from inventory import *
# import sys
# import os
#
#
#
#
#
#
#
# def customer():
#     "Determines all customer actions and takes inputs to complete them"
#     print('Are you renting or returning an item? ')
#     choice = input("rent or return\n").strip().lower()
#     if choice == "rent":
#         rent()
#     elif choice == "return":
#         return_item()
#     elif choice == "q":
#         print("System closing...")
#         sys.exit()
#     else:
#         print("\nINVALID INPUT\n")
#         print('did you mean rent or return? ')
#         customer()
#
#
# def rent():
#     "Input determines what item is being rented"
#     inv = data_from_file('inventory.csv')
#     print(view_inv(inv))
#     item = input("What will you be renting? Product name: ").strip().capitalize()
#     if item == "Q":
#         print('System closing...')
#         sys.exit()
#     else:
#         customer_choice = choose_item(data_from_file('inventory.csv'), item)
#         if customer_choice == None:
#             print("\nInvalid choice " + item + " is not in inventory\n")
#             rent()
#         else:
#             print(customer_choice.deposit_value, customer_choice.price)
#             print("You must place a deposit of $", customer_choice.deposit_value, "along with a fee of $",
#                   customer_choice.price, "every hour the item is rented. Deposits are refunded upon return.\n")
#             print("Confirm you purchase for\n", str(customer_choice))
#             confirmation = input('y/n\n').strip().lower()
#             if confirmation == "y":
#                 update_inventory(customer_choice.name, int(customer_choice.quantity) - 1, 'inventory.csv')
#                 update_transaction(datetime.datetime.now(), customer_choice.name, "pending", 'transaction.csv')
#                 update_deposits(customer_choice.deposit_value, 'deposit.csv')
#                 restart()
#             elif confirmation == "n":
#                 restart()
#             elif confirmation == "q":
#                 print("System closing...")
#                 sys.exit()
#             else:
#                 print('invalid entry')
#                 restart()
#
#
# def restart():
#     "Takes in user input to direct them to a different program section of their choice"
#     print(
#         "\nType: rent to rent an item\nType: return to return an item\nType: start to restart program\nType: q to quit\n")
#     choice = input().strip().lower()
#     if choice == "rent":
#         rent()
#     elif choice == "return":
#         return_item()
#     elif choice == "start":
#         start()
#     elif choice == "q":
#         print('System closing....')
#     else:
#         print("invalid input")
#         restart()
#
#
# def return_item():
#     "contains inputs to determine how to calculate revenue on returned items"
#     inv = data_from_file('inventory.csv')
#     for item in inv:
#         print("\n" + item[0])
#     item = input("\nWhat item are you returning\n").strip().capitalize()
#     if item == 'Q':
#         print("System closing....")
#         sys.exit()
#     else:
#         returning_item = get_item_by_name(data_from_file('inventory.csv'), item)
#         if returning_item == None:
#             print("Invalid Input " + item + " is not in inventory to be returned")
#             return_item()
#         else:
#             hours = input("How many hours was the product rented? ").strip().lower()
#             if hours == "q":
#                 print('System closing....')
#                 sys.exit()
#             elif hours.isdigit():
#                 item_status = input("Is the product broken or damaged y/n? ").strip().lower()
#                 if item_status == "y":
#                     print("Your deposit will not be returned you owe the following:" + str(
#                         returning_item.replacement_value) + " dollars for replacement of the item. and " + "$" + str(
#                         int(returning_item.price) * int(hours)) + " for rent.")
#                     rent_amount = int(returning_item.price) * int(hours)
#                     sales_tax = rent_amount * 0.07
#                     update_revenue(rent_amount, sales_tax, 'revenue.csv')
#                     update_transaction(datetime.datetime.now(), returning_item.name, "compensated", 'transaction.csv')
#                     restart()
#                 elif item_status == 'n':
#                     print("Your deposit will be returned you owe the following: $" + str(
#                         int(returning_item.price) * int(hours)) + " for rent.")
#                     return_deposits(returning_item.deposit_value, 'deposit.csv')
#                     update_inventory(returning_item.name, int(returning_item.quantity) + 1, 'inventory.csv')
#                     rent_amount = int(returning_item.price) * int(hours)
#                     sales_tax = rent_amount * 0.07
#                     update_revenue(rent_amount, sales_tax, 'revenue.csv')
#                     update_transaction(datetime.datetime.now(), returning_item.name, "returned", 'transaction.csv')
#                     restart()
#                 elif item_status == "q":
#                     print('System closing....')
#                 else:
#                     print('\nInvalid Input\n')
#                     return_item()
#
#             else:
#                 print('invalid input')
#                 print('hours must be a number')
#                 return_item()
#
#
# def start():
#     "Initialized program start"
#
#     print('At anytime q will exit program')
#     action = input('Are you a customer or manager\n').strip().lower()
#     if action == "customer":
#         customer()
#     elif action == "manager":
#         manager()
#     elif action == "q":
#         print('System closing....')
#         sys.exit()
#     else:
#         print("\nINVALID INPUT\n")
#         start()
#
#
# def manager():
#     "Inputs for all manager actions"
#     choice = input(
#         'Type: i to view inventory\nType: t to view transaction history\nType: r to view revenue\nType: Replace to add a replacement item to inventory.\nType: s to restart\n').strip().lower()
#     if choice == "i":
#         inv = data_from_file('inventory.csv')
#         print(view_inv(inv))
#         manager()
#     elif choice == "t":
#         trans = data_from_file('transaction.csv')
#         print(view_trans(trans))
#         manager()
#     elif choice == "r":
#         trans = data_from_file('revenue.csv')
#         print("\n")
#         rev = view_revenue('revenue.csv', 'deposit.csv')
#         print(rev[0], rev[1], "\n" + rev[2], rev[3], "\n" + rev[4], rev[5], "\n" + rev[6], rev[7])
#         print("\n")
#         manager()
#     elif choice == 'rq':
#         name = input("Product being replaced: ").strip().capitalize()
#         quantity = input("How many? ").strip()
#         if quantity.isdigit() != True:
#             print("invalid input")
#             manager()
#         if name == "q" or quantity == "q":
#             print('System closing...')
#             sys.exit()
#         inv = data_from_file("inventory.csv")
#         item = get_item_by_name(inv, name)
#         if item == None:
#             print('invaid input')
#             manager()
#         update_inventory(name, int(item.quantity) + int(quantity), 'inventory.csv')
#         print("\nInventory has been updated\n")
#         manager()
#     elif choice == "s":
#         start()
#     elif choice == "q":
#         print('System closing....')
#         sys.exit()
#
#
# start()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # inventory_items = [Rental('Wheelchair', 20, 90, 100, 900), Rental('Scooters', 20, 100, 100, 1000),
# #                    Rental('Hospital Bed', 20, 300, 100, 3000), Rental('Stretchers', 20, 100, 100, 1000, ),
# #                    Rental('Surgical Tools', 20, 20, 100, 200), Rental('MRI Machines', 20, 400, 100, 4000),
# #                    Rental('Leg Braces', 20, 40, 100, 400), Rental('Shower chair', 20, 10, 100, 100),
# #                    Rental('Walking boot', 20, 20, 100, 200), Rental('X-ray machine', 20, 500, 100, 5000),
# #                    Rental('Crutches', 20, 50, 100, 500)]
# # class Transaction:
# #
# #     def __init__(self, date, inventory_item, status):
# #         self.date = date
# #         self.inventory_item = inventory_item
# #         self.status = status
# #
# #
# #     def __repr__(self):
# #         return 'Transaction(date={},inventory_item={},status={})'.format(repr(self.date), repr(self.inventory_item),
# #                                                                    repr(self.status))
# #
# #
# # transaction = [
# #     Transaction(date.today(), 'inventory_item', 'status')
# # ]
# #
# # # Inventory
# # def add_trans(inventory_item):
# #     with open('Transaction.p', 'wb') as data:
# #      update = pickle.dump(transaction, data)
# #
# #     return repr(Transaction)
# #
# # # class Transaction
# #  def in_stock(self):
# #         if self.quantity > 0:
# #             return True
# #         else:
# #             return False
# #
# # # Stores data (serialize)
# #
# # def save(transaction):
# #     with open('Transaction.', 'wb') as data:
# #         pickle.dump(transaction, data)
# #
# # print(repr(transaction))
# #
# #
# # #  Loads(deserialize)
# #
# # def load():
# #     with open('Transaction.csv', 'rb') as data:
# #         return pickle.load(data)
# #
# #
# # class TestClass:
# #     def test_one(self):
# #         x = "this"
# #         assert 'h' in x
# #
# #     def test_two(self):
# #         x = "hello"
# #         assert hasattr(x, 'check')
# #
# #
# #
# # def choose_item(inventory_items, name):
# #     customer_item = ''
# #     for i in inventory_items:
# #         customer_item = Rental(i[0], i[1], i[2], i[3], i[4],)
# #     if customer_item.name == name:
# #         return customer_item
# #     else:
# #         customer_item = None
# #         return customer_item