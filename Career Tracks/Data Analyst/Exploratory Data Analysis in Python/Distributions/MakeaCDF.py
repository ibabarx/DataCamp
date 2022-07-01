"""
1 > Select the 'age' column. Store the result in age.
2 > Compute the CDF of age. Store the result in cdf_age.
3 > Calculate the CDF of 30.
"""

# Select the age column
age = gss['age']

# Compute the CDF of age
cdf_age = Cdf(age)

# Calculate the CDF of 30
print(cdf_age(30))
