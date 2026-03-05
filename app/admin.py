from django.contrib import admin
from .models import *

class PaisInline(admin.TabularInline):
    model = Pais
    extra = 1

@admin.register(Continente)
class ContinenteAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [PaisInline]

admin.site.register(Pais)

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

class TemporadaInline(admin.TabularInline):
    model = Temporada
    extra = 1

@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'duracao', 'genero', 'diretor')
    list_filter = ('nota',)
    search_fields = ('titulo', 'diretor__nome', 'pais__nome')
    inlines = [TemporadaInline]

class EpisodioInline(admin.TabularInline):
    model = Episodio
    extra = 1 

@admin.register(Temporada)
class TemporadaAdmin(admin.ModelAdmin):
    list_display =('serie', 'numero')
    inlines = [EpisodioInline]

@admin.register(Episodio)
class EpisodioAdmin(admin.ModelAdmin):
    list_display = ('numero', 'nome', 'temporada', 'duracao', 'data')
    list_filter = ('temporada',)
    search_fields = ('nome',)

   