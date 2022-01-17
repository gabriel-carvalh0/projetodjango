import imp
from pipes import Template
from re import template
from django.db import models
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User
from .forms import UserAdminCreationForm

class IndexView(LoginRequiredMixin, TemplateView):

    template_name = 'accounts/conta.html'



class RegisterView(CreateView):

    model = User
    template_name = 'accounts/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('index')

index = IndexView.as_view()
register = RegisterView.as_view()