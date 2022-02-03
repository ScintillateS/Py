numeral_1 = input("Enter a number:  ")
numeral_2 = input("Enter another smaller number:  ")
numeral_3 = input("Enter another larger number:  ")

def Range(numeral_1, numeral_2, numeral_3):
    if numeral_3 < numeral_1:
        print("Enter a larger number.")
    elif numeral_2 > numeral_1:
        print("Enter a smaller number.")

    elif numeral_1 > numeral_2 and numeral_1 < numeral_3:
        print("Your number is in range.")

    elif numeral_3 == numeral_1 == numeral_2:
        print("Enter different numbers.")
Range(numeral_1, numeral_2, numeral_3)



