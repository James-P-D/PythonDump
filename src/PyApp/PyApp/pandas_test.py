import sys
import os
import pandas as pd # 'pip.exe install pandas' Currently using 1.0.3

def pandas_examples():
    print("Pandas Examples")
    print()

    print("Pandas is a high-level data manipulation tool. It's key data structure is the DataFrame")

    print("We can initialise a DataFrame from a dictionary")
    dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }
    brics_df = pd.DataFrame(dict)
    print()
    print("Original dictionary")
    print(dict)
    print()
    print("Pandas Dataframe")
    print(brics_df)

    print()
    print("By default, dataframes are indexed by numbers, but we can change that")
    brics_df.index = ["BR", "RU", "IN", "CH", "SA"]
    print()
    print("Pandas Dataframe")
    print(brics_df)

    print()
    print("We can get columns as Pandas Series")
    print()
    print(brics_df["country"])
    print()
    print("We can get columns as Pandas DataFrames")
    print()
    print(brics_df[["country"]])
    print()
    print("We can get multiple columns as Pandas DataFrames")
    print()
    print(brics_df[["country", "population"]])
    print()
    print("We can get first two rows (start at row 0, up to row < 2)")
    print()
    print(brics_df[0:2])
    print()
    print("We can get rows by numbered-index")
    print()
    print(brics_df.iloc[[2]])
    print()
    print("We can get rows by string-index")
    print()
    print(brics_df.loc[["IN", "BR"]])
    

    print()
    print("Finally, we can also import DataFrames from CSV files")
    people_df = pd.read_csv('people.csv')
    # We could also specify the index column if there was one in the CSV file
    # cars = pd.read_csv('cars.csv', index_col = 0)
    print()
    print(people_df)

