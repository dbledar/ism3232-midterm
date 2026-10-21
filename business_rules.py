# business_rules.py
# Author: Darian Peters


def calculate_license_cost(seat_price: float, seats: int) -> float:
    """Returns the total license cost based on seat price and number
    of seats"""
    return seat_price * seats


def get_seat_discount(seats: int, education: bool = False) -> float:
    """Returns the total discount based on number of seats and
    whether the customer is an education customer"""
    if seats < 10:
        return 0.0
    elif seats >= 10 and seats < 50:
        return 0.07
    else:
        if education:
            return 0.16
        else:
            return 0.07


def calculate_license_total(
    seat_price: float, seats: int, education: bool = False
) -> float:
    """Returns the license total for one order based on discount and
    onboarding fee (if it applies)"""
    license_cost = calculate_license_cost(seat_price, seats)
    discount = get_seat_discount(seats, education)
    if discount * license_cost <= 400:
        onboard_fee = 60
    else:
        onboard_fee = 0

    return license_cost * (1 - discount) + onboard_fee
