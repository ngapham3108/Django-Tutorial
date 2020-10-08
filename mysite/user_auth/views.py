from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterForm
# Create your views here.
def register(req):
    if req.method == 'POST':
        response = HttpResponse()
        response.write("<h1>Thanks for registering</h1></br>")
        response.write("Your username: " + req.POST['username'] + "</br>")
        response.write("Your email: " + req.POST['email'] + "</br>")
        return response
    registerForm = RegisterForm()
    return render(req, 'user_auth/register.html', {'form': registerForm})