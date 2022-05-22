"""
1> Import namedtuple from collections.
2> Create a namedtuple called DateDetails with a type name of DateDetails and fields of 'date', 'stop', and 'riders'.
3> Create a list called labeled_entries.
4> Iterate over the entries list, unpacking it into date, stop, and riders.
5> Create a new DateDetails namedtuple instance for each entry and append it to labeled_entries.
6> Print the first 5 items in labeled_entries. This has been done for you, so hit 'Submit Answer' to see the result!
"""
# Import namedtuple from collections
from collections import namedtuple

# Create the namedtuple: DateDetails
DateDetails = namedtuple('DateDetails', ['date', 'stop', 'riders'])

# Create the empty list: labeled_entries
labeled_entries = []

# Iterate over the entries list
for date, stop, riders in entries:
    # Append a new DateDetails namedtuple instance for each entry to labeled_entries
    labeled_entries.append(DateDetails(date,stop,riders))
    
# Print the first 5 items in labeled_entries
print(labeled_entries[:5])
