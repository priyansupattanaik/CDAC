num = int(input("Enter number: "))

sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    num = num // 10

print(f"Sum of digits = {sum_digits}")