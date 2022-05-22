"""
1> Print the first key in ridership_date (Remember to make keys a list before slicing).
2> Pop the first item from ridership_date and print it.
3> Print the last key in ridership_date.
4> Pop the last item from ridership_date and print it.
"""
# Print the first key in ridership_date
print(list(ridership_date)[0])

# Pop the first item from ridership_date and print it
print(ridership_date.popitem(last=False))

# Print the last key in ridership_date
print(list(ridership_date)[len(ridership_date)-1])

# Pop the last item from ridership_date and print it
print(ridership_date.popitem(last=True))
