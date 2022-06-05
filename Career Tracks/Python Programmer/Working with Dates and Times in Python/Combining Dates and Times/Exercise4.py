"""
Parsing pairs of strings as datetimes
Up until now, you've been working with a pre-processed list of datetimes for W20529's trips. For this exercise, you're going to go one step back in the data cleaning
pipeline and work with the strings that the data started as.
Explore onebike_datetime_strings in the IPython shell to determine the correct format. datetime has already been loaded for you.
"""
"""
1> Outside the for loop, fill out the fmt string with the correct parsing format for the data.
2> Within the for loop, parse the start and end strings into the trip dictionary with start and end keys and datetime objects for values.
"""

# Write down the format string
fmt = "%Y-%m-%d %H:%M:%S"

# Initialize a list for holding the pairs of datetime objects
onebike_datetimes = []

# Loop over all trips
for (start, end) in onebike_datetime_strings:
  trip = {'start': datetime.strptime(start, fmt),
          'end': datetime.strptime(end, fmt)}
  
  # Append the trip
  onebike_datetimes.append(trip)
