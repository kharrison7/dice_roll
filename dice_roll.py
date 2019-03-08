"""
To Roll  Dice in Terminal Using Python.
To run in terminal - python dice_roll.py
"""
import random

def roll(sides=6):
    num_rolled = random.randint(1,sides)
    return num_rolled

def main():
    sides = 6
    rolling = True
    while rolling:
        roll_again = input("Enter -> Roll. Q -> Quit.")
        if roll_again.lower() != "q":
            num_rolled = roll(sides)
            print("You rolled a", num_rolled)
        else:
            rolling = False

    print("I hope you had fun rolling.")

main()

"""
From Py projects:
https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/
https://www.youtube.com/watch?v=b6U3rw-cH6A&list=PLhP5GzqIk6qsYjU_3tod0nqoWGXlq9RvF&index=2&t=0s
"""
