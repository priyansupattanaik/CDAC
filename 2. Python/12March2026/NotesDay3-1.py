# %% [markdown]
# # Functions in Python
# 
# ## What is a Function?
# - A function is a named, reusable block of code that performs a specific task
# - It helps to avoid repetition of code
# - It organizes programs in a better manner
# - It makes debugging easier
# - It reuses logic whenever needed
# 
# ## Syntax:
# ```python
# def function_name(parameters):
#     # code to be executed
#     return value
# ```

# %% [markdown]
# ## Basic Function Example

# %%
def add(a, b):
    return a + b

result = add(2, 3)
print("Addition result:", result)  # Output: Addition result: 5

# %% [markdown]
# # Types of Arguments in Functions
# 
# 1. **Positional Arguments**
# 2. **Keyword Arguments**
# 3. **Default Arguments**
# 4. **Variable Length Arguments**

# %% [markdown]
# ## 1. Positional Arguments
# - The order of parameters is important
# - Values are assigned according to their position

# %%
def sub(a, b):
    print(f"{a} - {b} = {a - b}")

print("Positional Arguments:")
sub(10, 5)   # Output: 10 - 5 = 5
sub(5, 10)   # Output: 5 - 10 = -5

# %% [markdown]
# ## 2. Keyword Arguments
# - Arguments are identified by parameter names
# - Order doesn't matter when using keywords

# %%
def sub(a, b):
    print(f"{a} - {b} = {a - b}")

print("Keyword Arguments:")
sub(a=10, b=5)   # Output: 10 - 5 = 5
sub(b=10, a=5)   # Output: 5 - 10 = -5

# %% [markdown]
# ## 3. Default Arguments
# - Parameters that have pre-assigned values
# - If caller doesn't provide a value, the default is used

# %%
def greet(name="Guest"):
    print(f"Hello, {name}!")

print("Default Arguments:")
greet("Alice")    # Output: Hello, Alice!
greet()           # Output: Hello, Guest!

# %% [markdown]
# ## 4. Variable Length Arguments (*args)
# - Used when the number of arguments is not known in advance
# - `*args` collects multiple values into a tuple

# %%
def sum_all(*numbers):
    """Calculate sum of all numbers passed as arguments"""
    total = 0
    for num in numbers:
        total += num
    print(f"Sum of {numbers} = {total}")

print("Variable Length Arguments:")
sum_all(1, 2, 3)           # Output: Sum of (1, 2, 3) = 6
sum_all(4, 50, 6, 7)       # Output: Sum of (4, 50, 6, 7) = 67
sum_all(10, 20, 30, 40, 50) # Output: Sum of (10, 20, 30, 40, 50) = 150

# %% [markdown]
# # Return Statement
# 
# The `return` statement is used to send a value back from a function:
# - Can return a single value
# - Can return multiple values (as a tuple)
# - Returns `None` if no return statement is specified

# %%
# Example 1: Returning a single value
def square(a):
    return a * a

x = square(5)
print(f"Square of 5: {x}")           # Output: Square of 5: 25
print(f"Square of 7: {square(7)}")    # Output: Square of 7: 49

# %%
# Example 2: Returning multiple values
def calculate(a, b):
    """Returns sum, difference, and product"""
    return a + b, a - b, a * b

# Unpacking returned values
sum_val, diff_val, prod_val = calculate(10, 5)
print(f"For numbers 10 and 5:")
print(f"Sum: {sum_val}")        # Output: Sum: 15
print(f"Difference: {diff_val}") # Output: Difference: 5
print(f"Product: {prod_val}")    # Output: Product: 50

# %%
# Example 3: Function with no return (returns None)
def display_message(msg):
    print(msg)
    # No return statement

result = display_message("Hello World")
print(f"Return value: {result}")  # Output: Return value: None

# %% [markdown]
# # Recursive Functions
# 
# A recursive function is a function that calls itself:
# - Useful for problems that can be broken into smaller versions of the same problem
# - **Must have a base condition** to stop recursion
# - Without a base condition, recursion continues infinitely (causing RecursionError)

# %%
# Example 1: Factorial using recursion
def factorial(n):
    """Calculate factorial using recursion"""
    # Base condition
    if n == 0:
        return 1
    # Recursive call
    return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")     # Output: Factorial of 5: 120
print(f"Factorial of 0: {factorial(0)}")     # Output: Factorial of 0: 1
print(f"Factorial of 3: {factorial(3)}")     # Output: Factorial of 3: 6

# %%
# Example 2: Fibonacci sequence using recursion
def fibonacci(n):
    """Return nth Fibonacci number"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("First 10 Fibonacci numbers:")
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}", end="  ")
# Output: F(0)=0  F(1)=1  F(2)=1  F(3)=2  F(4)=3  F(5)=5  F(6)=8  F(7)=13  F(8)=21  F(9)=34

# %%
# Example 3: Infinite recursion (DANGER - will cause error)
def infinite_recursion():
    """This function will cause RecursionError"""
    return infinite_recursion()

# Uncomment the line below to see RecursionError
# infinite_recursion()  # RecursionError: maximum recursion depth exceeded

# %% [markdown]
# # Lambda Functions
# 
# Lambda functions are small, anonymous functions:
# - Anonymous meaning they don't require a function name
# - Generally written in one line
# - Very useful for short operations
# 
# **Syntax:**
# ```python
# lambda arguments: expression
# ```

# %%
# Example 1: Basic lambda function
square_lambda = lambda n: n * n
print(f"Square of 5 using lambda: {square_lambda(5)}")  # Output: Square of 5 using lambda: 25

# %%
# Example 2: Lambda with multiple arguments
add_lambda = lambda a, b: a + b
print(f"Addition using lambda: {add_lambda(10, 5)}")    # Output: Addition using lambda: 15

# %%
# Example 3: Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]

# Using lambda with map
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Squared numbers: {squared_numbers}")  # Output: Squared numbers: [1, 4, 9, 16, 25]

# Using lambda with filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")        # Output: Even numbers: [2, 4]

# %%
# Example 4: Lambda without assigning to variable
print(f"Direct lambda call: {(lambda x, y: x * y)(6, 7)}")  # Output: Direct lambda call: 42

# %% [markdown]
# # Summary of Function Types

# %%
print("=" * 50)
print("FUNCTION TYPES SUMMARY")
print("=" * 50)

# Regular function
def regular_func(x):
    return x * 2

# Lambda function
lambda_func = lambda x: x * 2

print(f"Regular function: {regular_func(5)}")
print(f"Lambda function: {lambda_func(5)}")

# Function with default args
def power(base, exponent=2):
    return base ** exponent

print(f"Power with default: {power(4)}")      # 4^2 = 16
print(f"Power with args: {power(4, 3)}")      # 4^3 = 64

# Function with variable args
def multiply_all(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(f"Multiplication: {multiply_all(2, 3, 4)}")  # 2*3*4 = 24