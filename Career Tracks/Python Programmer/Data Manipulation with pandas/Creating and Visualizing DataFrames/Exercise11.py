"""
1> Sort airline_totals by the values of bumps_per_10k from highest to lowest, storing as airline_totals_sorted.
2> Print your sorted DataFrame.
3> Save the sorted DataFrame as a CSV called "airline_totals_sorted.csv".
"""

# Create airline_totals_sorted
airline_totals_sorted = airline_totals.sort_values('bumps_per_10k',ascending=False)

# Print airline_totals_sorted
print(airline_totals_sorted)

# Save as airline_totals_sorted.csv
airline_totals_sorted.to_csv("airline_totals_sorted.csv")
