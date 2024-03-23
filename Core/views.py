from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from Core.forms import CreateUserForm

def index(request):
    return render(request, "index.html")

def login_view(request):
     if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            print("Signed in successfully.")
            return redirect('index') 
     else:
        login_form = AuthenticationForm()
     return render(request, 'login.html', {'login_form': login_form})


def signup_post(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            print("User Created:", user)
            return redirect('login')
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = CreateUserForm()
        return render(request, 'login.html', {'form': form})
    
    
