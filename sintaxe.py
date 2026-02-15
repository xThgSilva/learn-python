# Como dar um print no terminal
print("Dando um print no terminal!")

# Declarando váriaveis
nome = "Thiago"     # Tipo string ""
idade = 18          # Tido inteiro
altura = 1.82       # Tipo float
isAtivo = True      # Tipo boolean

# Interpolação de strings usando ,
print("Bem vindo",nome,"sua idade é",idade,"anos!")

# Interpolação de string usando f-string (format)
print(f"Bem vindo {nome}! Sua idade é {idade} anos!")

# Ver o tipo do dado
print(f"{type(nome)} | {type(idade)} | {type(altura)} | {type(isAtivo)}")

# Receber um dado do terminal - sempre retorna um tipo string
carro = input("Digite uma marca de carro:")
print(f"Carro informado: {carro} | tipo: {type(carro)}")

# Fazendo o cast para int e float
n1 = int(input("Digite um número:"))
n2 = float(input("Digite outro número:"))
print(f"Values: {n1} | {n2}")
print(f"Types: {type(n1)} | {type(n2)}")

# Operações básicas
a = 10
b = 20

print(f"Soma: {a + b}")
print(f"Sub: {a - b}")
print(f"Multi: {a * b}")
print(f"Divisão: {a / b}")
print(f"Divisão inteira: {a // b}")
print(f"Resto (mod): {a % b}")
print(f"Potência: {a ** 20}")