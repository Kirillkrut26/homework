import pytest

from src.classes import Category


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
