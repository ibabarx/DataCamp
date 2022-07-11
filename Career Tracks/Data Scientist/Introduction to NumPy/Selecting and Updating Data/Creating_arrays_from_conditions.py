"""
Create and print a 1D array called trunk_stump_diameters, which replaces a tree's trunk diameter with its stump diameter if the trunk diameter is zero.
"""

# Create and print a 1D array of tree and stump diameters
trunk_stump_diameters = np.where(tree_census[:, 2] == 0, tree_census[:, 3], tree_census[:, 2])
print(trunk_stump_diameters)
