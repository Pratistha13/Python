import time
print("(1) Read the notebook \n(2) Add note \n(3) Empty the notebook \n(4) Quit")

myfile = "facts.txt"

while True:
    selection = int(input("Please select one: "))

    if selection == 1:
        handle = open(myfile, "r")
        contents = handle.read()
        timenow = time.strftime("%X %x")
        print(contents.rstrip("\n"), ":::", timenow)
        print("(1) Read the notebook \n(2) Add note \n(3) Empty the notebook \n(4) Quit")

    elif selection == 2:
        handle = open(myfile, "a")
        addition = input("Write a new note: ")
        handle.write(addition + "\n")
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
