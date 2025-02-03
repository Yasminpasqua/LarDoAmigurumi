from django.urls import path
from .views import HomeReceitas, LinhasView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeReceitas, name='HomeReceitas'),
    path('linhas/', LinhasView.as_view(), name='linhas'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)