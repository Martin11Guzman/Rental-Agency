from datetime import date, datetime
import pickle
from Classes import *
"""
                                 # SCRATCH FILE
                                 IGNORE all code within this file..
                                 This file was for notes,examples,trial and error testing, and scratch work.

"""

inventory_items = [Rental('Wheelchair', 20, 90, 100, 900), Rental('Scooters', 20, 100, 100, 1000),
                   Rental('Hospital Bed', 20, 300, 100, 3000), Rental('Stretchers', 20, 100, 100, 1000, ),
                   Rental('Surgical Tools', 20, 20, 100, 200), Rental('MRI Machines', 20, 400, 100, 4000),
                   Rental('Leg Braces', 20, 40, 100, 400), Rental('Shower chair', 20, 10, 100, 100),
                   Rental('Walking boot', 20, 20, 100, 200), Rental('X-ray machine', 20, 500, 100, 5000),
                   Rental('Crutches', 20, 50, 100, 500)]
class Transaction:

    def __init__(self, date, inventory_item, status):
        self.date = date
        self.inventory_item = inventory_item
        self.status = status


    def __repr__(self):
        return 'Transaction(date={},inventory_item={},status={})'.format(repr(self.date), repr(self.inventory_item),
                                                                   repr(self.status))


transaction = [
    Transaction(date.today(), 'inventory_item', 'status')
]

# Inventory
def add_trans(inventory_item):
    with open('Transaction.p', 'wb') as data:
     update = pickle.dump(transaction, data)
    
    return repr(Transaction)

# class Transaction
 def in_stock(self):
        if self.quantity > 0:
            return True
        else:
            return False

# Stores data (serialize)

def save(transaction):
    with open('Transaction.', 'wb') as data:
        pickle.dump(transaction, data)

print(repr(transaction))


#  Loads(deserialize)

def load():
    with open('Transaction.csv', 'rb') as data:
        return pickle.load(data)


class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')


