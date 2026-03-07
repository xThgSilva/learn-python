"""
Create a program that:
Keep asking for numbers until the user enters 0
Show the total sum
Show how many numbers were entered
Show the average
"""

total = 0
count = 0
is_active = True

while is_active:
    num = int(input("Enter a number (0 to exit): "))

    if num == 0:
        is_active = False
    else:
        total += num
        count += 1

print("Problem data:")
print(f"Sum = {total}")
print(f"Count = {count}")

if count == 0:
    print("It is not possible to calculate the average.")
else:
    print(f"Average = {total / count}")
