from django.core.exceptions import RequestAborted
from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from django.http import HttpResponse
from app_ecommerce.forms import ContactForm

from catalog.models import Category
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'index.html', context)


def contact(request):
    success = True
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            message = 'Nome{0}/nE-Mail:{1}/n{2}'.format(name, email, message)
            send_mail(
                'Contato Do Django E-Commerce', message, settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL    ]
             )
    else:
        form = ContactForm()
    context = {
        'form': form,
        'success': success, 
    }
    return render(request, 'contact.html', context)


    