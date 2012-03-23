#coding: utf-8
from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=128)
    fone = models.CharField(max_length=16)
    email = models.EmailField(blank=True)
    
    def __unicode__(self):
        return self.nome

# blank = true significa que o campo é opcional logo é uma forma de validacao do formulario
# null = true significa que este campo no BD pode aceitar null e para funcionar tem usar tambem o blank = true
# toda classe do models.Model representara uma tabela na base de dados

