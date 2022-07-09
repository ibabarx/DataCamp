"""

 1. Create a variable called sports_column that holds the data from the "Sport" column of the DataFrame object.
 2. Use the unique method of this variable to find all the unique different sports that are present in this data, and assign these values into a new variable 
    called sports.
 3. Print the sports variable to the console.

"""

# Extract the "Sport" column
sports_column = summer_2016_medals['Sport']

# Find the unique values of the "Sport" column
sports = sports_column.unique()

# Print out the unique sports values
print(sports)
