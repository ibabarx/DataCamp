"""
1 > Use sns.catplot() to create a bar plot with "study_time" on the x-axis and final grade ("G3") on the y-axis, using the student_data DataFrame.
2 > Using the order parameter and the category_order list that is provided, rearrange the bars so that they are in order from lowest study time to highest.
3 > Update the plot so that it no longer displays confidence intervals.
"""

# Create bar plot of average final grade in each study category
sns.catplot(kind='bar',data=student_data,x="study_time",y="G3")
# Show plot
plt.show()


# List of categories from lowest to highest
category_order = ["<2 hours",  "2 to 5 hours", "5 to 10 hours", ">10 hours"]
# Rearrange the categories
sns.catplot(x="study_time", y="G3",data=student_data,kind="bar",order=category_order)
# Show plot
plt.show()


# List of categories from lowest to highest
category_order = ["<2 hours",  "2 to 5 hours", "5 to 10 hours", ">10 hours"]
# Turn off the confidence intervals
sns.catplot(x="study_time", y="G3", data=student_data,kind="bar",order=category_order,ci=None)
# Show plot
plt.show()
