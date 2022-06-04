"""
1> Use .itertuples() to loop over yankees_df and grab each row's runs scored and runs allowed values.
2> Now, calculate each row's run differential using calc_run_diff(). Be sure to append each row's run differential to run_diffs.
3> Append a new column called 'RD' to the yankees_df DataFrame that contains the run differentials you calculated.
4> In what year within your DataFrame did the New York Yankees have the highest run differential?
"""

run_diffs = []
# Loop over the DataFrame and calculate each row's run differential
for row in yankees_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA
  
 run_diff = calc_run_diff(runs_scored, runs_allowed)
 run_diffs.append(run_diff) 
  
 # Append new column
yankees_df['RD'] = run_diffs
print(yankees_df) 

#In 1998 (with a Run Differential of 309)
