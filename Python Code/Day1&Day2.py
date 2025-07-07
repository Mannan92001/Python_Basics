# 1. Variables
# Assigning values to variables of different types
name = "John"  # String
age = 30  # Integer
height = 5.9  # Float
is_employed = True  # Boolean

print(name, age, height, is_employed)

# 2. Strings
# Concatenation of strings
greeting = "Hello"
message = greeting + " " + name
print(message)

# String formatting using f-strings
print(f"Hi, my name is {name} and I am {age} years old.")

# 3. If-Else and Elif Conditions
# Checking if a number is positive, negative, or zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

# 4. For Loop
# Print all numbers from 1 to 5
for i in range(1, 6):
    print(i)

# Print all even numbers between 1 and 10
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# 5. While Loop
# Printing numbers from 1 to 5 using a while loop
i = 1
while i <= 5:
    print(i)
    i += 1

# 6. Use Case Method - Checking Divisibility by 3 and 5
# Checking divisibility of a number by both 3 and 5
num = int(input("Enter a number to check divisibility: "))
if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is divisible by both 3 and 5")
elif num % 3 == 0:
    print(f"{num} is divisible by 3")
elif num % 5 == 0:
    print(f"{num} is divisible by 5")
else:
    print(f"{num} is not divisible by 3 or 5")

# 7. Functions
# Define a simple function
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# Function with a return value (sum of two numbers)
def add_numbers(a, b):
    return a + b

sum_result = add_numbers(5, 7)
print(f"Sum: {sum_result}")

# 8. Methods of Functions
# Function with default arguments
def multiply(a, b=2):  # Default value of b is 2
    return a * b

result1 = multiply(5)
result2 = multiply(5, 3)
print(f"Multiplying 5 by default 2: {result1}")
print(f"Multiplying 5 by 3: {result2}")
