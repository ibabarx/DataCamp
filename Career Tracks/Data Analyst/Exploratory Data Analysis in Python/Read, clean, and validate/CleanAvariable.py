"""
1 > In the 'nbrnaliv' column, replace the value 8, in place, with the special value NaN.
2 > Confirm that the value 8 no longer appears in this column by printing the values and their frequencies.
"""

# Replace the value 8 with NaN
nsfg['nbrnaliv'].replace([8], np.nan, inplace=True)

# Print the values and their frequencies
print(nsfg['nbrnaliv'].value_counts())
