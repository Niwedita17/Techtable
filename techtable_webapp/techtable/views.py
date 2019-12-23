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

def about_us(request):
    return render(request, 'techtable/about-us.html')


def blog(request):
    return render(request, 'techtable/blog.html')


def blog_detail(request):
    return render(request, 'techtable/blog-detail.html')


def blog_full_width(request):
    return render(request, 'techtable/blog-full-width.html')

def blog_grid(request):
    return render(request, 'techtable/blog-grid.html')

def candidate_detail(request):
    return render(request, 'techtable/candidate-detail.html')

def candidate_listing(request):
    return render(request, 'techtable/company-listing.html')

def company_detail(request):
    return render(request, 'techtable/company-detail.html')

def dashboard(request):
    return render(request, 'techtable/dashboard.html')

def developers(request):
    return render(request, 'techtable/developers.html')

def edit_profile(request):
    return render(request, 'techtable/edit-profile.html')


def faqs(request):
    return render(request, 'techtable/faqs.html')


def job_detail(request):
    return render(request, 'techtable/job-detail.html')

def job_listing(request):
    return render(request, 'techtable/job-listing.html')

def packages(request):
    return render(request, 'techtable/packages.html')

def post_job(request):
    return render(request, 'techtable/post-job.html')

def typography(request):
    return render(request, 'techtable/typography.html')



