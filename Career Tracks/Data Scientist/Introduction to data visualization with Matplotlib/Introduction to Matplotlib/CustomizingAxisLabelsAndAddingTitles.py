"""

    Use the set_xlabel method to add the label: "Time (months)".
    Use the set_ylabel method to add the label: "Precipitation (inches)".
    Use the set_title method to add the title: "Weather patterns in Austin and Seattle".

"""

ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

# Customize the x-axis label
ax.set_xlabel("Time (months)")

# Customize the y-axis label
ax.set_ylabel("Precipitation (inches)")

# Add the title
ax.set_title("Weather patterns in Austin and Seattle")

# Display the figure
plt.show()
