"""
1> Explore your new DataFrame first by printing the first few rows of the sales DataFrame.
2> Print information about the columns in sales.
3> Print the mean of the weekly_sales column.
4> Print the median of the weekly_sales column.
"""
# Print the head of the sales DataFrame
print(sales.head())

# Print the info about the sales DataFrame
print(sales.info())

# Print the mean of weekly_sales
print(sales['weekly_sales'].mean())

# Print the median of weekly_sales
print(sales['weekly_sales'].median())
