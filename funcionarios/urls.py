from django.urls import path

from .views import ( FuncionarioListView, FuncionarioCreateView, FuncionarioUpdateView, FuncionarioDeleteView)


urlpatterns = [

    path('', FuncionarioListView.as_view(), name='listar_funcionarios'),
    path('cadastrar/',  FuncionarioCreateView.as_view(), name='cadastrar_funcionario'),
    path('editar/<int:pk>/', FuncionarioUpdateView.as_view(), name='editar_funcionario'),
    path('deletar/<int:pk>/', FuncionarioDeleteView.as_view(), name='deletar_funcionario'), 
]