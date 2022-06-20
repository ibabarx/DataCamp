"""
1 > Use relplot() and the mpg DataFrame to create a scatter plot with "horsepower" on the x-axis and "mpg" on the y-axis. Vary the size of the points by the number of 
    cylinders in the car ("cylinders").
2 > To make this plot easier to read, use hue to vary the color of the points by the number of cylinders in the car ("cylinders").    
"""

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
# Create scatter plot of horsepower vs. mpg
sns.relplot(data=mpg,x="horsepower",y="mpg",size="cylinders",kind='scatter')
# Show plot
plt.show()


# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
# Create scatter plot of horsepower vs. mpg
sns.relplot(x="horsepower", y="mpg", data=mpg, kind="scatter", size="cylinders",hue="cylinders")
# Show plot
plt.show()
