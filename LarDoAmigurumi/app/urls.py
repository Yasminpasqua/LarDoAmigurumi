from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeReceitas, name='HomeReceitas'),
    path('linhas/', LinhasView.as_view(), name='linhas'),
    path('materiais/', MateriaisView.as_view(), name='materiais'),
    path('receitas/', ReceitasView.as_view(), name='receitas'),
    path('sobrenos/', SobreNosView.as_view(), name='sobrenos'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)