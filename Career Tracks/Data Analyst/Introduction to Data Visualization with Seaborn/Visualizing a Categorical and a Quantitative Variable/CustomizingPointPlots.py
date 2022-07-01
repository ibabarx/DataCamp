"""
1 > Use sns.catplot() and the student_data DataFrame to create a point plot with "famrel" on the x-axis and number of absences ("absences") on the y-axis.
2 > Add "caps" to the end of the confidence intervals with size 0.2.
3 > Remove the lines joining the points in each category.
"""

# Create a point plot of family relationship vs. absences
sns.catplot(kind='point',data=student_data,x="famrel",y="absences")
# Show plot
plt.show()

# Add caps to the confidence interval
sns.catplot(x="famrel", y="absences", data=student_data, kind="point",capsize=0.2) 
# Show plot
plt.show()

# Remove the lines joining the points
sns.catplot(x="famrel", y="absences",data=student_data,kind="point",capsize=0.2,join=False)         
# Show plot
plt.show()
