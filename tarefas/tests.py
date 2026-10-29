from datetime import date, timedelta

from django.test import TestCase
from django.urls import reverse

from .models import Categoria, Tarefa


class ModelosTarefasTestCase(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nome="Estudos")

    def test_categoria_e_tarefa_possuem_representacao_legivel(self):
        tarefa = Tarefa.objects.create(
            titulo="Revisar models",
            descricao="Estudar persistência com Django.",
            prioridade=Tarefa.Prioridade.ALTA,
            data_prevista=date.today(),
            categoria=self.categoria,
        )

        self.assertEqual(str(self.categoria), "Estudos")
        self.assertEqual(str(tarefa), "Revisar models")
        self.assertEqual(tarefa.situacao, Tarefa.Situacao.PENDENTE)

    def test_consulta_filtra_tarefas_pendentes(self):
        Tarefa.objects.create(
            titulo="Pendente",
            data_prevista=date.today(),
            categoria=self.categoria,
        )
        Tarefa.objects.create(
            titulo="Concluída",
            data_prevista=date.today(),
            situacao=Tarefa.Situacao.CONCLUIDA,
            categoria=self.categoria,
        )

        pendentes = Tarefa.objects.filter(situacao=Tarefa.Situacao.PENDENTE)

        self.assertEqual(pendentes.count(), 1)
        self.assertEqual(pendentes.first().titulo, "Pendente")

    def test_tarefa_pode_ser_atualizada_e_persistida(self):
        tarefa = Tarefa.objects.create(
            titulo="Atualizar situação",
            data_prevista=date.today(),
            categoria=self.categoria,
        )

        tarefa.situacao = Tarefa.Situacao.CONCLUIDA
        tarefa.save()

        self.assertEqual(
            Tarefa.objects.get(pk=tarefa.pk).situacao,
            Tarefa.Situacao.CONCLUIDA,
        )


class RotasTarefasTestCase(TestCase):
    def setUp(self):
        categoria = Categoria.objects.create(nome="Estudos")
        Tarefa.objects.create(
            titulo="Tarefa mais tarde",
            data_prevista=date.today() + timedelta(days=2),
            categoria=categoria,
        )
        Tarefa.objects.create(
            titulo="Tarefa mais cedo",
            data_prevista=date.today(),
            categoria=categoria,
        )

    def test_inicio_renderiza_link_da_lista(self):
        response = self.client.get(reverse("inicio"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sistema Web de Gestão de Tarefas")
        self.assertContains(response, "/tarefas/")

    def test_lista_exibe_tarefas_ordenadas_por_data(self):
        response = self.client.get(reverse("lista_tarefas"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tarefa mais cedo")
        self.assertContains(response, "Tarefa mais tarde")
        self.assertLess(
            response.content.index(b"Tarefa mais cedo"),
            response.content.index(b"Tarefa mais tarde"),
        )
