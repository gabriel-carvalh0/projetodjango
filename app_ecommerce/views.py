from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from django.http import HttpResponse

from catalog.models import Category


def index(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')


    