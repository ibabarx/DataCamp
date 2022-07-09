"""
Use the ax.hist method to add a histogram of the "Weight" column from the mens_rowing DataFrame.
Use ax.hist to add a histogram of "Weight" for the mens_gymnastics DataFrame.
Set the x-axis label to "Weight (kg)" and the y-axis label to "# of observations".
"""

fig, ax = plt.subplots()
# Plot a histogram of "Weight" for mens_rowing
ax.hist(mens_rowing['Weight'])

# Compare to histogram of "Weight" for mens_gymnastics
ax.hist(mens_gymnastics['Weight'])

# Set the x-axis label to "Weight (kg)"
ax.set_xlabel("Weight (kg)")

# Set the y-axis label to "# of observations"
ax.set_ylabel("# of observations")

plt.show()
