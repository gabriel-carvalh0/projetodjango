from django.core.exceptions import RequestAborted
from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from django.http import HttpResponse
from app_ecommerce.forms import ContactForm

from catalog.models import Category


def index(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'index.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)


    