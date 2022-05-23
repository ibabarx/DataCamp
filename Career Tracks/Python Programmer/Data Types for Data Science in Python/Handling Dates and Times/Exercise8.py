"""
1> Import the pendulum module.
2> Create a now datetime for Tokyo ('Asia/Tokyo') called tokyo_dt.
3> Convert tokyo_dt to Los Angeles time ('America/Los_Angeles'). Store the result as la_dt.
4> Print the ISO 8601 string of la_dt, using the .to_iso8601_string() method.
"""
# Import the pendulum module
import pendulum

# Create a now datetime for Tokyo: tokyo_dt
tokyo_dt = pendulum.now('Asia/Tokyo')

# Covert the tokyo_dt to Los Angeles: la_dt
la_dt = tokyo_dt.in_timezone('America/Los_Angeles')

# Print the ISO 8601 string of la_dt
print(la_dt.to_iso8601_string())
