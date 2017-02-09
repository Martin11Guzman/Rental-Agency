import pickle


class Inventory:
    def __init__(self, quantity, current_quantity, price):
        self.quantity = quantity
        self.current_quantity = current_quantity
        self.price = price

    def __repr__(self):
        return 'Inventory(quantity={},current_quantity={},price={})'.format(repr(self.quantity),
                                                                            repr(self.current_quantity),
                                                                            repr(self.price))


inventory_items = {
    'Wheelchair': Inventory(20, 20, 900),
    'Scooters': Inventory(20, 20, 1000),
    'Hospital Beds': Inventory(20, 20, 3000),
    'Stretchers': Inventory(20, 20, 1000),
    'Surgical tools': Inventory(20, 20, 200),
    'MRI machines': Inventory(20, 20, 4000),
    'Leg Braces': Inventory(20, 20, 400),
    'Shower chair': Inventory(20, 20, 100),
    'Walking boot': Inventory(20, 20, 200),
    'X-ray machine': Inventory(20, 20, 5000),
    'Crutches': Inventory(20, 20, 500)}


# Stores data (serialize)

def save(inventory_items):
    with open('Inventory.csv', 'wb') as data:
        pickle.dump(inventory_items, data)

# Loads(deserialize)

def load():
    with open('Inventory.csv', 'rb') as data:
        return pickle.load(data)

