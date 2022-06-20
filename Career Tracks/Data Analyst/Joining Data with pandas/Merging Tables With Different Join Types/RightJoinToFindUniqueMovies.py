"""
1 > Merge action_movies and scifi_movies tables with a right join on movie_id. Save the result as action_scifi.
2 > Update the merge to add suffixes, where '_act' and '_sci' are suffixes for the left and right tables, respectively.
3 > From action_scifi, subset only the rows where the genre_act column is null.
"""

# Merge action_movies to the scifi_movies with right join
action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right',
                                   suffixes=('_act','_sci'))

# From action_scifi, select only the rows where the genre_act column is null
scifi_only = action_scifi[action_scifi['genre_act'].isnull()]

# Merge the movies and scifi_only tables with an inner join
movies_and_scifi_only = movies.merge(scifi_only,left_on='id',right_on='movie_id',how='inner')

# Print the first few rows and shape of movies_and_scifi_only
print(movies_and_scifi_only.head())
print(movies_and_scifi_only.shape)
