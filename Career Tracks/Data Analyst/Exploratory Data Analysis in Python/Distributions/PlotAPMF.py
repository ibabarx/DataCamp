"""
1 > Select the 'age' column from the gss DataFrame and store the result in age.
2 > Make a normalized PMF of age. Store the result in pmf_age.
3 > Plot pmf_age as a bar chart.
"""

# Select the age column
age = gss['age']

# Make a PMF of age
pmf_age = Pmf(age,normalize=True)

# Select the age column
age = gss['age']
# Make a PMF of age
pmf_age = Pmf(age)
# Plot the PMF
pmf_age.bar()
# Label the axes
plt.xlabel('Age')
plt.ylabel('PMF')
plt.show()
