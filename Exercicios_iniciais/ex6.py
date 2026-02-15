print("=== Loja qualquer ===")
saldo = float(input("Informe a quantia de dinheiro que possui: "))

chocolate = 2.50
chiclete = 1.99
coca = 8.89

print(f"Com R${saldo} reais, você consegue comprar:")
print(f"{saldo // chocolate} barras de chocolate.")
print(f"{saldo // chiclete} chicletes.")
print(f"{saldo // coca} latas de coca-cola.")