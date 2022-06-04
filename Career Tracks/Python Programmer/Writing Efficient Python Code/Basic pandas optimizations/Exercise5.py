"""
1> Apply sum() to each column of rays_df to collect the sum of each column. Be sure to specify the correct axis.
2> Apply sum() to each row of rays_df, only looking at the 'RS' and 'RA' columns, and specify the correct axis.
3> Use .apply() and a lambda function to apply text_playoffs() to each row's 'Playoffs' value of the rays_df DataFrame.
"""

# Gather sum of all columns
stat_totals = rays_df.apply(sum, axis=0)
print(stat_totals)

# Gather total runs scored in all games per year
total_runs_scored = rays_df[['RS', 'RA']].apply(sum, axis=1)
print(total_runs_scored)

# Convert numeric playoffs to text by applying text_playoffs()
textual_playoffs = rays_df.apply(lambda row: text_playoffs(row['Playoffs']), axis=1)
print(textual_playoffs)
