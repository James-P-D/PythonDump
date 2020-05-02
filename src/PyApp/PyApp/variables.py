import sys
import os

def variable_examples():
    print("Variable Examples")
    print()

    print("Variables are dymanically typed")
    name = "James"
    print(name)
    name = 1234
    print(name) 

    print("We can specify floats either by specifying decimal digits or by using float()")
    float1 = 4.0
    float2 = float(4)
    print("float1 =", float1)
    print("float2 =", float2)

    print("We can assign multiple variables at the same time")
    a, b = 12, 487
    print("a =", a)
    print("b =", b)

    print("We have all the normal arithmetic operators")
    print("5 + 2 =", 5+2)
    print("5 - 2 =", 5-2)
    print("5 * 2 =", 5*2)
    print("5 / 2 =", 5/2)
    print("5 % 2 =", 5%2)
    print("5 ** 2 =", 5**2)
    print("5 // 2 =", 5//2)
    
    print("Strings are surrounded by single or double quotes")
    string1 = "One example"
    string2 = 'Another example'
    print(string1)
    print(string2)

    print("We can embedd single of double quotes with backslashes or using single quotes in double-quoted string, or vice versa")
    string3 = "Like \"this\""
    string4 = 'Or \'this\''
    string5 = 'Like "this"'
    string6 = "Or 'this'"
    print(string3)
    print(string4)
    print(string5)
    print(string6)

    print("We can create multi-line strings with '''")
    multi_line_quote = '''just
like
this'''
    print(multi_line_quote)
    
    print("We can contatonate string with +")
    print("string1 = " +  string1 + " string2 = " + string2)

    print("We can pring something multiple times with *, although why anyone would want to do this is left as an exercise for the reader.")
    print("(Note each string is sent to stdout without a new line!)")
    print("Hello world!" * 5)

    print("the print() method always adds a newline. To remove it set the 'end' to empty string (eurgh!)")
    print("I have new lines. ", end="")
    print("Don't you?")

    print("We can use \%s to embedd strings, printf-style")
    print("string1 = %s string2 = %s string literal = %s" % (string1, string2, "Some string literal"))

    print("We also have \%d for numbers, \%f for floats, \%x or \%X for hex (lower/uppercase)")

    print("We can use 'del' to delete variables")
    temp_variable = 1234
    print(temp_variable)
    del temp_variable
    # If we un-comment the following line, we'll get a runtime exception
    #print(temp_variable)

    print("We can use f\" to format output") # https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python
    print(f"a sting = {string1} int = {a} half an int as a float = {a / 2} same but as int = {int(a / 2)}")

    