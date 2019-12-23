from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

def index(request):
    return redirect('techtable:index')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            # get user id
            user_id = user.username
            login(request, user)
            return HttpResponseRedirect(reverse('AttendanceManagement:student', args=(user_id,)))
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})

def register(request):
    return render(request, 'account/register.html')

