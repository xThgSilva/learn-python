"""
Create a function that:
Receives a number and returns:
- The square root
- The number squared
- The number rounded up
- The number rounded down
You must use methods from the math library
"""
import math

num = float(input("Enter a number: "))
print("=" * 20)
print("Performing calculations...")
print("=" * 20)
print(f"Square root = {math.sqrt(num)}")
print(f"Number squared = {math.pow(num, 2)}")
print(f"Rounded up = {math.ceil(num)}")
print(f"Rounded down = {math.floor(num)}")
