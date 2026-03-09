"""
Create a name picker where the user enters 5 names.
The program selects one randomly and then shuffles the entire list,
showing the new order.
"""
import random

names = []

for i in range(1, 6):
    name = input(f"Enter the {i}º name: ")
    names.append(name)

chosen_index = random.randint(0, len(names) - 1)  # Or random.choice(names)
chosen_name = names[chosen_index]

print(f"Original name list = {names}")
print("=" * 20)
print("Selecting and shuffling names...")
print("=" * 20)
print(f"Chosen name: {chosen_name}")

random.shuffle(names)  # Shuffling after showing the original list
print(f"Shuffled list: {names}")