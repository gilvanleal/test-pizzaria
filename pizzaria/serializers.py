from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import Pizza, Tamanho, Sabor, Personalizacao, Pedido

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

class TamanhoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tamanho
        fields = ['url', 'nome', 'valor', 'tempo']

class SaborSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sabor
        fields = ['url', 'nome', 'valor', 'tempo']


class PersonalizacaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Personalizacao
        fields = ['url', 'nome', 'valor', 'tempo']

class PizzaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Pizza
        fields = '__all__'

class PedidoSerializer(serializers.HyperlinkedModelSerializer):
    valor = serializers.DecimalField(max_digits=5, decimal_places=2, read_only=True)

    class Meta:
        model = Pedido
        fields = ('url', 'numero', 'cliente', 'pizza', 'tempo', 'valor')
