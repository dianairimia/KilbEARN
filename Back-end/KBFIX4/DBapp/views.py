from django.shortcuts import render
from django.http import HttpResponse
from DBapp.models import Main, Friends
from django import forms
from . import forms
from django.shortcuts import redirect
import hashlib


def Hasher(x):
    return hashlib.sha256(str(x).encode('utf-8')).hexdigest()

def Authenticate(username, password):
    for p in Main.objects.raw('SELECT "username" FROM "Main"'):
        print(p)




def index(request):
    print(request.session)
    val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
    return render(request, 'DBapp/index.html', context=val_dict)


def computer(request):
    print(request.session)
    val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
    return render(request, 'DBapp/computer.html', context=val_dict)

def LoginPage(request):
    print(request.session)
    val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
    return render(request, 'DBapp/login.html', context=val_dict)

def instructions(request):
    print(request.session)
    val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
    return render(request, 'DBapp/instructions.html', context=val_dict)

def mainmenu(request):
    print(request.session)
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

def board(request):
        val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
        return render(request, 'DBapp/board.html', context=val_dict)


def register(request):
    form=forms.Register()
    try:
        if request.method == 'POST':
            form=forms.Register(request.POST)
            if form.is_valid():
                data = Main(username=form.cleaned_data['username'], hash=Hasher(form.cleaned_data['password']), email=form.cleaned_data['email'], hs="0", sts="Offline" )
                data.save()
                Authenticate("s","s")
                return redirect('mainmenu.html')
    except:
        #return render(request, 'DBapp/register2.html', {'form':form})
        print("DUPLICATE")

    return render(request, 'DBapp/register.html', {'form':form})

def settings(request):
    val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
    return render(request, 'DBapp/settings.html', context=val_dict)

def welcome(request):
    val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
    return render(request, 'DBapp/welcome.html', context=val_dict)
