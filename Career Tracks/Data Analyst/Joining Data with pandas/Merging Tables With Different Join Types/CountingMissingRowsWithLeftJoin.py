"""
1 > What column is likely the best column to merge the two tables on?
2 > Merge the movies table, as the left table, with the financials table using a left join, and save the result to movies_financials.
3 > Count the number of rows in movies_financials with a null value in the budget column. 
"""

on='id'

# Merge movies and financials with a left join
movies_financials = movies.merge(financials,on='id',how='left')

# Count the number of rows in the budget column that are missing
number_of_missing_fin = movies_financials['budget'].isnull().sum()
# Print the number of movies missing financials
print(number_of_missing_fin)
