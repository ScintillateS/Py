input_list = [12, 63, 84, 71, 31, 162, 6]
smallest_number = 10000
for number in input_list:
    print(number)
    if smallest_number > number:
        smallest_number = number
print(smallest_number)