"""
Use the hist method to display a histogram of the "Weight" column from the mens_rowing DataFrame, label this as "Rowing".
Use hist to display a histogram of the "Weight" column from the mens_gymnastics DataFrame, and label this as "Gymnastics".
For both histograms, use the histtype argument to visualize the data using the 'step' type and set the number of bins to use to 5.
Add a legend to the figure, before it is displayed.
"""

fig, ax = plt.subplots()

# Plot a histogram of "Weight" for mens_rowing
ax.hist(mens_rowing['Weight'],histtype='step',label='Rowing',bins=5)

# Compare to histogram of "Weight" for mens_gymnastics
ax.hist(mens_gymnastics['Weight'],histtype='step',label='Gymnastics',bins=5)

ax.set_xlabel("Weight (kg)")
ax.set_ylabel("# of observations")

# Add the legend and show the Figure
ax.legend()
plt.show()
