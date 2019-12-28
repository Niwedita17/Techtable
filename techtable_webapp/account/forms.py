from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models
from django.contrib.auth import get_user_model

user_instance = get_user_model()


class CandidateSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "placeholder": "Password"
        }))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "placeholder": "Password"
        }))

    class Meta:
        model = models.CandidateInfo
        fields = ('name', 'username', 'email', 'password', 'password2')


class EmployerSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "placeholder": "Password"
        }))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "placeholder": "Password"
        }))

    class Meta:
        model = models.EmployerInfo
        fields = ('name', 'username', 'email', 'password', 'password2')
