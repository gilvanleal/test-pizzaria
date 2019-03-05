import operator, functools
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pedido(models.Model):
    numero = models.CharField(max_length=10)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    pizza = models.OneToOneField('Pizza', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.numero

    def compute(self, prop):
        props = [obs for obs in self.pizza.personalizacao.all()]
        props.append(self.pizza.tamanho)
        props.append(self.pizza.sabor)
        return [getattr(p, prop) for p in props]

    @property
    def tempo(self):
        return functools.reduce(operator.add, self.compute('tempo'))
    
    @property
    def valor(self):
        return functools.reduce(operator.add, self.compute('valor'))

    @property
    def tamanho(self):
        return self.pizza.tamanho.nome


class Pizza(models.Model):
    tamanho = models.ForeignKey('Tamanho', on_delete=models.CASCADE)
    sabor = models.ForeignKey('Sabor', on_delete=models.CASCADE)
    personalizacao = models.ManyToManyField('Personalizacao', blank=True)

    def __str__(self):
        return '{} {} {}'.format(self.tamanho, self.sabor, self.personalizacao.all())

class Propriedade(models.Model):
    class Meta:
        abstract = True

    nome = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    tempo = models.IntegerField(default=0, help_text="Tempo em minutos")

    def __str__(self):
        return self.nome

class Tamanho(Propriedade):
    pass

class Sabor(Propriedade):
    pass

class Personalizacao(Propriedade):
    pass
