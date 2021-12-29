# Created by Billy Terimpundu 
# Created on December 2021
# This program gets the user to guess a number
# between 1 and 11 and tells them if it's correct.
import random


def main():

    # set correct number
    correct = random.randint(1, 11)

    # input
    user_number = float(input("Guess a number between 1 and 11: "))
    print("")

    # Check number
    if user_number >= 11:
        print("Number must be between 1 and 11 silly")

    elif user_number <= -1:
        print("Number must be between 1 and 11 silly")

    # Process and output
    elif user_number == correct:
        print("You've guessed correctly!")

    else:
        print("You've guessed incorrectly!")
        print("The correct number was: {}". format(correct))


if __name__ == "__main__":
    main()