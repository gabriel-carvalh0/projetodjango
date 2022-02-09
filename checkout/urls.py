import imp
from os import name
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'carrinho/adicionar/(?P<slug>.*)/$', views.create_cartitem, name='create_cartitem'),
    url(r'carrinho/$', views.cart_item, name='cart_item'),
]