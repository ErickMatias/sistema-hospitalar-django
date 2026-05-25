from django.urls import reverse_lazy
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import CargoPermitidoMixin
from .models import Prontuario
from .forms import ProntuarioForm


class ProntuarioListView(
    LoginRequiredMixin,
    CargoPermitidoMixin,
    ListView
):
    model = Prontuario
    template_name = 'prontuarios/listar.html'
    context_object_name = 'prontuarios'

    cargos_permitidos = ['MEDICO', 'ADMIN']

    def get_queryset(self):
        funcionario = self.request.user.funcionario

        if funcionario.cargo == 'MEDICO':
            return Prontuario.objects.filter(
                consulta__medico=funcionario
            )

        return Prontuario.objects.all()


class ProntuarioCreateView(
    LoginRequiredMixin,
    CargoPermitidoMixin,
    CreateView
):
    model = Prontuario
    form_class = ProntuarioForm
    template_name = 'prontuarios/form.html'
    success_url = reverse_lazy('listar_prontuarios')

    cargos_permitidos = ['MEDICO', 'ADMIN']

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        funcionario = self.request.user.funcionario

        consultas = form.fields['consulta'].queryset.exclude(
            status='CANCELADA'
        )

        if funcionario.cargo == 'MEDICO':
            consultas = consultas.filter(
                medico=funcionario
            )

        form.fields['consulta'].queryset = consultas

        return form


class ProntuarioUpdateView(
    LoginRequiredMixin,
    CargoPermitidoMixin,
    UpdateView
):
    model = Prontuario
    form_class = ProntuarioForm
    template_name = 'prontuarios/form.html'
    success_url = reverse_lazy('listar_prontuarios')

    cargos_permitidos = ['MEDICO', 'ADMIN']

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        funcionario = self.request.user.funcionario

        consultas = form.fields['consulta'].queryset.exclude(
            status='CANCELADA'
        )

        if funcionario.cargo == 'MEDICO':
            consultas = consultas.filter(
                medico=funcionario
            )

        form.fields['consulta'].queryset = consultas

        return form


class ProntuarioDeleteView(
    LoginRequiredMixin,
    CargoPermitidoMixin,
    DeleteView
):
    model = Prontuario
    template_name = 'prontuarios/deletar.html'
    success_url = reverse_lazy('listar_prontuarios')

    cargos_permitidos = ['ADMIN']