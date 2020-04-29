import sys
import os

def sum_numbers(a, b):
    return a + b

def get_list(a, b):
    return [a, b]

def get_tuple(a, b):
    return (a, b)

def get_multiple_values(a):
    return a, a*a, a*a*a

def try_to_increment(a):
    print("Inside function a is initially ", a)
    a += 1
    print("Inside function a is now ", a)

def sum_numbers(*args):  # Note we are also function overloading here, since we already have a sum_numbers() method!
    total = 0    
    for arg in args:
        total += arg
    return total

def outside_function():
    def inside_function():
        print("Start inside_function()")
        print("End inside_function()")
    print("Start outside_function()")
    inside_function()
    print("End outside_function()")

def outside_function_with_vars(x):
    def inside_function_with_vars():
        print("Start inside_function_with_vars(), x = ", x)        
        print("End inside_function_with_vars()")    
    print("Start outside_function_with_vars(), x = ", x)
    inside_function_with_vars()
    print("End outside_function_with_vars()")

def function_examples():
    print("Function Examples")
    print()

    print("Add two numbers")
    print(sum_numbers(10, 15))
    
    print("Get a list")
    print(get_list(11, 22))

    print("Get a tuple")
    print(get_tuple(5, 7))

    print("Get multiple return values")
    print(get_multiple_values(5))

    print("Get multiple return values and split them into separate variables")
    x, y, z = get_multiple_values(5)
    print(x)
    print(y)
    print(z)

    print("Python is call-by-value on basic types (ints, floats, booleans, strings etc.)")
    num = 5;
    print("Before calling function num = ", num)
    try_to_increment(num)
    print("After calling function num = ", num)

    print("We can call functions with multiple number of arguments")
    print("1 + 2 + 3 = ", sum_numbers(1, 2, 3))
    print("1 + 2 + 3 + 4 + 5 + 6 = ", sum_numbers(1, 2, 3, 4, 5, 6))

    print("We can have functions declared within functions. It's like Turbo Pascal 6 all over again :)")
    outside_function()

    print("Note that inside_function() can only be called form outside_function(). Attempting to call inside_function() here will cause an error`")
    #inside_function()

    print("Functions inside functions can use parameters from outside their scope")
    outside_function_with_vars(5)

