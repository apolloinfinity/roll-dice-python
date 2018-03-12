"""Small program that simulates the rolling of a dice.

"""
import random as r

def roll_dice():
    min = 1
    max = 6
    die_1 = r.randint(min, max)
    die_2 = r.randint(min, max)
    choice = input("Do yo want to roll the dice?")
    while True:
        if choice == "yes" or "y":
            print(die_1)
            print(die_2)
        if choice == "no" or "n":
            break
    

if __name__ == "__main__": roll_dice()