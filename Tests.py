from Classes import *
import pytest
import os
import datetime
import csv
from inventory import *

""" Module purpose is to Test my logic of this Application"""





class Test_Rental():
    def test_class_rental(self):
        items = Rental('Wheelchair', 20, 90, 100, 900)
        assert items.name == 'Wheelchair'
        assert items.quantity == 20
        assert items.deposit == 90
        assert items.price == 100
        assert items.replacement_value == 900
        assert repr(items) == 'Rental(name={},quantity={},deposit={},price={},replacement_value={})'.format(repr(items.name),
        repr(items.quantity), repr(items.price), repr(items.deposit), repr(items.replacement_value))
