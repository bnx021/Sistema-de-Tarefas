"""Modelo em memória para representar uma tarefa."""


class Tarefa:
    """Representa uma tarefa do sistema."""

    def __init__(self, titulo, descricao, prioridade):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.situacao = "Pendente"

    def concluir(self):
        """Marca a tarefa como concluída."""
        self.situacao = "Concluída"

    def exibir_resumo(self):
        """Retorna os principais dados da tarefa em uma única linha."""
        return (
            f"Título: {self.titulo} | "
            f"Prioridade: {self.prioridade} | "
            f"Situação: {self.situacao}"
        )
