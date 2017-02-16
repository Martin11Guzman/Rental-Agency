# from inventory import *
# def rent():
#     "Input determines what item is being rented"
#     show = data_from_file('inventory.csv')
#     print(view_inv(show))
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
#             print("You must place a deposit of $", customer_choice.deposit_value,\
#                 "along with a fee of $", customer_choice.price,\
#                 "every hour the item is rented. Deposits are refunded upon return.\n")
#             print("Confirm you purchase for\n", str(customer_choice))
#             confirmation = input('y/n\n').strip().lower()
#             if confirmation == "y":
#                 update_inventory(customer_choice.name, \
#                 int(customer_choice.quantity)- 1, 'inventory.csv')
#                 update_transaction(datetime.datetime.now(),\
#                  customer_choice.name, "pending", 'transaction.csv')
#                 update_deposits(customer_choice.deposit_value, 'deposit.csv')
#                 restart()
#             elif confirmation == "n":
#                 restart()
#             elif confirmation == "q":
#                 print("System closing...")
#                 sys.exit()
#             else:
#                 print('invalid entry')
# restart()