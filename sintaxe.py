# How to print in the terminal
print("Printing in the terminal!")

# Declaring variables
name = "Thiago"     # String type ""
age = 18            # Integer type
height = 1.82       # Float type
isActive = True     # Boolean type

# String interpolation using commas
print("Welcome", name, "your age is", age, "years!")

# String interpolation using f-string (format)
print(f"Welcome {name}! Your age is {age} years!")

# Check the type of the data
print(f"{type(name)} | {type(age)} | {type(height)} | {type(isActive)}")

# Receive input from the terminal - always returns a string
carBrand = input("Enter a car brand: ")
print(f"Car entered: {carBrand} | type: {type(carBrand)}")

# Casting to int and float
n1 = int(input("Enter a number: "))
n2 = float(input("Enter another number: "))
print(f"Values: {n1} | {n2}")
print(f"Types: {type(n1)} | {type(n2)}")

# Basic operations
a = 10
b = 20

print(f"Sum: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Integer division: {a // b}")
print(f"Remainder (mod): {a % b}")
print(f"Power: {a ** 2}")
