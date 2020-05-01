import sys
import os
import numpy as np # 'pip.exe install numpy' Currently using 1.18.3

def numpy_examples():
    print("Numpy Examples")
    print()

    print("We can create 2 new lists height and weight")
    height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
    weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]
    
    print("We can print the type of the arrays")
    print(type(height))
    print(type(weight))
    
    print("We can create 2 numpy arrays from height and weight arrays")
    np_height = np.array(height)
    np_weight = np.array(weight)

    print("We can print the type of the numpy arrays. Note they are 'numpy.ndarray' to signify Nth Dimensional Arrays")
    print(type(np_height))
    print(type(np_weight))

    print("We can print the contents of the numpy arrays")
    print(np_height)
    print(np_weight)

    print("Calculate the BMI of each item (weight / (height ^ 2))")
    bmi = np_weight / (np_height ** 2)
    print(bmi)

    print("Only print those items with BMI > 25")
    print(bmi[bmi > 25])

    print("Create list of weights in KG and print")
    weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]
    print(weight_kg)

    print("Create a numpy array np_weight_kg from weight_kg and print")
    np_weight_kg = np.array(weight_kg)    
    
    print("Create numpy array np_weight_lbs from np_weight_kg and print")
    np_weight_lbs = np_weight_kg * 2.2
    print(np_weight_lbs)

    print("Create numpy array [0 1 2 .. 25 26] with arange()")
    np_range = np.arange(27)
    print(np_range)

    print("Create 2-d numpy array")
    two_dimensional = np.ndarray((2, 10))
    print(two_dimensional)

    print("Create initialised 2-d numpy array of type int32")
    initialised_two_d_array = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
    print(initialised_two_d_array)

    print("We can access individual elements with [x,y]")
    print(initialised_two_d_array[1, 2])
