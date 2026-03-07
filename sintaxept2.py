# If/else conditions
age = int(input("Enter your age: "))

if age >= 18:
    print("Access granted.")
else:
    print("Access denied! You must be of legal age.")

# Logical operators - and | or | not (&& ; || ; !=)
hasDriverLicense = True

if age >= 18 and hasDriverLicense:
    print("You can drive.")
else:
    print("You are not of legal age or you don't have a driver's license.")

# Loop structures
counter = 1

while counter < 10:
    print(f"Count: {counter}")
    counter += 1

# By default, the loop variable (i in this case) starts at 0
for i in range(5):
    print(f"Current loop value of i: {i}")

# Using parameters, range starts at the first (1) and ends before the last (6 - 1)
for i in range(1, 6):
    print(f"Current loop value with parameters: {i}")

# Creating an array (list) - already dynamic
products = ["cellphone", "notebook", "keyboard", "mouse", "mousepad", "power_supply", "fan"]

# Accessing an element of the array - array[index]
print(products[1])  # notebook

# Adding elements to the array
products.append("macbook")
print(products[7])

# Iterating through the array
for product in products:
    print(f"Product name: {product}")

# Iterating through the array and getting the index
for i in range(len(products)):
    print(f"{i + 1}º product = {products[i]}")  # +1 for easier understanding

# Array (list) functions
numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(f"Highest number = {max(numbers)}")
print(f"Lowest number = {min(numbers)}")
print(f"Sum of numbers = {sum(numbers)}")
print(f"Array size (elements) = {len(numbers)}")

# Array (list) manipulation functions
numbers.insert(0, 21)    # Adds number 21 at position 0 (index, value)
print(numbers)

numbers.remove(20)       # Removes the value from the array
print(numbers)

numbers.pop(0)           # Removes the number by index (in this case, the first)
print(numbers)

print(f"Slicing = {numbers[1:5]}")  
# Cuts elements outside the indices, shows numbers from index 1 to final - 1

# Iterating the list with index and value
for i, value in enumerate(numbers):
    print(f"Index: {i} | Value: {value}")

# Creating functions
def function_name(parameter):
    print(parameter)
    # Can return a value using "return x"

function_name("Testing functions")

# Functions with default parameters
def greeting(name, message="Hello"):  # message will be "Hello" if not passed
    return f"{message}, {name}"

print(greeting("User"))
print(greeting("User", "Test"))
