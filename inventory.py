from Classes import *
import csv


def check_if_files_exist():
    datafile="/home/basecamp/Desktop/Rental-Agency/inventory.csv"
    try:
        make_data_files(datafile)
        make_data_files('revenue.csv')
        make_data_files('deposit.csv')
        make_data_files('transaction.csv')

        print("Testing your dns servers, please wait...")
    except IOError as e:
       print("Error: %s not found." % datafile)

def make_data_files(f):
    with open(f, 'w') as files:
        return files.close()

def data_from_file(f):
    with open(f, newline='') as inv:
        data = csv.reader(inv, delimiter=',', quotechar='|')
        return list(data)


