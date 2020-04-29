import sys
import os
import random

def square_numbers():
    for i in range(10):
        yield i * i

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1, 15)

def fibonacci():
    a = 1
    yield a

    b = 1
    yield b

    for i in range(8):
        c = a + b
        yield c
        a = b
        b = c

def infinite_yield():
    while True:
        yield random.randint(1, 40)

def generator_examples():
    print("Generator Examples")
    print()

    print("Square numbers")
    for sn in square_numbers():
        print(sn)

    print("Lottery numbers")
    for random_number in lottery():
        print("And the next number is... %d!" %(random_number))

    print("Fibonacci numbers")
    for fn in fibonacci():
        print(fn)

    # Note we cannot get the length of infinite_yield()
    #print("Length of infinite_yield is " + len(infinite_yield()))
    #for infinite_random_number in infinite_yield():
    #    print(infinite_random_number)