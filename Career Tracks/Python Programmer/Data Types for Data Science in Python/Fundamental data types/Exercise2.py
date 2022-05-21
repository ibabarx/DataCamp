"""
1> Create an empty list called baby_names.
2> Use a for loop to iterate over each row of records appending the name, found in the fourth element of row, to baby_names.
3> Print each name in baby_names in alphabetical order. To do this:
   Use the sorted() function as part of a for loop to iterate over the sorted names, printing each one.
"""

baby_names = []

for row in records:
    baby_names.append(row[3])

for name in sorted(baby_names):
    print(name)
