"""

    1. To import CSV files you still need the pandas package: import it as pd.
    2. Use pd.read_csv() to import cars.csv data as a DataFrame. Store this DataFrame as cars.
    3. Print out cars. Does everything look OK?

"""

# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

# Print out cars
print(cars)
