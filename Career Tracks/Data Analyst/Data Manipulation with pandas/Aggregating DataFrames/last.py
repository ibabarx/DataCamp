"""
1 > Print the mean weekly_sales by department and type, filling in any missing values with 0.
2 > Print the mean weekly_sales by department and type, filling in any missing values with 0 and summing all rows and columns.
"""

# Print mean weekly_sales by department and type; fill missing values with 0
print(sales.pivot_table(index='department',values='weekly_sales',columns='type',fill_value=0))

# Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", margins=True, fill_value=0))
