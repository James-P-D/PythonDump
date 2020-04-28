import sys
import os

def dictionary_examples():
    print("Dictionary Examples")
    print()

    print("Dictionaries (or maps) are key/value pairs")
    superheros = {"Superman" : "Clark Kent",
                  "Batman" : "Bruce Wayne",
                  "Spiderman" : "Peter Parker"}
    print(superheros)

    print("We can get values by their key two ways...")
    print(superheros["Batman"])
    print(superheros.get("Batman"))

    print("We can get the number of key entries (which will also be number of values)")
    print(len(superheros))

    print("We can delete items by key with the del keyword")
    del superheros["Batman"]
    print(superheros)

    print("We can add new items")
    superheros["Catwoman"] = "Selina Kyle"
    print(superheros)

    print("..or overwrite exsting ones")
    superheros["Catwoman"] = "Some Other Name"
    print(superheros)

    print("We can get all the keys")
    print(superheros.keys())

    print("We can get all the values")
    print(superheros.values())
