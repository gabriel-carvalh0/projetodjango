from django.urls import path

from . import views
from django.urls import path
from django.contrib import admin



urlpatterns = [
    path(r'^$', views.product_list, name='product_list'),
    path(r'^(?P<slug>[/w_-]+)/$', views.category, name='category'),
    path(r'^produtos/(?P<slug>[/w_-]+)/$', views.product, name='product'),
]
