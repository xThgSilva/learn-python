print("=== Random Store ===")

balance = float(input("Enter the amount of money you have: "))

chocolate = 2.50
gum = 1.99
coke = 8.89

print(f"With ${balance}, you can buy:")

print(f"{balance // chocolate} chocolate bars.")
print(f"{balance // gum} gums.")
print(f"{balance // coke} cans of Coca-Cola.")
