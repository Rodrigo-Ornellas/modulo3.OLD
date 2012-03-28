#coding: utf-8

# primeiro importa coisas do python, segundo do django e terceiro da aplicacao
from django.contrib import admin
from .models import Atleta, Cliente, Pedido, Entregador

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('fone', 'nome', 'endereco')
    list_display_links = list_display
    search_fields = ['fone', 'nome', 'logradouro']
    list_filter = ('logradouro',)

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('hora_inclusao', 'cliente', 'pronto', 'partiu')
    list_filter = ('pronto',)
    
    def hora_inclusao(self, obj):
        return obj.inclusao.strftime('%H:%M')  
    
    def partiu(self, obj):
        return bool(obj.pronto and obj.entregador and obj.partida)
    partiu.boolean = True        

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
