from django.shortcuts import render, redirect
from django.contrib import messages


def register(request):
    # If the request is a post then it is a form submission
    if request.method == 'POST':
        # Register user
        print("Posted")
        messages.error(request, 'Testing Error message')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    # If the request is a post then it is a form submission
    if request.method == 'POST':
        # Register user
        print("Login User")
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
