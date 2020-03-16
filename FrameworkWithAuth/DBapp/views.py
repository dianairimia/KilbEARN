from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from DBapp.models import Main, Friends
from django.contrib.auth.models import User
from django import forms
from . import forms
from django.shortcuts import redirect
import hashlib
from KilbEarn import main

from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required



def Hasher(x):
    return hashlib.sha256(str(x).encode('utf-8')).hexdigest()





def index(request):
    if request.user.is_authenticated:
        logout(request)
    val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
    return render(request, 'DBapp/index.html', context=val_dict)

@login_required
def computer(request):
    print(request.session)
    val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
    return render(request, 'DBapp/computer.html', context=val_dict)

def LoginPage(request):
    if request.user.is_authenticated:
        logout(request)
    else:
        print("Nope")
    if request.method=="POST":
        username=request.POST.get('username')
        password=Hasher(request.POST.get('password'))



        for i in Main.objects.all():
            x=str(i).split()
            if x[0] == username and x[1]== password:
                print("LOGGED IN")
                for p in User.objects.all():
                    if username==str(p):
                        login(request,p)
                        return render(request, 'DBapp/mainmenu.html')




        return render(request, 'DBapp/login.html')
    else:
        print("Invalid Login Details or none submitted")
        return render(request, 'DBapp/login.html')

@login_required
def instructions(request):
    print(request.session)
    val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
    return render(request, 'DBapp/instructions.html', context=val_dict)

@login_required
def mainmenu(request):
    print(request.session)
    val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
    return render(request, 'DBapp/mainmenu.html', context=val_dict)

@login_required
def noroom(request):
    form1=forms.NoRoomNameGrab()
    val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
    return render(request, 'DBapp/noroom.html', {'form':form1})

@login_required
def people(request):
    val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
    return render(request, 'DBapp/people.html', context=val_dict)

@login_required
def play(request):
    val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
    return render(request, 'DBapp/play.html', context=val_dict)

@login_required
def profile(request):
    val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
    return render(request, 'DBapp/profile.html', context=val_dict)

@login_required
def board(request):
        val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
        return render(request, 'DBapp/board.html', context=val_dict)
        if request.method=="POST":
            main()


def register(request):
    if request.user.is_authenticated:
        logout(request)
    form=forms.Register()
    try:
        if request.method == 'POST':
            form=forms.Register(request.POST)
            if form.is_valid():
                data = Main(username=form.cleaned_data['username'], hash=Hasher(form.cleaned_data['password']), email=form.cleaned_data['email'], hs="0", sts="Offline" )
                data.save()
                safecopy = User(username=form.cleaned_data['username'], password=Hasher(form.cleaned_data['password']), email=form.cleaned_data['email'])
                safecopy.save()
                for users in User.objects.all():
                    if str(users)==form.cleaned_data['username']:
                        login(request, users)
                return redirect('mainmenu.html')
    except:
        #return render(request, 'DBapp/register2.html', {'form':form})
        print("DUPLICATE")

    return render(request, 'DBapp/register.html', {'form':form})

@login_required
def settings(request):
    val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
    return render(request, 'DBapp/settings.html', context=val_dict)


def welcome(request):
    if request.user.is_authenticated:
        logout(request)
    val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
    return render(request, 'DBapp/welcome.html', context=val_dict)
