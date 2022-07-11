"""
1. Print the data type of the elements in sudoku_game.
2. Change the data type of sudoku_game to be int8, an 8-bit integer; name the new array small_sudoku_game.
3. Print the data type of small_sudoku_game to be sure that your change to int8 is reflected.
"""

# Print the data type of sudoku_game
print(sudoku_game.dtype)

# Change the data type of sudoku_game to int8
small_sudoku_game = sudoku_game.astype(np.int8)

# Print the data type of small_sudoku_game
print(small_sudoku_game.dtype)
