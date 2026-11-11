import pytest

from src.classes import Category, Product


@pytest.fixture()
def smartphones_category():
    iphone = Product("iphone", "какой-то айфон", 100000.0, 5)

    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации,"
        " но и получения дополнительных функций для удобства жизни",
        [iphone],
    )

@pytest.fixture()
def samsung_product():
    return Product("Samsung", "Топ за свои деньги", 80000.0, 3)

def test_Category(smartphones_category, samsung_product):
    assert smartphones_category.name == "Смартфоны"
    assert smartphones_category.description == (
        "Смартфоны,"
        " как средство не только коммуникации,"
        " но и получения дополнительных"
        " функций для удобства жизни"
    )
    assert smartphones_category.products == "iphone, 100000.0 руб. Остаток: 5 шт.\n"
    assert smartphones_category.category_count == 1
    assert smartphones_category.product_count == 1

    smartphones_category.add_product(samsung_product)
    assert smartphones_category.products == (
        "iphone, 100000.0 руб. Остаток: 5 шт.\n"
        "Samsung, 80000.0 руб. Остаток: 3 шт.\n"
    )

    assert smartphones_category.products == (
        "iphone, 100000.0 руб. Остаток: 5 шт.\n"
        "Samsung, 80000.0 руб. Остаток: 3 шт.\n"
    )


    samsung_product.price = 100000.0
    assert samsung_product.price == 100000.0
    samsung_product.price = -100000.0
    assert samsung_product.price == 100000.0

