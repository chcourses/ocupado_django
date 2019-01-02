from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from django.urls import reverse


class Empresa(models.Model):
    nome = models.CharField(max_length=140, unique=True)
    lote = models.IntegerField(
        unique=True, null=True, verbose_name='lote', name='lote')
    etapa = models.IntegerField(null=True, verbose_name='etapa', name='etapa')
    razao_social = models.CharField(max_length=140, default=None, blank=True)
    logo = models.ImageField(
        upload_to='empresas/logo/', default=None, blank=True, null=True)
    grupo = models.CharField(max_length=140, default=None, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True, blank=True, null=True)
    sede = models.CharField(max_length=140, default=None, blank=True)
    rodovias = models.TextField(max_length=360, default=None, blank=True)
    # contrato
    # TAMs
    # rodoviasMODEL

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('emp-detail', kwargs={'pk': self.id})
