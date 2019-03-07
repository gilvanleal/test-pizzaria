from django.test import TestCase
from django.contrib.auth.models import User

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Pizza, Tamanho, Sabor, Personalizacao, Pedido
from .serializers import PizzaSerializer, TamanhoSerializer, SaborSerializer

class PropiedadeTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='uds_user', password='password')
        self.tamanhos = [
            {'nome': 'Pequena', 'valor': "20.00", 'tempo': 15},
            {'nome': 'Média', 'valor': "30.00",'tempo': 20},
            {'nome': 'Grande','valor': "40.00",'tempo': 25}
        ]
        self.sabores = [
            {'nome': 'Calabresa', 'valor': "0.00", 'tempo': 0},
            {'nome': 'Marguerita:', 'valor': "0.00",'tempo': 0},
            {'nome': 'Portuguesa:', 'valor': "0.00",'tempo': 5}
        ]
        self.personalizacao = [
            {'nome': 'Extra bacon', 'valor': "3.00", 'tempo': 0},
            {'nome': 'Sem cebola:', 'valor': "0.00", 'tempo': 0},
            {'nome': 'Borda recheada:', 'valor': "5.00", 'tempo': 5}
        ]

        # self.pizza = {
        #     'tamanho': reverse('tamanho-detail', args=[Tamanho.objects.create(**self.tamanhos[0]).id]),
        #     'sabor': reverse('sabor-detail', args=[Sabor.objects.create(**self.sabores[0]).id]),
        # }

    
    def create_propriedade(self, str_url, values, klass):
        url = reverse(str_url)
        self.client.force_authenticate(self.user)
        for i, t in enumerate(values, start=1):
            response = self.client.post(url, t, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(klass.objects.count(), i)
        self.client.logout()
        for p in values:
            self.assertTrue(klass.objects.filter(nome=p['nome'], valor=p['valor'], tempo=p['tempo']).exists())

    def test_create_tamanho(self):
        self.create_propriedade('tamanho-list', self.tamanhos, Tamanho)
    
    def test_create_sabor(self):
        self.create_propriedade('sabor-list', self.sabores, Sabor)

    def test_create_personalizacao(self):
        
        self.create_propriedade('personalizacao-list', self.personalizacao, Personalizacao)


class PizzaTests(APITestCase):
    def setUp(self):
        self.tamanhos = [
            {'nome': 'Pequena', 'valor': "20.00", 'tempo': 15},
            {'nome': 'Média', 'valor': "30.00", 'tempo': 20},
            {'nome': 'Grande','valor': "40.00", 'tempo': 25}
        ]
        self.sabores = [
            {'nome': 'Calabresa', 'valor': "0.00", 'tempo': 0},
            {'nome': 'Marguerita', 'valor': "0.00", 'tempo': 0},
            {'nome': 'Portuguesa', 'valor': "0.00", 'tempo': 5}
        ]
        self.personalizacao = [
            {'nome': 'Extra bacon', 'valor': "3.00", 'tempo': 0},
            {'nome': 'Sem cebola', 'valor': "0.00",'tempo': 0},
            {'nome': 'Borda recheada','valor': "5.00",'tempo': 5}
        ]
        for v, k in [(self.tamanhos, Tamanho), (self.sabores, Sabor), (self.personalizacao, Personalizacao)]:
            for p in v:
                k.objects.create(**p)


    def test_create_pizza(self):
        url = reverse('pizza-list')
        data = {
            'tamanho': reverse('tamanho-detail', args=[Tamanho.objects.get(nome='Grande').id]),
            'sabor': reverse('sabor-detail', args=[Sabor.objects.get(nome='Calabresa').id]),
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pizza.objects.count(), 1)
    
    def test_create_pizza_personalizada(self):
        url = reverse('pizza-list')
        data = {
            'tamanho': reverse('tamanho-detail', args=[Tamanho.objects.get(nome='Grande').id]),
            'sabor': reverse('sabor-detail', args=[Sabor.objects.get(nome='Calabresa').id]),
            'personalizacao': [reverse('personalizacao-detail', args=[Personalizacao.objects.get(nome='Borda recheada').id])]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pizza.objects.count(), 1)
    
    def test_create_pizza_personalizada_2(self):
        url = reverse('pizza-list')
        data = {
            'tamanho': reverse('tamanho-detail', args=[Tamanho.objects.get(nome='Grande').id]),
            'sabor': reverse('sabor-detail', args=[Sabor.objects.get(nome='Calabresa').id]),
            'personalizacao': [
                reverse('personalizacao-detail', args=[Personalizacao.objects.get(nome='Borda recheada').id]),
                reverse('personalizacao-detail', args=[Personalizacao.objects.get(nome='Sem cebola').id]),
                ]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pizza.objects.count(), 1)

class PedidoTests(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create(username='uds_user', password='password')
        self.tamanhos = [
            {'nome': 'Pequena', 'valor': "20.00", 'tempo': 15},
            {'nome': 'Média', 'valor': "30.00",'tempo': 20},
            {'nome': 'Grande','valor': "40.00",'tempo': 25}
        ]
        self.sabores = [
            {'nome': 'Calabresa', 'valor': "0.00", 'tempo': 0},
            {'nome': 'Marguerita', 'valor': "0.00",'tempo': 0},
            {'nome': 'Portuguesa','valor': "0.00",'tempo': 5}
        ]
        self.personalizacao = [
            {'nome': 'Extra bacon', 'valor': "3.00", 'tempo': 0},
            {'nome': 'Sem cebola', 'valor': "0.00",'tempo': 0},
            {'nome': 'Borda recheada', 'valor': "5.00",'tempo': 5}
        ]
        for v, k in [(self.tamanhos, Tamanho), (self.sabores, Sabor), (self.personalizacao, Personalizacao)]:
            for p in v:
                k.objects.create(**p)

    def test_pedir_uma_pizza(self):
        pizza_data = {
            'tamanho': reverse('tamanho-detail', args=[Tamanho.objects.get(nome='Média').id]),
            'sabor': reverse('sabor-detail', args=[Sabor.objects.get(nome='Calabresa').id]),
            'personalizacao': [
                reverse('personalizacao-detail', args=[Personalizacao.objects.get(nome='Borda recheada').id]),
                reverse('personalizacao-detail', args=[Personalizacao.objects.get(nome='Sem cebola').id]),
                ]
        }
        r_pizza = self.client.post(reverse('pizza-list'), pizza_data, format='json')
        pedido_data = {
            'numero': 'PED1233UDS',
            'cliente': reverse('user-detail', args=[self.user.id]),
            'pizza': r_pizza.data['url']
        }
        r_pedido = self.client.post(reverse('pedido-list'), pedido_data, format='json')
        self.assertEqual(r_pedido.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pedido.objects.count(), 1)
        self.assertEqual(r_pedido.data['tempo'], 25)
        self.assertEqual(r_pedido.data['valor'], '35.00')
    
