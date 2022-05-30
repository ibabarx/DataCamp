"""
1> Create an empty list called formal_list using the formal name (list()).
2> Create an empty list called literal_list using the literal syntax ([]).
3> Print out the type of formal_list and literal_list to show that both naming conventions create a list.
4> Use %timeit in your IPython console to compare runtimes between creating a list using the formal name
   (list()) and the literal syntax ([]). Don't include the print() statements when timing.
"""

# Create a list using the formal name
formal_list = list()
print(formal_list)

# Create a list using the literal syntax
literal_list = []
print(literal_list)

# Print out the type of formal_list
print(type(formal_list))

# Print out the type of literal_list
print(type(literal_list))


%timeit formal = list()
%timeit literal =[]
# RESULT : 76.9 ns +- 4.01 ns per loop (mean +- std. dev. of 7 runs, 10000000 loops each)
#          23.1 ns +- 0.568 ns per loop (mean +- std. dev. of 7 runs, 10000000 loops each)
