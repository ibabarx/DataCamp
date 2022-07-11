"""
1. Find the mean sales projection multiplier for each industry; save in an array called mean_multipliers.
2. Print the shapes of mean_multipliers and monthly_sales to ensure they are suitable for broadcasting.
3. Multiply each monthly sales value by the mean multiplier you found for that industry; save in an array called projected_sales.
"""

# Find the mean sales projection multiplier for each industry
mean_multipliers = monthly_industry_multipliers.mean(axis=0)
print(mean_multipliers)

# Print the shapes of mean_multipliers and monthly_sales
print(mean_multipliers.shape, monthly_sales.shape)

# Multiply each value by the multiplier for that industry
projected_sales = monthly_sales * mean_multipliers
print(projected_sales)
