
from django.urls import path
from .views import * 

app_name = 'accounts'


urlpatterns = [
    path('', index, name='index'),
    path(r'^ alterar-dados/$', update_user, name='update_user'),
    path(r'^ alterar-senha/$', update_password, name='update_password'),
    path(r'^registro/$', register, name='register'),
]
