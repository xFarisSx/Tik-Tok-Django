from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

attrs = {
	'class':'form-input',
	'autocomplete': 'off'
}

class Register(UserCreationForm):
	photo = forms.ImageField(required=False)
	email = forms.EmailField(required=True, widget=forms.EmailInput(attrs=attrs))
	password1 = forms.CharField(
		strip=False,
		label='Password',
		widget=forms.PasswordInput(attrs=attrs)
	)
	password2 = forms.CharField(
		strip=False,
		label='Confirm Password',
		widget=forms.PasswordInput(attrs=attrs)
	)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		widgets = {
			'username':forms.TextInput(attrs=attrs),
			'email':forms.EmailInput(attrs=attrs),
			'password1':forms.PasswordInput(attrs=attrs),
			'password2':forms.PasswordInput(attrs=attrs),
		}
		help_texts = {
            'username': None,
            'email': None,
			'password1':None,
			'password2':None
        }

	def save(self, commit=True):
		user = super(Register, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(label='Username', widget=forms.TextInput(attrs=attrs))
    
    password = forms.CharField(
		label='Password',
  		widget=forms.PasswordInput(attrs=attrs)
	)
