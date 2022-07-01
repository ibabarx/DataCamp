"""
1 > Plot a histogram of agecon with 20 bins.
2 > Adapt your code to make an unfilled histogram by setting the parameter histtype to be 'step'.
"""

# Plot the histogram
plt.hist(agecon, bins=20)
# Label the axes
plt.xlabel('Age at conception')
plt.ylabel('Number of pregnancies')
# Show the figure
plt.show()

# Plot the histogram
plt.hist(agecon, bins=20, histtype='step')
# Label the axes
plt.xlabel('Age at conception')
plt.ylabel('Number of pregnancies')
# Show the figure
plt.show()
