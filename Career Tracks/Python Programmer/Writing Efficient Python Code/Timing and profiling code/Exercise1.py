"""
1> Use list comprehension and range() to create a list of integers from 0 to 50 called nums_list_comp.
2> Use range() to create a list of integers from 0 to 50 and unpack its contents into a list called nums_unpack.
3> Use %timeit within your IPython console (i.e. not within the script.py window) to compare the runtimes for creating a list of integers from 0 to 50 using list
   comprehension vs. unpacking the range object. Don't include the print() statements when timing.Which method was faster?
"""

# Create a list of integers (0-50) using list comprehension
nums_list_comp = [num for num in range(51)]
print(nums_list_comp)

# Create a list of integers (0-50) by unpacking range
nums_unpack = [range(51)]
print(nums_unpack)

%timeit nums_list_comp = [num for num in range(51)]
%timeit nums_unpack = [range(51)]
# RESULTS : 2.57 us +- 54.1 ns per loop (mean +- std. dev. of 7 runs, 100000 loops each)
#           177 ns +- 19.7 ns per loop (mean +- std. dev. of 7 runs, 10000000 loops each)
