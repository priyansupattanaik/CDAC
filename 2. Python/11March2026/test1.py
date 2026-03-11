nums = [10, 20 , 30 ,40, 50]

print(20 in nums)
print(60 in nums)
print(20 not in nums)
print(60 not in nums)

text = "Hello, World!"
print("Hello" in text)
print("Python" in text)
print("Hello" not in text)

#Identity operators
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is y)  # True, because x and y refer to the same object
print(x is z)  # False, because x and z refer to different objects