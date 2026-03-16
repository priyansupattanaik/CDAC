n = 5

for i in range(1, n + 1):
    if i % 2 != 0:  # odd row
        start = 1
    else:           # even row
        start = 0
    
    for j in range(i):
        if j % 2 == 0:
            print(start, end="")
        else:
            print(1 - start, end="")
    print()