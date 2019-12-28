
from django.conf.urls import url
from . import views

app_name = 'accounts'


urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^candidate-login/$', views.candidate_login, name='candidate-login'),
        url(r'^employer-login/$', views.employer_login, name='employer-login'),
        url(r'^candidate-register/$', views.candidate_register, name='candidate-register'),
        url(r'^employer-register/$', views.employer_register, name='employer-register'),
        url(r'^logout/$', views.logout_view, name='logout'),
    ]