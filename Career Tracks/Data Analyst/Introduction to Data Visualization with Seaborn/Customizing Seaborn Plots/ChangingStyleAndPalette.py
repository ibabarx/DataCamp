"""
1 > Set the style to "whitegrid" to help the audience determine the number of responses in each category.
2 > Set the color palette to the sequential palette named "Purples".
3 > Change the color palette to the diverging palette named "RdBu".
"""

# Set the style to "whitegrid"
sns.set_style("whitegrid")
# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes", "Often", "Always"]
sns.catplot(x="Parents Advice", data=survey_data, kind="count", order=category_order)
# Show plot
plt.show()

# Set the color palette to "Purples"
sns.set_style("whitegrid")
sns.set_palette('Purples')

# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes", "Often", "Always"]
sns.catplot(x="Parents Advice", data=survey_data, kind="count", order=category_order)
# Show plot
plt.show()

# Change the color palette to "RdBu"
sns.set_style("whitegrid")
sns.set_palette("RdBu")

# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes", "Often", "Always"]
sns.catplot(x="Parents Advice", data=survey_data, kind="count", order=category_order)
# Show plot
plt.show()
