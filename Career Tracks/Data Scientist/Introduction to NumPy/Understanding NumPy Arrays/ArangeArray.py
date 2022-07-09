"""

    Using np.arange(), create a 1D array called one_to_ten which holds all integers from one to ten (inclusive).
    Create a scatterplot with doubling_array as the y values and one_to_ten as the x values.

"""

# Create an array of integers from one to ten
one_to_ten = np.arange(1,11)

# Create your scatterplot
plt.scatter(one_to_ten,doubling_array)
plt.show()
