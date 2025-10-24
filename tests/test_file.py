import pytest
from src.item import *

test_create_item():
    #arrange
    name = 'Desk'
    price = '5.00'
    count = 3

    #act
    product = Item(name, price, count)

    #assert
    assert(Product.get_name() == name)
    assert(Product.get_price() == price)
    assert(Product.get_count() == count)


