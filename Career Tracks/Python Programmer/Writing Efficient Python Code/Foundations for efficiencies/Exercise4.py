"""
1> Use map() and the method str.upper() to convert each name in the list names to uppercase. Save this to the variable names_map.
2> Print the data type of names_map.
3> Unpack the contents of names_map into a list called names_uppercase using the star character (*).
4> Print names_uppercase and observe its contents.
"""

# Use map to apply str.upper to each element in names
names_map  = map(str.upper, names)

# Print the type of the names_map
print(type(names_map))

# Unpack names_map into a list
names_uppercase = [*names_map]

# Print the list created above
print(names_uppercase)
