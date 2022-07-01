"""
1 > Add the following title to the plot: "Average MPG Over Time".
2 > Label the x-axis as "Car Model Year" and the y-axis as "Average MPG".
"""

# Create line plot
g = sns.lineplot(x="model_year", y="mpg_mean", 
                 data=mpg_mean,
                 hue="origin")
# Add a title "Average MPG Over Time"
g.set_title("Average MPG Over Time")
# Show plot
plt.show()


# Create line plot
g = sns.lineplot(x="model_year", y="mpg_mean", 
                 data=mpg_mean,
                 hue="origin")
# Add a title "Average MPG Over Time"
g.set_title("Average MPG Over Time")
# Add x-axis and y-axis labels
g.set(xlabel="Car Model Year",ylabel="Average MPG")
# Show plot
plt.show()
