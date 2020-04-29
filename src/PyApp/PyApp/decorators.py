import sys
import os

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def say_whee():
    print("Whee!")

@do_twice
def greet(name):
    print("Hello", name)

def decorator_examples():
    print("Decorator Examples")
    print()

    say_whee()

    greet("James")