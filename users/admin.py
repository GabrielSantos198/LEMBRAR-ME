from django.contrib import admin
from .models import User
from django.contrib.auth import admin as auth_admin
from .forms import UserChangeForm, UserCreationForm

# Register your models here.
@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    fieldsets = (
            ("Campos Personalizados",  {"fields":("username","password","bio",)}),
        )

