#forms.py
from django import forms
class RegisterForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=50)
    password = forms.CharField(widget=forms.PasswordInput, label='Pass Word')
    email = forms.EmailField(label='Email')
