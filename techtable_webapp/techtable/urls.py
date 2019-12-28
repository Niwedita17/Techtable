
from django.conf.urls import url
from . import views as user_views
from django.contrib.auth import views as auth_views

app_name = 'techtable'

urlpatterns = [
        url(r'^$', user_views.index, name='index'),
        #127.0.0.1/techtable/
        url(r'^internapplytpage/$', user_views.internapplytpage, name='internapplytpage'),
        url(r'^postaninternsip/$', user_views.postaninternsip, name='postaninternsip'),
        url(r'^contact-us/$', user_views.contact_us, name='contact-us'),
        url(r'^job-detail/$', user_views.job_detail, name='job-detail'),
        url(r'^404/$', user_views.pageNotFound, name='404'),
        url(r'^applyforajob/$', user_views.applyforintenship, name='applyforajob'),

        url(r'^candidate-detail/$', user_views.candidate_detail, name='candidate-detail'),
        url(r'^candidate-listing/$', user_views.candidate_listing, name='candidate-listing'),
        url(r'^company-detail/$', user_views.company_detail, name='company-detail'),
        url(r'^companydashboard/$', user_views.companydashboard, name='companydashboard'),
        url(r'^edit-profile/$', user_views.edit_profile, name='edit-profile'),
        url(r'^job-listing/$', user_views.job_listing, name='job-listing'),
    ]