import csv
class Rental():
    def __init__(self, name, quantity, deposit, price, replacement_value):
        self.name = name
        self.quantity = quantity
        self.deposit = deposit
        self.price = price
        self.replacement_value = replacement_value


    def __repr__(self):
        return 'Rental(name={},quantity={},deposit={},price={},replacement_value={})'.format(repr(self.name),
        repr(self.quantity), repr(self.price), repr(self.deposit), repr(self.replacement_value))

# inventory_items = [Rental('Wheelchair', 20, 90, 100, 900), Rental('Scooters', 20, 100, 100, 1000),
#                    Rental('Hospital Bed', 20, 300, 100, 3000), Rental('Stretchers', 20, 100, 100, 1000, ),
#                    Rental('Surgical Tools', 20, 20, 100, 200), Rental('MRI Machines', 20, 400, 100, 4000),
#                    Rental('Leg Braces', 20, 40, 100, 400), Rental('Shower chair', 20, 10, 100, 100),
#                    Rental('Walking boot', 20, 20, 100, 200), Rental('X-ray machine', 20, 500, 100, 5000),
#                    Rental('Crutches', 20, 50, 100, 500)]





class Transaction():
    """ This object symbolizes a transaction that has been made."""
    def __init__(self, datetime, inventory_items, status):
        self.datetime = datetime
        self.inventory_item = inventory_items
        self.status = status


    def __str__(self):
        return "date: " + str(self.datetime) + " Item " + str(self.inventory_item) + " status " + self.status

