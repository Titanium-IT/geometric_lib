import pytest
from square import area, perimeter


# Тест для функции area
def test_area():
    a = 4  # Пример стороны квадрата
    expected_area = a * a
    assert (
        area(a) == expected_area
    )  # Проверяем, что возвращаемое значение совпадает с ожидаемым


# Тест для функции perimeter
def test_perimeter():
    a = 4  # Пример стороны квадрата
    expected_perimeter = 4 * a
    assert (
        perimeter(a) == expected_perimeter
    )  # Проверяем, что возвращаемое значение совпадает с ожидаемым


# Дополнительный тест для другого значения стороны квадрата
def test_area_edge_case():
    a = 0  # Сторона квадрата равна 0
    assert area(a) == 0  # Площадь квадрата с нулевой стороной должна быть 0


def test_perimeter_edge_case():
    a = 0  # Сторона квадрата равна 0
    assert perimeter(a) == 0  # Периметр квадрата с нулевой стороной должен быть 0
