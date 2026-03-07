"""
Modify the program to also show:
Highest number entered
Lowest number entered
"""

highest = None
lowest = None

while True:
    num = int(input("Enter a number (0 to exit): "))

    if num == 0:
        break

    if highest is None:
        highest = num
        lowest = num
    else:
        if num > highest:
            highest = num
        if num < lowest:
            lowest = num

print("Problem data:")
print(f"Highest number = {highest}")
print(f"Lowest number = {lowest}")
