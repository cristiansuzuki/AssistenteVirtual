from neuralintents import GenericAssistant
import sys

todos = ['Lavar carro', 'Dar comida pros gatos', 'Estudar', 'Trabalhar']

def todo_show():
    print("Lista de tarefas: ")
    for todo in todos:
        print(todo)

def todo_add():
    todo = input("O que você deseja adicionar na lista ?: ")
    todos.append(todo)

def todo_remove():
    idx= int(input("Qual item você deseja remover ? (número):")) - 1
    if idx < len(todos):
        print(f"Removendo {todos[idx]}")
        todos.pop(idx)
    else:
        print("Não existe um item nessa posição...")

def bye():
    print("Tchau !")
    sys.exit(0)        

mappings = {
    'todoshow': todo_show,
    'todoadd': todo_add,
    'todoremove': todo_remove,
    'goodbye': bye
}

assistant = GenericAssistant("intents.json", mappings)

assistant.train_model()
assistant.save_model()

assistant.load_model()

while True:
    message = input("Mensagem: ")
    assistant.request(message)