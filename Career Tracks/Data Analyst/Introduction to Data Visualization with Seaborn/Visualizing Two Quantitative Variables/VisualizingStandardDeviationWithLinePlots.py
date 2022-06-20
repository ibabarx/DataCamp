"""
Change the plot so the shaded area shows the standard deviation instead of the confidence interval for the mean.
"""


# Make the shaded area show the standard deviation
sns.relplot(x="model_year", y="mpg",
            data=mpg, kind="line",ci='sd')

# Show plot
plt.show()
