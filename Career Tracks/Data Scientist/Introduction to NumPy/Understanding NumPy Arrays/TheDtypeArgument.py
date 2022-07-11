"""
Using np.zeros(), create an array of zeros that has three rows and two columns; call it zero_array.
Print the data type of zero_array.
Create a new array of zeros called zero_int_array, which will also have three rows and two columns, but the data type should be np.int32.
Print the data type of zero_int_array.
"""

# Create an array of zeros with three rows and two columns
zero_array = np.zeros((3, 2))

# Print the data type of zero_array
print(zero_array.dtype)

# Create a new array of int32 zeros with three rows and two columns
zero_int_array = np.zeros((3,2),dtype=np.int32)

# Print the data type of zero_int_array
print(zero_int_array.dtype)
