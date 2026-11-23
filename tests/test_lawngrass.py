import pytest

from classes import LawnGrass


@pytest.fixture
def grass():
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.00,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )


def test_lawngrass(grass):
    assert grass.name == "Газонная трава"
    assert grass.description == "Элитная трава для газона"
    assert grass.price == 500.00
    assert grass.quantity == 20
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"
