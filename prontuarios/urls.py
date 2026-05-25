from django.urls import path
from .views import (ProntuarioListView, ProntuarioCreateView, ProntuarioUpdateView, ProntuarioDeleteView)

urlpatterns = [

    path('',  ProntuarioListView.as_view(),  name='listar_prontuarios'),
    path('cadastrar/',  ProntuarioCreateView.as_view(),  name='cadastrar_prontuario'),
    path('editar/<int:pk>/',  ProntuarioUpdateView.as_view(),  name='editar_prontuario'),
    path('deletar/<int:pk>/',  ProntuarioDeleteView.as_view(),  name='deletar_prontuario') 
]