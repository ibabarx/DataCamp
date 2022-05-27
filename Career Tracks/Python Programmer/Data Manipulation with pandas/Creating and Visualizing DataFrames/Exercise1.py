"""
1> Print the head of the avocados dataset. What columns are available?
2> For each avocado size group, calculate the total number sold, storing as nb_sold_by_size.
3> Create a bar plot of the number of avocados sold by size.
4> Show the plot.
"""

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Look at the first few rows of data
print(avocados.head())

# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby('size')['nb_sold'].sum()

# Create a bar plot of the number of avocados sold by size
plt.plot(kind='bar')

# Show the plot
plt.show()
