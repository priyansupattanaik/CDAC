n = 5
for i in range(1, n + 1):
    if i <= (n + 1) // 2:
        print(" " * (i - 1) + "*" * (n - i + 1))
    else:
        print(" " * (n - i) + "*" * (i))