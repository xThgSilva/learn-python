"""
Ask numbers and store them in a list

Show:
Original list
Highest number (without max)
Lowest number (without min)
"""

numbers = []

while True:
    number = int(input("Enter a number (0 to exit): "))

    if number == 0:
        break
    else:
        numbers.append(number)

if len(numbers) == 0:
    print("There are no numbers in the list.")
else:
    highest = numbers[0]
    lowest = numbers[0]

    for i in range(len(numbers)):
        if highest < numbers[i]:
            highest = numbers[i]
        if lowest > numbers[i]:
            lowest = numbers[i]

    reversed_list = []

    for i in range(len(numbers) - 1, -1, -1):
        reversed_list.append(numbers[i])

print("Problem data:")
print(f"Full list:\n{numbers}")
print(f"Reversed list:\n{reversed_list}")
print(f"Highest number = {highest}")
print(f"Lowest number = {lowest}")
