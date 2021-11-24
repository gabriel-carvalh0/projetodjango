from django.urls import path

from . import views
from django.urls import path
from django.contrib import admin



urlpatterns = [
    path(r'^$', views.product_list, name='product_list'),
]
