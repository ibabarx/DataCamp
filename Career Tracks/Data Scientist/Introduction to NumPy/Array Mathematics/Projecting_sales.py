"""
1. Create an array called projected_monthly_sales which contains projected sales for all three industries based on the multipliers you have gathered.
2. Create a graph that plots two lines: current liquor store sales by month and projected liquor store sales by month; months will be represented by an array of the
   numbers one through twelve.
"""

# Create an array of monthly projected sales for all industries
projected_monthly_sales = monthly_sales * monthly_industry_multipliers
print(projected_monthly_sales)

# Graph current liquor store sales and projected liquor store sales by month
plt.plot(np.arange(1,13), monthly_sales[:,0], label="Current liquor store sales")
plt.plot(np.arange(1,13), projected_monthly_sales[:,0], label="Projected liquor store sales")
plt.legend()
plt.show()
