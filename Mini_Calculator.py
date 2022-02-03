number1 = input("Enter a number.  ")
number2 = input("Enter a number.  ")
operation = input("What operation do you want.  ")

#check the type of operation
if operation == "addition":
    print(int(number1) + int(number2))
elif operation == "substraction":
    print(int(number1) - int(number2))