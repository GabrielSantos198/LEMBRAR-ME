from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    sumario = models.CharField(max_length=150)
    conteudo = RichTextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    criacao = models.DateTimeField(auto_now_add=True)
    editado = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.titulo


    def save(self, *args, **kwargs):
        quantidade = Post.objects.filter(user=self.user).count()
        quantidade_total = Post.objects.all().count()
        if not self.slug:
            self.slug = slugify(f"{quantidade_total+1}_{quantidade+1}-{self.titulo}")
        return super().save(*args, **kwargs)

