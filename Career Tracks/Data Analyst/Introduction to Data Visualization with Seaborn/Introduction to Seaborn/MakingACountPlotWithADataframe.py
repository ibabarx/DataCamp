"""
Import Matplotlib, pandas, and Seaborn using the standard names.
Create a DataFrame named df from the csv file located at csv_filepath.
Use the countplot() function with the x= and data= arguments to create a count plot with the "Spiders" column values on the x-axis.
Display the plot.
"""

# Import Matplotlib, pandas, and Seaborn
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Create a count plot with "Spiders" on the x-axis
sns.countplot(x="Spiders",data=df)

# Display the plot
plt.show()
