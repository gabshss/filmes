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
    continente = ForeignKey(Continente, on-delete = models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"

class Genero(models.Model):
    nome = models.CharField(max_length=100, verbose_name = "Gênero")

    def __str__(self):
        return self.nome 



