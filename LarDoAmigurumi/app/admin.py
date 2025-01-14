from django.contrib import admin
from .models import *

admin.site.register(Linha)
admin.site.register(Tipo_linha)

admin.site.register(Tipo_agulha)
admin.site.register(Enchimento)
admin.site.register(Tipo_enchimento)
admin.site.register(Marca_linha)
admin.site.register(Cor)


class AgulhaInline(admin.TabularInline):
    model = Agulha
    extra = 1
admin.site.register(Agulha)

class MateriaisAdmin(admin.ModelAdmin):
    inlines = [AgulhaInline]

admin.site.register(Materiais, MateriaisAdmin)

