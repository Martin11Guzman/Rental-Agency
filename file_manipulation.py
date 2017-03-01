from inventory import *
import datetime
import csv
import time

"""This file involves functions that directly communicate to the percistent files that collect data"""


def check_if_files_exist():
    """ None ->  None
    function checks path to see if files exist

                    """
    datafile="/home/basecamp/Desktop/Rental-Agency/inventory.csv"
    try:
        make_data_files(datafile)
        make_data_files('deposit.csv')
        make_data_files('transaction.csv')
        make_rows("inventory.csv", inv_items())
        print("<<<<<<<ESTABLISHING FILES>>>>>>>")
        time.sleep(1)
        print("Testing Inventory's  dns server, please wait till data loads...")
    except IOError as e:
       print("Error: %s not found." % datafile)

def make_data_files(f):
    """(f) -> None"""
    with open(f, 'w') as files:
        return files.close()

def data_from_file(f):
    """ (list of lists) -> (Rental)"""
    with open(f, newline='') as data:
        invent = csv.reader(data, delimiter=',', quotechar='|')
        return list(invent)
    # with open(f, 'rb') as data:
    #     invent = pickle.load(f)

def make_rows(f, attributes):
    """(f, attributes) -> None"""
    with open(f, 'a', newline='') as file:
        writer = csv.writer(file)
        for row in attributes:
            writer.writerow(row)
    with open(f) as file:
        data = file.read()
        return data

def update_deposits(deposit, f):
    """(deposit(int), file) -> None"""
    return make_rows(f, [[deposit]])

def show_transaction(transactions):
    """datetime, Rental(obj), status(str) -> None"""
    trans_string = ""
    for transaction in transactions:
        trans_string += ("\nDatetime: " + str(transaction[0]) + "\nRental:" + str(transaction[1]) +
                                         "\nstatus " + str(transaction[2]) + "\n")
    return trans_string



def renovate_transaction(date, item, status, f):
    """datetime, Rental(obj), status(str) -> list"""
    return make_rows(f, [[date, item, status]])



