from business_rules import (
    calculate_license_total,
    format_license_line,
    gets_trainer,
    largest_license,
    needs_contract_review,
    total_licensed,
)

orders = [
    {"company": "Pine Books", "seat_price": 40.00, "seats": 5, "education": False},
    {"company": "Quarry School", "seat_price": 35.00, "seats": 12, "education": True},
    {"company": "Redwood Cargo", "seat_price": 45.00, "seats": 60, "education": False},
    {"company": "Summit College", "seat_price": 50.00, "seats": 150, "education": True},
    {"company": "Tidal Health", "seat_price": 55.00, "seats": 100, "education": False},
    {"company": "Upland Farms", "seat_price": 60.00, "seats": 24, "education": False},
    {"company": "Vega Dental", "seat_price": 30.00, "seats": 25, "education": True},
    {"company": "Willow Law", "seat_price": 400.00, "seats": 9, "education": False},
]
total_reviews = 0
total_trainers = 0
total_orders = 0

print("Cloudstep Software - Order Report")
for order in orders:
    company = order["company"]
    total = calculate_license_total(
        order["seat_price"], order["seats"], order.get("education", False)
    )
    contract_review = needs_contract_review(total)
    if contract_review:
        total_reviews += 1
    trainer = gets_trainer(order["seats"], total)
    if trainer:
        total_trainers += 1
    print(format_license_line(company, total, contract_review, trainer))
    total_orders += 1
print(f"Orders: {total_orders}")
print(f"Total licensed: ${total_licensed(orders):.2f}")
print(f"Average license total: ${total_licensed(orders) / total_orders:.2f}")
print(f"Largest license total: {largest_license(orders)}")
print(f"Contract reviews needed: {total_reviews}")
print(f"Trainers assigned: {total_trainers}")
