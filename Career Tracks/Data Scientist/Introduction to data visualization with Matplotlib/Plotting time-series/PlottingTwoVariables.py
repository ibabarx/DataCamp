"""

    Use plt.subplots to create a Figure and Axes objects called fig and ax, respectively.
    Plot the carbon dioxide variable in blue using the Axes plot method.
    Use the Axes twinx method to create a twin Axes that shares the x-axis.
    Plot the relative temperature variable in red on the twin Axes using its plot method.

"""

import matplotlib.pyplot as plt

# Initalize a Figure and Axes
fig,ax = plt.subplots()

# Plot the CO2 variable in blue
ax.plot(climate_change.index, climate_change['co2'], color='b')

# Create a twin Axes that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature in red
ax2.plot(climate_change.index, climate_change['relative_temp'], color='r')

plt.show()
