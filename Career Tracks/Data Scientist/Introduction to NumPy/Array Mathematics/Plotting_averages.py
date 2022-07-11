"""
1. Create a 1D array called avg_monthly_sales, which contains an average sales amount for each month across the three industries.
2. Plot an array of the numbers one through twelve (representing each month) on the x-axis and avg_monthly_sales on the y-axis.
   Plot an array of the numbers one through twelve on the x-axis and the department store sales column of monthly_sales on the y-axis.
"""

# Create the 1D array avg_monthly_sales
avg_monthly_sales = monthly_sales.mean(axis=1)
print(avg_monthly_sales)

# Plot avg_monthly_sales by month
plt.plot([ 1,2,3,4,5,6,7,8,9,10,11,12], avg_monthly_sales, label="Average sales across industries")

# Plot department store sales by month
plt.plot([ 1,2,3,4,5,6,7,8,9,10,11,12], monthly_sales[:,2], label="Department store sales")
plt.legend()
plt.show()
