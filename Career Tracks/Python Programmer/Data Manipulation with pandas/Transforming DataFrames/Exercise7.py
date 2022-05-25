"""
1> Add a new column to homelessness, named total, containing the sum of the individuals and family_members columns.
2> Add another column to homelessness, named p_individuals, containing the proportion of homeless people in each state who are individuals.
"""

# Add total col as sum of individuals and family_members
homelessness['total'] =  homelessness['individuals'] + homelessness['family_members']

# Add p_individuals col as proportion of total that are individuals
homelessness['p_individuals'] = homelessness['individuals']/homelessness['total']
# See the result
print(homelessness)

