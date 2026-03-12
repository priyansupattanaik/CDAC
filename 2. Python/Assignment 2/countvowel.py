str = input("Enter a word: ")
vowels = "aeiouAEIOU"
count = 0

for char in str:
    if char in vowels:
        count += 1

print(f"Number of vowels = {count}")