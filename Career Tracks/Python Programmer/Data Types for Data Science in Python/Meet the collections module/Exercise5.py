"""
1> Import OrderedDict from collections.
2> Create an OrderedDict called ridership_date.
3> Iterate over the list entries, unpacking it into date and riders.
4> If a key does not exist in ridership_date for the date, set it equal to 0 (if only you could use defaultdict here!)
5> Add riders to the date key of ridership_date.
6> Print the first 31 records. Remember to convert the items into a list.
"""
# Import OrderedDict from collections
from collections import OrderedDict

# Create an OrderedDict called: ridership_date
ridership_date = OrderedDict()

# Iterate over the entries
for date,riders in entries:
    # If a key does not exist in ridership_date, set it to 0
    if date not in ridership_date:
        ridership_date[date]=0
        
    # Add riders to the date key in ridership_date
    ridership_date[date] += riders
    
# Print the first 31 records
print(list(ridership_date.items())[:31])
