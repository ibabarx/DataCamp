"""
Split lines or split the line?
You are about to leave work when a colleague asks you to use your string manipulation skills to help him. You need to read strings from a file in a way that if the file 
contains strings on different lines, they are stored as separate elements. He also wants you to break the strings into pieces if you see that they contain commas.
The text of the file has been already saved in the variable file. You can use print(file) to view the variable in the IPython Shell.
"""
"""
1> Split the string file into many substrings at line boundaries.
2> Print out the resulting variable file_split.
3> Complete the for-loop to split the strings into many substrings using commas as a separator element.
"""

# Split string at line boundaries
file_split = file.split(sep='\n')

# Print file_split
print(file_split)

# Complete for-loop to split by commas
for substring in file_split:
    substring_split = substring.split(sep=',')
    print(substring_split)
