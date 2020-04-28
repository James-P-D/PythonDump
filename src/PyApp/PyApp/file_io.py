import sys
import os

def file_io_examples():
    print("File I/O Examples")
    print()

    print("Overwrite or create a file for writing")
    test_file = open("test.txt", "wb")
 
    print("Get the file mode used")
    print(test_file.mode)
 
    print("Get the files name")
    print(test_file.name)
 
    print("Write text to a file with a newline")
    test_file.write(bytes("Write me to the file\n", 'UTF-8'))
 
    print("Close the file")
    test_file.close()
 
    print("Opens a file for reading and writing")
    test_file = open("test.txt", "r+")
 
    print("Read text from the file")
    text_in_file = test_file.read() 
    print(text_in_file)
 
    print("Delete the file")
    os.remove("test.txt")
