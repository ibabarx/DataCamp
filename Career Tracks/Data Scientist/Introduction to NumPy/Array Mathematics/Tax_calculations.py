"""
1. Create an array called tax_collected which calculates tax collected by industry and month by multiplying each element in monthly_sales by 0.05.
2. Create an array that keeps track of total_tax_and_revenue collected by each industry and month by adding each element in tax_collected with its 
   corresponding element in monthly_sales.
"""

# Create an array of tax collected by industry and month
tax_collected = monthly_sales * 0.05
print(tax_collected)

# Create an array of sales revenue plus tax collected by industry and month
total_tax_and_revenue = tax_collected + monthly_sales
print(total_tax_and_revenue)
