num_terms = int(input("Enter number of terms: "))
a, b = 0, 1

for _ in range(num_terms):
    print(a, end=" ")
    a, b = b, a + b