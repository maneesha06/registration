from django.shortcuts import render
from .forms import SignupForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
	return render(request,'loginapp/index.html')

@login_required
def special(request):
	return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
	return HttpResponseRedirect(reverse('index'))

def signup(response):
	if response.method == "POST":
		form = SignupForm(response.POST)
		if form.is_valid():
		    form.save()

	else:
		form = SignupForm()

	return render(response, "loginapp/signup.html", {"form": form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                user_login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'loginapp/login.html', {})





# Create your views here.
