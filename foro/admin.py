from django.contrib import admin
from . import models


from django.db.models import TextField

class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("titulo",)}

class HiloAdmin(admin.ModelAdmin):
    list_display = ("titulo", "usuario", "categoria", "fecha")


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "hilo", "get_categoria", "fecha")


admin.site.register(models.Categoria, CategoriaAdmin)
admin.site.register(models.Hilo, HiloAdmin)
admin.site.register(models.Comentario, ComentarioAdmin)

                    
