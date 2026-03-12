num_str = input("Enter number: ")

if num_str == num_str[::-1]:
    print(f"{num_str} is Palindrome")
else:
    print(f"{num_str} is not Palindrome")