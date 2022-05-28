"""
1> To use the DataFrame() function you need, first import the pandas package with the alias pd.
2> Create a DataFrame from the list of dictionaries in list_of_dicts by calling pd.DataFrame(). Assign the resulting DataFrame to df.
3> Inspect the contents of df printing the head of the DataFrame. Head of the DataFrame df can be accessed by calling df.head().
"""

# Import the pandas package
import pandas as pd

# Turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]

# Turn list of dicts into a DataFrame: df
df = pd.DataFrame(list_of_dicts)

# Print the head of the DataFrame
print(df.head())
