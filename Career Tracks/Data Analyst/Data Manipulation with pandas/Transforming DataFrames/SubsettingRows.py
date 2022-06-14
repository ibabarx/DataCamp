"""
1 > Filter homelessness for cases where the number of individuals is greater than ten thousand, assigning to ind_gt_10k. View the printed result.
2 > Filter homelessness for cases where the USA Census region is "Mountain", assigning to mountain_reg. View the printed result.
3 > Filter homelessness for cases where the number of family_members is less than one thousand and the region is "Pacific", assigning to fam_lt_1k_pac. View the 
    printed result. 
"""

# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[homelessness['individuals']>10000]
# See the result
print(ind_gt_10k)


# Filter for rows where region is Mountain
mountain_reg = homelessness[homelessness['region']=='Mountain']
# See the result
print(mountain_reg)


# Filter for rows where family_members is less than 1000 and region is Pacific
family_members_condition = homelessness['family_members'] < 1000
region_condition = homelessness['region'] == 'Pacific'
fam_lt_1k_pac = homelessness[family_members_condition & region_condition]
# See the result
print(fam_lt_1k_pac)
