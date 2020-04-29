import sys
import os
from functools import partial

def multiply(x, y):
    print("%d times %d will be ..." % (x, y))
    return x * y

def func(u,v,w,x):
    return u*4 + v*3 + w*2 + x

def partial_function_examples():
    print("Partial Function Examples")
    print()

    # Partial functions allow one to derive a function with x parameters to a function with
    # fewer parameters and fixed values set for the more limited function.
    
    # Create a new function that multiplies by 2
    doubler = partial(multiply, 2)
    print(doubler(4))

    # Create a function that always calls multiply() with 2 and 5
    always_2_times_5 = partial(multiply, 2, 5)
    print(always_2_times_5())

