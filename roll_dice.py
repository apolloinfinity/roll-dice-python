"""roll-dice.py, By Javier Ramirez, 03-16-2018
Updated: 3-27-18
Small program that simulates the rolling of a dice. Still a work in progress but got the MVP working.
"""
import random as r

def roll_dice():
    sides = 6
    rolling = True
    while rolling:
        dice_1 = r.randint(1, sides)
        dice_2 = r.randint(1, sides)
        roll_again = input("Ready to roll?\nY for yes or N for no. ")
        if roll_again.lower() != "n":
            print(f'First dice rolled a {dice_1}')
            print(f'Second dice rolled a {dice_2}')
            print(f'Your total is {dice_1 + dice_2}')
        else:
            rolling = False
    

if __name__ == "__main__": roll_dice()
