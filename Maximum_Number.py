def Maximum_Number(number_1, number_2, number_3):

    if number_1 > number_2 and number_1 > number_3:
        print(number_1, "is the greatest number.")

    elif number_2 > number_1 and number_2 > number_3:
        print(f"{number_2} is the greatest number.")

    elif number_3 > number_1 and number_3 > number_2:
        print(f"{number_3} is the greatest number.")

    else:
        print("Please input different numbers")

a = int(input("Enter a number:  "))
b = int(input("Enter another number:  "))
c = int(input("Enter another number:  "))

Maximum_Number(a, b, c)
