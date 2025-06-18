from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import CustomUser

User = get_user_model()

def home_view(request):
    return render(request, 'home.html')


def login_view(request):
    error = None
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = "Невірний email або пароль"

    return render(request, 'authentication/login.html', {'error': error})




from django.contrib.auth.forms import UserCreationForm


def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        User = get_user_model()

        if User.objects.filter(email=email).exists():
            return render(request, 'authentication/register.html', {'error': 'Користувач з таким email вже існує.'})

        user = User.objects.create_user(email=email, password=password)
        user.save()

        return redirect('login')

    return render(request, 'authentication/register.html')



def logout_view(request):
    logout(request)
    return redirect('login')
