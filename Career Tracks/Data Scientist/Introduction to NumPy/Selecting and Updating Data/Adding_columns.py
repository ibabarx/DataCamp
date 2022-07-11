"""
1. Print the shapes of both tree_census and trunk_stump_diameters.
2. Reshape trunk_stump_diameters so that it can be appended as the last column in tree_census; call the reshaped array reshaped_diameters.
3. Concatenate reshaped_diameters to the end of tree_census so that it becomes the last column; call the new array concatenated_tree_census.
"""

# Print the shapes of tree_census and trunk_stump_diameters
print(trunk_stump_diameters.shape, tree_census.shape)

# Reshape trunk_stump_diameters
reshaped_diameters = trunk_stump_diameters.reshape((1000, 1))

# Concatenate reshaped_diameters to tree_census as the last column
concatenated_tree_census = np.concatenate((tree_census,reshaped_diameters),axis=1)
print(concatenated_tree_census)
