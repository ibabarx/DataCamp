"""
1 > Select 'agecon' and 'agepreg', divide them by 100, and assign them to the local variables agecon and agepreg.
2 > Compute the difference, which is an estimate of the duration of the pregnancy. Keep in mind that for each pregnancy, agepreg will be larger than agecon.
3 > Use .describe() to compute the mean duration and other summary statistics.
"""

# Select the columns and divide by 100
agecon = nsfg['agecon'] / 100
agepreg = nsfg['agepreg'] / 100

# Compute the difference
preg_length = agepreg - agecon

# Compute summary statistics
print(preg_length.describe())
