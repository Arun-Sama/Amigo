"""import random

print("Winning Rules of the Rock paper scissor game as follows: \n"
      + "Rock vs paper->paper wins \n"
      + "Rock vs scissor->Rock wins \n"
      + "paper vs scissor->scissor wins \n")
# print("(Multiplayer or single player)?")

while True:
    player = int(input("choose No.of players(1 or 2):  \n"))
    while player > 2 or player < 1:
        player = int(input("\n Enter valid input \n choose No.of players(1 or 2):  \n"))
    if player == 1:
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
    else:
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
        print("Enter choice \n 1 Rock, \n 2 paper, and \n 3 scissor \n")
        user_choice2 = int(input("User Turn2 : "))
        while user_choice2 > 3 or user_choice2 < 1:
            user_choice2 = int(input("Enter the valid input : "))
        if user_choice2 == 1:
            choice_name2 = "Rock"
        elif user_choice2 == 2:
            choice_name2 = "Paper"
        else:
            choice_name2 = "Scissor"
        print("User Choice is " + choice_name2)
        print(choice_name + "v/s" + choice_name2)
        if (user_choice == 1 and user_choice2 == 3) or (user_choice == 3 and user_choice2 == 1):
            print("Rock wins =>", end="")
            result = "Rock"
        elif (user_choice == 1 and user_choice2 == 2) or (user_choice == 2 and user_choice2 == 1):
            print("Paper wins =>", end="")
            result = "Paper"
        else:
            print("scissor wins =>", end="")
            result = "scissor"
        if result == choice_name:
            print("User Wins")
        else:
            print("User 2 Wins")
        print("Do you want to play again? (Y/N)")
        ans = input()

        if ans == "n" or ans == "N":
            break

    print("Thanks for playing")"""

'''a = '2'
b = "2"
print(a+b)'''