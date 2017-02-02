stock = {'apples': 5, 'oranges': 2, 'pears': 0 }
already_ate = {'john'}
food = input('what food was eaten? ')
person = input('who ate the food? ')

def menu():
    print("Press 1 to add stock. ")
    print("Press 2 to check stock. ")
    print("Press 3 to enter purchase. ")
    print("Press q to quit the program . ")