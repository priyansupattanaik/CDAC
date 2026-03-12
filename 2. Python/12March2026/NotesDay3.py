# %% [markdown]
# # Python Dictionaries (key:value pairs)

# %% [markdown]
# ## Basic Dictionary Creation

# %%
# Creating a dictionary
student = {"name": "Amit", "addr": "mumbai", "course": "AI"}
print(student)  # Output: {'name': 'Amit', 'addr': 'mumbai', 'course': 'AI'}

# Accessing values using keys
print(student["name"])  # Output: Amit

# %% [markdown]
# ## Valid Dictionary Keys
# - Allowed: int, float, str, tuple, frozenset
# - Not Allowed: list, set, dictionary (mutable types)

# %%
# This will raise TypeError: unhashable type: 'list'
# d = {[1,2]: "a"}  # Uncomment to see error

# Valid key types
valid_dict = {
    1: "integer key",
    3.14: "float key",
    "name": "string key",
    (1, 2): "tuple key"
}
print(valid_dict)
# Output: {1: 'integer key', 3.14: 'float key', 'name': 'string key', (1, 2): 'tuple key'}

# %% [markdown]
# ## Dictionary Constructor - dict()

# %%
# Creating dictionary from list of tuples
d = dict([("a", 1), ("b", 2), ("c", 3)])
print("From list of tuples:", d)  # Output: From list of tuples: {'a': 1, 'b': 2, 'c': 3}

# %% [markdown]
# ## Using zip() to Create Dictionary

# %%
key = ["id", "name", "addr"]
values = ["s1", "Amit", "mumbai"]
d = dict(zip(key, values))
print("Dictionary from zip:", d)  # Output: Dictionary from zip: {'id': 's1', 'name': 'Amit', 'addr': 'mumbai'}

# %% [markdown]
# ## Accessing Dictionary Values

# %%
student = {"name": "Amit", "addr": "mumbai", "course": "AI"}

# Using square brackets (raises KeyError if key doesn't exist)
print("Using []:", student["name"])  # Output: Using []: Amit
# print(student["age"])  # Uncomment to see KeyError

# Using get() method (returns None if key doesn't exist)
print("Using get():", student.get("name"))  # Output: Using get(): Amit
print("Using get() for missing key:", student.get("age"))  # Output: Using get() for missing key: None

# %% [markdown]
# ## Default Values with get()

# %%
student = {"name": "Amit", "addr": "mumbai", "course": "AI"}

# Providing default value if key not found
print("With default value:", student.get("age", "Not Found"))  # Output: With default value: Not Found

# %% [markdown]
# ## Modifying Dictionary Values

# %%
# Direct assignment
student = {"name": "Amit", "addr": "mumbai", "course": "AI"}
print("Original:", student)  # Output: Original: {'name': 'Amit', 'addr': 'mumbai', 'course': 'AI'}

student["name"] = "Rohit"
print("Modified:", student)  # Output: Modified: {'name': 'Rohit', 'addr': 'mumbai', 'course': 'AI'}

# %% [markdown]
# ## Using update() Method

# %%
student = {"name": "Amit", "addr": "mumbai", "course": "AI"}
print("Before update:", student)  # Output: Before update: {'name': 'Amit', 'addr': 'mumbai', 'course': 'AI'}

student.update({"name": "Ravi"})
print("After update:", student)  # Output: After update: {'name': 'Ravi', 'addr': 'mumbai', 'course': 'AI'}

# %% [markdown]
# ## Key Methods Summary
# - `dict[key]` - Access value (raises KeyError if missing)
# - `dict.get(key, default)` - Access value (returns default if missing)
# - `dict.update(other_dict)` - Update multiple keys
# - `dict[key] = value` - Add or modify single key

# %%
student = {"name": "Amit", "addr": "mumbai", "course": "AI"}
student.pop("name")
print(student)  # Output: {'addr': 'mumbai', 'course': 'AI'}

# %%
student = {"name": "Amit", "addr": "mumbai", "course": "AI"}
x = student.pop("addr")
print(x)  # Output: mumbai

# %%
student = {"name": "Amit", "addr": "mumbai", "course": "AI"}
student.popitem()
print(student)  # Output: {'name': 'Amit', 'addr': 'mumbai'}  # Removes last inserted item

# %%
student.clear()
print(student)  # Output: {}  # Empty dictionary

# %%
student = {"name": "Amit", "addr": "mumbai", "course": "AI"}
del student["name"]
print(student)  # Output: {'addr': 'mumbai', 'course': 'AI'}

# %%
student = {"name": "Amit", "addr": "mumbai", "course": "AI"}
print(student.keys())    # Output: dict_keys(['name', 'addr', 'course'])
print(student.values())  # Output: dict_values(['Amit', 'mumbai', 'AI'])
print(student.items())   # Output: dict_items([('name', 'Amit'), ('addr', 'mumbai'), ('course', 'AI')])

# %%
student = {"name": "Amit", "addr": "mumbai", "course": "AI"}

# Iterating through keys
for k in student:
    print(k)  # Output: name, addr, course

# Iterating through values
for v in student.values():
    print(v)  # Output: Amit, mumbai, AI

# Iterating through key-value pairs
for item in student.items():
    print(item)  # Output: ('name', 'Amit'), ('addr', 'mumbai'), ('course', 'AI')

# %%
# Shallow copy
s = {"name": "Amit", "addr": "mumbai", "course": "AI"}
s1 = s.copy()
s1["name"] = "Rohit"
print(s)   # Output: {'name': 'Amit', 'addr': 'mumbai', 'course': 'AI'}
print(s1)  # Output: {'name': 'Rohit', 'addr': 'mumbai', 'course': 'AI'}
print(id(s), id(s1))  # Output: Different IDs

# %%
# Reference assignment (not a copy)
s = {"name": "Amit", "addr": "mumbai", "course": "AI"}
s1 = s
print(s)   # Output: {'name': 'Amit', 'addr': 'mumbai', 'course': 'AI'}
print(s1)  # Output: {'name': 'Amit', 'addr': 'mumbai', 'course': 'AI'}
print(id(s), id(s1))  # Output: Same IDs

# %% [markdown]
# ## TEST

# %%
s = {"Amit": 80, "Sneha": 90, "Raj": 60, "Ravi": 85}

# Access value
print(s["Raj"])  # Output: 60

# Update with new key
s.update({"Rani": 65})
print(s)  # Output: {'Amit': 80, 'Sneha': 90, 'Raj': 60, 'Ravi': 85, 'Rani': 65}

# Update existing key
s.update({"Raj": 75})
print(s)  # Output: {'Amit': 80, 'Sneha': 90, 'Raj': 75, 'Ravi': 85, 'Rani': 65}

# Pop a key
print(s.pop("Ravi"))  # Output: 85
print(s)  # Output: {'Amit': 80, 'Sneha': 90, 'Raj': 75, 'Rani': 65}

# Pop last item
print(s.popitem())  # Output: ('Rani', 65) or last item
print(s)  # Output: {'Amit': 80, 'Sneha': 90, 'Raj': 75}

# %% [markdown]
# # Search

# %%
name = input("Enter name: ")
if name in s:
    print("MARKS:", s[name])
else:
    print("Student not found")

# %% [markdown]
# # Dictionary Operations

# %%
# Highest marks
highest = max(s, key=s.get)
print("Highest marks student:", highest)
print("Marks =", s[highest])

# %%
# Total count of students
print("Total students:", len(s))

# %%
# Average marks
print("Average marks:", sum(s.values()) / len(s))

# %%
# Display students above 80 score
print("Students with marks above 80:")
for student, marks in s.items():
    if marks > 80:
        print(student, ":", marks)

# %% [markdown]
# # List Operations

# %%
n = [12, 45, 67, 23, 89, 34, 38, 90, 34, 19, 34, 56, 78, 90, 23, 45]

# Find the largest number
largest = n[0]
for num in n:
    if num > largest:
        largest = num
print("The largest number is:", largest)  # Output: The largest number is: 90

# Find number of even numbers
count = 0
for num in n:
    if num % 2 == 0:
        count += 1
print("Total even numbers:", count)  # Output: Total even numbers: 9

# Find unique numbers
unique = []
for num in n:
    if num not in unique:
        unique.append(num)
print("Unique numbers:", unique)
# Output: Unique numbers: [12, 45, 67, 23, 89, 34, 38, 90, 19, 56, 78]

# Reverse a list using slicing
reversed_list = n[::-1]
print("Reversed list:", reversed_list)

# %%
# Reverse a list without using reverse() method
reversed_list = []
for i in range(len(n) - 1, -1, -1):
    reversed_list.append(n[i])
print("Reversed list:", reversed_list)

# %%
# Calculate sum of numbers
total = 0
for num in n:
    total += num
print("Sum of all numbers:", total)  # Output: Sum of all numbers: 759

# %%
# Second largest number
largest = n[0]
second_largest = n[0]
for num in n:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print("The second largest number is:", second_largest)  # Output: The second largest number is: 89

# %%
# Segregate positive, negative, and zero numbers
numbers = [12, -45, 0, 23, -89, 34, 38, 0, 34, 19, -34, 56, -78, 90, 23, -45]
positive = []
negative = []
zero = []

for num in numbers:
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)
    else:
        zero.append(num)

print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zero numbers:", zero)

# %% [markdown]
# # Set Operations

# %%
# Creating a set
s = {10, 20, 30, 40, 50}
print(s)  # Output: {40, 10, 50, 20, 30} (order may vary)

# %%
# Creating set from list
s = set([1, 2, 3, 4])
print(s)  # Output: {1, 2, 3, 4}

# Adding elements
s.add(5)
print(s)  # Output: {1, 2, 3, 4, 5}

s.add(3)  # Duplicate - no change
print(s)  # Output: {1, 2, 3, 4, 5}

# Update with multiple elements
s.update([6, 7, 8])
print(s)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Update with duplicates
s.update([3, 4, 5])
print(s)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Remove elements
s.remove(3)
print(s)  # Output: {1, 2, 4, 5, 6, 7, 8}

# Discard (no error if element doesn't exist)
s.discard(10)
print(s)  # Output: {1, 2, 4, 5, 6, 7, 8}

# Pop random element
s.pop()
print(s)  # Output: Some random element removed

# Set operations
s1 = {10, 20, 30}
s2 = {30, 40, 50}

print("Union:", s1.union(s2))                    # Output: {10, 20, 30, 40, 50}
print("Intersection:", s1.intersection(s2))      # Output: {30}
print("Difference (s1 - s2):", s1.difference(s2))  # Output: {10, 20}
print("Symmetric difference:", s1.symmetric_difference(s2))  # Output: {10, 20, 40, 50}