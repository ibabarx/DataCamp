"""
1 > Set the style to "darkgrid".
2 > Set a custom color palette with the hex color codes "#39A7D0" and "#36ADA4".
"""

# Set the style to "darkgrid"
sns.set_style('darkgrid')

# Set a custom color palette

sns.set_palette(["#39A7D0","#36ADA4"])
# Create the box plot of age distribution by gender
sns.catplot(x="Gender", y="Age", data=survey_data, kind="box")

# Show plot
plt.show()
