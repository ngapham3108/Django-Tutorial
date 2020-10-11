from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponse
# Create your views here.
def fileUploaderView(req):
    if req.method == 'POST':
        form = UploadFileForm(req.POST,req.FILES)
        if form.is_valid():
            upload(req.FILES['file'])
            return HttpResponse('<h1>File uploaded successfully')
        else:
            return HttpResponse('<h1>File uploaded unsuccessfully')
    form = UploadFileForm()
    return render(req, 'file_uploader/fileUploaderTemplate.html', {'form': form})
def upload(f):
    file = open('File_Upload/'+f.name, 'wb+')
    for chunk in f.chunks():
        file.write(chunk)
