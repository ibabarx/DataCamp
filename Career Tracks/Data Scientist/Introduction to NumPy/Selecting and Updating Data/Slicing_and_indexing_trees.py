"""
1. Select all rows of data from the second column, representing block IDs; save the resulting array as block_ids.
   Print the first five block IDs from block_ids.
2. Select the tenth block ID from block_ids, saving the result as tenth_block_id.
3. Select five consecutive block IDs from block_ids, starting with the tenth ID, and save as block_id_slice
"""

# Select all rows of block ID data from the second column
block_ids = tree_census[:,1]
# Print the first five block_ids
print(block_ids[:5])


# Select all rows of block ID data from the second column
block_ids = tree_census[:, 1]
# Select the tenth block ID from block_ids
tenth_block_id = block_ids[9]
print(tenth_block_id)


# Select all rows of block ID data from the second column
block_ids = tree_census[:, 1]
# Select five block IDs from block_ids starting with the tenth ID
block_id_slice = block_ids[9:14]
print(block_id_slice)
