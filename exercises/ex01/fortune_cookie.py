"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730322809"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
fortune: int = (randint(1, 4))

if fortune == 1:
    print("the grasshopper looks for better days.")
else: 
    if fortune == 2:
        print("The journey of 1000 miles begins with a single step.")
    else:
        if fortune == 3:
            print("Just do it.")
        else: 
            print("Don't text em, nothing good will come from this.")

print("Now, go spread positive vibes!")
