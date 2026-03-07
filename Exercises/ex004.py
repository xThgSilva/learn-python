"""
Ask numbers until 0 is entered
Store them in a list

Then show:
Sum
Count
Average
Highest
Lowest
"""

numbers = []

while True:
    num = int(input("Enter a number (0 to exit): "))

    if num == 0:
        break

    numbers.append(num)

if len(numbers) == 0:
    print("There are no numbers in the list.")
else:
    print(f"Sum = {sum(numbers)}")
    print(f"Count = {len(numbers)}")
    print(f"Average = {sum(numbers) / len(numbers)}")
    print(f"Lowest number = {min(numbers)}")
    print(f"Highest number = {max(numbers)}")
