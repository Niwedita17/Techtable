from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect#, render_to_response, get_object_or_404, get_list_or_404
from django.urls import reverse
from django.utils.datetime_safe import date
from django.template import RequestContext

# from .models import
# Create your views here.

def index(request):
    return render(request, 'techtable/index.html')

def internapplytpage(request):
    return render(request, 'techtable/internapplytpage.html')


def postaninternsip(request):
    return render(request, 'techtable/postaninternsip.html')

def requestservices(request):
    return render(request, 'techtable/requestservices.html')


def provideserveices(request):
    return render(request, 'techtable/provideserveices.html')


def contact_us(request):
    return render(request, 'techtable/contact-us.html')

def applyforintenship(request):
    return render(request, 'techtable/applyforajob.html')


