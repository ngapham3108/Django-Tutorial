from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(req):
    response = HttpResponse()
    response.write("<h1>this's my site</h1>")
    return response

def detail(req,qid):
    return HttpResponse("You're looking at question %s." % qid)

def results(req,qid):
    return HttpResponse("You're looking at results of the question %s." % qid)

def vote(req,qid):
    return HttpResponse("You're voting on question %s." % qid)