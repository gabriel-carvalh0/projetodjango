
from django.urls import path
from . import views




urlpatterns = [
    path(r'^$', views.index, name='index'),
    path(r'^registro/$', views.register, name='register'),
]