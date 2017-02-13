from Classes import *
import pickle
import csv




def load(Rental):
    try:
        with open('inventory.p', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return inventory_items



def save():
    with open('inventory.p', 'wb') as data:
        pickle.dump(inventory_items, data)

# def choose_item(inventory_items, name):
#     customer_item = ''
#     for i in inventory_items:
#         customer_item = Rental(i[0], i[1], i[2], i[3], i[4],)
#     if customer_item.name == name:
#         return customer_item
#     else:
#         customer_item = None
#         return customer_item
# load(repr(inventory_items))





