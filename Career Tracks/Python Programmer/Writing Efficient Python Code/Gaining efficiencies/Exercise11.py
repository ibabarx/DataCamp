"""
1> Use NumPy to eliminate the for loop used to create the z-scores.
   Then, combine the names, hps, and z_scores objects together into a list called poke_zscores2
2> Use list comprehension to replace the for loop used to collect Pokémon with the highest HPs based on their z-score.
"""

# Calculate the total HP avg and total HP standard deviation
hp_avg = np.mean(hps)
hp_std = np.std(hps)
# Use NumPy to eliminate the previous for loop
z_scores = (hps - hp_avg)/hp_std
# Combine names, hps, and z_scores
poke_zscores2 = [*zip(names, hps, z_scores)]
print(*poke_zscores2[:3], sep='\n')

# Use list comprehension with the same logic as the highest_hp_pokemon code block
highest_hp_pokemon2 = [(name, hp, zscore) for name,hp,zscore in poke_zscores2 if zscore > 2]
print(*highest_hp_pokemon2, sep='\n')
