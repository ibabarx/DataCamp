"""
1> Calculate the mean temperature for each year, assigning to mean_temp_by_year.
2> Filter mean_temp_by_year for the year that had the highest mean temperature.
3> Calculate the mean temperature for each city (across columns), assigning to mean_temp_by_city.
4> Filter mean_temp_by_city for the city that had the lowest mean temperature.
"""
# Get the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean()

# Filter for the year that had the highest mean temp
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis="columns")

# Filter for the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])
