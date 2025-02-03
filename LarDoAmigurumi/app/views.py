from django.shortcuts import render
from django.views import View
from .models import *

def HomeReceitas(request):
    return render(request, 'HomeReceitas.html')

class LinhasView(View):
    def get(self, request, *args, **kwargs):
        linhas = Linha.objects.all()
        return render(request, 'linhas.html', {'linhas': linhas})
class MateriaisView(View):
    def get(self, request, *args, **kwargs):
        materiais = Materiais.objects.all()
        return render(request, 'materiais.html', {'materiais': materiais})
class ReceitasView(View):
    def get(self, request, *args, **kwargs):
        receita = Receita.objects.all()
        return render(request, 'receitas.html', {'receita': receita})

class SobreNosView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'sobrenos.html')