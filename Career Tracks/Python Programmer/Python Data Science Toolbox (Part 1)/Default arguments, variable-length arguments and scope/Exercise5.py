"""
1> Complete the function header with the function name shout_echo. It accepts an argument word1 and a default argument echo with default value 1, in that order.
2> Use the * operator to concatenate echo copies of word1. Assign the result to echo_word.
3> Call shout_echo() with just the string, "Hey". Assign the result to no_echo.
4> Call shout_echo() with the string "Hey" and the value 5 for the default argument, echo. Assign the result to with_echo.
"""

# Define shout_echo
def shout_echo(word1, echo = 1):
    """Concatenate echo copies of word1 and three
     exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1*echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo() with "Hey": no_echo
no_echo = shout_echo("Hey")

# Call shout_echo() with "Hey" and echo=5: with_echo
with_echo = shout_echo("Hey",echo=5)

# Print no_echo and with_echo
print(no_echo)
print(with_echo)
