import csv
from collections import namedtuple, OrderedDict

Item = namedtuple('Item', ['quantity', 'current_quantity', 'price'])
Inventory = OrderedDict([
    ('Wheelchair:', Item(20, 20, 900)),
    ('Scooters:', Item(20, 20, 1000)),
    ('Hospital Beds:', Item(20, 20, 3000)),
    ('Stretchers:', Item(20, 20, 1000)),
    ('Surgical tools:', Item(20, 20,  200)),
    ('MRI machines:', Item(20, 20, 4000)),
    ('Leg Braces:', Item(20, 20, 400)),
    ('Shower chair:', Item(20, 20,  100)),
    ('Walking boot:', Item(20, 20, 200)),
    ('X-ray machine:', Item(20, 20, 5000)),
    ('Crutches:', Item(20, 20, 500))])



with open('Inventory.csv', 'w') as f:
    w = csv.writer(f)
    w.writerow(('name', 'quantity', 'current_quantity', 'price'))    # field header
    w.writerows([(name, data.quantity, data.current_quantity, data.price) for name, data in Inventory.items()])
