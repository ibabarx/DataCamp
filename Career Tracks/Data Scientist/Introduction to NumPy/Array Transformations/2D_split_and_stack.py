"""
1. Split monthly_sales into four arrays representing quarterly data across industries; print q1_sales.
2. Stack the four quarterly sales arrays to create a 3D array, quarterly_sales, made up of the four quarterly 2D arrays in order from the first to last quarter.
"""

# Split monthly_sales into quarterly data
q1_sales, q2_sales, q3_sales, q4_sales = np.split(monthly_sales, 4)

# Print q1_sales
print(q1_sales)

# Stack the four quarterly sales arrays
quarterly_sales = np.stack([q1_sales, q2_sales, q3_sales, q4_sales])
print(quarterly_sales)
