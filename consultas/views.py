from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView, DetailView)
from core.mixins import CargoPermitidoMixin
from .models import Consulta
from .forms import ConsultaForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required


class ConsultaListView(LoginRequiredMixin, CargoPermitidoMixin, ListView):
    model = Consulta

    template_name = 'consultas/listar.html'

    context_object_name = 'consultas'

    cargos_permitidos = [
        'MEDICO',
        'RECEPCIONISTA',
        'ADMIN'
    ]

    def get_queryset(self):

        usuario = self.request.user

        if usuario.funcionario.cargo == 'MEDICO':

            return Consulta.objects.filter(
                medico=usuario.funcionario
            )

        return Consulta.objects.all()


class ConsultaCreateView(LoginRequiredMixin, CargoPermitidoMixin, CreateView):

    model = Consulta

    form_class = ConsultaForm

    template_name = 'consultas/form.html'

    success_url = reverse_lazy(
        'listar_consultas'
    )

    cargos_permitidos = [
        'RECEPCIONISTA',
        'ADMIN'
    ]

    def form_valid(self, form):

        form.instance.criado_por = self.request.user

        return super().form_valid(form)


class ConsultaUpdateView(LoginRequiredMixin, CargoPermitidoMixin, UpdateView):

    model = Consulta

    form_class = ConsultaForm

    template_name = 'consultas/form.html'

    success_url = reverse_lazy(
        'listar_consultas'
    )

    cargos_permitidos = [
        'MEDICO',
        'RECEPCIONISTA',
        'ADMIN'
    ]


class ConsultaDeleteView(LoginRequiredMixin, CargoPermitidoMixin, DeleteView):

    model = Consulta

    template_name = 'consultas/deletar.html'

    success_url = reverse_lazy(
        'listar_consultas'
    )

    cargos_permitidos = [
        'ADMIN'
    ]

class ConsultaDetailView(
    LoginRequiredMixin,
    CargoPermitidoMixin,
    DetailView
):
    model = Consulta

    template_name = 'consultas/detalhes.html'

    context_object_name = 'consulta'

    cargos_permitidos = [
        'MEDICO',
        'RECEPCIONISTA',
        'ADMIN'
    ]

@login_required
def realizar_consulta(request, pk):

    consulta = get_object_or_404(Consulta, pk=pk)

    funcionario = request.user.funcionario

    if funcionario.cargo not in ['MEDICO', 'ADMIN']:
        raise PermissionDenied

    if funcionario.cargo == 'MEDICO' and consulta.medico != funcionario:
        raise PermissionDenied

    consulta.status = 'REALIZADA'
    consulta.save()

    messages.success(
        request,
        'Consulta finalizada com sucesso.'
    )

    return redirect('listar_consultas')


@login_required
def cancelar_consulta(request, pk):

    consulta = get_object_or_404(Consulta, pk=pk)

    funcionario = request.user.funcionario

    if funcionario.cargo not in ['RECEPCIONISTA', 'ADMIN']:
        raise PermissionDenied

    consulta.status = 'CANCELADA'
    consulta.save()

    messages.success(
        request,
        'Consulta cancelada com sucesso.'
    )

    return redirect('listar_consultas')