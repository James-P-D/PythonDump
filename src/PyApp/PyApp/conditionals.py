import sys
import os

def conditional_examples():
    print("Conditional Examples")
    print()

    print("If statements are all pretty straightforward. Just remember to use 'elif' for 'else if' ladders")
    print("Also remember to use 'and' 'or' 'not' rather than C-style symbols (&&, ||, !)")
    print("Finally, Python doesn't have a Switch statement :(")

    age = 30
    if age > 16 :
        print('You are old enough to drive')
 
    if age > 16 :
        print('You are old enough to drive')
    else :
        print('You are not old enough to drive')
        
    if age >= 21 :
        print('You are old enough to drive a tractor trailer')
    elif age >= 16:
        print('You are old enough to drive a car')
    else :
        print('You are not old enough to drive')
    
    if ((age >= 1) and (age <= 18)):
        print("You get a birthday party")
    elif (age == 21) or (age >= 65):
        print("You get a birthday party")
    elif not(age == 30):
        print("You don't get a birthday party")
    else:
        print("You get a birthday party yeah")

    print("We can also use 'in' to check for items in a list")
    my_list = [10, 20, 30]
    print("my_list =", my_list)
    if 20 in my_list:
        print("20 is in the list")
    else:
        print("20 is not in the list")

    print("Note there is a difference between 'is' and '==' for checking for equality.")
    print("'is' checks for instance equality")
    print("'==' checks for value equality")
    list1 = [1,2,3]
    list2 = [1,2,3]
    print("list1 =", list1)
    print("list2 =", list2)
    print("list1 is list2 =", list1 is list2)
    print("list1 == list2 =", list1 == list2)
    
    print("Note that python also uses 'if's for the ternary conditional operator ('?:')")
    int1 = 10
    int2 = 20
    biggest_int = int1 if int1 > int2 else int2
    print("int1 =", int1)
    print("int2 =", int2)
    print("biggest_int = int1 if int1 > int2 else int2 is... ", biggest_int)