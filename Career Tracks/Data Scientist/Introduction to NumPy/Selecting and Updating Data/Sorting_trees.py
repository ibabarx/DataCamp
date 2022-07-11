"""
Create an array called sorted_trunk_diameters which selects only the trunk diameter column from tree_census and sorts it so that the smallest trunk diameters are at the 
top of the array and the largest at the bottom.
"""

# Extract trunk diameters information and sort from smallest to largest
sorted_trunk_diameters = np.sort(tree_census[:,2],axis=0)
print(sorted_trunk_diameters)
