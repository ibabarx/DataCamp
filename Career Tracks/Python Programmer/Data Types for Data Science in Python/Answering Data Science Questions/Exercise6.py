"""
1> Loop over the crimes_by_district dictionary, unpacking it into the variables district and crimes.
2> Create an empty Counter object called year_count.
3> Loop over the crimes:
4> If there was an arrest,
    Convert crime['Date'] to a datetime object called year.
    Add the crime to the Counter for the year, by using year as the key of year_count.
5> Print the Counter. This has been done for you, so hit 'Submit Answer' to see the result!
"""

# Loop over the crimes_by_district using expansion as district and crimes
for district, crimes in crimes_by_district.items():
    # Print the district
    print(district)
    
    # Create an empty Counter object: year_count
    year_count = Counter()
    
    # Loop over the crimes:
    for crime in crimes:
        # If there was an arrest
        if crime['Arrest'] == 'true':
            # Convert the Date to a datetime and get the year
            year = datetime.strptime(crime['Date'], '%m/%d/%Y %I:%M:%S %p').year
            # Increment the Counter for the year
            year_count[year] += 1
            
    # Print the counter
    print(year_count)
