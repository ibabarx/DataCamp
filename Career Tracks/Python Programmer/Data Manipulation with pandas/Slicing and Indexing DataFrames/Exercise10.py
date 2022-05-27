"""
Use .loc[] on temp_by_country_city_vs_year to take subsets.
1> From Egypt to India.
2> From Egypt, Cairo to India, Delhi.
3> From Egypt, Cairo to India, Delhi, and 2005 to 2010.
"""
# Subset for Egypt to India
temp_by_country_city_vs_year.loc['Egypt':'India']

# Subset for Egypt, Cairo to India, Delhi
temp_by_country_city_vs_year.loc[('Egypt','Cairo'):('India','Delhi')]

# Subset for Egypt, Cairo to India, Delhi, and 2005 to 2010
temp_by_country_city_vs_year.loc[('Egypt','Cairo'):('India','Delhi'),2005:2010]
