from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect  # , render_to_response, get_object_or_404, get_list_or_404
from django.urls import reverse
from django.utils.datetime_safe import date
from django.template import RequestContext

# from .forms import EditProfileForm
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
    return render(request, 'techtable/postaninternsip.html')


def contact_us(request):
    return render(request, 'techtable/contact-us.html')


def applyforintenship(request):
    return render(request, 'techtable/applyforajob.html')


def candidate_detail(request):
    return render(request, 'techtable/candidate-detail.html')


def candidate_listing(request):
    return render(request, 'techtable/company-listing.html')


def company_detail(request):
    return render(request, 'techtable/company-detail.html')


def companydashboard(request):
    return render(request, 'techtable/companydashboard.html')


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

def pageNotFound(request):
    return render(request, 'techtable/404.html')




