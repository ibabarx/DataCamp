"""
1. Print the shapes of tree_census and new_trees to confirm they are compatible to concatenate.
2. Add rows to the end of tree_census containing data for the new trees from the new_trees 2D array; save the new array as updated_tree_census.
"""

# Print the shapes of tree_census and new_trees
print(tree_census.shape, new_trees.shape)

# Add rows to tree_census which contain data for the new trees
updated_tree_census = np.concatenate((tree_census,new_trees))
print(updated_tree_census)
