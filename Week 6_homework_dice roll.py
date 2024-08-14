# -*- coding: utf-8 -*-

import random

def roll_dice(sides):
    return random.randint(1, sides)

def main():
    try:
        num_sides = int(input("Enter the number of sides for the die: "))
        num_dice = int(input("Enter the number of dice to roll: "))

        total = 0
        for _ in range(num_dice):
            roll = roll_dice(num_sides)
            print(f"You rolled a {roll}")
            total += roll

        print(f"Total of all dice rolls: {total}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
    
