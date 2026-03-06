from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView 
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='index'),
    path('filme/delete/<int:id>/', DeleteFilmeView.as_view(), name='delete_filme'),
    path('serie/delete/<int:id>/', DeleteSerieView.as_view(), name='delete_serie'),
    path('filme/editar/<int:id>/', EditarFilmeView.as_view(), name='editar_filme'),
    path('serie/editar/<int:id>/', EditarSerieView.as_view(), name='editar_serie'),

    path('filme/', filme, name='filme'),
    path('serie/', serie, name='serie'),
    path('pessoa/', pessoa, name='pessoa'),
    path('genero/', genero, name='genero'),
    path('pais/', pais, name='pais'),
    path('continente/', continente, name='continente'),
    path('temporada/', temporada, name='temporada'),
    path('episodio/', episodio, name='episodio'),
]