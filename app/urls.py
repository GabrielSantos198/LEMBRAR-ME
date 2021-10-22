from django.urls import path
from . import views


urlpatterns = [
    path('', views.Entrar.as_view(), name='entrar'),
    path('cadastrar/', views.Cadastrar.as_view(), name='cadastrar'),
    path('usuario/confs/sair/', views.Sair.as_view(), name='sair'),
    path('usuario/', views.Usuario.as_view(), name='usuario'),
    path('usuario/anotacao/<slug:slug>/', views.Anotacao.as_view(), name='anotacao'),
    path('usuario/excluir/anotacao/<slug:slug>/', views.ExcluirAnotacao.as_view(), name='excluir-anotacao'),
    path('usuario/editar/anotacao/<slug:slug>/', views.EditarAnotacao.as_view(), name='editar-anotacao'),
    path('usuario/nova-anotacao/', views.NovaAnotacao.as_view(), name='nova-anotacao'),
    path('usuario/buscar/', views.Buscar.as_view(), name='buscar'),
    path('usuario/confs/', views.Confs.as_view(), name='confs'),
    path('usuario/confs/alterar-senha/', views.AlterarSenha.as_view(), name='alterar-senha'),
    path('usuario/confs/alterar-senha/sucesso/', views.Sucesso.as_view(), name='sucesso'),
    path('usuario/confs/deletar-conta/<int:pk>/', views.DeletarConta.as_view(), name='deletar-conta'),
    path('politicas/', views.Politicas.as_view(), name='politicas'),
    path('usuario/confs/definir-senha/', views.DefinirSenha.as_view(), name='definir-senha'),
    path('usuario/confs/definir-senha/sucesso/', views.SucessoDefinicao.as_view(), name='sucesso-definicao'),
]
