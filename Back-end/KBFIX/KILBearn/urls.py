
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from DBapp import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^DB/', include('DBapp.urls')),
    url(r'^login', views.LoginPage, name='index'),
    url(r'^computer', views.computer, name='index'),
    url(r'^instructions', views.instructions, name='index'),
    url(r'^noroom', views.noroom, name='index'),
    url(r'^people', views.people, name='index'),
    url(r'^play', views.play, name='index'),
    url(r'^profile', views.profile, name='index'),
    url(r'^register', views.register, name='index'),
    url(r'^settings', views.settings, name='index'),
    url(r'^welcome', views.welcome, name='index'),
    url(r'admin/', admin.site.urls),
]
