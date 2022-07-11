"""
1. Create an array called hundred_diameters which contains the first 100 trunk diameters in tree_census
2. Create an array,every_other_diameter, which contains only every other trunk diameter for trees with row indices from 50 to 100, inclusive.
"""

# Create an array of the first 100 trunk diameters from tree_census
hundred_diameters = tree_census[:100,2]
print(hundred_diameters)


# Create an array of trunk diameters with even row indices from 50 to 100 inclusive
every_other_diameter = tree_census[50:101:2,2]
print(every_other_diameter)
