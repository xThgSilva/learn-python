import math

a = int(input("Enter coefficient A: "))
b = int(input("Enter coefficient B: "))
c = int(input("Enter coefficient C: "))


def calculate_discriminant(a, b, c):
    return b * b - 4 * a * c


def first_root(a, b, c):
    discriminant = calculate_discriminant(a, b, c)
    return (-b + math.sqrt(discriminant)) / (2 * a)


def second_root(a, b, c):
    discriminant = calculate_discriminant(a, b, c)
    return (-b - math.sqrt(discriminant)) / (2 * a)


print("=" * 20)
print("Equation result")
print("=" * 20)

delta = calculate_discriminant(a, b, c)
print(f"Discriminant = {delta}")

if delta < 0:
    print("The equation has no real roots.")
else:
    print(f"First root = {first_root(a, b, c)}")
    print(f"Second root = {second_root(a, b, c)}")