# ISM3232 Midterm: Cloudstep Software

- **Name:** Darian Peters
- **Version:** 1.3.0
- **Date:** 10/23/2026

## What This Program Does
This program takes the records of Cloudstep Software's clients and transforms them into a simple to read, plaintext report.

## Business Rules
This program relies on six business rules:
1. The order total is equal to the price per seat times the number of seats.
2. The discount applied onto the order depends on the number of seats: Fewer than 10 seats get no discount, fewer than 50 get a 7% discount, and 50 or more seats get a 16% discount.
3. The 16% discount is only applicable for educational institutions.
4. Every order has a $60 onboarding fee unless the discounted total is greater than $400.
5. Any order totalling more than $5,000 requires contract review
6. Any order totalling more than $3,000 or having 25 seats or more gets a dedicated trainer.

## How to Run
Input the following commands in your terminal, in order:
```
cd ~/ism3232-midterm
python -m venv .venv
source .venv/bin/activate
pip install -r requirements
python3 main.py
```
## How to Test
Input the following commands in your terminal for testing:
```
ruff format .
ruff check .
pytest -v
```
There are 24 tests in test_business_rules.py that pytest runs when called. They are:
1. **test_calculate_license_cost()**: Ensures that the calculate_license_cost() function works properly.
2. **test_discount_low()**: Ensures that orders with less than 10 seats receive no discount.
3. **test_discount_low_boundary()**: Ensures that orders with exactly 10 seats receive a 7% discount.
4. **test_discount_high()**: Ensures that orders greater than 10 seats receive a 7% discount.
5. **test_discount_high_education()**: Ensures that orders from educational institutions with greater than 50 receive a 16% discount.
6. **test_discount_high_education_boundary()**: Ensures that orders from educational institutions with exactly 50 seats recieve a 16% discount.
7. **test_calculate_license_total_low_discount()**: Ensures that order totals are calculated with the correct onboarding fees and discounts when there are less than 10 seats (no discount).
8. **test_calculate_license_total_high_discount()**: Ensures thatEnsures that order totals are calculated with the correct onboarding fees and discounts when there are less than 10 seats and discounted totals are greater than $400.
9. **test_calculate_license_total_onboard_boundary()**: Ensures that orders with a discounted total of exactly $400 still recieve an onboarding fee.
10. **test_calculate_license_total_onboard_education_boundary()**: Ensures that orders from educational institutions with a discounted total of exactly $400 still recieve an onboarding fee.
11. **test_needs_contract_review_low()**: Ensures that orders totalling less than $5,000 do not require contract review.
12. **test_needs_contract_review_high()**: Ensures that orders totalling more than $5,000 do require contract review.
13. **test_needs_contract_review_boundary()**: Ensures that orders totalling exactly $5,000 do not require contract review.
14. **test_needs_trainer_false_false()**: Ensures that orders with less than 25 seats and totalling less than $3,000 are not assigned a dedicated trainer.
15. **test_needs_trainer_true_false()**: Ensures that orders with more than 25 seats are assigned a dedicated trainer.
16. **test_needs_trainer_false_true()**: Ensures that orders totalling more than $3,000 are assigned a dedicated trainer.
17. **test_needs_trainer_true_true()**: Likely redundant, but ensures that orders with more than 25 seats and totalling more than $3,000 are assigned a dedicated trainer.
18. **test_needs_trainer_seats_boundary()**: Ensures that orders with exactly 25 seats are assigned a dedicated trainer.
19. **test_needs_trainer_total_boundary()**: Ensures that orders totalling exactly $3,000 are not assigned a dedicated trainer.
20. **test_total_licensed()**: Ensures that total_licensed() correctly sums all order totals
21. **test_largest_license()**: Ensures that largest_license() correctly identifies the order with the largest license.
22. **test_largest_license_tie()**: Ensures that if there is a tie for the largest order, the order that comes first is returned.
23. **test_largest_license_empty()**: Ensures that if an empty list is passed through, an empty string is returned.
24. **test_format_license_line()**: Ensures that report entries follow the standardized format.

## Files in This Repository
The files in this repository are:
- **README.md**: The file you're reading now!
- **business_rules.py**: Python script containing all functions that enforce the business rules.
- **commands.md**: Log of activity done in the terminal during the making of this project.
- **main.py**: The primary executable python script that contains all records.
- **tests**: Repository containing the aforementioned testing functions.
- **eggman.jpg**: eggman

## AI Use Statement
AI was not used at any time during this project.