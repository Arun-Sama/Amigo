import random

import time

true = ["T", "t", "True"]
false = ["F", "f", "False"]
correct = 0  # Storing the correct answers

name = input("What's your name?")  # Storing the user's name

print("\nOK, " + name + ", let's get started. Remember, the following answers are only True or False.")
time.sleep(2)

print("\nParis is the capital of France.")
choice = input(">>> ")
if choice in true:
    correct += 1  # If correct, the user gets one point
else:
    correct += 0

print("\nEngland is an island.")
choice = input(">>> ")
if choice in false:
    correct += 1
else:
    correct += 0

print("\nNorthern Ireland isn't part of Great Britain.")
choice = input(">>> ")
if choice in false:
    correct += 1
else:
    correct += 0

print("\nAndorra is between France and Spain.")
choice = input(">>> ")
if choice in true:
    correct += 1
else:
    correct += 0

print("\nIran use to be part of the Persian Empire.")
choice = input(">>> ")
if choice in true:
    correct += 1
else:
    correct += 0

print("\nTurkmenistan isn't a real country.")
choice = input(">>> ")
if choice in false:
    correct += 1
else:
    correct += 0

print("\nYou're finished, " + name + ". You got", correct, "out of 6 correct.")

"""print("Winning Rules of the Rock paper scissor game as follows: \n"
      + "Rock vs paper->paper wins \n"
      + "Rock vs scissor->Rock wins \n"
      + "paper vs scissor->scissor wins \n")

while True:
    print("Enter choice \n 1 Rock, \n 2 paper, and \n 3 scissor \n")
    user_choice = int(input("User Turn : "))
    while user_choice > 3 or user_choice < 1:
        user_choice = int(input("Enter the valid input : "))
    if user_choice == 1:
        choice_name = "Rock"
    elif user_choice == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissor"
    print("User Choice is " + choice_name)
    print("\nNow its computer turn....")
    comp_choice = random.randint(1, 3)
    while comp_choice == user_choice:
        comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    else:
        comp_choice_name = "Scissor"
    print("Computer Choice is" + comp_choice_name)
    print(choice_name + "v/s" + comp_choice_name)

    if (user_choice == 1 and comp_choice == 3) or (user_choice == 3 and comp_choice == 1):
        print("Rock wins =>", end="")
        result = "Rock"
    elif (user_choice == 1 and comp_choice == 2) or (user_choice == 2 and comp_choice == 1):
        print("Paper wins =>", end="")
        result = "Paper"
    else:
        print("scissor wins =>", end="")
        result = "scissor"
    if result == choice_name:
        print("User Wins")
    else:
        print("Computer Wins")

    print("Do you want to play again? (Y/N)")
    ans = input()

    if ans == "n" or ans == "N":
        break

print("Thanks for playing")"""
