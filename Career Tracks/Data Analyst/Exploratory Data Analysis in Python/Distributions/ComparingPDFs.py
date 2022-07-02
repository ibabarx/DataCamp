"""
1 > Evaluate the normal PDF using dist, which is a norm object with the same mean and standard deviation as the data.
2 > Make a KDE plot of the logarithms of the incomes, using log_income, which is a Series object.
"""

# Evaluate the normal PDF
xs = np.linspace(2, 5.5)
ys = dist.pdf(xs)

# Plot the model PDF
plt.clf()
plt.plot(xs, ys, color='gray')

# Plot the data KDE
sns.kdeplot(log_income)

# Label the axes
plt.xlabel('log10 of realinc')
plt.ylabel('PDF')
plt.show()

