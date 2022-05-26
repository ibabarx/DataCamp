"""
1> Remove rows of sales with duplicate pairs of store and type and save as store_types and print the head.
2> Remove rows of sales with duplicate pairs of store and department and save as store_depts and print the head.
3> Subset the rows that are holiday weeks using the is_holiday column, and drop the duplicate dates, saving as holiday_dates.
4> Select the date column of holiday_dates, and print.
"""

# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=['store','type'])
print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=['store','department'])
print(store_depts.head())

# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales['is_holiday']==True].drop_duplicates(subset='date')

# Print date col of holiday_dates
print(holiday_dates['date'])
