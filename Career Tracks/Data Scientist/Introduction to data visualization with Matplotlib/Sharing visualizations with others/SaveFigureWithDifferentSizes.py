"""
1 . Set the figure size as width of 3 inches and height of 5 inches and save it as 'figure_3_5.png' with default resolution.
2 . Set the figure size to width of 5 inches and height of 3 inches and save it as 'figure_5_3.png' with default settings.
"""

# Set figure dimensions and save as a PNG
fig.savefig('figure_3_5.png')
fig.set_size_inches([3,5])

# Set figure dimensions and save as a PNG
fig.savefig('figure_5_3.png')
fig.set_size_inches([5,3])
