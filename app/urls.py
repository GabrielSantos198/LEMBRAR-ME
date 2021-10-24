from django.urls import path
from . import views


urlpatterns = [
    path('', views.Entrar.as_view(), name='entrar'),
    path('cadastrar/', views.Cadastrar.as_view(), name='cadastrar'),
    path('@<str:username>/confs/sair/', views.Sair.as_view(), name='sair'),
    path('@<str:username>/', views.Usuario.as_view(), name='usuario'),
    path('@<str:username>/anotacao/<slug:slug>/', views.Anotacao.as_view(), name='anotacao'),
    path('@<str:username>/excluir/anotacao/<slug:slug>/', views.ExcluirAnotacao.as_view(), name='excluir-anotacao'),
    path('@<str:username>/editar/anotacao/<slug:slug>/', views.EditarAnotacao.as_view(), name='editar-anotacao'),
    path('@<str:username>/nova-anotacao/', views.NovaAnotacao.as_view(), name='nova-anotacao'),
    path('@<str:username>/buscar/', views.Buscar.as_view(), name='buscar'),
    path('@<str:username>/confs/', views.Confs.as_view(), name='confs'),
    path('@<str:username>/confs/alterar-senha/', views.AlterarSenha.as_view(), name='alterar-senha'),
    path('sucesso/', views.Sucesso.as_view(), name='sucesso'),
    path('@<str:username>/confs/deletar-conta/<int:pk>/', views.DeletarConta.as_view(), name='deletar-conta'),
    path('politicas/', views.Politicas.as_view(), name='politicas'),
    path('@<str:username>/confs/definir-senha/', views.DefinirSenha.as_view(), name='definir-senha'),
    path('sucesso-definicao/', views.SucessoDefinicao.as_view(), name='sucesso-definicao'),
]
