from django.urls import reverse_lazy
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Funcionario
from .forms import FuncionarioForm


class FuncionarioListView(LoginRequiredMixin, ListView):
    model = Funcionario
    template_name = 'funcionarios/listar.html'
    context_object_name = 'funcionarios'


class FuncionarioCreateView(LoginRequiredMixin, CreateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = 'funcionarios/form.html'
    success_url = reverse_lazy(
        'listar_funcionarios'
    )


class FuncionarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = 'funcionarios/form.html'
    success_url = reverse_lazy(
        'listar_funcionarios'
    )


class FuncionarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Funcionario
    template_name = 'funcionarios/deletar.html'
    success_url = reverse_lazy(
        'listar_funcionarios'
    )