from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    sumario = models.CharField(max_length=150)
    conteudo = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    criacao = models.DateTimeField(auto_now_add=True)
    editado = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.titulo


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        return super().save(*args, **kwargs)
