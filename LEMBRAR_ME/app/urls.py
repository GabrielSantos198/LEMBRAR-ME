from django.urls import path
from . import views


urlpatterns = [
    path('', views.Anotacoes.as_view(), name="anotacoes"),
    path('conteudo/<slug:slug>/', views.Conteudo.as_view(), name="conteudo"),
    path('excluir/<slug:slug>/', views.Excluir.as_view(), name="excluir"),
    path('editar/<slug:slug>/', views.Editar.as_view(), name="editar"),
    path('novo/', views.Novo.as_view(), name="novo"),
    path('buscar/', views.Buscar.as_view(), name="buscar"),
    path('confs/', views.Confs.as_view(), name="confs"),
    path('confs/alterar-senha/', views.AlterarSenha.as_view(), name="alterar"),
    path('confs/alterar-senha/sucesso/', views.Sucesso.as_view(), name="sucesso"),
    path('user/delete/<int:pk>/', views.UserDelete.as_view(), name="user_delete"),
]
