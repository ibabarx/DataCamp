"""
1. Delete the stump diameter column from tree_census, and save the new 2D array as tree_census_no_stumps.
   Using np.where(), find the indices of any trees on block 313879, a private block. Save the indices in an array called private_block_indices.
2. Using the indices you just found using np.where(), delete the rows for trees on block 313879 from tree_census_no_stumps, saving the new 2D array as tree_census_clean.
   Print the shape of tree_census_clean.   
"""

# Delete the stump diameter column from tree_census
tree_census_no_stumps = np.delete(tree_census,3,axis=1)
# Save the indices of the trees on block 313879
private_block_indices = np.where(tree_census_no_stumps[:,1]==313879)


# Delete the stump diameter column from tree_census
tree_census_no_stumps = np.delete(tree_census, 3, axis=1)
# Save the indices of the trees on block 313879
private_block_indices = np.where(tree_census[:,1] == 313879)
# Delete the rows for trees on block 313879 from tree_census_no_stumps
tree_census_clean = np.delete(tree_census_no_stumps, private_block_indices, axis=0)
# Print the shape of tree_census_clean
print(tree_census_clean.shape)
