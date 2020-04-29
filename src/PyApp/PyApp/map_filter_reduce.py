import sys
import os
from functools import reduce

def double_it(n):
    return n * 2

def add_one(n):
    return n + 1

def add_x(n, x):
    return n + x

def has_short_name(name):
    return len(name) <= 5

def map_filter_reduce_examples():
    print("Map, Filter, Reduce Examples")
    print()

    print("Map Examples")
    print()

    string_list = ["Adam", "Bob", "Catherine", "Douglas", "Ed", "Frances", "George", "Hannah", "Ian"]
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("Maps can be used to apply a function to every item in a list")
    print("name_list = ", string_list)
    print("int_list = ", int_list)
    
    uppercase_string_list = list(map(str.upper, string_list))
    print("uppercase_string_list = ", uppercase_string_list)

    double_it_list = list(map(double_it, int_list))
    print("double_it_list = ", double_it_list)

    print("We apply multiple functions, one after the other")
    double_it_and_add_one_list = list(map(add_one, (map(double_it, int_list))))
    print("double_it_and_add_one_list = ", double_it_and_add_one_list)
    add_one_and_double_it_list = list(map(double_it, (map(add_one, int_list))))
    print("add_one_and_double_it_list = ", add_one_and_double_it_list)
    
    print("We can supply additional arguments to the function we are mapping by adding them at the end")
    add_an_increasing_number = list(map(add_x, int_list, [10, 20, 30, 40, 50]))
    print("add_an_increasing_number = ", add_an_increasing_number)
    
    print("Finally, we could also use 'lambda' to create anonymous functions")
    doubled_again = list(map(lambda i: i * 2, int_list))
    print("doubled_again = ", doubled_again)

    ####################################################################################################

    print("Filter Examples")
    print()

    print("Filters are used for applying boolean-returning functions to iterable objects so we can exclude certain values")
    short_names = list(filter(has_short_name, string_list))
    print("short_names = ", short_names)
    print("Like Maps, we can also perform it on ints, and also can use lambda to create anonymous functions")
    even_numbers = list(filter(lambda i: i % 2 == 0 , int_list))
    print("even_numbers = ", even_numbers)

    ####################################################################################################

    print("Reduce Examples")
    print()

    print("Reduce applys a function with two arguments cumulatively to the elements of the list, giving a final result")
    print("Remember to 'from functools import reduce'")
    total = reduce(add_x, int_list)
    print("total = ", total)

    concatonated = reduce(lambda i, j: i + j, string_list)
    print("concatonated = ", concatonated)