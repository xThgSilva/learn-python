import math

a = int(input("Informe o coeficiente A: "))
b = int(input("Informe o coeficiente B: "))
c = int(input("Informe o coeficiente C: "))

def calcDeterminante(a, b, c):
    return b*b - 4*a*c

def primeiraRaiz(a, b, c):
    determinante = calcDeterminante(a, b, c)
    return (-b + math.sqrt(determinante)) / (2*a)

def segundaRaiz(a, b, c):
    determinante = calcDeterminante(a, b, c)
    return (-b - math.sqrt(determinante)) / (2*a)

print("="*20)
print("Resultado da equação")
print("="*20)

delta = calcDeterminante(a, b, c)
print(f"Determinante = {delta}")

if delta < 0:
    print("A equação não possui raízes reais.")
else:
    print(f"Primeira Raiz = {primeiraRaiz(a, b, c)}")
    print(f"Segunda Raiz = {segundaRaiz(a, b, c)}")
