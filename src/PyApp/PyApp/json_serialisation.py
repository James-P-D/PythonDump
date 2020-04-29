import sys
import os
import json

def json_serialisation_examples():
    print("JSON Serialisation Examples")
    print()

    json_string = json.dumps([1, 2, 3, "a", "b", "c"])
    print("json_string = ", json_string)

    json_object = json.loads(json_string)
    print("json_object = ", json_object)
