# -*- coding: utf-8 -*-

"""
 White-box code examples.
"""
import re


def is_even(num):
    """
    Checks if a number is even.
    """
    return num % 2 == 0


def divide(a, b):
    """
    Simple division function.
    """
    result = 0
    if b != 0:
        result = a / b
    return result


def get_grade(score):
    """
    Grade function.
    """
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    return grade


def is_triangle(a, b, c):
    """
    Determines if 3 numbers can form a triangle.
    """
    if a + b > c and a + c > b and b + c > a:
        return "Yes, it's a triangle!"

    return "No, it's not a triangle."


# 1
def check_number_status(number):
    """
    Checks if a given number is positive, negative, or zero.
    """
    if number > 0:
        return "Positive"

    if number < 0:
        return "Negative"

    return "Zero"


# 2
def validate_password(password):
    """
    Validates user passwords.
    """
    # Check length
    if len(password) < 8:
        return False

    # Check for at least one uppercase letter, one lowercase letter,
    # one digit, and one special character.
    if (
        not re.search(r"[A-Z]", password)
        or not re.search(r"[a-z]", password)
        or not re.search(r"\d", password)
        or not re.search(r"[!@#$%&]", password)
    ):
        return False

    return True


# 3
def calculate_total_discount(total_amount):
    """
    Calculates the discount for a customer's purchase based on the total amount.
    """
    if total_amount < 100:
        return 0

    if 100 <= total_amount <= 500:
        return 0.1 * total_amount

    return 0.2 * total_amount


# 4
def calculate_order_total(items):
    """
    Processes user orders in an e-commerce system.
    The function calculates the total price of the items in the order,
    applying different discounts based on the quantity of each item.
    """
    total_price = 0

    for item in items:
        quantity = item["quantity"]
        price_per_item = item["price"]

        # Apply discounts based on quantity
        if 1 <= quantity <= 5:
            total_price += quantity * price_per_item
        elif 6 <= quantity <= 10:
            total_price += 0.95 * quantity * price_per_item  # 5% discount
        else:
            total_price += 0.9 * quantity * price_per_item  # 10% discount

    return total_price


# 5
def calculate_items_shipping_cost(items, shipping_method):
    """
    Calculates shipping costs for an online shopping system.
    The function calculates shipping costs based on the total weight of the
    items in the order and the shipping method chosen by the customer.
    """
    total_weight = sum(item["weight"] for item in items)

    if shipping_method == "standard":
        if total_weight <= 5:
            return 10

        if 5 < total_weight <= 10:
            return 15

        return 20

    if shipping_method == "express":
        if total_weight <= 5:
            return 20

        if 5 < total_weight <= 10:
            return 30

        return 40

    raise ValueError("Invalid shipping method")


# 6
def validate_login(username, password):
    """
    Validates user login credentials.
    """
    if 5 <= len(username) <= 20 and 8 <= len(password) <= 15:
        return "Login Successful"

    return "Login Failed"


# 7
def verify_age(age):
    """
    Determines whether a person is eligible for a certain service based on their age.
    """
    if 18 <= age <= 65:
        return "Eligible"

    return "Not Eligible"


# 8
def categorize_product(price):
    """
    Determines the price category of a product based on its price.
    """
    if 10 <= price <= 50:
        return "Category A"

    if 51 <= price <= 100:
        return "Category B"

    if 101 <= price <= 200:
        return "Category C"

    return "Category D"


# 9
def validate_email(email):
    """
    Validates email addresses.
    """
    if 5 <= len(email) <= 50 and "@" in email and "." in email:
        return "Valid Email"

    return "Invalid Email"


# 10
def celsius_to_fahrenheit(celsius):
    """
    Converts temperatures from Celsius to Fahrenheit.
    """
    if -100 <= celsius <= 100:
        return (celsius * 9 / 5) + 32

    return "Invalid Temperature"


# 11
def validate_credit_card(card_number):
    """
    Validates credit card numbers.
    """
    if 13 <= len(card_number) <= 16 and card_number.isdigit():
        return "Valid Card"

    return "Invalid Card"


# 12
def validate_date(year, month, day):
    """
    Validates dates.
    """
    if 1900 <= year <= 2100 and 1 <= month <= 12 and 1 <= day <= 31:
        return "Valid Date"

    return "Invalid Date"


# 13
def check_flight_eligibility(age, frequent_flyer):
    """
    Checks the eligibility of a passenger to book a flight.
    """
    if 18 <= age <= 65 or frequent_flyer:
        return "Eligible to Book"

    return "Not Eligible to Book"


# 14
def validate_url(url):
    """
    Validates URLs.
    """
    if len(url) <= 255 and url.startswith("http://") or url.startswith("https://"):
        return "Valid URL"

    return "Invalid URL"


# 15
def calculate_quantity_discount(quantity):
    """
    Calculates discounts based on the quantity of a product.
    """
    if 1 <= quantity <= 5:
        return "No Discount"

    if 6 <= quantity <= 10:
        return "5% Discount"

    return "10% Discount"


# 16
def check_file_size(size_in_bytes):
    """
    Checks if the size is valid for a file.
    """
    if 0 <= size_in_bytes <= 1048576:  # 1 MB in bytes
        return "Valid File Size"

    return "Invalid File Size"


# 17
def check_loan_eligibility(income, credit_score):
    """
    Checks if and which loan can be granted based on the income and credit score.
    """
    if income < 30000:
        return "Not Eligible"

    if 30000 <= income <= 60000:
        if credit_score > 700:
            return "Standard Loan"

        return "Secured Loan"

    if credit_score > 750:
        return "Premium Loan"

    return "Standard Loan"


# 18
def calculate_shipping_cost(weight, length, width, height):
    """
    Calculates the shipping cost based on the package weight and dimensions.
    """
    if weight <= 1 and length <= 10 and width <= 10 and height <= 10:
        return 5

    if (
        1 < weight <= 5
        and 11 <= length <= 30
        and 11 <= width <= 30
        and 11 <= height <= 30
    ):
        return 10

    return 20


# 19
def grade_quiz(correct_answers, incorrect_answers):
    """
    Grades online quizzes based on the number of correct and incorrect answers.
    """
    if correct_answers >= 7 and incorrect_answers <= 2:
        return "Pass"

    if correct_answers >= 5 and incorrect_answers <= 3:
        return "Conditional Pass"

    return "Fail"


# 20
def authenticate_user(username, password):
    """
    Authenticates users based on their username and password.
    """
    if username == "admin" and password == "admin123":
        return "Admin"

    if len(username) >= 5 and len(password) >= 8:
        return "User"

    return "Invalid"


# 21
def get_weather_advisory(temperature, humidity):
    """
    Provides weather advisories based on temperature and humidity.
    """
    if temperature > 30 and humidity > 70:
        return "High Temperature and Humidity. Stay Hydrated."

    if temperature < 0:
        return "Low Temperature. Bundle Up!"

    return "No Specific Advisory"
