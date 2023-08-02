from django.db import models
from django.urls import reverse


class PlanoAula(models.Model):
    titulo = models.CharField(max_length=1000)
    objetivo_geral = models.TextField()
    objetivos_especificos = models.TextField()
    conteudo = models.TextField()
    metodologia = models.TextField()
    avaliacao = models.TextField()
    materiais = models.TextField()
    referencias_basicas = models.TextField()
    referencias_complementar = models.TextField()
    dia_criacao= models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("PlanoAula")
        verbose_name_plural = ("PlanoAulas")

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("editar_plano_aula", kwargs={"pk": self.pk})
