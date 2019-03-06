from django.contrib import admin
from .models import Pizza, Tamanho, Sabor, Personalizacao, Pedido

# Register your models here.


admin.site.register([Pizza, Tamanho, Sabor, Personalizacao, Pedido])
