import sys
import os

def set_examples():
    print("Set Examples")
    print()

    print("Sets are lists with no duplicate items")
    my_string = "my name is James and therefore James is my name"
    print(my_string)
    string_set = set(my_string.split())
    print(string_set)

    print("This set was supposed to have duplicate items, but it won't")
    bad_set = set([10, 20, 30, 20, 10])
    print("bad_set = ", bad_set)
    
    print("We can do set intersections, differences, symmetric differences, unions")
    set1 = set([10, 20, 30, 40, 50])
    print("set1 = ", set1)
    set2 = set([30, 40, 50, 60, 70])
    print("set2 = ", set2)
    print("set1.intersection(set2) = ", set1.intersection(set2))
    print("set2.intersection(set1) = ", set2.intersection(set1))

    print("set1.difference(set2) = ", set1.difference(set2))
    print("set2.difference(set1) = ", set2.difference(set1))

    print("set1.symmetric_difference(set2) = ", set1.symmetric_difference(set2))
    print("set2.symmetric_difference(set1) = ", set2.symmetric_difference(set1))

    print("set1.union(set2) = ", set1.union(set2))
    print("set2.union(set1) = ", set2.union(set1))
    
