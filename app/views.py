from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages
from .forms import FilmeForm, SerieForm

class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

    def post(self, request, *args, **kwargs):
        pass

def index(request):
    filmes = Filme.objects.all().order_by('titulo')[:5]
    series = Serie.objects.all().order_by('titulo')[:5]

    return render(request, 'index.html', {
        'filmes': filmes,
        'series': series
    })


def filme(request):
    lista_filmes = Filme.objects.all().order_by('titulo')
    return render(request, 'filme.html', {'filmes': lista_filmes})


def serie(request):
    lista_series = Serie.objects.all().order_by('titulo')
    return render(request, 'serie.html', {'series': lista_series})


def pessoa(request):
    lista_pessoas = Pessoa.objects.all().order_by('nome')
    return render(request, 'pessoa.html', {'pessoas': lista_pessoas})


def genero(request):
    lista_generos = Genero.objects.all().order_by('nome')
    return render(request, 'genero.html', {'generos': lista_generos})


def pais(request):
    lista_paises = Pais.objects.all().order_by('nome')
    return render(request, 'pais.html', {'paises': lista_paises})


def continente(request):
    lista_continentes = Continente.objects.all().order_by('nome')
    return render(request, 'continente.html', {'continentes': lista_continentes})


def temporada(request):
    lista_temporadas = Temporada.objects.all().order_by('numero')
    return render(request, 'temporada.html', {'temporadas': lista_temporadas})


def episodio(request):
    lista_episodios = Episodio.objects.all().order_by('nome')
    return render(request, 'episodio.html', {'episodios': lista_episodios})

class DeleteFilmeView(View):
    def get(self, request, id, *args, **kwargs):
        filme = get_object_or_404(Filme, id=id)
        filme.delete()
        messages.success(request, 'Filme excluído com sucesso!') # Success message
        return redirect('filme')

class DeleteSerieView(View):
    def get(self, request, id, *args, **kwargs):
        serie = get_object_or_404(Serie, id=id)
        serie.delete()
        messages.success(request, 'Série excluída com sucesso!') # Success message
        return redirect('serie')

class EditarFilmeView(View):
    template_name = 'editar_filme.html'

    def get(self, request, id, *args, **kwargs):
        filme = get_object_or_404(Filme, id=id)
        form = FilmeForm(instance=filme)
        return render(request, self.template_name, {
            'filme': filme,
            'form': form
        })

    def post(self, request, id, *args, **kwargs):
        filme = get_object_or_404(Filme, id=id)
        form = FilmeForm(request.POST, instance=filme)

        if form.is_valid():
            form.save()
            messages.success(request, 'Filme atualizado com sucesso!')
            return redirect('editar_filme', id=id)

        return render(request, self.template_name, {
            'filme': filme,
            'form': form
        })

class EditarSerieView(View):
    template_name = 'editar_serie.html'

    def get(self, request, id, *args, **kwargs):
        serie = get_object_or_404(Serie, id=id)
        form = SerieForm(instance=serie)
        return render(request, self.template_name, {
            'serie': serie,
            'form': form
        })

    def post(self, request, id, *args, **kwargs):
        serie = get_object_or_404(Serie, id=id)
        form = SerieForm(request.POST, instance=serie)

        if form.is_valid():
            form.save()
            messages.success(request, 'Série atualizadoa com sucesso!')
            return redirect('editar_serie', id=id)

        return render(request, self.template_name, {
            'serie': serie,
            'form': form
        })