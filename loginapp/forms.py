from django import forms
from .models import models
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from loginapp.models import UserProfileInfo

class SignupForm(UserCreationForm):
	email = models.EmailField()

	class Meta():
		model = User
		fields = ["username", "email", "password1", "password2"]

class UserProfileInfoForm(forms.ModelForm):
	class Meta():
		model = UserProfileInfo
		fields = ["user"]




