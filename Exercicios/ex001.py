"""
Exercício nível iniciante/intermediário

Faça um programa que:
Peça um número
Mostre a tabuada dele de 1 até 10
"""

num = int(input("Digite um número para a tabuada: "))

for i in range(1, 11):
    print(f"{num} x {i} = {i * num}")
