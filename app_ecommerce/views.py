from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'login.html')

def starter(request):
    return render(request, 'starter.html')