"""'
Cria uma função que:
- Receba uma lista
- Retorne o maior número da lista
- Sem usar max()
"""
numeros = [3, 7, 2, 9, 5]
def maiorNumeroDaLista(array):
    maior = array[0]

    for num in array:
        if num > maior:
            maior = num
    
    return maior

print(f"Maior número da lista: {maiorNumeroDaLista(numeros)}")
