"""
1> Import datetime from the datetime module.
2> Store the local datetime as local_dt and print it.
3> Store the UTC datetime as utc_dt and print it.
"""
# Import datetime from the datetime module
from datetime import datetime

# Compute the local datetime: local_dt
local_dt = datetime.now()

# Print the local datetime
print(local_dt)

# Compute the UTC datetime: utc_dt
utc_dt = datetime.utcnow()

# Print the UTC datetime
print(utc_dt)
