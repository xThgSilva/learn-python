nome = input("Digite seu nome: ")
idade = int(input("Informe sua idade: "))
altura = float(input("Informe sua altura: "))

print("Dados do usuário:")
print(f"Nome: {nome} | Idade: {idade} | Altura: {altura}")
print("Tipos dos dados:")
print(f"{type(nome)} | {type(idade)} | {type(altura)}")