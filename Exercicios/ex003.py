"""
Modifique seu programa para também mostrar:
Maior número digitado
Menor número digitado
"""
maior = None
menor = None

while True:
    num = int(input("Digite um número (0 para sair): "))

    if num == 0:
        break

    if maior is None:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print("Dados do problema:")
print(f"Maior número = {maior}")
print(f"Menor número = {menor}")
