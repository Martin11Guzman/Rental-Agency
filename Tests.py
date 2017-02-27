from Classes import *
import pytest
import os
import datetime
import csv
from inventory import *

""" Module purpose is to Test my logic of this Application"""



def test_view_inv():
    inventory = [['Wheelchair', '20', '90', '100', '900']]
    test = view_inv(inventory)
    assert test == ('\nRental: ' + 'Wheelchair' + '\nQuantity: '+  '20' + '\nDeposit: '+
"$" + '90' +"\nPrice Per Week: "+ "$" + '100' + '\nReplacement Value: '+ '$' + '900' + "\n")


class Test_Rental():
    def test_class_rental(self):
        items = Rental('Wheelchair', 20, 90, 100, 900)
        assert items.name == 'Wheelchair'
        assert items.quantity == 20
        assert items.deposit == 90
        assert items.price == 100
        assert items.replacement_value == 900
        assert str(items) == 'Rental(name={},quantity={},deposit={},price={},replacement_value={})'.format(str(items.name),
        str(items.quantity), str(items.deposit), str(items.price), str(items.replacement_value))
