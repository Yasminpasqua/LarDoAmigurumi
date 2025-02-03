from django.shortcuts import render
from django.views import View
from .models import Linha

def HomeReceitas(request):
    return render(request, 'HomeReceitas.html')

class LinhasView(View):
    def get(self, request, *args, **kwargs):
        linhas = Linha.objects.all()
        return render(request, 'linhas.html', {'linhas': linhas})
