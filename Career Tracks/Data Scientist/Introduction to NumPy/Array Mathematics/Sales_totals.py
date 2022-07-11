"""
1. Create a 2D array which contains a single column of total monthly sales across industries; call it monthly_industry_sales.
2. Concatenate monthly_industry_sales with monthly_sales into a new array called monthly_sales_with_total, with the monthly cross-industry sales information in the 
   final column.
"""

# Create a 2D array of total monthly sales across industries
monthly_industry_sales = monthly_sales.sum(axis=1, keepdims=True)
print(monthly_industry_sales)

# Add this column as the last column in monthly_sales
monthly_sales_with_total = np.concatenate((monthly_sales,monthly_industry_sales),axis=1)
print(monthly_sales_with_total)
