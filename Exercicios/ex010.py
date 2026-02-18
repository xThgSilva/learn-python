"""
Crie uma função que:
- Receba uma lista
- Receba um parâmetro opcional par=True
- Se par=True, retorne apenas números pares
- Se par=False, retorne apenas números ímpares
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def listarParesImpares(tipo = "impar"):
    novaLista = []
    if tipo == "par":
        for num in numeros:
            if num % 2 == 0:
                novaLista.append(num)
    else:
        for num in numeros:
            if num % 2 == 1:
                novaLista.append(num)

    return novaLista

def filtraNumeros(par = True):
    if par is True:
      return listarParesImpares("par")
    else:
       return listarParesImpares()

print(filtraNumeros())

""" - Forma bem mais simples
def filtrar(lista, par=True):
    novaLista = []

    for num in lista:
        if par and num % 2 == 0:
            novaLista.append(num)
        elif not par and num % 2 == 1:
            novaLista.append(num)

    return novaLista

print(filtrar(numeros))
print(filtrar(numeros, par=False))
"""