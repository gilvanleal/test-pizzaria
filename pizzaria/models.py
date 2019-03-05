from django.db import models

# Create your models here.

class Cliente(models.Model):
    pass

class Pedido(models.Model):
    numero = models.CharField(max_length=10)
    

class Item(models.Model):
    pedido = models.ForeignKey('Pedido')

class ItemAbstrato(models.Model):
    TAMANHO, SABOR, ADCIONAL = 'tamanho', 'sabor', 'adicional'

    nome = models.CharField()
    valor = models.DecimalField(max_digits=5, decimal_precision=2)
    tempo = models.IntegerField()
    tipo = models.CharField(max_length=3, choices=[(TAMANHO, TAMANHO.title()), (SABOR, SABOR.title()), (ADCIONAL, ADCIONAL.title())])

