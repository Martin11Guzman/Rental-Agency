class Rental():
    def __init__(self, name, quantity, deposit, price, replacement_value):
        self.name = name
        self.quantity = quantity
        self.deposit = deposit
        self.price = price
        self.replacement_value = replacement_value


    def __repr__(self):
        return 'Rental(name={},quantity={},deposit={},price={},replacement_value={})'.format(repr(self.name),
        repr(self.quantity), repr(self.deposit), repr(self.price), repr(self.replacement_value))


def inv_items():

    inventory_items = [['Wheelchair', 20, 90, 100, 900], ['Scooters', 20, 100, 100, 1000],
                       ['Hospital bed', 20, 300, 100, 3000], ['Stretchers', 20, 100, 100, 1000, ],
                       ['Surgical tools', 20, 20, 100, 200], ['Mri machine', 20, 400, 100, 4000],
                       ['Leg braces', 20, 40, 100, 400], ['Shower chair', 20, 10, 100, 100],
                       ['Walking boot', 20, 20, 100, 200], ['X-ray machine', 20, 500, 100, 5000],
                       ['Crutches', 20, 50, 100, 500]]
    return inventory_items



def pick_password():
    file = '/home/basecamp/Desktop/Rental-Agency/pswd.txt'
    print("Please input the same username you registered' ")
    password = input()
    target = open(file, 'w')
    target.write(password)
    file = '/home/basecamp/Desktop/Rental-Agency/existence_check.txt'
    target = open(file, 'w')
    target.write('YES')

def password_check():
    file = '/home/basecamp/Desktop/Rental-Agency/pswd.txt'
    pwd_check = open(file).read()
    userpass = input("Create a Username.. If your such a 'CEO'\n")
    if userpass == pwd_check:
        print('Username accepted!')
        print('Saved into our Extremely secured Database so no worries!;)?')

    elif userpass != pwd_check:
        print('Sorry, wrong password.\n')
        exit()
    else:
        print('Invalid syntax.')
        exit()








class Transaction():
    """ This object symbolizes a transaction that has been made."""
    def __init__(self, datetime, inventory_items, status):
        self.datetime = datetime
        self.inventory_item = inventory_items
        self.status = status


    def __str__(self):
        return "date: " + str(self.datetime) + " Item " + str(self.inventory_item) + " status " + str(self.status)
