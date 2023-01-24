from django import forms


attrs = {
	'class':'form-input',
	'autocomplete': 'off'
}
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs=attrs))
    songname = forms.CharField(max_length=50,required=True, widget=forms.TextInput(attrs=attrs))
    file = forms.FileField(required=True)
