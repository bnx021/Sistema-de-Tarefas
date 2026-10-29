# Sistema de Gestão de Tarefas

Projeto didático de uma aplicação Django para cadastro e consulta de tarefas persistidas em SQLite.

## Requisitos

Python 3.10 ou superior, pip e Django entre as versões 5 e 6.

## Instalação e execução

Na raiz do projeto, crie e ative um ambiente virtual e instale as dependências:

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
python -m pip install -r requirements.txt
```

Aplique as migrações e execute as verificações:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py check
python manage.py test
```

Para iniciar o servidor:

```bash
python manage.py runserver
```

Abra `http://127.0.0.1:8000/` para a página inicial, `http://127.0.0.1:8000/tarefas/` para a listagem e `http://127.0.0.1:8000/admin/` para o Django Admin.

## Models e persistência

A aplicação `tarefas` possui os models `Categoria` e `Tarefa`. Cada tarefa tem título, descrição, prioridade, data prevista, situação e uma categoria. O relacionamento usa `ForeignKey` com `on_delete=models.PROTECT`, impedindo a exclusão de uma categoria que ainda possui tarefas.

Para criar um usuário administrativo:

```bash
python manage.py createsuperuser
```

Também é possível validar o ORM pelo shell:

```bash
python manage.py shell
```

```python
from tarefas.models import Categoria, Tarefa

Tarefa.objects.all()
Tarefa.objects.filter(situacao="PENDENTE")
Tarefa.objects.order_by("data_prevista")

pendente = Tarefa.objects.filter(situacao="PENDENTE").first()
pendente.situacao = "CONCLUIDA"
pendente.save()
```

## Dificuldade encontrada

A versão anterior da aplicação exibia uma lista fixa criada diretamente na view. A dificuldade foi substituir essa estrutura sem alterar as rotas existentes. A solução foi criar os models, gerar as migrações e fazer a view consultar `Tarefa.objects.order_by("data_prevista")`, mantendo a mesma URL e o mesmo template.

## Organização

| Arquivo ou pasta | Responsabilidade |
| --- | --- |
| `gestao_tarefas/settings.py` | Configurações do projeto e registro da aplicação. |
| `gestao_tarefas/urls.py` | Rotas gerais e inclusão das rotas de `tarefas`. |
| `tarefas/models.py` | Models persistentes `Categoria` e `Tarefa`. |
| `tarefas/admin.py` | Registro dos models no Django Admin. |
| `tarefas/views.py` | Views da página inicial e da listagem persistida. |
| `tarefas/urls.py` | Rotas `/` e `/tarefas/`. |
| `tarefas/templates/tarefas/` | Templates HTML das páginas. |
| `manage.py` | Comandos administrativos do Django. |
