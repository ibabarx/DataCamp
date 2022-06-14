"""
Sort the index of temperatures_ind.
Use slicing with .loc[] to get these subsets:
  from Pakistan to Russia.
  from Lahore to Moscow. (This will return nonsense.)
  from Pakistan, Lahore to Russia, Moscow.
"""

# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Subset rows from Pakistan to Russia
print(temperatures_srt.loc['Pakistan':'Russia'])

# Try to subset rows from Lahore to Moscow
print(temperatures_srt.loc['Lahore':'Moscow'])

# Subset rows from Pakistan, Lahore to Russia, Moscow
print(temperatures_srt.loc[('Pakistan','Lahore'):('Russia','Moscow')])
