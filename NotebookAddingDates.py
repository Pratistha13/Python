import time

'''In this exercise, add a feature which includes the date and time of the written note to the program.
The program works as earlier, but saves data in the form "[note]:::[date and time]" meaning that there 
is a three-colon separator between the note and timestamp.'''

print("(1) Read the notebook \n(2) Add note \n(3) Empty the notebook \n(4) Quit")

myfile = "notebook.txt"

while True:
    selection = int(input("Please select one: "))

    if selection == 1:
        handle = open(myfile, "r")
        contents = handle.read()
        print(contents + "\n")
        print("(1) Read the notebook \n(2) Add note \n(3) Empty the notebook \n(4) Quit")

    elif selection == 2:
        handle = open(myfile, "a")
        addition = input("Write a new note: ")
        timenow = time.strftime("%X %x")
        handle.write(addition + ":::" + timenow + "\n")
        handle.close()
        print("(1) Read the notebook \n(2) Add note \n(3) Empty the notebook \n(4) Quit")

    elif selection == 3:
        handle = open(myfile, "w")
        handle.close()
        print("Notes deleted.")
        print("(1) Read the notebook \n(2) Add note \n(3) Empty the notebook \n(4) Quit")

    elif selection == 4:
        print("Notebook shutting down, thank you.")
        break
    else:
        print("Not a proper selection")
