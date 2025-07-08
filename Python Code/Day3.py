# 1. List and List Methods
# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing list elements
print(f"First fruit: {fruits[0]}")

# Adding elements to the list
fruits.append("orange")
print(f"Fruits after adding an element: {fruits}")

# Removing an element from the list
fruits.remove("banana")
print(f"Fruits after removal: {fruits}")

# Finding the length of the list
print(f"Number of fruits: {len(fruits)}")

# Sorting the list
fruits.sort()
print(f"Sorted fruits: {fruits}")

# 2. Tuple and Tuple Conditions
# Creating a tuple
coordinates = (10, 20, 30)

# Accessing tuple elements
print(f"First coordinate: {coordinates[0]}")

# Check if an element exists in the tuple
if 20 in coordinates:
    print("20 is in the tuple")

# 3. Set and Set Methods
# Creating a set
unique_numbers = {1, 2, 3, 4, 5}

# Adding an element to the set
unique_numbers.add(6)
print(f"Set after adding an element: {unique_numbers}")

# Removing an element from the set
unique_numbers.remove(4)
print(f"Set after removal: {unique_numbers}")

# Check if an element exists in the set
if 3 in unique_numbers:
    print("3 is in the set")

# 4. Dictionary and Dictionary Methods
# Creating a dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}

# Accessing dictionary elements
print(f"Name: {person['name']}")

# Adding a new key-value pair
person["job"] = "Engineer"
print(f"Person after adding job: {person}")

# Removing a key-value pair
del person["city"]
print(f"Person after removing city: {person}")

# Getting a value using the `get()` method
print(f"Age: {person.get('age')}")

# 5. F-String
# Using f-string to format output
name = "Bob"
age = 28
greeting = f"My name is {name} and I am {age} years old."
print(greeting)

# 6. Docstring
# Function with a docstring
def add_numbers(a, b):
    """
    This function takes two numbers as input and returns their sum.
    Parameters:
    a (int, float): The first number.
    b (int, float): The second number.
    
    Returns:
    int, float: The sum of the two numbers.
    """
    return a + b

# Calling the function
result = add_numbers(5, 7)
print(f"Sum of 5 and 7 is: {result}")
