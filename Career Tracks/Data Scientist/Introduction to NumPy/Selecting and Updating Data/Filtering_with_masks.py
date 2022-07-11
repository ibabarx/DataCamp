"""
1. Using Boolean indexing, create an array, largest_tree_data, which contains the row of data on the largest tree in tree_census corresponding to the tree with a 
   diameter of 51.
2. Slice largest_tree_data to retrieve only the block id of the block the largest tree is located on; save this block id as largest_tree_block_id.
3. 
"""

# Create an array which contains row data on the largest tree in tree_census
largest_tree_data = tree_census[tree_census[:, 2] == 51]
print(largest_tree_data)

# Slice largest_tree_data to get only the block ID
largest_tree_block_id = largest_tree_data[:, 1]
print(largest_tree_block_id)

# Create an array which contains row data on all trees with largest_tree_block_id
trees_on_largest_tree_block = tree_census[tree_census[:, 1] == largest_tree_block_id]
print(trees_on_largest_tree_block)
