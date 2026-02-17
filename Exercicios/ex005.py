"""
- Faça um programa que:
- Peça 5 números
- Guarde numa lista

Mostre:
- A lista original
- O maior número (sem usar max)
- O menor número (sem usar min)
"""
numeros = []

while True:
    numero = int(input("Digite um número (0 para sair): "))

    if numero == 0:
        break
    else:
        numeros.append(numero)

if len(numeros) == 0:
    print("Não há números na lista.")
else:
    maior = numeros[0]
    menor = numeros[0]

    for i in range(len(numeros)):
        if maior < numeros[i]:
            maior = numeros[i]
        if menor > numeros[i]:
            menor = numeros[i]

    invertida = []
    for i in range(len(numeros) - 1, - 1, -1):
        invertida.append(numeros[i])

print("Dados do problema:")
print(f"Lista completa:\n{numeros}")
print(f"Lista invertida:\n{invertida}")
print(f"Maior número = {maior}")
print(f"Menor número = {menor}")
