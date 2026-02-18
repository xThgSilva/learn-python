"""
Mini CRUD de Lista de Tarefas
Você vai criar um sistema simples de tarefas.

Regras:
Você terá uma lista vazia no começo:
- tarefas = []

Você precisa criar funções para:

1️⃣ Criar tarefa
- Recebe a lista e uma descrição.
- Adiciona na lista.
- criarTarefa(lista, descricao)

2️⃣ Listar tarefas
Mostra todas as tarefas numeradas.
Exemplo:
- 1 - Estudar Python
- 2 - Treinar
- 3 - Ler livro
- listarTarefas(lista)

3️⃣ Deletar tarefa
- Recebe a lista e o número da tarefa.
- Remove da lista.
- deletarTarefa(lista, indice)
"""
tarefas = []

def adicionarTarefa(array, tarefa):
    if tarefa == "":
        print("[ERRO] A tarefa não pode ter título vazio.")
    else:
        array.append(tarefa)
        print("Tarefa adicionada!")

def listarTarefas(array):
    if len(array) == 0:
        print("Não há tarefas registradas.")
    else:
        for i, valor in enumerate(array):
            print(f"{i + 1}º tarefa - {valor}")

def excluirTarefa(array, indice):
    idCorreto = indice - 1
    array.pop(idCorreto)
    print("Tarefa excluida!")

isActive = True
while isActive:
    print("=== Gerenciador de tarefas\n")
    opc = int(input("Escolha uma opção:\n[1] - Adicionar tarefa\n[2] - Listar Tarefas\n[3] - Excluir tarefa\n[0] - Sair"))

    if opc == 1:
        nome = input("Digite o nome da tarefa: ")
        adicionarTarefa(tarefas, nome)
    elif opc == 2:
        listarTarefas(tarefas)
    elif opc == 3:
        listarTarefas(tarefas)
        indice = int(input("Informe o indice do produto: "))

        excluirTarefa(tarefas, indice)
    else:
        isActive = False

print("Programa encerrado...")
