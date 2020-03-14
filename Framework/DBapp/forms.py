from django import forms


class Register(forms.Form):
    firstname=forms.CharField(required=True, label=False, widget=forms.TextInput( attrs={'class' : 'form-control', 'type' : 'firstname', 'id' : "inputFirstName", 'placeholder' :"First Name" }))
    username=forms.CharField(required=True, label=False, widget=forms.TextInput(attrs={'class' : 'form-control', 'type' : 'username', 'id' : "username", 'placeholder' : "Username" }))
    email=forms.CharField(required=True, label=False, widget=forms.TextInput(attrs={'class' : 'form-control', 'type' : 'email', 'id' : "inputEmail", 'placeholder' : "Email" }))
    password=forms.CharField(required=True, label=False, widget = forms.PasswordInput(attrs={'class' : 'form-control', 'type' : 'password', 'id' : "inputPassword", 'placeholder' : "Password" }))

class Login(forms.Form):
    username=forms.CharField(required=True, label=False, widget=forms.TextInput(attrs={'class' : 'form-control', 'type' : 'username', 'id' : "username", 'placeholder' : "Username" }))
    password=forms.CharField(required=True, label=False, widget = forms.PasswordInput(attrs={'class' : 'form-control', 'type' : 'password', 'id' : "inputPassword", 'placeholder' : "Password" }))
