import pytest

from src.classes import CategoryIterator, Category, Product


@pytest.fixture()
def smartphones_category():
    iphone = Product("iphone", "какой-то айфон", 100000.0, 5)

    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации,"
        " но и получения дополнительных функций для удобства жизни",
        [iphone],
    )


def test_category_iterator(smartphones_category):
    iterator = CategoryIterator(smartphones_category)
    assert next(iterator).name == "iphone"

    with pytest.raises(StopIteration):
        next(iterator)
