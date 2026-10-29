from django.shortcuts import render

from .models import Tarefa


def inicio(request):
    return render(request, "tarefas/inicio.html")


def lista_tarefas(request):
    tarefas = Tarefa.objects.order_by("data_prevista")
    return render(request, "tarefas/lista.html", {"tarefas": tarefas})
