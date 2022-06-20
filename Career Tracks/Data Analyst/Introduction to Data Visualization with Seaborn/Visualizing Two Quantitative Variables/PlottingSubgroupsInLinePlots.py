"""
1 > Use relplot() and the mpg DataFrame to create a line plot with "model_year" on the x-axis and "horsepower" on the y-axis. Turn off the confidence intervals on the 
    plot.
2 > Create different lines for each country of origin ("origin") that vary in both line style and color.    
3 > Add markers for each data point to the lines. Use the dashes parameter to use solid lines for all countries, while still allowing for different marker styles for 
    each line.
"""

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
# Create line plot of model year vs. horsepower
sns.relplot(data=mpg,x="model_year",y="horsepower",kind='line',ci=None)
# Show plot
plt.show()


# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
# Change to create subgroups for country of origin
sns.relplot(x="model_year", y="horsepower", data=mpg, kind="line", ci=None)
# Show plot
plt.show()


# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
# Add markers and make each line have the same style
sns.relplot(x="model_year", y="horsepower", data=mpg, kind="line", ci=None, style="origin", hue="origin",dashes=False,markers=True)
# Show plot
plt.show()
