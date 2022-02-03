def Pascal_Triangle(n):
    num1 = [1]
    num2 = [0]
    for number in range(n):
        print(num1)

        num1 = [l + r for l,r in zip(num1 + num2, num2 + num1)]
numeral = int(input("Enter a number of rows:  "))

Pascal_Triangle(numeral)