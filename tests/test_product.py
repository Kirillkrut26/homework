import pytest

from src.classes import Product


@pytest.fixture()
def iphone():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

@pytest.fixture()
def samsung_product():
    return {'name':'Samsung', 'description':'Норм телефон', 'price':50000.0, 'quantity':5}


def test_Product(iphone,samsung_product):
    assert iphone.name == "Iphone 15"
    assert iphone.description == "512GB, Gray space"
    assert iphone.price == 210000.0
    assert iphone.quantity == 8

    samsung = Product.new_product(samsung_product)
    assert samsung.name == "Samsung"
    assert samsung.description == 'Норм телефон'
    assert samsung.price == 50000.0
    assert samsung.quantity == 5

    samsung.price = 100000.0
    assert samsung.price == 100000.0
    samsung.price = -100000.0
    assert samsung.price == 100000.0

