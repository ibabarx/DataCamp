"""
1 > Use sns.catplot() to create a box plot with the student_data DataFrame, putting "internet" on the x-axis and "G3" on the y-axis.
2 > Add subgroups so each box plot is colored based on "location".
3 > Do not display the outliers.
"""

# Create a box plot with subgroups and omit the outliers
sns.catplot(data=student_data,x="internet",y="G3",hue="location",sym="",kind='box')

# Show plot
plt.show()
