from django.contrib import admin
from .models import *

admin.site.register(Linha)

class AgulhaInline(admin.TabularInline):
    model = Agulha
    extra = 1

class TipoAgulhaAdmin(admin.ModelAdmin):
    inlines = [AgulhaInline]

class Linhainline(admin.TabularInline):
    model = Linha
    extra = 1

class TipoLinhaAdmin(admin.ModelAdmin):
    inlines = [Linhainline]

class MarcaLinhaAdmin(admin.ModelAdmin):
    inlines = [Linhainline]

class CorAdmin(admin.ModelAdmin):
    inlines = [Linhainline]

admin.site.register(Tipo_linha, TipoLinhaAdmin)
admin.site.register(Tipo_agulha, TipoAgulhaAdmin)
admin.site.register(Enchimento)
admin.site.register(Marca_linha, MarcaLinhaAdmin)
admin.site.register(Cor, CorAdmin)
admin.site.register(Receita)
admin.site.register(Categoria)
admin.site.register(Agulha)
admin.site.register(Materiais)

