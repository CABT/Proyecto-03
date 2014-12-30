from django.contrib import admin
from .models import RegistroUsuario

# Register your models here.

class RegistroAdmin(admin.ModelAdmin):
    fields = ['username', 'correo', 'pais', 'avatar',  'is_superuser', 'is_staff', 'is_active',
              'last_login', 'date_joined']
admin.site.register(RegistroUsuario, RegistroAdmin)
