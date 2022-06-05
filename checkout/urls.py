import imp
from os import name
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'carrinho/adicionar/(?P<slug>.*)/$', views.create_cartitem, name='create_cartitem'),
    url(r'carrinho/$', views.cart_item, name='cart_item'),
    url(r'^finalizando/$', views.checkout, name='checkout'),
    url(r'^finalizando/(?P<pk>\d+)/pagseguro/$', views.pagseguro_view, name='pagseguro_view'),
    url(r'^meus-pedidos/$', views.order_list, name='order_list'),
    url(r'^meus-pedidos/(?P<pk>.*)/$', views.order_detail, name='order_detail'),
]