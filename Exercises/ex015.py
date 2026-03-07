"""
Only even numbers in an interval

Create a function that:
- Receives start and end
- Returns only the even numbers within that interval (inclusive)
"""
def even_numbers_interval(start, end):
    even_numbers = []

    for num in range(start, end + 1): # Vai começar pelo "inicio", e terminar no "fim" escolhido, de 2 em 2, mostrando apenas os pares
        if num % 2 == 0:
            even_numbers.append(num)

    return even_numbers

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print(even_numbers_interval(start, end))

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