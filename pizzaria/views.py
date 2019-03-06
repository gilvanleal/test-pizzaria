from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, AllowAny, IsAuthenticatedOrReadOnly

from .models import Pizza, Tamanho, Sabor, Personalizacao, Pedido
from .serializers import UserSerializer, PizzaSerializer, TamanhoSerializer, SaborSerializer, PersonalizacaoSerializer, PedidoSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = (AllowAny,)

class PizzaViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
            
class TamanhoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Tamanho.objects.all()
    serializer_class = TamanhoSerializer


class SaborViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Sabor.objects.all()
    serializer_class = SaborSerializer


class PersonalizacaoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Personalizacao.objects.all()
    serializer_class = PersonalizacaoSerializer
