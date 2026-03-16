n = 7
for i in range(1, n + 1):
    if i <= (n + 1) // 2:
        print("*" * i + " " * (n - 2 * i) + "*" * i)
    else:
        print("*" * (n - i + 1) + " " * (2 * i - n - 2) + "*" * (n - i + 1))