"""
Versão Lista - Refaça aquele exercício de:
- Pedir números até digitar 0
- Guardar numa lista

Depois mostrar:
- Soma
- Quantidade
- Média
- Maior
- Menor
Agora usando lista + funções prontas.
"""
numeros = []

while True:
    num = int(input("Informe um número (0 para sair): "))

    if num == 0:
        break

    numeros.append(num)

if len(numeros) == 0:
        print("Não há números na lista suficientes para mostras os dados.")

else:
        print(f"Soma do array = {sum(numeros)}")
        print(f"Quantidade dos elementos do array = {len(numeros)}")
        print(f"Média do array = {sum(numeros) / len(numeros)}")
        print(f"Menor número do array = {min(numeros)}")
    