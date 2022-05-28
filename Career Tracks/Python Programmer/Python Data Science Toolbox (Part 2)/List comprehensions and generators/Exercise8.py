"""
1> Complete the function header for the function get_lengths() that has a single parameter, input_list.
2> In the for loop in the function definition, yield the length of the strings in input_list.
3> Complete the iterable part of the for loop for printing the values generated by the get_lengths() generator function. Supply the call to get_lengths(), 
   passing in the list lannister.
"""

# Create a list of strings
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Define generator function get_lengths
def get_lengths(input_list):
    """Generator function that yields the
    length of the strings in input_list."""

    # Yield the length of a string
    for person in input_list:
        yield len(person)

# Print the values generated by get_lengths()
for value in get_lengths(lannister):
    print(value)
