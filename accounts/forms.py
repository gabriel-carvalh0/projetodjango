from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from .models import User

class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email']


class UserAdminForm(forms.ModelForm):


    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'is_active', 'is_staff']