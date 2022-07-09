"""

    1. Create a 3D array called game_and_solution by stacking the two 2D arrays, sudoku_game and sudoku_solution, on top of one another; in the final array, 
       sudoku_game should appear before sudoku_solution.
    2. Print game_and_solution.

"""

# Create the game_and_solution 3D array
game_and_solution = np.array([sudoku_game,sudoku_solution])

# Print game_and_solution
print(game_and_solution) 
