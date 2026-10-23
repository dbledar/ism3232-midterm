import math

from business_rules import (
    calculate_license_cost,
    calculate_license_total,
    get_seat_discount,
)


def test_calculate_license_cost():
    assert calculate_license_cost(100, 5) == 500


def test_discount_low():
    assert get_seat_discount(5) == 0.0


def test_discount_low_boundary():
    assert get_seat_discount(10) == 0.07


def test_discount_high():
    assert get_seat_discount(100) == 0.07


def test_discount_high_education():
    assert get_seat_discount(100, education=True) == 0.16


def test_discount_high_education_boundary():
    assert get_seat_discount(50, education=True) == 0.16


def test_calculate_license_total_low_discount():
    assert math.ceil(calculate_license_total(100, 10)) == 930.0


def test_calculate_license_total_high_discount():
    assert calculate_license_total(100, 100) == 9300.0


def test_calculate_license_total_onboard_boundary():
    assert calculate_license_total(43, 10) == 459.9
