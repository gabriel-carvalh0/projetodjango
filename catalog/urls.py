from django.urls import path
from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^categoria/(?P<slug>.*)/$', views.category, name='category'),
    url(r'^produtos/(?P<slug>.*)/$', views.product, name='product'),
]
