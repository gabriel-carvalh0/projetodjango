from django.urls import path
from . import views




urlpatterns = [
    path(r'^registro/$', views.register, name='register')
]
