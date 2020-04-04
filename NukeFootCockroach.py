import random

"""
Implement the game so that the other player is computer controlled, 
and chooses randomly either foot(number 1), cockroach(number 3) or nuke(number 2). 
Also implement a feature which keeps the score, calculating both rounds the player won, and ties. 
If the player wins, print "You WIN!", if they loose "You LOSE!". 
If the round was a tie, either "It is a tie!" or "Both LOSE!", depending on if the tie was caused by a nuke or not. 
If the player selects "quit", the game ends and the final score is given.
"""

win = 0
loss = 0
tie = 0
count = 0
while True:
    you = input("Foot, Nuke or Cockroach? (Quit ends): ")

    if you == "Quit":
        print("You played ", count, " rounds and won ", win, " rounds, playing tie in ", tie, " rounds.")
        break
    if you != "Cockroach" and you != "Nuke" and you != "Foot":
        print("Incorrect selection.")
        continue

    else:
        computer = random.randint(0, 3)
        if computer == 1:
            computer = "Foot"
        elif computer == 2:
            computer = "Nuke"
        else:
            computer = "Cockroach"

        print("You chose: ", you)
        print("Computer chose:  ", computer)

        if you == computer == "Nuke":
            print("Both LOSE!")
            tie = tie + 1
        elif you == computer:
            print("It is a tie!")
            tie = tie + 1
        elif you == "Foot":
            if computer == "Nuke":
                print("You LOSE!")
                loss = loss + 1
            else:
                print("You WIN!")
                win = win + 1
        elif you == "Nuke":
            if computer == "Cockroach":
                print("You LOSE!")
                loss = loss + 1
            else:
                print("You WIN!")
                win = win + 1
        elif you == "Cockroach":
            if computer == "Foot":
                print("You LOSE!")
                loss = loss + 1
            else:
                print("You WIN!")
                win = win + 1

        else:
            print(" ")

        count = count + 1




