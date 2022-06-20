"""
1 > Import Matplotlib and Seaborn using the standard naming convention.
2 > Create a scatter plot of GDP (gdp) vs. number of phones per 1000 people (phones).
3 > Display the plot.
4 > Change the scatter plot so it displays the percent of the population that can read and write (percent_literate) on the y-axis.
"""

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Change this scatter plot to have percent literate on the y-axis
sns.scatterplot(x=gdp, y=phones)

# Show plot
plt.show()

# Change this scatter plot to have percent literate on the y-axis
sns.scatterplot(x=gdp, y=percent_literate)
