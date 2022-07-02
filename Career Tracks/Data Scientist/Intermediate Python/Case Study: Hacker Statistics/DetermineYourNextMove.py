"""

    1. Roll the dice. Use randint() to create the variable dice.
    2. Finish the if-elif-else construct by replacing ___:
    3. If dice is 1 or 2, you go one step down.
    4. if dice is 3, 4 or 5, you go one step up.
    5. Else, you throw the dice again. The number of eyes is the number of steps you go up.
    6. Print out dice and step. Given the value of dice, was step updated correctly?

"""

# NumPy is imported, seed is set

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice == 3 or dice == 4 or dice == 5 :
    step += 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)
