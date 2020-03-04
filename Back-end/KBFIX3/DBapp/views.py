from django.shortcuts import render
from django.http import HttpResponse
from DBapp.models import Main, Friends
from django import forms
from . import forms


def index(request):
    val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
    return render(request, 'DBapp/index.html', context=val_dict)


def computer(request):
    val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
    return render(request, 'DBapp/computer.html', context=val_dict)

def LoginPage(request):
    val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
    return render(request, 'DBapp/login.html', context=val_dict)

def instructions(request):
    val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
    return render(request, 'DBapp/instructions.html', context=val_dict)

def mainmenu(request):
    val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
    return render(request, 'DBapp/mainmenu.html', context=val_dict)

def noroom(request):
    val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
    return render(request, 'DBapp/noroom.html', context=val_dict)

def people(request):
    val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
    return render(request, 'DBapp/people.html', context=val_dict)

def play(request):
    val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
    return render(request, 'DBapp/play.html', context=val_dict)

def profile(request):
    val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
    return render(request, 'DBapp/profile.html', context=val_dict)

def register(request):
    form=forms.Register()
    if request.method == 'POST':
        form=forms.Register(request.POST)
        if form.is_valid():
            print("FINISHING TODAY")
            #print("NAME: " + form.cleaned_data['username'])

    return render(request, 'DBapp/register.html', {'form':form})

def settings(request):
    val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
    return render(request, 'DBapp/settings.html', context=val_dict)

def welcome(request):
    val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
    return render(request, 'DBapp/welcome.html', context=val_dict)
