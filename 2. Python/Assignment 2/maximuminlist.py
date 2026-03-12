# maximum in list

numbers = [10, 20, 5, 30, 15]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print("Maximum number in the list is:", max_num)