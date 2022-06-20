"""
1 > Modify the code to use relplot() instead of scatterplot().
2 > Modify the code to create one scatter plot for each level of the variable "study_time", arranged in columns.
3 > Adapt your code to create one scatter plot for each level of a student's weekly study time, this time arranged in rows.
"""

# Change to use relplot() instead of scatterplot()
sns.relplot(x="absences",y="G3",     data=student_data,kind='scatter')
# Show plot
plt.show()


# Change to make subplots based on study time
sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter",col='study_time')
# Show plot
plt.show()


# Change this scatter plot to arrange the plots in rows instead of columns
sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter", 
            row="study_time")
# Show plot
plt.show()
