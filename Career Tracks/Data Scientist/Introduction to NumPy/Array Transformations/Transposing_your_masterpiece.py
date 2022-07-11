"""
Transpose the 3-D rgb_array so that the image appears rotated 90 degrees left and as a mirror image of itself.
"""

# Transpose rgb_array
transposed_rgb = np.transpose(rgb_array,axes=(1,0,2))
plt.imshow(transposed_rgb)
plt.show()
