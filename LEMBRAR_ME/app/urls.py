from django.urls import path
from . import views


urlpatterns = [
    path('', views.Perfil.as_view(), name="perfil"),
    path('conteudo/<slug:slug>/', views.Conteudo.as_view(), name="conteudo"),
    path('excluir/<slug:slug>/', views.Excluir.as_view(), name="excluir"),
    path('editar/<slug:slug>/', views.Editar.as_view(), name="editar"),
]
