"""
1 > Group sales by "type", take the sum of "weekly_sales", and store as sales_by_type.
    Calculate the proportion of sales at each store type by dividing by the sum of sales_by_type. Assign to sales_propn_by_type.
2 >     
"""

# Group by type; calc total weekly sales
sales_by_type = sales.groupby("type")["weekly_sales"].sum()
# Get proportion for each type
sales_propn_by_type = sales_by_type / sum(sales_by_type)
print(sales_propn_by_type)


# From previous step
sales_by_type = sales.groupby("type")["weekly_sales"].sum()
# Group by type and is_holiday; calc total weekly sales
sales_by_type_is_holiday = sales.groupby(['type','is_holiday'])['weekly_sales'].sum()
print(sales_by_type_is_holiday)
