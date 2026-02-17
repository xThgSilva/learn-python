"""
Parte 1
Crie uma função que:
- Receba uma lista
- Retorne o maior e o menor número
- A soma
- A media
- Sem usar max(), min(), sum() ou media()
"""
numeros = [3, 7, 2, 9, 5]
def analisarLista(array):
    if len(array) == 0:
        print("A lista é inválida")
        return None, None, None, None
    
    else:
        maior = array[0]
        menor = array[0]
        soma = 0

        for num in array:
            soma += num

            if num > maior:
                maior = num
            if num < menor:
                menor = num
        
        media = soma / len(array)
        return maior, menor, soma, media

maior, menor, soma, media = analisarLista(numeros)
print("Dados do problemma:")
print(f"Lista: {numeros}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
print(f"Soma da lista: {soma}")
print(f"Média da lista: {media}")
