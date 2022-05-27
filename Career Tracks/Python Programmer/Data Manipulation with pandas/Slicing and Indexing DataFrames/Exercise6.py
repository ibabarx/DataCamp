"""
1> Use .loc[] slicing to subset rows from India, Hyderabad to Iraq, Baghdad.
2> Use .loc[] slicing to subset columns from date to avg_temp_c.
3> Slice in both directions at once from Hyderabad to Baghdad, and date to avg_temp_c.
"""
# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[('India','Hyderabad'):('Iraq','Baghdad')])

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:,'date':'avg_temp_c'])

# Subset in both directions at once
print(temperatures_srt.loc[('India','Hyderabad'):('Iraq','Baghdad'),'date':'avg_temp_c'])
