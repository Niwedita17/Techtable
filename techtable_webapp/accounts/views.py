from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .tokens import account_activation_token
from .forms import CandidateSignupForm, EmployerSignupForm, EditProfileForm


def home_view(request):
    return redirect('techtable:index')


def candidate_register(request):
    form = CandidateSignupForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.candidate.name = form.cleaned_data.get('name')
        user.candidate.email = form.cleaned_data.get('email')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('../')
    else:
        form = CandidateSignupForm()
    return render(request, 'accounts/candidate-register.html', {'form': form})


def employer_register(request):
    form = CandidateSignupForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.employer.name = form.cleaned_data.get('name')
        user.employer.email = form.cleaned_data.get('email')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('../')
    else:
        form = EmployerSignupForm()
    return render(request, 'accounts/employer-register.html', {'form': form})


def candidate_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            # get user id
            user_id = user.username
            login(request, user)
            return redirect('../')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/candidate-login.html', {'form': form})


def employer_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            # get user id
            user_id = user.username
            login(request, user)
            return redirect('../')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/employer-login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('techtable:index')


def edit_profile(request):
    args = {}
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        form.actual_user = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('update_profile_success'))
        else:
            form = EditProfileForm()
            args['form'] = form
    return render(request, 'accounts/edit-profile.html', args)
