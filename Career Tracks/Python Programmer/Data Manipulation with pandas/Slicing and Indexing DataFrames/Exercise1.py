"""
1> Look at temperatures.
2> Set the index of temperatures to "city", assigning to temperatures_ind.
3> Look at temperatures_ind. How is it different from temperatures?
4> Reset the index of temperatures_ind, keeping its contents.
5> Reset the index of temperatures_ind, dropping its contents.
"""

# Look at temperatures
print(temperatures)

# Index temperatures by city
temperatures_ind = temperatures.set_index('city')

# Look at temperatures_ind
print(temperatures_ind)

# Reset the index, keeping its contents
print(temperatures_ind.reset_index())

# Reset the index, dropping its contents
print(temperatures_ind.reset_index(drop=True))
