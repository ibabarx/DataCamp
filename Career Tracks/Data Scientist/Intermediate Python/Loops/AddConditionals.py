"""

    1. Inside the while loop, complete the if-else statement:
        If offset is greater than zero, you should decrease offset by 1.
        Else, you should increase offset by 1.

"""

# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0 :
      offset -= 1
    else : 
      offset += 1    
    print(offset)
