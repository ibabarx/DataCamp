"""
1> Import the Counter object from collections.
2> Create a Counter of the stations list called station_count.
3> Print the 5 most common elements.
"""
# Import the Counter object
from collections import Counter

# Create a Counter of the stations list: station_count
station_count = Counter(stations)

# Find the 5 most common elements
print(station_count.most_common(5))
