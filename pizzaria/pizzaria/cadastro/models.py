#coding: utf-8
from django.db import models

# Create your models here.
class Atleta(models.Model):
    nome = models.CharField(max_length=128, db_index=True)
    cpf = models.CharField(max_length=11, db_index=True)
    email = models.EmailField(blank=True)
    dob = models.CharField(max_length=4, db_index=True)
    fone = models.CharField(max_length=16, db_index=True)
    logradouro = models.CharField(max_length=32, db_index=True)    
    numero = models.PositiveIntegerField(u'número') 
    complemento = models.CharField(max_length=32, blank=True)
    cidade = models.CharField(max_length=32)
    estado = models.CharField(max_length=32)
    cep = models.PositiveIntegerField(u'CEP')
    tipo = models.CharField(max_length=4, db_index=True)
    obs = models.TextField(u'observação', blank=True)

    def __unicode__(self):
        return self.nome
    
    def endereco(self):
        return u'%s, %s' % (self.logradouro, self.numero)
    endereco.short_description = u'Endereço'

