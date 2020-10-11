from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.
def register(req):
    if req.method == 'POST':
        response = HttpResponse()
        response.write("<h1> Thanks for registering </h1> <br>")
        response.write("Your UserName: "+ req.POST['username']+'<br>')
        response.write("Your PassWord: " + req.POST['password'] + '<br>')
        response.write("Your Email: " + req.POST['email'] + '<br>')
        return response
    register_form = forms.RegisterForm()
    return render(req,'user_auth/register.html',{'form': register_form})

