num_1 = int(input("Enter a number:  "))
num_3 = 0
while num_1 > 0:
    num_2 = num_1 % 10
    print(num_2,end = "")
    num_1 = num_1 // 10
    num_3 = num_3 + num_2
    print(" ",num_2**3)
print("   ")
print(num_3)

