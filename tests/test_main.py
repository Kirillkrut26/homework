import pytest

from src.main import Product, Category


@pytest.fixture()
def iphone():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


def test_Product(iphone):
    assert iphone.name == "Iphone 15"
    assert iphone.description == "512GB, Gray space"
    assert iphone.price == 210000.0
    assert iphone.quantity == 8


@pytest.fixture()
def smartphones_category(iphone):
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации,"
        " но и получения дополнительных функций для удобства жизни",
        [iphone],
    )


def test_Category(smartphones_category, iphone):
    assert smartphones_category.name == "Смартфоны"
    assert smartphones_category.description == (
        "Смартфоны,"
        " как средство не только коммуникации,"
        " но и получения дополнительных"
        " функций для удобства жизни"
    )
    assert smartphones_category.products == [iphone]
    assert smartphones_category.category_count == 1
    assert smartphones_category.product_count == 1
