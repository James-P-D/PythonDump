import sys
import os

def tuple_examples():
    print("Tuple Examples")
    print()

    print("Tuples are list lists, except they values in tuples can't be changed")
    tuple1 = (10, 20, 40, 50, 30, 50)
    print(tuple1)

    print("We have len, min, max we can use on tuples")
    print("len(tuple1) = ", len(tuple1))
    print("min(tuple1) = ", min(tuple1))
    print("max(tuple1) = ", max(tuple1))

    print("We can convert tuples to lists with list()")
    new_list = list(tuple1)
    print(new_list)

    print("..and back to tuples with tuple()")
    back_to_tuple = tuple(new_list)
    print(back_to_tuple)
    