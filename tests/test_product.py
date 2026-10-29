import pytest

from src.classes import Product


@pytest.fixture()
def iphone():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


def test_Product(iphone):
    assert iphone.name == "Iphone 15"
    assert iphone.description == "512GB, Gray space"
    assert iphone.price == 210000.0
    assert iphone.quantity == 8
