"""
1> Import Counter from the collections module.
2> Use Counter() to collect the count of each generation from the generations list. Save this as gen_counts.
3> Write a better for loop that places a one-time calculation outside (above) the loop. Use the exact same syntax as the original for loop (simply copy and paste 
   the one-time calculation above the loop).
"""

# Import Counter
from collections import Counter 

# Collect the count of each generation
gen_counts = Counter(generations)

# Improve for loop by moving one calculation above the loop
total_count = len(generations)

for gen,count in gen_counts.items():
    gen_percent = round(count / total_count * 100, 2)
    print('generation {}: count = {:3} percentage = {}'
          .format(gen, count, gen_percent))
