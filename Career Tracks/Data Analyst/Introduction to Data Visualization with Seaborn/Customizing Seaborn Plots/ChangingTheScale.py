"""
1 > Set the scale ("context") to "paper", which is the smallest of the scale options.
2 > Change the context to "notebook" to increase the scale.
3 > Change the context to "talk" to increase the scale.
4 > Change the context to "poster", which is the largest scale available.
"""

# Set the context to "paper"
sns.set_context("paper")
# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",data=survey_data, kind="bar")
# Show plot
plt.show()

# Set the context to "paper"
sns.set_context("notebook")
# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",data=survey_data, kind="bar")
# Show plot
plt.show()

# Set the context to "paper"
sns.set_context("talk")
# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",data=survey_data, kind="bar")
# Show plot
plt.show()

# Set the context to "paper"
sns.set_context("poster")
# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",data=survey_data, kind="bar")
# Show plot
plt.show()
