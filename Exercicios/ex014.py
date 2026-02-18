"""'
Contagem regressiva
- Crie uma função que:
- Receba um número n
- Retorne uma lista de n até 0
"""
def contagemRegressiva(num):
    contagem = []
    for num in range(num, -1, -1):  # Vai começar de num, indo até 0, diminuindo 1 a cada vez
        contagem.append(num)

    return contagem

contador = int(input("Digite um número para regressiva: "))
print(f"Contagem:\n{contagemRegressiva(contador)}")
