import pytest
from src.model import *

test_create_product():
    #arrange
    name = 'Desk'
    price = '5.00'
    count = 3

    #act
    product = Product(name, price, count)

    #assert
    assert(Product.get_name() == name)
    assert(Product.get_price() == price)
    assert(Product.get_count() == count)


