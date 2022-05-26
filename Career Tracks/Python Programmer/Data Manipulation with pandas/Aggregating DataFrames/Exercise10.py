"""
1> Get the mean weekly_sales by type using .pivot_table() and store as mean_sales_by_type
2> Get the mean and median (using NumPy functions) of weekly_sales by type using .pivot_table() and store as mean_med_sales_by_type
3> Get the mean of weekly_sales by type and is_holiday using .pivot_table() and store as mean_sales_by_type_holiday.
"""

# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_table(values='weekly_sales',index='type')
# Print mean_sales_by_type
print(mean_sales_by_type)

# Import NumPy as np
import numpy as np
# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(values='weekly_sales',index='type',aggfunc=[np.mean,np.median])
# Print mean_med_sales_by_type
print(mean_med_sales_by_type)

# Pivot for mean weekly_sales by store type and holiday 
mean_sales_by_type_holiday = sales.pivot_table(values='weekly_sales',index='type',columns='is_holiday')
# Print mean_sales_by_type_holiday
print(mean_sales_by_type_holiday)