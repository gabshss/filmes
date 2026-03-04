from django.contrib import admin
from .models import *

@admin.register(Continente)
class ContinenteAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ('nome', 'continente')
    list_filter = ('continente',)
    search_fields = ('nome',)

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'nacionalidade')
    list_filter = ('cargo','nacionalidade')
    search_fields = ('nome', 'cargo', 'nacionalidade')  

@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'pais', 'diretor', 'data')
    list_filter = ('genero','pais','data')
    search_fields = ('titulo', 'diretor__nome', 'pais')

@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'duracao', 'genero', 'diretor')
    list_filter = ('nota',)
    search_fields = ('titulo', 'diretor', 'pais')
    
@admin.register(Temporada)
class TemporadaAdmin(admin.ModelAdmin):
    list_display = ('serie', 'numero')


@admin.register(Episodio)
class EpisodioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'temporada', 'duracao', 'data')
    list_filter =  ('temporada',)
    search_fields = ('nome',)