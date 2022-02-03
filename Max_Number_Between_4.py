def Max_Number_Between_4(nums):
    maximum = nums[0]
    for n in nums:
        if n > maximum:
            maximum = n
    print(maximum)

num_list = [ ]
for num in range(0, 4):
    numeral = int(input("Enter a number:  "))
    num_list.append(numeral)
print(num_list)

Max_Number_Between_4(num_list)
