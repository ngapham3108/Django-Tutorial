from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(label='Title', max_length=50)
    file = forms.FileField()
