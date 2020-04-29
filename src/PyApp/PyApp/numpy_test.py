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

    print("We can print the type of the numpy arrays")
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

