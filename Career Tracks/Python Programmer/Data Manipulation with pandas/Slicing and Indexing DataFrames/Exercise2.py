"""
1> Create a list called cities that contains "Moscow" and "Saint Petersburg".
2> Use [] subsetting to filter temperatures for rows where the city column takes a value in the cities list.
3> Use .loc[] subsetting to filter temperatures_ind for rows where the city is in the cities list.
"""

# Make a list of cities to subset on
cities = ["Moscow", "Saint Petersburg"]

# Subset temperatures using square brackets
print(temperatures[temperatures["city"].isin(cities)])

# Subset temperatures_ind using .loc[]
print(temperatures_ind.loc[cities])
