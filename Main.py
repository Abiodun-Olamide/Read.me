from random import randint

# R for "rock"

# P for "paper"

# S for "scissors"

t = ["R", "P", "S"]

#assign a random play to the computer

computer = t[randint(0,2)]

player = False

while player == False:

    player = input("Pick an option between R, P, S?")

    if player == computer:

        print("Tie!")

    elif player == "R":

        if computer == "P":

            print("You lose!", computer, "covers", player)

        else:

            print("You win!", player, "smashes", computer)

    elif player == "P":

        if computer == "S":

            print("You lose!", computer, "cut", player)

        else:

            print("You win!", player, "covers", computer)

    elif player == "S":

        if computer == "R":

            print("You lose...", computer, "smashes", player)

        else:

            print("You win!", player, "cut", computer)

    else:

        print("That's not a valid play. Check your spelling!")

    #player was set to True, but we want it to be False so the loop continues

    player = False

    computer = t[randint(0,2)]
