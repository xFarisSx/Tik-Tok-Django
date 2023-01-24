from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50, required=True)
    songname = forms.CharField(max_length=50,required=True)
    file = forms.FileField(required=True)
