"""
1> Print the first five rows of the dbacks_df DataFrame to see what the data looks like.
2> Create a pandas Series called win_percs by applying the calc_win_perc() function to each row of the DataFrame with a lambda function.
3> Create a new column in dbacks_df called WP that contains the win percentages you calculated in the above step.
"""

# Display the first five rows of the DataFrame
print(dbacks_df.head())

# Create a win percentage Series 
win_percs = dbacks_df.apply(lambda row: calc_win_perc(row['W'], row['G']), axis=1)
print(win_percs, '\n')

# Append a new column to dbacks_df
dbacks_df['WP'] = win_percs
print(dbacks_df, '\n')
# Display dbacks_df where WP is greater than 0.50
print(dbacks_df[dbacks_df['WP'] >= 0.50])
