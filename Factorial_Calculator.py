numeral = int(input("Enter any positive number:  "))
factorial = 0 + 1
def Calculator(factorial):
    if numeral < 0:
        print("Sorry, use a positive number.")

    elif numeral == 0:
        print("The factorial is 1")

    else:
        for n in range(1,numeral + 1):
            factorial = factorial * n
        print(f"The factorial of {numeral} is {factorial} .")


Calculator(factorial)