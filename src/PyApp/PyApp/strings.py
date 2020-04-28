import sys
import os

def string_examples():
    print("String Examples")
    print()

    long_string = "this is a nice long string"
    print(long_string)

    print("We can get the length of a string with len")
    print(len(long_string))

    print("We can ranges from a string with [START_INDEX:END_INDEX]")
    print(long_string[10:14])

    print("We can get the last 6 characters with [-6:]")
    print(long_string[-6:])

    print("We can get everything up to the last 6 characters with [:-6]")
    print(long_string[:-6])

    print("We can get the number of instances of the letter 'i' using count()")
    print("Number of 'i's in string is", long_string.count("i"))

    print("We can capitalise the first letter with capitalise()")
    print(long_string.capitalize())

    print("We can make the string all uppercase with upper()")
    print(long_string.upper())

    print("We can make the string all lowercase with lower()")
    print(long_string.lower())

    print("We can check if a string starts with a certain string using startswith()")
    print(long_string.startswith("this"))

    print("We can check if a string ends with a certain string using endswith()")
    print(long_string.endswith("string"))

    print("We can find the index of a substring, in this case 'nice'")
    print(long_string.find("nice"))

    print("We can use replace")
    print(long_string.replace("long", "short"))

    print("We can split on a string, e.g. space, with split()")
    print(long_string.split(" "))

    print("We can strip whitespace from the start and end of a string with strip()")
    string_with_whitespace = "    Lots     of     whitespace  at the   start and end      "
    print("Before: \"%s\"" % string_with_whitespace)
    print("Before: \"%s\"" % string_with_whitespace.strip())

