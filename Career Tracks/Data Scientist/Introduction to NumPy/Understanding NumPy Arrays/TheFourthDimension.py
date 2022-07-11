"""
1. Create another 3D array called new_game_and_solution with a different 2D game and 2D solution pair: new_sudoku_game and new_sudoku_solution. new_sudoku_game should 
   appear before new_sudoku_solution.
2. Create a 4D array called games_and_solutions by making an array out of the two 3D arrays: game_and_solution and new_game_and_solution, in that order.
3. Print the shape of games_and_solutions.
"""

# Create a second 3D array of another game and its solution 
new_game_and_solution = np.array([new_sudoku_game,new_sudoku_solution])

# Create a 4D array of both game and solution 3D arrays
games_and_solutions = np.array([game_and_solution,new_game_and_solution])

# Print the shape of your 4D array
print(games_and_solutions.shape)
