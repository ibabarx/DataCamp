"""
1> Create a dictionary of lists with the new data called avocados_dict.
2> Convert the dictionary to a DataFrame called avocados_2019.
3> Print your new DataFrame.
"""

# Create a dictionary of lists with new data
avocados_dict = {
  "date": ["2019-11-17","2019-12-01"],
  "small_sold": [10859987,9291631],
  "large_sold": [7674135,6238096]
}

# Convert dictionary into DataFrame
avocados_2019 = pd.DataFrame(avocados_dict)

# Print the new DataFrame
print(avocados_2019)
