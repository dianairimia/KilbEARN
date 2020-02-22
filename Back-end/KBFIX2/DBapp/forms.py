from django import forms


class Login(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
    email=forms.CharField()
