# data/sample_functions.py

def add_numbers(a, b):
    return a + b

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def reverse_string(s):
    return s[::-1]

def calculate_discount(price, discount_percent):
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Invalid discount percentage")
    return price - (price * discount_percent / 100)
