"""Small program that simulates the rolling of a dice.

"""
import random as r

def roll_dice():
    sides = 6
    dice_1 = r.randint(1, sides)
    dice_2 = r.randint(1, sides)
    rolling = True
    while rolling:
        roll_again = input("Ready to roll?\nY for yes or N for no. ")
        if roll_again.lower() != "n":
            print(f'First dice rolled a {dice_1}')
            print(f'Second dice rolled a {dice_2}')
        else:
            rolling = False
    

if __name__ == "__main__": roll_dice()