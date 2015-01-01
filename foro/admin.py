from django.contrib import admin
from . import models
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField

class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("titulo",)}

class HiloAdmin(MarkdownModelAdmin):
    list_display = ("titulo", "usuario", "categoria", "fecha")
    prepopulated_fields = {"slug": ("titulo",)}
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

class ComentarioAdmin(MarkdownModelAdmin):
    list_display = ("id", "usuario", "hilo", "get_categoria", "fecha")
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

admin.site.register(models.Categoria, CategoriaAdmin)
admin.site.register(models.Hilo, HiloAdmin)
admin.site.register(models.Comentario, ComentarioAdmin)

                    
