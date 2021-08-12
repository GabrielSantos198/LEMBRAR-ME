from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Post
# Create your views here.

@method_decorator(login_required, name='dispatch')
class Perfil(ListView):
    template_name = 'perfil.html'


    def get_queryset(self):
        return Post.objects.filter(user_id=self.request.user.id)


@method_decorator(login_required, name='dispatch')
class Conteudo(DetailView):
    template_name = 'conteudo.html'


    def get_queryset(self):
        return Post.objects.filter(user_id=self.request.user.id)


@method_decorator(login_required, name="dispatch")
class Excluir(DeleteView):
    template_name = 'excluir.html'
    success_url = '/'


    def get_queryset(self):
        return Post.objects.filter(user_id=self.request.user.id)


@method_decorator(login_required, name="dispatch")
class Editar(UpdateView):
    template_name = "editar.html"
    success_url = '/'
    fields = ('titulo', 'sumario', 'conteudo')


    def get_queryset(self):
        return Post.objects.filter(user_id=self.request.user.id)

