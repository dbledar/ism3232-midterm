from business_rules import (
    calculate_license_cost,
    calculate_license_total,
    format_license_line,
    get_seat_discount,
    gets_trainer,
    largest_license,
    needs_contract_review,
    total_licensed,
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
    assert round(calculate_license_total(100, 4), 2) == 460.0


def test_calculate_license_total_high_discount():
    assert calculate_license_total(100, 100) == 9300.0


def test_calculate_license_total_onboard_boundary():
    assert calculate_license_total((1 / 93), 40000) == 460.0


def test_calculate_license_total_onboard_education_boundary():
    assert round(calculate_license_total((1 / 21), 10000, True), 2) == 460.0


def test_needs_contract_review_low():
    assert not needs_contract_review(100.0)


def test_needs_contract_review_high():
    assert needs_contract_review(10000.0)


def test_needs_contract_review_boundary():
    assert not needs_contract_review(5000.0)


def test_gets_trainer_false_false():
    assert not gets_trainer(5, 100.0)


def test_gets_trainer_true_false():
    assert gets_trainer(50, 100.0)


def test_gets_trainer_false_true():
    assert gets_trainer(5, 10000.0)


def test_gets_trainer_true_true():
    assert gets_trainer(50, 10000.0)


def test_gets_trainer_seats_boundary():
    assert gets_trainer(25, 100.0)


def test_gets_trainer_total_boundary():
    assert not gets_trainer(5, 3000.0)


def test_total_licensed():
    assert (
        total_licensed(
            [{"seat_price": 3.0, "seats": 2}, {"seat_price": 6.0, "seats": 5}]
        )
        == 156.0
    )


def test_largest_license():
    assert (
        largest_license(
            [
                {"company": "feddy fazbear pizza", "seat_price": 3.0, "seats": 2},
                {"company": "afton robots", "seat_price": 6.0, "seats": 5},
            ]
        )
        == "afton robots"
    )


def test_largest_license_tie():
    assert (
        largest_license(
            [
                {"company": "feddy fazbear pizza", "seat_price": 6.0, "seats": 5},
                {"company": "afton robots", "seat_price": 6.0, "seats": 5},
            ]
        )
        == "feddy fazbear pizza"
    )


def test_largest_license_empty():
    assert largest_license([]) == ""


def test_format_license_line():
    assert (
        format_license_line("feddy fazbear", 10.0, False, False)
        == "feddy fazbear: $10.00 | contract review: no | trainer: no"
    )
