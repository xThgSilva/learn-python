"""
Função acumuladora
- Crie uma função que:
- Receba dois números: inicio e fim
- Retorne a soma de todos os números entre eles (inclusive)
"""
def somaIntervalo(inicio, fim):
    soma = 0
    for num in range(inicio, fim + 1):
        soma += num

    return soma

inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))
print(f"A soma em sequência de {inicio} a {fim} é = {somaIntervalo(inicio, fim)}")
