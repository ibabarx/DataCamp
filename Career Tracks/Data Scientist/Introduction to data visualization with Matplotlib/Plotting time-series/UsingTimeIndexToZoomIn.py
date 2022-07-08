"""

    Use plt.subplots to create a Figure with one Axes called fig and ax, respectively.
    Create a variable called seventies that includes all the data between "1970-01-01" and "1979-12-31".
    Add the data from seventies to the plot: use the DataFrame index for the x value and the "co2" column for the y values.

"""

import matplotlib.pyplot as plt

# Use plt.subplots to create fig and ax
fig, ax = plt.subplots()

# Create variable seventies with data from "1970-01-01" to "1979-12-31"
seventies = climate_change["1970-01-01":"1979-12-31"]

# Add the time-series for "co2" data from seventies to the plot
ax.plot(seventies.index, seventies["co2"])

# Show the figure
plt.show()
