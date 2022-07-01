"""
Rotate the x-tick labels 90 degrees.
"""

# Create point plot
sns.catplot(x="origin", 
            y="acceleration", 
            data=mpg, 
            kind="point", 
            join=False, 
            capsize=0.1)

# Rotate x-tick labels

plt.xticks(rotation=90)
# Show plot
plt.show()
