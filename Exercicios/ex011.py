"""
Crie uma função que:
Receba um número e retorne:
- "positivo" se for maior que 0
- "negativo" se for menor que 0
- "zero" se for 0
"""
def classificaNumero(num):
    message = None
    if num > 0:
        message = f"{num} é positivo"
    elif num < 0:
        message = f"{num} é negatvo"
    else:
        message = f"{num} é apenas zero"

    return message

print(classificaNumero(10))
print(classificaNumero(-10))
print(classificaNumero(0))
