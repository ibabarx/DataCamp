"""
1. Flip rgb_array so that it is the mirror image of the original, with the ocean on the right and grassy knoll on the left.
2. Flip rgb_array so that it is upside down but otherwise remains the same. 
"""

# Flip rgb_array so that it is the mirror image of the original
mirrored_monet = np.flip(rgb_array,axis=1)
plt.imshow(mirrored_monet)
plt.show()

# Flip rgb_array so that it is upside down
upside_down_monet = np.flip(rgb_array,axis=(0,1))
plt.imshow(upside_down_monet)
plt.show()
