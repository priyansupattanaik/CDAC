str = input("Enter a string: ")
if str == str[::-1]:
    print(f"{str} is Palindrome")
else:
    print(f"{str} is not Palindrome")