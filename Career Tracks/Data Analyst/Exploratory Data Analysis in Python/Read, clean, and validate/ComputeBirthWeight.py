"""
Make a Boolean Series called full_term that is true for babies with 'prglngth' greater than or equal to 37 weeks.
Use full_term and birth_weight to select birth weight in pounds for full-term babies. Store the result in full_term_weight.
Compute the mean weight of full-term babies.
"""

# Create a Boolean Series for full-term babies
full_term = nsfg['prglngth']>=37

# Select the weights of full-term babies
full_term_weight = birth_weight[full_term]

# Compute the mean weight of full-term babies
print(full_term_weight.mean())
