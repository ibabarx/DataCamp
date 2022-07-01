"""
Select 'realinc' from the gss dataset.
Make a Cdf object called cdf_income.
Create a plot of cdf_income using .plot().
"""

# Select realinc
income = gss['realinc']

# Make the CDF
cdf_income = Cdf(income)

# Plot it
cdf_income.plot()

# Label the axes
plt.xlabel('Income (1986 USD)')
plt.ylabel('CDF')
plt.show()
