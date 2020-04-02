print("Calculator")

options = True
while True:

    if options:
        firstnumber = int(input("Give the first number: "))
        secondnumber = int(input("Give the second number: "))

        options = False

    print("(1) +\n(2) -\n(3) *\n(4) /\n(5)Change numbers\n(6)Quit")
    print("Current numbers: ", firstnumber, secondnumber)


    select = int(input("Please select something (1-6): "))

    if select == 1:
        sum = firstnumber + secondnumber
        print("The result is: ", sum)

    elif select == 2:
        sub = firstnumber - secondnumber
        print("The result is: ", sub)

    elif select == 3:
        mul = firstnumber * secondnumber
        print("The result is: ", mul)

    elif select == 4:
        div = firstnumber / secondnumber
        print("The result is: ", div)

    elif select == 6:
        print("Thank you!")
        break

    elif select == 5:
        options =True

    else:
        print("Nothing to show")

