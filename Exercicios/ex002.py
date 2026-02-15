"""
Faça um programa que:
Continue pedindo números até o usuário digitar 0
Mostre a soma total dos números digitados
Mostre quantos números foram digitados
Mostre a média
"""

soma = 0
quantidade = 0
isActive = True

while isActive:
    num = int(input("Digite um número (0 para sair)"))

    if num == 0:
        isActive = False
    else:
        soma += num
        quantidade += 1

print("Dados do problema:")
print(f"Soma = {soma}")
print(f"Quantidade = {quantidade}")
if quantidade == 0:
    print("Não é possível calcular a média.")
else:
    print(f"Média = {soma / quantidade}")