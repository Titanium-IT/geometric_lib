import pytest
from triangle import area, perimeter


# Тест для функции area
def test_area():
    a, b, c = 3, 4, 5  # Пример длины сторон треугольника (пифагорова тройка)
    expected_area = (a + b + c) / 2
    assert (
        area(a, b, c) == expected_area
    )  # Проверяем, что возвращаемое значение совпадает с ожидаемым


# Тест для функции perimeter
def test_perimeter():
    a, b, c = 3, 4, 5  # Пример длины сторон треугольника (пифагорова тройка)
    expected_perimeter = a + b + c
    assert (
        perimeter(a, b, c) == expected_perimeter
    )  # Проверяем, что возвращаемое значение совпадает с ожидаемым


# Дополнительный тест для другого треугольника
def test_area_edge_case():
    a, b, c = 0, 0, 0  # Треугольник с нулевыми сторонами
    assert area(a, b, c) == 0  # Площадь треугольника с нулевыми сторонами должна быть 0


def test_perimeter_edge_case():
    a, b, c = 0, 0, 0  # Треугольник с нулевыми сторонами
    assert (
        perimeter(a, b, c) == 0
    )  # Периметр треугольника с нулевыми сторонами должен быть 0
