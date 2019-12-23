from django.conf.urls import url
from . import views as user_views
from django.contrib.auth import views as auth_views

app_name = 'techtable'

urlpatterns = [
    url(r'^$', user_views.index, name='index'),
    #127.0.0.1/account/
    url(r'^internapplytpage/$', user_views.internapplytpage, name='internapplytpage'),
    url(r'^postaninternsip/$', user_views.postaninternsip, name='postaninternsip'),
    url(r'^requestservices/$', user_views.requestservices, name='requestservices'),
    url(r'^provideserveices/$', user_views.provideserveices, name='provideserveices'),
    url(r'^contact-us/$', user_views.contact_us, name='contact-us'),

    url(r'^applyforintenship/$', user_views.applyforintenship, name='applyforintenship'),
    #url(r'^contact-us/$', user_views.contact_us, name='contact-us'),
    #url(r'^contact-us/$', user_views.contact_us, name='contact-us'),
    #url(r'^contact-us/$', user_views.contact_us, name='contact-us'),

]