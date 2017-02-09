from datetime import date, datetime
import pickle

class Transaction:
    def __init__(self, datetime, item, status):
        self.datetime = date
        self.item = item
        self.status = str

    def __repr__(self):
        return 'Transaction(date={},item={},status={})'.format(repr(self.datetime), repr(self.item),
                                                                   repr(self.status))


transaction = {
    'Transaction': (date.today(), 'item', 'status')
}

# Stores data (serialize)

def save(transaction):
    with open('Transaction.csv', 'wb') as data:
        pickle.dump(transaction, data)

# Loads(deserialize)

def load():
    with open('Transaction.csv', 'rb') as data:
        return pickle.load(data)

save(transaction)
