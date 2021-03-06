"""
Unix timestamps
Datetimes are sometimes stored as Unix timestamps: the number of seconds since January 1, 1970. This is especially common with computer infrastructure, 
like the log files that websites keep when they get visitors.
"""
"""
1> Complete the for loop to loop over timestamps.
2> Complete the code to turn each timestamp ts into a datetime.
"""

# Import datetime
from datetime import datetime

# Starting timestamps
timestamps = [1514665153, 1514664543]

# Datetime objects
dts = []

# Loop
for ts in timestamps:
  dts.append(datetime.fromtimestamp(ts))
  
# Print results
print(dts)
