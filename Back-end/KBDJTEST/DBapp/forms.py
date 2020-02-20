from django import forms


class Login(ModelForm):
    username=forms.CharField()
    password=forms.CharField()
    email=forms.CharField()
