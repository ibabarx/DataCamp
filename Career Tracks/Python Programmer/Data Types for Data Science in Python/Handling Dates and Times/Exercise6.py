"""
1> Import timedelta from the datetime module.
2> Build a timedelta of 30 days called glanceback using timedelta().
3> Iterate over the review_dates, using date as your iterator variable.
    Calculate the date 30 days back by subtracting glanceback from date.
    Print the date, along with 'day_type' and 'total_ridership' from daily_summaries for that date.
    Print the prior_period_dt, along with 'day_type' and 'total_ridership' from daily_summaries for that date (prior_period_dt).
"""
# Import timedelta from the datetime module
from datetime import timedelta

# Build a timedelta of 30 days: glanceback
glanceback = timedelta(days=30)

# Iterate over the review_dates as date
for date in review_dates:
    # Calculate the date 30 days back: prior_period_dt
    prior_period_dt = date - glanceback
    
    # Print the review_date, day_type and total_ridership
    print('Date: %s, Type: %s, Total Ridership: %s' %
         (date, 
          daily_summaries[date]['day_type'], 
          daily_summaries[date]['total_ridership']))

    # Print the prior_period_dt, day_type and total_ridership
    print('Date: %s, Type: %s, Total Ridership: %s' %
         (prior_period_dt, 
          daily_summaries[prior_period_dt]['day_type'], 
          daily_summaries[prior_period_dt]['total_ridership']))
