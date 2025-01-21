import numpy as np
import pandas as pd
import csv

"""
Will require more work outside of class to fully understand what the lab tasks require, but some good progress
and understanding has been made, and hopefully there will be a way to learn what else is needed in future
"""

nba = pd.read_csv("NBA.csv")
pd.set_option("display.max_columns", None)
pd.set_option("display.precision", 2)
"""print(type(nba))""" # Prints the type of the CSV file, which becomes a dataframe when used with pandas
"""print(len(nba))""" # Prints the number of rows within the dataframe, which is 126314
"""print(nba.shape)""" # Prints (126314, 23), which is (number of rows, number of columns)
"""print(nba.head())""" # Provides the headings for each column
# print(nba.loc[126313])
# print(nba)
