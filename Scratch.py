from inventory import *





def choose_item(inventory_list, name):
    for i in inventory_list:
        customer_item = Rental(i[0], i[1], i[2], i[3], i[4])
        if customer_item.name == name:
            return customer_item
        else:
            customer_item = None
        return customer_item

def update_deposits(deposit, f):
    return write_row(f, [[deposit]])

def update_revenue(rent, sales_tax, f):
    return write_row(f, [[rent, sales_tax]])













