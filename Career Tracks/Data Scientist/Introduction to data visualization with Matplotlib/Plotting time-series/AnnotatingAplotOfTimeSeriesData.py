"""
Use the ax.plot method to plot the DataFrame index against the relative_temp column.
Use the annotate method to add the text '>1 degree' in the location (pd.Timestamp('2015-10-06'), 1)
"""

fig, ax = plt.subplots()

# Plot the relative temperature data
ax.plot(climate_change.index,climate_change['relative_temp'])

# Annotate the date at which temperatures exceeded 1 degree
ax.annotate('>1 degree', xy=(pd.Timestamp('2015-10-06'), 1))

plt.show()
