from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(req):
    respond = HttpResponse()
    respond.write("<h1>this's my site</h1>")
    return respond
