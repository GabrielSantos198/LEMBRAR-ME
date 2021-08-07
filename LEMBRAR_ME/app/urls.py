from django.urls import path
from . import views


urlpatterns = [
    path('', views.PagInicial.as_view(), name="inicio"),
]
