"""
1 > Use .melt() on ten_yr to unpivot everything except the metric column, setting var_name='date' and value_name='close'. Save the result to bond_perc.
2 > Using the .query() method, select only those rows were metric equals 'close', and save to bond_perc_close.
3 > Use merge_ordered() to merge dji (left table) and bond_perc_close on date with an inner join, and set suffixes equal to ('_dow', '_bond'). Save the result to 
    dow_bond.
4 > Using dow_bond, plot only the Dow and bond values.
"""

# Use melt on ten_yr, unpivot everything besides the metric column
bond_perc = ten_yr.melt(id_vars='metric',var_name='date',value_name='close')
# Use query on bond_perc to select only the rows where metric=close
bond_perc_close = bond_perc.query('metric == "close"')

# Merge (ordered) dji and bond_perc_close on date with an inner join
dow_bond = pd.merge_ordered(dji,bond_perc_close,on='date',suffixes=['_dow', '_bond'],how='inner')


# Plot only the close_dow and close_bond columns
dow_bond.plot(y=['close_dow','close_bond'], x='date', rot=90)
plt.show()
