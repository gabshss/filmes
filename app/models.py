from django.db import models
class Continente(models.Model):
    nome = models.CharField(max_length=100, verbose_name = "Continente")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Continente"
        verbose_name_plural = "Continentes"

class Pais(models.Model):
    nome = models.CharField(max_length=100, verbose_name = "País")
    continente = models.ForeignKey(Continente, on_delete = models.CASCADE,verbose_name="Continente")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"

class Genero(models.Model):
    nome = models.CharField(max_length=100, verbose_name = "Gênero")

    def __str__(self):
        return self.nome 

    class Meta:
        verbose_name = "Gênero"
        verbose_name_plural = "Gêneros"

class Pessoa(models.Model):
    cargo = models.CharField(max_length=100, verbose_name = "Cargo")
    nome = models.CharField(max_length=100, verbose_name = "Nome")
    insta = models.CharField(max_length=100, verbose_name = "Instagram")
    nacionalidade = models.CharField(max_length=100, verbose_name = "Nacionalidade")
    
    def __str__(self):
        return f"{self.nome} ({self.cargo})"

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

class Filme(models.Model):
    titulo = models.CharField(max_length=100,verbose_name = "Título")
    duracao = models.CharField(max_length=100,verbose_name = "Duração")
    sinopse = models.TextField(verbose_name = "Sinopse")
    data = models.DateField(verbose_name = "Data de lançamento")
    nota = models.DecimalField(max_digits=3, decimal_places=1, verbose_name = "Nota de avaliação")
    genero = models.ForeignKey(Genero, on_delete = models.CASCADE, verbose_name = "Gênero")
    pais = models.ForeignKey(Pais, on_delete = models.CASCADE, verbose_name ="País")
    diretor = models.ForeignKey(Pessoa, on_delete = models.CASCADE, verbose_name = "Diretor")
    atores = models.ManyToManyField(Pessoa, related_name="filmes_como_ator", verbose_name="Atores", blank=True,)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Filme"
        verbose_name_plural = "Filmes"
        
class Serie(models.Model):
    titulo = models.CharField(max_length=100,verbose_name = "Título")
    duracao = models.CharField(max_length=100,verbose_name = "Duração")
    sinopse = models.TextField(verbose_name = "Sinopse")
    data = models.DateField(verbose_name = "Data de lançamento")
    nota = models.DecimalField(max_digits=3, decimal_places=1, verbose_name = "Nota de avaliação")
    genero = models.ForeignKey(Genero, on_delete = models.CASCADE, verbose_name = "Gênero")
    pais = models.ForeignKey(Pais, on_delete = models.CASCADE, verbose_name ="País")
    diretor = models.ForeignKey(Pessoa, on_delete = models.CASCADE, verbose_name = "Diretor")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Série"
        verbose_name_plural = "Séries"

class Temporada(models.Model):
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, related_name="temporadas", verbose_name="Série")
    numero = models.IntegerField(verbose_name="Número da temporada")

    def __str__(self):
        return f"{self.serie.titulo} - {self.numero}ª Temporada"

    class Meta:
        verbose_name = "Temporada"
        verbose_name_plural = "Temporadas"
        unique_together = ("serie", "numero")

class Episodio(models.Model):
    nome = models.CharField(max_length=100, verbose_name = "Título")
    temporada = models.ForeignKey(Temporada, on_delete = models.CASCADE, verbose_name = "Temporada")
    numero = models.IntegerField(verbose_name="Número do episódio")
    duracao = models.CharField(max_length=100, verbose_name = "Duração")
    data = models.DateField(verbose_name = "Data de lançamento")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Episódio"
        verbose_name_plural = "Episódios"





