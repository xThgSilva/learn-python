"""
Apenas pares no intervalo
Crie uma função que:
- Receba inicio e fim
- Retorne apenas os números pares nesse intervalo (inclusive)
"""
def paresNoIntervalo(inicio, fim):
    numerosPares = []
    for num in range(inicio, fim + 1, 1):   # Vai começar pelo "inicio", e terminar no "fim" escolhido, de 2 em 2, mostrando apenas os pares
        if num % 2 == 0:
            numerosPares.append(num)

    return numerosPares

inicio = int(input("Digite um número para o inicio: "))
fim = int(input("Digite um número para o final: "))
print(paresNoIntervalo(inicio, fim))

""" - Função para que funcione ao contrário também
def paresNoIntervalo(inicio, fim):
    numerosPares = []

    if inicio <= fim:
        for num in range(inicio, fim + 1):
            if num % 2 == 0:
                numerosPares.append(num)
    else:
        for num in range(inicio, fim - 1, -1):
            if num % 2 == 0:
                numerosPares.append(num)

    return numerosPares
"""