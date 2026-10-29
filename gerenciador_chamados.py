"""Protótipo de gerenciador de chamados internos."""


chamados = [
    {
        "id": 1,
        "titulo": "Sem acesso ao sistema interno",
        "prioridade": "alta",
        "situacao": "aberto",
        "categoria": "acesso",
    },
    {
        "id": 2,
        "titulo": "Impressora sem conexão",
        "prioridade": "média",
        "situacao": "em atendimento",
        "categoria": "hardware",
    },
    {
        "id": 3,
        "titulo": "E-mail não sincroniza",
        "prioridade": "alta",
        "situacao": "aberto",
        "categoria": "acesso",
    },
    {
        "id": 4,
        "titulo": "Atualização de software solicitada",
        "prioridade": "baixa",
        "situacao": "resolvido",
        "categoria": "software",
    },
    {
        "id": 5,
        "titulo": "Teclado com defeito",
        "prioridade": "média",
        "situacao": "aberto",
        "categoria": "hardware",
    },
]


def exibir_chamado(chamado):
    """Exibe um chamado de forma legível."""
    print(f"ID: {chamado['id']}")
    print(f"Título: {chamado['titulo']}")
    print(f"Prioridade: {chamado['prioridade']}")
    print(f"Situação: {chamado['situacao']}")
    print(f"Categoria: {chamado['categoria']}")
    print("-" * 30)


def listar_chamados():
    print("\n=== TODOS OS CHAMADOS ===")
    for chamado in chamados:
        exibir_chamado(chamado)


def filtrar_por_situacao(situacao_desejada):
    print(f"\n=== CHAMADOS COM SITUAÇÃO: {situacao_desejada} ===")
    encontrou_chamado = False

    for chamado in chamados:
        if chamado["situacao"] == situacao_desejada:
            exibir_chamado(chamado)
            encontrou_chamado = True

    if not encontrou_chamado:
        print("Nenhum chamado encontrado para essa situação.")


def atualizar_situacao(id_chamado, nova_situacao):
    print(f"\n=== ATUALIZAÇÃO DO CHAMADO {id_chamado} ===")

    for chamado in chamados:
        if chamado["id"] == id_chamado:
            chamado["situacao"] = nova_situacao
            print(f"Chamado atualizado com sucesso para '{nova_situacao}'.")
            break
    else:
        print("Chamado não encontrado.")


def mostrar_categorias_unicas():
    categorias = set()

    for chamado in chamados:
        categorias.add(chamado["categoria"])

    print("\n=== CATEGORIAS SEM REPETIÇÃO ===")
    for categoria in sorted(categorias):
        print(f"- {categoria}")


if __name__ == "__main__":
    listar_chamados()
    filtrar_por_situacao("aberto")
    filtrar_por_situacao("cancelado")
    atualizar_situacao(2, "resolvido")
    atualizar_situacao(99, "aberto")
    mostrar_categorias_unicas()
