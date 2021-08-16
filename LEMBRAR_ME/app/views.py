from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Post
from django.db.models import Q
# Create your views here.

@method_decorator(login_required, name='dispatch')
class Anotacoes(ListView):
    template_name = 'anotacoes.html'


    def get_queryset(self):
        return Post.objects.filter(user_id=self.request.user.id).order_by('-editado')


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
    template_name = 'editar.html'
    success_url = '/'
    fields = ('titulo', 'sumario', 'conteudo')


    def get_queryset(self):
        return Post.objects.filter(user_id=self.request.user.id)


@method_decorator(login_required, name="dispatch")
class Novo(CreateView):
    model = Post
    template_name = 'novo.html'
    fields = ('titulo', 'sumario', 'conteudo')
    success_url = "/"


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class Buscar(ListView):
    template_name = 'buscar.html'


    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(titulo__icontains=query) | Q(sumario__icontains=query), user_id=self.request.user.id
            )
        return object_list

