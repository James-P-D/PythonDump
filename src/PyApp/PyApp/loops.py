import sys
import os

def loop_examples():
    print("Loop Examples")
    print()

    print("We can loop through numbers with range(0, 10) which will go from 0 to 9")
    for x in range(0, 10):
        print(x, ' ', end="")
    print()

    print("We can step with a third parameter to range(). e.g. range(0, 10, 2)")
    for x in range(0, 10, 2):
        print(x, ' ', end="")
    print()

    print("We can 'for-each' a list using 'in': ")    
    shopping_list = ["Apples", "Bread", "Carrots", "Dates", "Eggplant"]
    print("shopping_list = ", shopping_list)
    for x in shopping_list:
        print(x, ' ', end="")
    print()

    print("We can also have loops within loops, for example when using lists of lists")
    num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]
    print("num_list = ", num_list)    
    for x in range(0,3):
        for y in range(0,3):
            print(num_list[x][y])

    print("Finally, Python has while loops (but no 'no..while' loops)")
    num = 100;
    while(num > 0):
        print(num)
        num = num - 10
