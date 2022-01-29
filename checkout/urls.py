import imp
from os import name
from django.urls import path

from . import views

urlpatterns = [
    path(r'carrinho/adicionar/(?P<slug>[/w_-]+)/$', views.create_cartitem, name='create_cartitem' )
]