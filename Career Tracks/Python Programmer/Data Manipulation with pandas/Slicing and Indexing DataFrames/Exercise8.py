"""
Use .iloc[] on temperatures to take subsets.
1> Get the 23rd row, 2nd column (index positions 22 and 1).
2> Get the first 5 rows (index positions 0 to 5).
3> Get all rows, columns 3 and 4 (index positions 2 to 4).
4> Get the first 5 rows, columns 3 and 4.
"""

# Get 23rd row, 2nd column (index 22, 1)
print(temperatures.iloc[22,1])

# Use slicing to get the first 5 rows
print(temperatures.iloc[0:5,:])

# Use slicing to get columns 3 to 4
print(temperatures.iloc[:,2:4])

# Use slicing in both directions at once
print(temperatures.iloc[0:5,2:4])
