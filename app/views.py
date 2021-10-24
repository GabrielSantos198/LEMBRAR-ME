from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Post
from django.db.models import Q
from django.core.paginator import Paginator
from allauth.account.views import PasswordChangeView, LoginView, SignupView, LogoutView, PasswordSetView
from users.models import User
# Create your views here.

class Entrar(LoginView):
    template_name = 'entrar.html'

    def get_success_url(self):
        return reverse('usuario', kwargs={'username': self.request.user.username})



class Cadastrar(SignupView):
    template_name = 'cadastrar.html'
    
    def get_success_url(self):
        return reverse('usuario', kwargs={'username': self.request.user.username})



class Sair(LogoutView):
    template_name = 'sair.html'
    success_url = '/'



@method_decorator(login_required, name='dispatch')
class Usuario(ListView):
    template_name = 'usuario.html'
    paginate_by = 15


    def get_queryset(self):
        return Post.objects.filter(user_id=self.request.user.id).order_by('-editado')



@method_decorator(login_required, name='dispatch')
class Anotacao(DetailView):
    template_name = 'anotacao.html'


    def get_queryset(self):
        return Post.objects.filter(user_id=self.request.user.id)



@method_decorator(login_required, name="dispatch")
class ExcluirAnotacao(DeleteView):
    template_name = 'excluir-anotacao.html'
    success_url = '/'

    def get_queryset(self):
        return Post.objects.filter(user_id=self.request.user.id)



@method_decorator(login_required, name="dispatch")
class EditarAnotacao(UpdateView):
    template_name = 'editar-anotacao.html'
    success_url = '/'
    fields = ('titulo', 'sumario', 'conteudo')


    def get_queryset(self):
        return Post.objects.filter(user_id=self.request.user.id)



@method_decorator(login_required, name="dispatch")
class NovaAnotacao(CreateView):
    model = Post
    template_name = 'nova-anotacao.html'
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



@method_decorator(login_required, name='dispatch')
class Confs(TemplateView):
    template_name = 'confs.html'



class AlterarSenha(PasswordChangeView):
    template_name = 'alterar-senha.html'
    success_url = '/sucesso'
    


@method_decorator(login_required, name='dispatch')
class Sucesso(TemplateView):
    template_name = 'sucesso.html'



@method_decorator(login_required, name='dispatch')
class DeletarConta(DeleteView):
    template_name = 'deletar-conta.html'
    success_url = '/'


    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class Politicas(TemplateView):
    template_name = 'politicas.html'


class DefinirSenha(PasswordSetView):
    template_name = 'definir-senha.html'
    success_url = '/sucesso-definicao'
    

@method_decorator(login_required, name='dispatch')
class SucessoDefinicao(TemplateView):
    template_name = 'sucesso-definicao.html'


