"""
Use relplot() and the mpg DataFrame to create a scatter plot with "acceleration" on the x-axis and "mpg" on the y-axis. Vary the style and color of the plot points by country of origin ("origin").
"""


# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot of acceleration vs. mpg

sns.relplot(data=mpg,x="acceleration",y="mpg",style="origin",hue="origin",kind='scatter')


# Show plot
plt.show()
