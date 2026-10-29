"""Demonstração da versão refatorada do controle de tarefas."""

from tarefa import Tarefa
from servicos import cadastrar_tarefa, filtrar_por_situacao, listar_tarefas


def executar_demonstracao():
    """Cadastra, conclui, lista e filtra tarefas em memória."""
    tarefas = []
    cadastrar_tarefa(
        tarefas,
        "Revisar chamados",
        "Verificar chamados pendentes da equipe",
        "Alta",
        Tarefa,
    )
    cadastrar_tarefa(
        tarefas,
        "Atualizar manual interno",
        "Ajustar instruções de atendimento",
        "Média",
        Tarefa,
    )
    cadastrar_tarefa(
        tarefas,
        "Planejar reunião",
        "Preparar pauta da reunião semanal",
        "Baixa",
        Tarefa,
    )

    tarefas[0].concluir()

    print("Todas as tarefas:")
    listar_tarefas(tarefas)
    print("\nTarefas concluídas:")
    listar_tarefas(filtrar_por_situacao(tarefas, "Concluída"))


if __name__ == "__main__":
    executar_demonstracao()
