"""
1 > Calculate the 75th percentile of income and store it in percentile_75th.
2 > Calculate the 25th percentile of income and store it in percentile_25th.
3 > Calculate the interquartile range of income. Store the result in iqr.
"""

# Calculate the 75th percentile 
percentile_75th = cdf_income.inverse(0.75)

# Calculate the 25th percentile
percentile_25th = cdf_income.inverse(0.25)

# Calculate the interquartile range
iqr = percentile_75th - percentile_25th

# Print the interquartile range
print(iqr)
