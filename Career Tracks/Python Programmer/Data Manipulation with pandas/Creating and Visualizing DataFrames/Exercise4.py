"""
1> Subset avocados for the conventional type, and the average price column. Create a histogram.
2> Create a histogram of avg_price for organic type avocados.
3> Add a legend to your plot, with the names "conventional" and "organic".
4> Show your plot.
"""

# Histogram of conventional avg_price 
avocados[avocados['type']=='conventional']['avg_price'].hist()

# Histogram of organic avg_price
avocados[avocados['type']=='organic']['avg_price'].hist()

# Add a legend
plt.legend(['conventional','organic'])

# Show the plot
plt.show()

"""
1> Modify your code to adjust the transparency of both histograms to 0.5 to see how much overlap there is between the two distributions.
"""

# Modify histogram transparency to 0.5 
avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5)

# Modify histogram transparency to 0.5
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5)

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()

"""
1> Modify your code to use 20 bins in both histograms.
"""

# Modify bins to 20
avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5,bins=20)

# Modify bins to 20
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5,bins=20)

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()
