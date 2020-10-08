from django.shortcuts import render

# Create your views here.
from django.db import models
from django.http import HttpResponse
from .forms import UploadFileForm
def fileUploaderView(request):
    if request.method == 'POST':
        form = UploadFileForm()