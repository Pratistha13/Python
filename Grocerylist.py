# create a small grocery shopping list with the list datastructure. In short, create a program that 
# allows the user to (1) add products to the list, (2) remove items and (3) print the list and quit.

mylist = []
while True:
    selection = int(input("Would you like to \n(1)Add or \n(2)Remove items or \n(3)Quit?: "))

    if selection == 1:
        grocery = input("What will be added?: ")
        mylist.append(grocery)

    elif selection == 2:
        print("There are ", len(mylist), "items in the list")
        question = int(input("Which item is deleted?: "))
        if question >= len(mylist):
            print("Incorrect selection.")
        else:
            mylist.pop(question)

    elif selection == 3:
        print("The following items remain in the list: ")
        for i in mylist:
            print(i)
        break
    else:
        print("Incorrect selection.")

