"""
1 > Merge toy_story and taglines on the id column with a left join, and save the result as toystory_tag.
2 > With toy_story as the left table, merge to it taglines on the id column with an inner join, and save as toystory_tag.
"""

# Merge the toy_story and taglines tables with a left join
toystory_tag = toy_story.merge(taglines,on='id',how='left')
# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)


# Merge the toy_story and taglines tables with a inner join
toystory_tag = toy_story.merge(taglines,on='id',how='inner')
# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)
