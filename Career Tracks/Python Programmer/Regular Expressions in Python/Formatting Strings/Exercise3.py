"""
What day is today?
It's lunch time and you are talking with some of your colleagues. They comment that they feel that every morning someone should send them a reminder of what day it is so
they can check in the calendar what their assignments are for that day.
You want to help out and decide to write a small script that takes the date and time of the day so that every morning, a message is sent to your colleagues. You can use 
the module datetime along with named placeholders to achieve your goal.
The date should be expressed as Month day, year, e.g. April 16, 2019 and the time as hh:mm, e.g. 16:30.
You write down some specifiers to help you: %d(day), %B (monthname), %m (monthnumber), %Y(year), %H (hour) and %M(minutes)
You can use the IPython Shell to explore the module datetime.
"""
"""
1> Import the function datetime from the module datetime .
2> Obtain the date of today and assign it to the variable get_date.
3> Complete the string message by adding to the placeholders named today and the format specifiers to format the date as month_name day, year and time as hour:minutes.
4> Print the message using the .format() method and the variable get_date to replace the named placeholder.
"""

# Import datetime 
from datetime import datetime

# Assign date to get_date
get_date = datetime.now()

# Add named placeholders with format specifiers
message = "Good morning. Today is {today:%B %d, %Y}. It's {today:%H:%M} ... time to work!"

# Use the format method replacing the placeholder with get_date
print(message.format(today=get_date))
