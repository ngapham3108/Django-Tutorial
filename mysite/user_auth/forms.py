from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label='UserName', max_length='50')
    password = forms.CharField(label='PassWord', widget=forms.PasswordInput)
    email = forms.EmailField(label='Email')

