"""
Beginner / intermediate exercise

Create a program that:
Ask for a number
Show its multiplication table from 1 to 10
"""

num = int(input("Enter a number for the multiplication table: "))

for i in range(1, 11):
    print(f"{num} x {i} = {i * num}")
    