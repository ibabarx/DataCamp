"""
1 > Use relplot() and the mpg DataFrame to create a line plot with "model_year" on the x-axis and "mpg" on the y-axis.
2 > Which of the following is NOT a correct interpretation of this line plot?
"""

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
# Create line plot
sns.relplot(data=mpg,x="model_year",y="mpg",kind='line')
# Show plot
plt.show()
