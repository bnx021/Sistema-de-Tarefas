"""Operações de negócio sobre uma coleção de tarefas."""


def cadastrar_tarefa(tarefas, titulo, descricao, prioridade, classe_tarefa):
    """Cria uma tarefa e a adiciona à lista recebida."""
    nova_tarefa = classe_tarefa(titulo, descricao, prioridade)
    tarefas.append(nova_tarefa)
    return nova_tarefa


def listar_tarefas(tarefas):
    """Imprime os resumos das tarefas, ou uma mensagem se a lista estiver vazia."""
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for indice, tarefa in enumerate(tarefas, start=1):
        print(f"{indice}. {tarefa.exibir_resumo()}")


def filtrar_por_situacao(tarefas, situacao):
    """Retorna somente as tarefas que possuem a situação informada."""
    return [tarefa for tarefa in tarefas if tarefa.situacao == situacao]
