import sys
import os

def exception_examples():
    print("Exception Examples")
    print()

    print("We can catch specific exceptions, in this case a possible ZeroDivisionError")
    print("Enter a number")
    number1 = int(sys.stdin.readline())
    print("Enter another number")
    number2 = int(sys.stdin.readline())

    try:
        print("%d / %d = %d" % (number1, number2, (number1 / number2)))
    except ZeroDivisionError:
        print("Divide by zero!")
    
    print("We can also catch generic exceptions")
    my_array = [1, 2, 3]
    for n in range(5):
        try:
            print(my_array[n])
        except:
            print("General exception!")