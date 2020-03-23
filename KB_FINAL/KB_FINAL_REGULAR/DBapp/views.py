from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from DBapp.models import Main, Friends, Icons
from django.contrib.auth.models import User
from django import forms
from . import forms
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import hashlib
import json
#import DBapp.KilbEarn as Kilbearn




def Hasher(x):
    return hashlib.sha256(str(x).encode('utf-8')).hexdigest()

def P2J():
    data={}
    data['players']=[]
    for x in list(Icons.objects.all()):
        y=str(x).split()
        data['players'].append({
            'name':y[0],
            'icon':y[1],
            'money':500,
            'locations':[],
        })
    with open('players.json', 'w+') as output:
        json.dump(data, output)




def index(request):
    if request.user.is_authenticated:
        logout(request)
    val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
    return render(request, 'DBapp/index.html', context=val_dict)

@login_required
def computer(request):
    val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }

    if request.method=="POST" and "sendNumberPlayer" in request.POST:
        x=len(list(Icons.objects.all()))
        if x>0:
            P2J()
            return render(request, 'DBapp/board.html')
        else:
            messages.error(request, "You need at least 1 player!")
            return render(request, 'DBapp/noroom.html')
    if request.method=="POST":
        if len(list(Icons.objects.all())) < 4:
            try:
                record=Icons(username=request.POST.get('Name'), icon=request.POST.get('icon'))
                record.save()
                print("Successfully added to database")
                return render(request, 'DBapp/noroom.html')
            except:
                messages.error(request, "You cannot use the same name or icon!")
                return render(request, 'DBapp/noroom.html')
        else:
            messages.error(request, "Player limit (4) exceeded!")
            return render(request, 'DBapp/noroom.html')


    return render(request, 'DBapp/noroom.html', context=val_dict)

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
    val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }

    if request.method=="POST" and "sendNumberPlayer" in request.POST:
        x=len(list(Icons.objects.all()))
        if x>1:
            P2J()
            return render(request, 'DBapp/board.html')
        else:
            messages.error(request, "You need at least 2 players!")
            return render(request, 'DBapp/noroom.html')
    if request.method=="POST":
        if len(list(Icons.objects.all())) < 4:
            try:
                record=Icons(username=request.POST.get('Name'), icon=request.POST.get('icon'))
                record.save()
                print("Successfully added to database")
                return render(request, 'DBapp/noroom.html')
            except:
                messages.error(request, "You cannot use the same name or icon!")
                return render(request, 'DBapp/noroom.html')
        else:
            messages.error(request, "Player limit (4) exceeded!")
            return render(request, 'DBapp/noroom.html')


    return render(request, 'DBapp/noroom.html', context=val_dict)

@login_required
def people(request):
    Icons.objects.all().delete()
    val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
    return render(request, 'DBapp/people.html', context=val_dict)

@login_required
def play(request):
    Icons.objects.all().delete()
    val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
    return render(request, 'DBapp/play.html', context=val_dict)

@login_required
def profile(request):
    if request.method=="POST" and 'Delete' in request.POST:
        cu=request.user
        for i in Main.objects.all():
            x=str(i).split()
            if str(request.user)==x[0]:
                i.delete()
        logout(request)
        cu.delete()
        return render(request, 'DBapp/Welcome.html')

    if request.method=="POST" and 'ChPass' in request.POST:
        newpass=request.POST.get('password')
        cu=request.user
        for i in Main.objects.all():
            x=str(i).split()
            if str(request.user) == x[0]:
                i.hash = Hasher(newpass)
                i.save()
        cu.set_password(newpass)
        cu.save()

        logout(request)
        return render(request, 'DBapp/Welcome.html')

    if request.method=="POST" and 'ChUsername' in request.POST:
        newname=request.POST.get('username')
        cu=request.user
        for i in Main.objects.all():
            x=str(i).split()
            if str(request.user) == x[0]:
                i.username = newname
                i.save()
        cu.username=newname
        cu.save()

        logout(request)
        return render(request, 'DBapp/Welcome.html')

    if request.method=="POST" and 'ChEmail' in request.POST:
        print("Implement change of Email")

    return render(request, 'DBapp/profile.html')


def board(request):
        val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
        return render(request, 'DBapp/board.html', context=val_dict)
        if method=="POST":
            #main()
            print("call main here")



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
    Icons.objects.all().delete()
    if request.user.is_authenticated:
        logout(request)
    val_dict = {'insert_val':"This can be modified with python, in the views.py file in DBapp" }
    return render(request, 'DBapp/welcome.html', context=val_dict)
