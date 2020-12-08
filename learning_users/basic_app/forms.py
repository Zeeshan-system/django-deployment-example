from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta():
        model = User
        fields=('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model= UserProfileInfo
        fields=('portfolio_sites','profile_pics')
