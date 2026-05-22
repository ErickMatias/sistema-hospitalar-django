from django.urls import path
from .views import PacienteListView, PacienteCreateView, PacienteUpdateView, PacienteDeleteView, PacienteDetailView

urlpatterns = [
    path('', PacienteListView.as_view(), name='listar_pacientes'),
    path('cadastrar/', PacienteCreateView.as_view(), name='cadastrar_paciente'),
    path('<int:pk>/editar/', PacienteUpdateView.as_view(), name='editar_paciente'),
    path('<int:pk>/deletar', PacienteDeleteView.as_view(), name='deletar_paciente'),
    path('<int:pk>/', PacienteDetailView.as_view(), name='detalhes_paciente'),
]