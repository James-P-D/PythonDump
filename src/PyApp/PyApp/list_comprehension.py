import sys
import os

def list_comprehension_examples():
    print("List Comprehension Examples")
    print()

    print("We can use list comprehension, F# (ML?) style!")
    sentence = "the quick brown fox jumps over the lazy dog"
    words = sentence.split()

    # Create new list but exclude 'the'
    word_lengths = [len(word) for word in words if word != "the"]
    print(words)
    print(word_lengths)

    print("We can get only the positive numbers")
    numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
    positive_numbers = [n for n in numbers if n > 0]
    print(positive_numbers)    