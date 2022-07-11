"""
Load the mystery_image.npy file using the alias f, saving the contents as an array called rgb_array.
"""

# Load the mystery_image.npy file 
with open('mystery_image.npy','rb') as f:
    rgd_array = np.load(f)
        

plt.imshow(rgb_array)
plt.show()
