from django.urls import path

from .views import (ConsultaListView, ConsultaCreateView, ConsultaUpdateView, ConsultaDeleteView, ConsultaDetailView,  realizar_consulta, cancelar_consulta)

urlpatterns = [
    path('', ConsultaListView.as_view(), name='listar_consultas'),
    path('cadastrar', ConsultaCreateView.as_view(), name='cadastrar_consulta'),
    path('editar/<int:pk>/', ConsultaUpdateView.as_view, name='editar_consulta'),
    path('deletar/<int:pk>', ConsultaDeleteView.as_view(), name='deletar_consulta'),
    path('detalhes/<int:pk>/', ConsultaDetailView.as_view(), name='detalhes_consulta'),
    path('<int:pk>/realizar/', realizar_consulta, name='realizar_consulta'),
    path('<int:pk>/cancelar/', cancelar_consulta, name='cancelar_consulta'),
]