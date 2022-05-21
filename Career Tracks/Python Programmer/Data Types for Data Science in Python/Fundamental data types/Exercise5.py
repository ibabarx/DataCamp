"""
1> Combine all the names in baby_names_2011 and baby_names_2014 by computing their union. Store the result as all_names.
2> Print the number of names that occur in all_names. You can use the len() function to compute the number of names in all_names.
3> Find all the names that occur in both baby_names_2011 and baby_names_2014 by computing their intersection. Store the result as overlapping_names.
4> Print the number of names that occur in overlapping_names
"""
# Find the union: all_names
all_names = baby_names_2011.union(baby_names_2014)

# Print the count of names in all_names
print(len(all_names))

# Find the intersection: overlapping_names
overlapping_names = baby_names_2011.intersection(baby_names_2014)

# Print the count of names in overlapping_names
print(len(overlapping_names))



