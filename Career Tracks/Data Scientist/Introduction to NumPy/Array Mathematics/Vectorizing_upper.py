"""
Create a vectorized function called vectorized_upper from the Python .upper() string method.
Apply vectorized_upper() to the names array and save the resulting array as uppercase_names.
"""

# Vectorize the .upper() string method
vectorized_upper = np.vectorize(str.upper)

# Apply vectorized_upper to the names array
uppercase_names = vectorized_upper(names)
print(uppercase_names)
