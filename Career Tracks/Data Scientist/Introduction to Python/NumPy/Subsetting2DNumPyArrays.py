"""
1 > Print out the 50th row of np_baseball.
2 > Make a new variable, np_weight_lb, containing the entire second column of np_baseball.
3 > Select the height (first column) of the 124th baseball player in np_baseball and print it out.
"""

# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Create np_baseball (2 cols)
np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49,:])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:,1]

# Print out height of 124th player
print(np_baseball[123,0])
