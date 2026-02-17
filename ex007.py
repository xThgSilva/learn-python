"""
Crie uma função que:
- Recebe uma lista
- Retorna a soma dos elementos
- Sem usar sum()
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def somaLista(array):
    soma = 0

    for num in array:
        soma += num

    return soma

print(f"Lista: {numeros}")
print(f"Soma dos elementos: {somaLista(numeros)}")
