from django.conf.urls import url
from DBapp import views

urlpatterns= [
    url(r'^$', views.index, name='index'),
    url(r'^mainGame', KilbEarn.main, name='index')
]
