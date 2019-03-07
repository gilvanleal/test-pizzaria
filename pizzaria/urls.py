from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet, PizzaViewSet, PedidoViewSet, TamanhoViewSet, SaborViewSet, PersonalizacaoViewSet

router = routers.DefaultRouter()
router.get_api_root_view().cls.__name__ = 'Api Pizzaria'
router.get_api_root_view().cls.__doc__ = 'Gerenciamento de pedido de pizza'
router.register(r'clientes', UserViewSet)
router.register(r'pizzas', PizzaViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'tamanhos', TamanhoViewSet)
router.register(r'sabores', SaborViewSet)
router.register(r'personalizacoes', PersonalizacaoViewSet)

urlpatterns = [
   url(r'^', include(router.urls)),
]
