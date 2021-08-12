from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('titulo',)}
    search_fields = ('titulo','conteudo')
