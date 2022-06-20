"""
Import Matplotlib and Seaborn using the standard naming conventions.
Use Seaborn to create a count plot with region on the y-axis.
Display the plot.
"""

# Import Matplotlib and Seaborn
import seaborn as sns
import matplotlib.pyplot as plt

# Create count plot with region on the y-axis
sns.countplot(y=region)

# Show plot
plt.show()
