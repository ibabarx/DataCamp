"""
1. Split the Monet rgb_array into red, green, and blue only pixel data; save the results as as red_array, green_array, and blue_array.
2. Create emphasized_blue_array, which replaces blue_array values with 255 if they are higher than the mean value of blue_array; otherwise, the value remains the same.
   Print the .shape of emphasized_blue_array.
3. Reshape emphasized_blue_array to remove the trailing third dimension; save as emphasized_blue_array_2D.   
"""

# Split rgb_array into red, green, and blue arrays
red_array, green_array, blue_array = np.split(rgb_array, 3, axis=2)

# Create emphasized_blue_array
emphasized_blue_array = np.where(blue_array > blue_array.mean(), 255, blue_array)

# Print the shape of emphasized_blue_array
print(emphasized_blue_array.shape)

# Remove the trailing dimension from emphasized_blue_array
emphasized_blue_array_2D = emphasized_blue_array.reshape((675,844))
