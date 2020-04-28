import sys
import os

def list_examples():
    print("List Examples")
    print()

    print("Lists can be created with square brackets")
    shopping_list = ["Apples", "Bread", "Carrots", "Dates", "Eggplant"]
    print(shopping_list)

    print("Arrays are zero-indexed")
    print("The 0th item is", shopping_list[0])
    print("The 1st item is", shopping_list[1])

    print("Lists can contain multiple different data-types")
    weird_list = ["String", 1234, 3.1415]
    print(weird_list)

    print("We can easily change an item in a list")
    shopping_list[0] = "Avocado"
    print(shopping_list)

    print("We can get sub-lists by using [START_INDEX:END_INDEX] so to get items 1..4 use [1:4] (remember zero-indexing)")
    print(shopping_list[1:4])

    print("We can get sub-lists from start-index to the end with [1:]")
    print(shopping_list[1:])

    print("Lists can contain lists. e.g. list3 = [list1, list2]")
    list1 = [1, 2, 3]
    list2 = ["a", "b", "c", "d"]
    list3 = [list1, list2]
    print("list1 = ", list1)
    print("list2 = ", list2)
    print("list3 = ", list3)

    print("And we can then get the 1st item of the 1st item (still remember zero-indexing)")
    print(list3[1][1])

    print("We can add to a list with append()")
    shopping_list.append("Figs");
    print(shopping_list);

    print("We can insert items with insert()")
    shopping_list.insert(0, "Aardvark");
    print(shopping_list);

    print("And we can remove items with remove()")
    shopping_list.remove("Aardvark");
    print(shopping_list);

    print("We can reverse a list with reverse()")
    number_list = [1, 5, 2, 10, 6, 9, 7, 8, 4, 3]
    print("number_list = ", number_list)
    number_list.reverse()
    print("number_list = ", number_list)

    print("And we can sort with sort()")
    print("Unsorted list = ", number_list)
    number_list.sort();
    print("Sorted list = ", number_list)
    
    print("We can use del to delete an item. e.g. del number_list[3] - (Note del is not a method of list!)")
    del number_list[3]
    print("number_list = ", number_list)
    
    print("We can combine list with +")        
    list4 = [10, 20, 30]
    list5 = [100, 200, 300]
    list6 = list4 + list5
    print("list4 = ", list4)
    print("list5 = ", list5)
    print("list6 = ", list6)
    
    print("We can get the length of a list with 'len'")
    print("Length of list6 is ", len(list6))

    print("We can get the minimum item of a list with 'min'")
    print("Min item of list6 is ", min(list6))

    print("We can get the maximum item of a list with 'max'")
    print("Max item of list6 is ", max(list6))

