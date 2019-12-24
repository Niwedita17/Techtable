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
#     jobprofile = user.jobprofile
#     companytype = user.companytype
#     worktime = user.worktime
#     jobbrief = user.jobbrief
#     joblocation = user.joblocation
    return render(request, 'techtable/internapplytpage.html')


def postaninternsip(request):
    return render(request, 'techtable/postaninternsip.html')
# not required for now
def requestservices(request):
    return render(request, 'techtable/requestservices.html')

# not required for now
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

# not required for now
def blog_detail(request):
    return render(request, 'techtable/blog-detail.html')


def blog_full_width(request)
    skillsrequired = user.skillsrequired:
    return render(request, 'techtable/blog-full-width.html')
# not required for now
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
# not required for now
def developers(request):
    return render(request, 'techtable/developers.html')

def edit_profile(request):
    return render(request, 'techtable/edit-profile.html')

# not required for now
def faqs(request):
    return render(request, 'techtable/faqs.html')


def job_detail(request):
#     jobid = user.jobid
#     jobprofile = user.jobprofile
#     numberofopenings = user.numberofopenings
#     jobdescription = user.jobdescription
#     skillsrequired = user.skillsrequired
#     jobresponsibilities = user.jobresponsibilities
#     monthlystipend = user.monthlystipend
#     perks = user.perks
#     jobtype = user.jobtype 
#     companytype = user.companytype
#     worktime = user.worktime
#     jobbrief = user.jobbrief
#     joblocation = user.joblocation
    return render(request, 'techtable/job-detail.html')
# not required for now
def job_listing(request):
    
    return render(request, 'techtable/job-listing.html')
# not required for now
def packages(request):
    return render(request, 'techtable/packages.html')

def post_job(request):
#     jobprofile = user.jobprofile
#     numberofopenings = user.numberofopenings
#     jobdescription = user.jobdescription
#     skillsrequired = user.skillsrequired
#     jobresponsibilities = user.jobresponsibilities
#     monthlystipend = user.monthlystipend
#     perks = user.perks
#     jobtype = user.jobtype 
#     companytype = user.companytype
#     worktime = user.worktime
#     jobbrief = user.jobbrief
#     joblocation = user.joblocation
    return render(request, 'techtable/post-job.html')
# not required for now
def typography(request):
    return render(request, 'techtable/typography.html')



