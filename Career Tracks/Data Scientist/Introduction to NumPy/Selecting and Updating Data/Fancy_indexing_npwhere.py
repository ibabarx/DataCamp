"""
1. Using fancy indexing, create an array called block_313879 which only contains data for trees with a block ID of 313879.
2. Using np.where(), create an array of row_indices for trees with a block ID of 313879.
   Using row_indices, create block_313879, which contains data for trees on block 313879.
"""

# Create the block_313879 array containing trees on block 313879
block_313879 = tree_census[tree_census[:,1]==313879]
print(block_313879)


# Create an array of row_indices for trees on block 313879
row_indices = np.where(tree_census[:,1]==313879)
# Create an array which only contains data for trees on block 313879
block_313879 = tree_census[tree_census[:,1]==313879]
print(block_313879)
