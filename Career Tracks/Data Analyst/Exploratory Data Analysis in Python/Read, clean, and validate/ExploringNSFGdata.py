"""
1 > Calculate the number of rows and columns in the DataFrame nsfg.
2 > Display the names of the columns in nsfg.
3 > Select the column 'birthwgt_oz1' and assign it to a new variable called ounces.
4 > Display the first 5 elements of ounces.
"""

# Display the number of rows and columns
nsfg.shape

# Display the names of the columns
nsfg.columns

# Select column birthwgt_oz1: ounces
ounces = nsfg['birthwgt_oz1']

# Print the first 5 elements of ounces
print(ounces.head())
