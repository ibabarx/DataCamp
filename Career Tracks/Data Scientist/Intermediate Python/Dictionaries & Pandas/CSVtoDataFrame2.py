"""

    1. Run the code with Run Code and assert that the first column should actually be used as row labels.
    2. Specify the index_col argument inside pd.read_csv(): set it to 0, so that the first column is used as row labels.
    3. Has the printout of cars improved now?

"""

# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('cars.csv',index_col=0)

# Print out cars
print(cars)
