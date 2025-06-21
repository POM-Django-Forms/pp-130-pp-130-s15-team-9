from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from django.contrib.auth import update_session_auth_hash

User = get_user_model()

def home_view(request):
    return render(request, 'home.html')

@login_required
def edit_profile_view(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            new_password = form.cleaned_data.get('password')
            if new_password:
                user.set_password(new_password)
            user.save()
            if new_password:
                update_session_auth_hash(request, user)
            return redirect('home')
    else:
        form = ProfileForm(instance=user)
    return render(request, 'authentication/edit_profile.html', {'form': form})

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
            error = "Incorrect email or password"

    return render(request, 'authentication/login.html', {'error': error})




from django.contrib.auth.forms import UserCreationForm


def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        User = get_user_model()

        if User.objects.filter(email=email).exists():
            return render(request, 'authentication/register.html', {'error': 'A user with this email exists.'})

        user = User.objects.create_user(email=email, password=password)
        user.save()

        return redirect('login')

    return render(request, 'authentication/register.html')

def register_email_only(request):
    if request.method == 'POST':
        form = EmailRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                messages.error(request, "A user with this email exists.")
            else:
                user = User.objects.create_user(username=email, email=email)
                user.set_unusable_password()
                user.save()
                messages.success(request, "User created.")
                return redirect('login')
    else:
        form = EmailRegistrationForm()

    return render(request, 'authentication/register_email_only.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
