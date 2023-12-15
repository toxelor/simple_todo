from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Chel

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Chel
        fields = ('username', 'password')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Chel
        fields = ('username', 'password')