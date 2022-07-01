"""
1 > Make a PMF for year with normalize=False and display the result.
"""

# Compute the PMF for year
pmf_year = Pmf(gss['year'], normalize=False)

# Print the result
print(pmf_year)
