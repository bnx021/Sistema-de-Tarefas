tarefas = []
prioridades_validas = ["baixa", "média", "media", "alta"]

while True:
    print("\n=== Menu de Tarefas ===")
    print("1 - Cadastrar tarefa")
    print("2 - Listar tarefas")
    print("3 - Atualizar situação de uma tarefa")
    print("4 - Encerrar sistema")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Título da tarefa: ").strip()
        prioridade = input("Prioridade (baixa, média ou alta): ").strip().lower()

        if titulo == "":
            print("O título não pode ficar vazio.")
        elif prioridade not in prioridades_validas:
            print("Prioridade inválida. Use baixa, média ou alta.")
        else:
            if prioridade == "media":
                prioridade = "média"

            tarefa = {
                "titulo": titulo,
                "prioridade": prioridade,
                "situacao": "pendente"
            }
            tarefas.append(tarefa)
            print("Tarefa cadastrada com sucesso.")

    elif opcao == "2":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\n=== Lista de Tarefas ===")
            numero = 1
            for tarefa in tarefas:
                print(f"{numero} - {tarefa['titulo']} | prioridade: {tarefa['prioridade']} | situação: {tarefa['situacao']}")
                numero = numero + 1

    elif opcao == "3":
        numero_informado = input("Número da tarefa que será concluída: ").strip()

        if not numero_informado.isdigit():
            print("Informe um número válido.")
        else:
            numero_tarefa = int(numero_informado)
            indice = numero_tarefa - 1

            if indice >= 0 and indice < len(tarefas):
                tarefas[indice]["situacao"] = "concluída"
                print("Tarefa atualizada com sucesso.")
            else:
                print("Tarefa inexistente.")

    elif opcao == "4":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida. Escolha um número de 1 a 4.")
