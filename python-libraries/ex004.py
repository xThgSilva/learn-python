"""
Create a list with 10 random numbers between 1 and 100 and then display:
- The largest number
- The smallest number
- Their average
"""
import random

numbers = []

for i in range(1, 11):
    numbers.append(random.randint(1, 100))

largest_number = numbers[0]
smallest_number = numbers[0]
total = 0

for number in numbers:
    if number > largest_number:
        largest_number = number
    elif number < smallest_number:
        smallest_number = number

    total += number

print(f"List = {numbers}")
print("=" * 20)
print("Displaying data...")
print("=" * 20)
print(f"Largest number = {largest_number}")
print(f"Smallest number = {smallest_number}")
print(f"Sum = {total}")
print(f"Average = {total / len(numbers)}")
