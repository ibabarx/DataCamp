"""
1. Print the shapes of blue_array and emphasized_blue_array_2D.
2. Reshape red_array and green_array so that they can be stacked with emphasized_blue_array_2D.
3. Stack red_array_2D, green_array_2D, and emphasized_blue_array_2D together (in that order) into a 3D array called emphasized_blue_monet.
"""

# Print the shapes of blue_array and emphasized_blue_array_2D
print(blue_array.shape, emphasized_blue_array_2D.shape)

# Reshape red_array and green_array
red_array_2D = red_array.reshape((675, 844))
green_array_2D = green_array.reshape((675, 844))

# Stack red_array_2D, green_array_2D, and emphasized_blue_array_2D
emphasized_blue_monet = np.stack([red_array_2D,green_array_2D,emphasized_blue_array_2D],axis=2)
plt.imshow(emphasized_blue_monet)
plt.show()
