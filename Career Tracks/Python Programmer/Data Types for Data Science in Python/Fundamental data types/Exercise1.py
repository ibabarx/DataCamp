"""
Create a list called baby_names with the names 'Ximena', 'Aliza', 'Ayden', and 'Calvin'.
Use the .extend() method on baby_names to add 'Rowen' and 'Sandeep' and print the list.
Use the .index() method to find the position of 'Aliza' in the list. Save the result as position.
Use the .pop() method with position to remove 'Aliza' from the list.
Print the baby_names list.
"""

baby_names = ['Ximena','Aliza','Ayden','Calvin']
baby_names.extend(['Rowen','Sandeep'])
print(baby_names)
position = baby_names.index('Aliza')
baby_names.pop(position)
print(baby_names)
