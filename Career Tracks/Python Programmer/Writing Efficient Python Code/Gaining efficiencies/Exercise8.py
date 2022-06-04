"""
Replace the above for loop using NumPy:
Create a total stats array (total_stats_np) using the .sum() method and specifying the correct axis.
Create an average stats array (avg_stats_np) using the .mean() method and specifying the correct axis.
Create a final output list (poke_list_np) by combining the names list, the total_stats_np array, and the avg_stats_np array.
"""

# Create a total stats array
total_stats_np = np.sum(stats,axis=1)

# Create an average stats array
avg_stats_np = np.mean(stats,axis=1)

# Combine names, total_stats_np, and avg_stats_np into a list
poke_list_np = [*zip(names, total_stats_np, avg_stats_np)]

print(poke_list_np == poke_list, '\n')
print(poke_list_np[:3])
print(poke_list[:3], '\n')
top_3 = sorted(poke_list_np, key=lambda x: x[1], reverse=True)[:3]
print('3 strongest Pokémon:\n{}'.format(top_3))
