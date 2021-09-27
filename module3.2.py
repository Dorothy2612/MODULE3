#Create a terminal coin flip game. The game should ask the user to make a selection
# , either '1' or '0'. Then the function should randomly select a value, again a '1'
# or a '0'. Then compare the values, and if they're equal you win, if they're not equal then the computer wins.
import random
answer=input("which number are you going to choose 1 or 0")
computer=random.choice([0,1])
if answer == computer:
    print("you win")
else:
    print("the computer wins")