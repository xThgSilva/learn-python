"""'
Contagem simples
- Crie uma função que:
- Receba um número n
- Retorne uma lista de 0 até n (inclusive)
"""
def contar(num):
    contagem = []
    for num in range(0, num + 1, 1):    # Vai começar do 0 e ir até número que defini, usando +1, indo de 1 em 1 por vez
        contagem.append(num)

    return contagem

contador = int(input("Digite um número final para contagem: "))
print(f"Contagem:\n {contar(contador)}")
