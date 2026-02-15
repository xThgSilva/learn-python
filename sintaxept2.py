# Condições if else
idade = int(input("Informe sua idade: "))

if idade >= 18:
    print("Acesso permitido.")
else :
    print("Acesso negado! é necessário ser maior de idade.")

# Operadores lógicos - and | or | not (&& ; || ; !=)
isHabilitado = True

if idade >= 18 and isHabilitado:
    print("Pode dirigir.")
else:
    print("Você não é maior de idade ou possui habilitação.")

# Estruturas de repetição
contador = 1

while contador < 10:
    print(f"Contagem: {contador}")
    contador += 1

# Por padrão, o valor do laço (i nesse caso) é 0
for i in range(5):
    print(f"Valor do i atual do loop: {i}")

# Usando parâmetros, o range começa no primeiro (1) e acaba no anterior do ultimo (6 - 1)
for i in range(1, 6):
    print(f"Valor atual do loop com parâmetros: {i}")

# Criando um array - ja é dinâmico
produtos = ["celular", "notebook", "teclado", "mouse", "mousepad", "fonte", "fam"]

# Acessar um elemento do array - array[indice]
print(produtos[1])  # notebook

# Adicionando elementos no array
produtos.append("macbook")
print(produtos[7])

# Percorrendo o array
for produto in produtos:
    print(f"Nome do produto: {produto}")

# Percorrendo o array e pegando o índice
for i in range(len(produtos)):
    print(f"{i + 1}º produto = {produtos[i]}")  # +1 para maior entendimento

# Funções de arrays
numeros = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(f"Maior número = {max(numeros)}")
print(f"Menor número = {min(numeros)}")
print(f"Soma dos números = {sum(numeros)}")
print(f"Quantidade do array (elementos) = {len(numeros)}")
