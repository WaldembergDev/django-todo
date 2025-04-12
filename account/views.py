from django.shortcuts import render, redirect
from .models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not email:
            messages.add_message(request, constants.WARNING, 'Informe um e-mail!')
            return redirect('/account/login')
        if not password:
            messages.add_message(request, constants.WARNING, 'Informe uma senha!')
            return redirect('/account/login')
        user = auth.authenticate(request, email = email, password = password)
        if user:
            auth.login(request, user)
            return redirect('/task/home')
        else:
            messages.add_message(request, constants.WARNING, 'E-mail ou senha inválidos!')
            return redirect('/account/login')
        

def cadastro(request):
    if request.method == 'GET':
        status = request.GET.get('status')
        return render(request, 'cadastro.html', {'status': status})
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(name = name, password = password)
        if user.exists():
            return redirect('/account/cadastro/?status=error_1')
        else:
            User.objects.create_user(name = name, email = email, password = password)
            return redirect('/account/cadastro/?status=success')

def logout(request):
    auth.logout(request)
    return redirect('/account/login')     