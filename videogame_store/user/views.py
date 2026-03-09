from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import SigninForm, LoginForm
from django.contrib import messages

# Create your views here.
def sign_in_view(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)# generate an instance with the form values 
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SigninForm()
    return render(request, 'user/signin.html', {'form':form})

def log_in_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)
            messages.error(request, 'Usuario o contraseña incorrectos')
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form':form})

def log_out_view(request):
    logout(request)
    return redirect('log-in')

@login_required
def profile_view(request):
    return render(request, 'user/profile.html')
