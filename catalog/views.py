from django.shortcuts import render

from app_ecommerce.views import product
from .models import Product

def product_list(request):
    context = {
        'product_list': Product.objects.all()
    }
    return render(request, 'catalog/product_list.html', context)