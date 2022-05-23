"""
1> Import Counter from collections.
2> Loop over the items from your dictionary, using tuple expansion to unpack locations_by_month.items() into month and locations.
3> Make a Counter of the locations called location_count.
4> Print the month.
5> Print the five most common crime locations.
"""
# Import Counter from collections
from collections import Counter

# Loop over the items from locations_by_month using tuple expansion of the month and locations
for month, locations in locations_by_month.items():
    # Make a Counter of the locations
    location_count = Counter(locations)
    # Print the month 
    print(month)
    # Print the most common location
    print(location_count.most_common(5))
