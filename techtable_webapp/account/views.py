from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from .forms import CandidateSignupForm, EmployerSignupForm

def index(request):
    return redirect('techtable:index')

def candidate_register(request):
    # if this is a POST request we need to process the form data
    template = 'account/candidate-register.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CandidateSignupForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                print("1")
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                print("2")
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password2']:
                print("3")
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                print("4")
                # save the table info to the database
                form.save()
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.c_name = form.cleaned_data['name']
                user.save()

                user_id = user.username
                # Login the user
                login(request, user)

                # redirect to accounts page:
                return HttpResponseRedirect(reverse('account/candidate-register.html', args=(user_id,)))

    # No post data available, let's just show the page.
    else:
        print("6")
        form = CandidateSignupForm()
    return render(request, template, {'form': form})


def employer_register(request):
    # if this is a POST request we need to process the form data
    template = 'account/employer-register.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CandidateSignupForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                print("1")
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                print("2")
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password2']:
                print("3")
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                print("4")
                # save the table info to the database
                form.save()
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.e_name = form.cleaned_data['name']
                user.save()

                user_id = user.username
                # Login the user
                login(request, user)

                # redirect to accounts page:
                return HttpResponseRedirect(reverse('account/employer-register.html', args=(user_id,)))

    # No post data available, let's just show the page.
    else:
        print("6")
        form = EmployerSignupForm()
    return render(request, template, {'form': form})


def candidate_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            # get user id
            user_id = user.username
            login(request, user)
            return HttpResponseRedirect(reverse('account/candidate-login.html', args=(user_id,)))
    else:
        form = AuthenticationForm()
    return render(request, 'account/candidate-login.html', {'form': form})

def employer_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            # get user id
            user_id = user.username
            login(request, user)
            return HttpResponseRedirect(reverse('account/employer-login.html', args=(user_id,)))
    else:
        form = AuthenticationForm()
    return render(request, 'account/employer-login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('techtable:index')
