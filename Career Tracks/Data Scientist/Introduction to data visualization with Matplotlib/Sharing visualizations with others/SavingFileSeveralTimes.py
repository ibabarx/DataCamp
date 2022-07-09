"""
1 - Examine the figure by calling the plt.show() function.
2 - Save the figure into the file my_figure.png, using the default resolution.
3 - Save the figure into the file my_figure_300dpi.png and set the resolution to 300 dpi
"""

# Show the figure
plt.show()

# Save as a PNG file
fig.savefig('my_figure.png')

# Save as a PNG file with 300 dpi
fig.savefig('my_figure_300dpi.png',dpi=300)
