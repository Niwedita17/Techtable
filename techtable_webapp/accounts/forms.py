from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models
from django.contrib.auth import get_user_model

user_instance = get_user_model()


class CandidateSignupForm(UserCreationForm):
    username = forms.CharField(max_length=150, help_text='UserName')
    name = forms.CharField(max_length=15, help_text='Name')
    email = forms.EmailField(max_length=50, help_text='Email')

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password1', 'password2',)


class EmployerSignupForm(UserCreationForm):
    username = forms.CharField(max_length=150, help_text='UserName')
    name = forms.CharField(max_length=15, help_text='Name')
    email = forms.EmailField(max_length=50, help_text='Email')

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password1', 'password2',)


class EditProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

        profile = kwargs.get('instance')
        if profile:
            kwargs['instance'] = profile.user

        self.user_form = CandidateSignupForm(*args, **kwargs)

        self.fields.update(self.user_form.fields)
        self.initial.update(self.user_form.initial)

    def save(self, *args, **kwargs):
        self.user_form.save(*args, **kwargs)
        return super(EditProfileForm, self).save(*args, **kwargs)

    class Meta:
        model = models.Candidate
        exclude = ('user',)

