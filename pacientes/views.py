from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Paciente
from .forms import PacienteForm
from django.contrib.auth.mixins import LoginRequiredMixin


class PacienteListView(
    LoginRequiredMixin,
      ListView
      ):
    
    model = Paciente
    template_name = 'pacientes/listar.html'
    context_object_name = 'pacientes'

class PacienteCreateView(
    LoginRequiredMixin,
    CreateView
    ):

    model = Paciente
    form_class = PacienteForm
    template_name = 'pacientes/cadastrar.html'
    success_url = reverse_lazy('listar_pacientes')

class PacienteUpdateView(
    LoginRequiredMixin,
    UpdateView
    ):

    model = Paciente
    form_class = PacienteForm
    template_name = 'pacientes/editar.html'
    success_url = reverse_lazy('listar_pacientes')

class PacienteDeleteView(
    LoginRequiredMixin,
    DeleteView
    ):

    model = Paciente
    template_name = 'pacientes/deletar.html'
    success_url = reverse_lazy('listar_pacientes')

class PacienteDetailView(
    LoginRequiredMixin,
    DetailView
    ):
    
    model = Paciente
    template_name = 'pacientes/detalhes.html'
    context_object_name = 'paciente'