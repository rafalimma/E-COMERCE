from django.contrib import admin
from . import models
# Register your models here.


class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'idade', 'data_nascimento', 'cpd', 'endereco', 'numero', 'complemento', 'bairro', 'cep', 'cidade', 'estado')
    search_fields = ('usuario__username', 'cpd', 'cidade')
    list_filter = ('estado',)

admin.site.register(models.Perfil, PerfilAdmin)
