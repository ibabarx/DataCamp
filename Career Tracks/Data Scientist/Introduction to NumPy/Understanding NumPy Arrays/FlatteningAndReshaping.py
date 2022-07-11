"""
Flatten sudoku_game so that it is a 1D array, and save it as flattened_game.
Print the .shape of flattened_game.
"""

# Flatten sudoku_game
flattened_game = sudoku_game.flatten()

# Print the shape of flattened_game
print(flattened_game.shape)

# Reshape flattened_game back to a nine by nine array
reshaped_game = np.reshape(flattened_game,newshape=(9,9))

# Print sudoku_game and reshaped_game
print(sudoku_game)
print(reshaped_game)
