num = input("Enter a number: ")
digits = len(num)
s = 0

for digit in num:
    s += int(digit) ** digits

if s == int(num):
    print(num,"is an Armstrong number")
else:
    print(num, "is not an Armstrong number")