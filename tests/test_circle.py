import pytest
import math
from circle import area, perimeter


# Тест для функции area
def test_area():
    # Пример радиуса
    r = 3
    expected_area = math.pi * r * r
    assert area(r) == pytest.approx(
        expected_area, rel=1e-9
    )  # Проверка с точностью до 1e-9


# Тест для функции perimeter
def test_perimeter():
    r = 3
    expected_perimeter = 2 * math.pi * r
    assert perimeter(r) == pytest.approx(
        expected_perimeter, rel=1e-9
    )  # Проверка с точностью до 1e-9


# Дополнительный тест для других значений радиуса
def test_area_edge_case():
    r = 0  # Радиус равен 0
    assert area(r) == 0  # Площадь круга с радиусом 0 должна быть 0


def test_perimeter_edge_case():
    r = 0  # Радиус равен 0
    assert perimeter(r) == 0  # Периметр круга с радиусом 0 должен быть 0
