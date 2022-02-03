input_list = [12, 63, 84, 71, 31, 162, 6]
largest_number = 0
for number in input_list:
    print(number)
    if largest_number < number:
        largest_number = number
print(f"The largest number is {largest_number}.")