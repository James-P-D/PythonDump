import sys
import os

# This method simply prints, and returns void
def add_two_numbers(a, b):
    def interal_add_two_numbers():
        print(a + b)
    return interal_add_two_numbers

# This method multiplies and *returns* the value
def multiply_two_numbers(a, b):
    def interal_multiply_two_numbers():
        return a * b
    return interal_multiply_two_numbers

def closure_examples():
    print("Closure Examples")
    print()

    # Remember to readup on functions within functions Pascal-style in functions.py
    # Closures can return functions!

    adder = add_two_numbers(5, 10)
    print("The result is ..")
    adder()

    multiplier = multiply_two_numbers(5, 10)
    print("The result is ..", multiplier())