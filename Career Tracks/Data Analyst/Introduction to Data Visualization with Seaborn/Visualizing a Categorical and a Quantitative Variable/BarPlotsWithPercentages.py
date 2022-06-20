"""
Use the survey_data DataFrame and sns.catplot() to create a bar plot with "Gender" on the x-axis and "Interested in Math" on the y-axis.
"""

# Create a bar plot of interest in math, separated by gender
sns.catplot(kind='bar',data=survey_data,x="Gender",y="Interested in Math")
# Show plot
plt.show()
