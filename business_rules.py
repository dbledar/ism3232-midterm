# business_rules.py
# Author: Darian Peters


def calculate_license_cost(seat_price: float, seats: int) -> float:
    """Returns the total license cost based on seat price and number
    of seats"""
    return seat_price * seats


def get_seat_discount(seats: int, education: bool = False) -> float:
    """Returns the total discount based on number of seats and
    whether the customer is an education customer. Seats less than
    10 gets no discount, otherwise gets 7% discount, education
    customers receive a 16% discount for 50 or more."""
    if seats < 10:
        return 0.0
    else:
        if education and seats >= 50:
            return 0.16
        else:
            return 0.07


def calculate_license_total(
    seat_price: float, seats: int, education: bool = False
) -> float:
    """Returns the license total for one order based on discount and
    onboarding fee (if the discounted amount is less than $400)."""
    license_cost = calculate_license_cost(seat_price, seats)
    discount = get_seat_discount(seats, education)
    if license_cost * (1 - discount) <= 400:
        onboard_fee = 60
    else:
        onboard_fee = 0

    return license_cost * (1 - discount) + onboard_fee


def needs_contract_review(total: float) -> bool:
    """Returns True when the license total is greater than $5,000."""
    return total > 5000.0


def gets_trainer(seats: int, total: float) -> bool:
    """Returns True if the customer buys 25 seats or more or if the
    license total is greater than $3,000."""
    return seats >= 25 or total > 3000.0


def total_licensed(orders: list) -> float:
    """Returns the sum of the license total for every order in
    the list without using sum()"""
    total = 0.0
    for order in orders:
        total += calculate_license_total(
            order["seat_price"], order["seats"], order.get("education", False)
        )
    return total


def largest_license(orders: list) -> str:
    """Returns the name of the company whose order has the
    largest license total"""
    largest = 0.0
    company = ""

    for order in orders:
        total = calculate_license_total(
            order["seat_price"], order["seats"], order.get("education", False)
        )
        if total > largest:
            largest = total
            company = order["company"]

    return company


def format_license_line(
    company: str,
    total: float,
    contract_review: bool,
    trainer: bool,
) -> str:
    """Returns one line of the report."""
    return f"{company}: ${total:.2f} | contract review: {'yes' if contract_review else 'no'} | trainer: {'yes' if trainer else 'no'}"
