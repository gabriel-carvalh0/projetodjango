
from django.urls import path
from .views import * 

from django.conf.urls import url
app_name = 'accounts'


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^alterar-dados/$', update_user, name='update_user'),
    url(r'^alterar-senha/$', update_password, name='update_password'),
    url(r'^registro/$', register, name='register'),
]
