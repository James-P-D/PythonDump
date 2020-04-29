import sys
import os

def times_by_n(n):
  return lambda a : a * n

def anonymous_function_examples():
    print("Anonymous Function Examples")
    print()

    print("We can create anonymous functions using lambda")
    doubler = lambda n: n * 2
    print("Double 5 =", doubler(5))

    add_a_to_b = lambda a, b: a + b
    print("5 + 10 =", add_a_to_b(5, 10))

    print("Functions can return lambdas")
    tripler = times_by_n(3)
    print("5 tripled is =", tripler(5))