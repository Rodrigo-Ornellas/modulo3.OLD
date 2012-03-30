#coding: utf-8

# primeiro importa coisas do python, segundo do django e terceiro da aplicacao
from django.contrib import admin
from django.forms import Textarea
from django.db.models import TextField

from .models import Atleta, Cliente, Pedido, Entregador, Pizza

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('fone', 'nome', 'endereco')
    list_display_links = list_display
    search_fields = ['fone', 'nome', 'logradouro']
    list_filter = ('logradouro',)


class PizzaAdmin(admin.TabularInline):
    model = Pizza
    #exclude = ('obs',)
    formfield_overrides = {
        TextField: { 'widget': Textarea(attrs={'rows':2,'cols':10})},
    }

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('hora_inclusao', 'cliente', 'pronto', 'partiu')
    list_select_related = True # é usado para sugerir ao Django para fazer um join espeficicamente para o campo cliente da listagem acima que nao faz parte da tabela Pedido mas sim da tabela Cliente. Caso contrario o Django faz um SELECT para trazer a listagem do PEDIDO e depois faz tantos JOINS quantos itens existentes na tabela.
    date_hierarchy = 'inclusao'    
    list_filter = ('pronto',)
    
    def hora_inclusao(self, obj):
        return obj.inclusao.strftime('%H:%M')  
    
    def partiu(self, obj):
        return bool(obj.pronto and obj.entregador and obj.partida)
    partiu.boolean = True 
    
    inlines = [PizzaAdmin]

    

# ============================================================
class AtletaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'fone', 'endereco', 'tipo' )
    search_fields = ['fone', 'nome', 'logradouro', 'tipo']
    list_filter = ('tipo',)

admin.site.register(Atleta, AtletaAdmin)
# ============================================================
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Entregador)
# admin.site.register(Pizza) << nao precisa pois ninguem nunca vai cadastrar uma pizza no admin
