"""
Where's the word?
Before finishing cleaning your dataset, you want to check if a specific word occurs in the reviews. You noticed earlier a specific pattern in the strings. Now, you 
want to create a function to check if a word is present between characters with index 12, and 50, remembering that ending position is exclusive, and print out the 
lowest index where this word occurs. There are two methods to handle this situation. You want to see which one works best.
The text of two movie reviews has been already saved in the variable movies. You can use print(movies) to view the variable in the IPython Shell.
"""
"""
1> Find the index where money occurs between characters with index 12 and 50. If not found, the method should return -1.
2> Find the index where money occurs between characters with index 12 and 50. If not found, it should raise an error.
"""

for movie in movies:
  # Find the first occurrence of word
  print(movie.find('money', 12, 51))
  
for movie in movies:
  try:
    # Find the first occurrence of word
  	print(movie.index('money', 12, 51))
  except ValueError:
    print("substring not found")
