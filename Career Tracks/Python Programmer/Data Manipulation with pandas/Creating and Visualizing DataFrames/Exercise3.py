"""
1> Create a scatter plot with nb_sold on the x-axis and avg_price on the y-axis. Title it "Number of avocados sold vs. average price".
2> Show the plot.
"""

# Scatter plot of avg_price vs. nb_sold with title
avocados.plot(x='nb_sold',y='avg_price',title='Number of avocados sold vs. average price',kind='scatter')

# Show the plot
plt.show()
