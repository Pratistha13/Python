import math

print("Calculator")
def calculator():
    while True:
        try:
            number = int(input("Give a number"))
            return number
        except(TypeError, ValueError):
            print("This input is invalid.")


options = True
while True:

    if options:
        firstnumber = calculator()
        secondnumber = calculator()

        options = False

    print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(number1/number2)\n(6)cos(number1/number2)\n(7)Change numbers\n(8)Quit")
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

    elif select == 5:
        print("The result is: ", math.sin(firstnumber / secondnumber))

    elif select == 6:
        print("The result is: ", math.cos(firstnumber / secondnumber))

    elif select == 8:
        print("Thank you!")
        break

    elif select == 7:
        options = True

    else:
        print("Nothing to show")

