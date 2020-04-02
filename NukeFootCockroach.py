from random import randint

win = 0
loss = 0
tie = 0
count = 0
choice = ["Foot", "Nuke", "Cockroach"]

you = input("Foot, Nuke or Cockroach? (Quit ends): ")
computer = choice[randint(0, 2)]
while you != "Quit":
    print("You chose: ", you)
    print("Computer chose:  ", computer)
    if you == computer == "Nuke":
        print("Both LOSE!")
        tie = tie+1
    elif you == computer:
        print("It is a tie!")
        tie = tie+1
    elif you == "Foot":
        if computer == "Nuke":
            print("You LOSE!")
            loss = loss+1
        else:
            print("You WIN!")
            win = win+1
    elif you == "Nuke":
        if computer == "Cockroach":
            print("You LOSE!")
            loss = loss+1
        else:
            print("You WIN!")
            win = win+1
    elif you == "Cockroach":
        if computer == "Foot":
            print("You LOSE!")
            loss = loss+1
        else:
            print("You WIN")
            win = win+1
    else:
        print("Incorrect selection.")
    you = input("Foot,Nuke or Cockroach? (Quit ends): ")
    computer = choice[randint(0, 2)]
    count = count+1

if you == "Quit":
    print("You played ", count, " rounds and won ", win, " rounds, playing tie in ", tie, " rounds.")

