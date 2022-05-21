"""
1> Import the Counter object from collections.
2> Print the first ten items from the stations list.
3> Create a Counter of the stations list called station_count.
4> Print the station_count.
"""
# Import the Counter object
from collections import Counter

# Print the first ten items from the stations list
print(stations[:10])

# Create a Counter of the stations list: station_count
station_count = Counter(stations)

# Print the station_count
print(station_count)
