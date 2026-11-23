import pytest

from classes import Smartphone


@pytest.fixture
def samsung():
    return Smartphone(
        "Samsung S26 Ultra",
        "флагманский смартфон Samsung 2026 года",
        100999.00,
        10,
        "Хорошая",
        "S26 Ultra",
        512,
        "black",
    )


def test_samsung(samsung):
    assert samsung.name == "Samsung S26 Ultra"
    assert samsung.description == "флагманский смартфон Samsung 2026 года"
    assert samsung.price == 100999
    assert samsung.quantity == 10
    assert samsung.efficiency == "Хорошая"
    assert samsung.model == "S26 Ultra"
    assert samsung.memory == 512
    assert samsung.color == "black"
